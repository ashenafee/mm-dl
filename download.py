import os
import subprocess
import zipfile

import requests
from tqdm import tqdm

from mymedia import MyMedia


def install_ffmpeg() -> None:
    """
    Install FFmpeg to the local directory.
    :return:
    """
    if os.name == 'nt':
        r = requests.get('https://www.gyan.dev/ffmpeg/builds/ffmpeg-relea'
                         'se-essentials.zip', stream=True)
    else:
        r = requests.get('https://evermeet.cx/ffmpeg/ffmpeg-5.1.1.zip',
                         stream=True)
    total_size_in_bytes = int(r.headers.get('content-length', 0))
    block_size = 1024

    # Download the file
    progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
    with open('ffmpeg.zip', 'wb') as ffmpeg:
        for chunk in r.iter_content(chunk_size=block_size):
            ffmpeg.write(chunk)
            progress_bar.update(len(chunk))
    progress_bar.close()

    # Unzip the file
    with zipfile.ZipFile('ffmpeg.zip', 'r') as zip_ref:
        zip_ref.extractall('ffmpeg')

    # Remove the zip file
    os.remove('ffmpeg.zip')

    if os.name == 'nt':
        # Get the subdirectory name
        subdirectory = os.listdir('ffmpeg')[0]

        # Rename the ffmpeg executable
        os.rename(f'./ffmpeg/{subdirectory}/bin/ffmpeg.exe', './ffmpeg.exe')
        os.rename(f'./ffmpeg/{subdirectory}/bin/ffprobe.exe', './ffprobe.exe')
    else:
        # Make the ffmpeg executable
        os.chmod('ffmpeg/ffmpeg', 0o777)


def download(link: str, filename: str, path: str) -> None:
    """
    Download a MyMedia video given a link to the video.
    :param link:
    :param filename:
    :param path:
    :return:
    """
    video = MyMedia(link)
    chunklist = video.get_chunklist()

    # Configure save path
    if path is not None:
        save_path = f"{path}/{filename}"
    else:
        save_path = filename
    
    # Check OS
    if os.name == 'nt':
        cmd = ['ffmpeg.exe', '-i', chunklist, '-c', 'copy', save_path + '.mp4']
    else:
        cmd = ['./ffmpeg/ffmpeg', '-i', chunklist, '-c', 'copy', save_path + '.mp4']

    try:
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   universal_newlines=True)
    except FileNotFoundError:
        cmd[0] = f"{os.path.expanduser('~')}/Downloads/ffmpeg/ffmpeg"
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT,
                                   universal_newlines=True)
    progress = tqdm(total=100, unit='%', unit_scale=True, desc='Downloading',
                    bar_format='{l_bar}{bar}|')
    duration = 0
    for line in process.stdout:
        if 'Duration: ' in line:
            duration = line.split('Duration: ')[1].split(',')[0]
            duration = duration.split(':')
            duration = int(duration[0]) * 3600 + int(duration[1]) * 60 + \
                       int(duration[2].split('.')[0])
        if 'time=' in line:
            time = line.split('time=')[1].split(' ')[0]
            time = time.split(':')
            time = int(time[0]) * 3600 + int(time[1]) * 60 + \
                   int(time[2].split('.')[0])
            progress.update(((time / duration) * 100) - progress.n)
    progress.close()

