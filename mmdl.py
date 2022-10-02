
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
    return os.path.exists('ffmpeg')


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

    download(sys.argv[1], filename)


if __name__ == '__main__':
    main()
