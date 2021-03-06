# mm-dl
*A script to download MyMedia videos using ffmpeg.*

## Prerequisites
---
- [Node.js](https://nodejs.org/en/)
- [FFmpeg](https://ffmpeg.org)

A guide on how to install FFmpeg can be found here for [macOS](https://superuser.com/questions/624561/install-ffmpeg-on-os-x) and for [Windows](https://www.wikihow.com/Install-FFmpeg-on-Windows).

## Usage
---
1. Download the latest release from [here](https://github.com/ashenafee/mm-dl/releases/download/1.0/mm-dl).
2. Open a Terminal/Command Prompt window.

    If you're on Windows, open the Command Prompt as administrator.

3. Navigate to the folder containing the file you downloaded in step 1.

    This can be done by typing `cd DIRECTORY`.

    For example, if I downloaded the binary file to my **Downloads** folder, I might type in:
    
    | OS      | Command                               |
    |:--------|:--------------------------------------|
    | macOS   | `cd "/Users/username/Downloads"`      |
    | Windows | `cd "C:\\Users\\username\\Downloads"` |

4. Type in the following to install the [ffmpeg-progressbar-cli](https://github.com/sidneys/ffmpeg-progressbar-cli) dependency:

    | OS      | Command                               |
    |:--------|:--------------------------------------|
    | macOS   | `sudo npm install --global ffmpeg-progressbar-cli`      |
    | Windows | `npm install --global ffmpeg-progressbar-cli` |

5. After installing the dependency, type in `python3 mm-dl.py` and hit enter. You should see the following as output:

    ```
    Usage: python3 mm-dl.py <MY_MEDIA_LINK> <FILENAME>
    ```

7. Try typing in `python3 mm-dl.py X Y` where `X` is your video link, and `Y` is the name you want to give the file. You should see:

    ```
    Downloading MyMedia ID: '...'
        Rendering ... | ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                 50% | ETA ...
    Success: MyMedia video '...' has been downloaded!
    ```

8. In Finder/File Explorer, navigate to the folder containing `mm-dl.py` (the file from step 1) and you should see your video `.mkv` downloaded.

## Disclaimer
---
mm-dl is a Python script to ease the process of downloading videos from MyMedia. It uses [ffmpeg](https://ffmpeg.org) and [ffmpeg-progressbar-cli](https://github.com/sidneys/ffmpeg-progressbar-cli) which carry out downloading.

I am not responsible for any copyright infringement. Additionally, I am not responsible for any inappropriate use of this tool, and I am not responsible for any loss of data or other damages.

What this tool does is off the input of the end-user, and not the developer. Use at your own risk.
