import os
import sys

try:
    from download import install_ffmpeg, download
except ImportError as e:
    # Install the modules
    os.system('pip3 install -r requirements.txt')


def check_ffmpeg() -> bool:
    """
    Check if FFmpeg is installed.
    :return:
    """
    # Check for the user's OS
    if os.name == 'nt':
        # Check if ffmpeg is in the downloads directory
        dl_dir = f"{os.path.expanduser('~')}/Downloads/ffmpeg"

        # Check if ffmpeg is in the current directory
        return os.path.exists('ffmpeg.exe') or os.path.exists(dl_dir)
    else:
        # Check if ffmpeg is in the user's Downloads directory
        dl_dir = f"{os.path.expanduser('~')}/Downloads/ffmpeg"
        return os.path.exists('ffmpeg') or os.path.exists(dl_dir)


def ask_filename() -> str:
    """
    Ask the user for a filename.
    :return:
    """
    return input('Enter a filename: ')


def main():
    if not check_ffmpeg():
        install_ffmpeg()

    filename = "temp"
    if len(sys.argv) < 2:
        print('Usage: python3 mmdl.py <link> <filename>')
        exit(1)
    elif len(sys.argv) == 2:
        filename = ask_filename()
    elif len(sys.argv) == 3:
        filename = sys.argv[2]
    else:
        print('Usage: python3 mmdl.py <link> <filename>')
        exit(1)

    download(sys.argv[1], filename, os.getcwd())


if __name__ == '__main__':
    main()
