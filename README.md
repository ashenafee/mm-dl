# mm-dl
*A script to download MyMedia videos using Python and ffmpeg.*

## Prerequisites
- [Python 3.10+](https://www.python.org/downloads/)

## Installation
1. Download the latest release from [here](https://github.com/ashenafee/mm-dl/archive/refs/heads/master.zip).
2. Unzip the download.
3. Open a Terminal/Command Prompt window.

    If you're on Windows, open the Command Prompt as administrator.

4. Navigate to the folder containing the file you downloaded in step 1.

    This can be done by typing `cd DIRECTORY`, where `DIRECTORY` is the path to the folder containing the file you downloaded in step 1.

    For example, if I downloaded and unzipped the archive in my **Downloads** folder, I might type in:
    
    | OS      | Command                               |
    |:--------|:--------------------------------------|
    | macOS   | `cd "/Users/username/Downloads"`      |
    | Windows | `cd "C:\\Users\\username\\Downloads"` |

5. Type in `python3 mmdl.py` and hit enter. It should begin downloading the ffmpeg binary for your OS:

    ```
    100% |██████████████████████████████| 24.2M/24.2M [00:06<00:00, 3.47MiB/s]
    Usage: python3 main.py <link> <filename>
    ```

## Usage
1. To use `mmdl`, type in `python3 mmdl.py <link> <filename>` and hit enter.
    ```
    Downloading:  100% |██████████████████████████████|
    ```
2. The video will be downloaded to the same folder as the ``mmdl.py`` file.

## Frequently Asked Questions (FAQs)

### How do I run the script on Windows?

Instead of typing `python3` in the commands, type in `python`.

### What format does this download the videos in?

The videos are downloaded in `.mp4` format for compatibility.

## Disclaimer
mm-dl is a Python script to ease the process of downloading videos from MyMedia. It uses [ffmpeg](https://ffmpeg.org) which carries out downloading.

I am not responsible for any copyright infringement. Additionally, I am not responsible for any inappropriate use of this tool, and I am not responsible for any loss of data or other damages.

What this tool does is off the input of the end-user, and not the developer. Use at your own risk.
