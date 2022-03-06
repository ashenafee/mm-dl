import sys
import os
from shutil import which


# Check if the correct number of arguments are passed
if (len(sys.argv) != 3):
    print("Usage: python3 mm-dl.py <MY_MEDIA_LINK> <FILENAME>")
    exit(1)

# Check if ffmpeg is in path
if (which("ffmpeg") == None):
    print("ffmpeg not found in PATH.\nPlease install ffmpeg from https://ffmpeg.org.")
    exit(1)

# Check if ffmpeg-bar is installed
if (which("ffmpeg-bar") == None):
    print("ffmpeg-bar not found. Please install ffmpeg-bar from https://github.com/sidneys/ffmpeg-progressbar-cli")
    exit(1)

ID=sys.argv[1][-32:]

# Begin download
print(f"Downloading MyMedia ID: '{ID}'")

# Run FFMPEG command in terminal
os.system(f"ffmpeg-bar -i \"https://stream.library.utoronto.ca:1935/MyMedia/play/mp4:1/{ID}.mp4/playlist.m3u8\" -codec copy \"{sys.argv[2]}.mkv\"")
print(f"Success: MyMedia video '{ID}' has been downloaded!")