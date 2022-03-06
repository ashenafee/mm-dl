import sys
import os
import requests
from shutil import which


# Check if the correct number of arguments are passed
if (len(sys.argv) != 3):
    print("Usage: python3 mm-dl.py <MY_MEDIA_LINK> <FILENAME>")
    exit(1)

# Flag for which ffmpeg to use
flag = False

# Check if ffmpeg is in path
if (which("ffmpeg") == None and (os.path.isdir("ffmpeg-5.0-essentials_build") == False or os.path.isfile("ffmpeg") == False)):
    print("ffmpeg not found in PATH.")

    # Ask whether to install ffmpeg locally
    print("\nDo you want to install ffmpeg locally? (y/n)")
    if (input() == "y"):
        print("Downloading ffmpeg...")
        
        # Check if macOS or Windows
        if (sys.platform == "darwin"):
            r = requests.get("https://evermeet.cx/ffmpeg/ffmpeg-5.0.zip")
            open("ffmpeg-5.0.zip", "wb").write(r.content)
            print("Extracting ffmpeg...")
            os.system("unzip ffmpeg-5.0.zip")
        elif (sys.platform == "win32"):
            r = requests.get("https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip", allow_redirects=True)
            open("ffmpeg-release-essentials.zip", "wb").write(r.content)
            print("Extracting ffmpeg...")
            
            # Current directory
            cd = os.getcwd()
            os.system(f"Expand-Archive -Force {cd}\ffmpeg-release-essentials.zip {cd}\ffmpeg-release-essentials")
        
        flag = True
    else:
        print("Exiting...")
        exit(1)

# Check if ffmpeg-bar is installed
if (which("ffmpeg-bar") == None):
    print("ffmpeg-bar not found. Please install ffmpeg-bar from https://github.com/sidneys/ffmpeg-progressbar-cli")
    exit(1)

ID=sys.argv[1][-32:]

# Begin download
print(f"Downloading MyMedia ID: '{ID}'")

# Run FFMPEG command in terminal
if (flag):
    # Use normal ffmpeg
    os.system(f"./ffmpeg-5.0-essentials_build/bin/ffmpeg.exe -i \"https://stream.library.utoronto.ca:1935/MyMedia/play/mp4:1/{ID}.mp4/playlist.m3u8\" -codec copy \"{sys.argv[2]}.mkv\"")

    if sys.platform == "win32":
        ffmpeg_instructions = "https://www.wikihow.com/Install-FFmpeg-on-Windows"
    elif sys.platform == "darwin":
        ffmpeg_instructions = "https://superuser.com/questions/624561/install-ffmpeg-on-os-x"

    print(f"Success: MyMedia video '{ID}' has been downloaded!")
    print(f"If you would like to see a neat progress bar when downloading, please install FFmpeg to your PATH. \
            More information can be found here: {ffmpeg_instructions}.")
else:
    # Use ffmpeg-bar
    os.system(f"ffmpeg -i \"https://stream.library.utoronto.ca:1935/MyMedia/play/mp4:1/{ID}.mp4/playlist.m3u8\" -codec copy \"{sys.argv[2]}.mkv\"")
    print(f"Success: MyMedia video '{ID}' has been downloaded!")
