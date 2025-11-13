#Github.com/Vasusen-code

from pyrogram.errors import FloodWait, InviteHashInvalid, InviteHashExpired, UserAlreadyParticipant
from telethon import errors, events

import asyncio, subprocess, re, os, time
from pathlib import Path
from datetime import datetime as dt

#Join private chat-------------------------------------------------------------------------------------------------------------

async def join(client, invite_link):
    try:
        await client.join_chat(invite_link)
        return "Successfully joined the Channel"
    except UserAlreadyParticipant:
        return "User is already a participant."
    except (InviteHashInvalid, InviteHashExpired):
        return "Could not join. Maybe your link is expired or Invalid."
    except FloodWait:
        return "Too many requests, try again later."
    except Exception as e:
        print(e)
        return "Could not join, try joining manually."
    
#Regex---------------------------------------------------------------------------------------------------------------
#to get the url from event

def get_link(string):
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex,string)   
    try:
        link = [x[0] for x in url][0]
        if link:
            return link
        else:
            return False
    except Exception:
        return False
    
#Screenshot---------------------------------------------------------------------------------------------------------------

def hhmmss(seconds):
    x = time.strftime('%H:%M:%S',time.gmtime(seconds))
    return x

async def screenshot(video, duration, sender):
    """Generate a screenshot from video at the middle timestamp.

    Args:
        video: Path to the video file
        duration: Duration of the video in seconds
        sender: User ID (used for custom thumbnail check)

    Returns:
        Path to the generated screenshot or None if failed
    """
    # Check if user has uploaded a custom thumbnail
    if os.path.exists(f'{sender}.jpg'):
        return f'{sender}.jpg'

    time_stamp = hhmmss(int(duration)/2)
    out = f"screenshot_{sender}_{dt.now().strftime('%Y%m%d_%H%M%S')}.jpg"

    cmd = [
        "ffmpeg",
        "-ss", f"{time_stamp}",
        "-i", f"{video}",
        "-frames:v", "1",
        "-vf", "scale=320:-1",  # Scale to reasonable thumbnail size
        f"{out}",
        "-y"
    ]

    try:
        process = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if process.returncode != 0:
            print(f"FFmpeg error: {stderr.decode().strip()}")
            return None

        if os.path.isfile(out):
            return out
        else:
            return None
    except Exception as e:
        print(f"Screenshot generation failed: {str(e)}")
        return None

def clean_up(file_paths):
    """Clean up temporary files.

    Args:
        file_paths: Single path string or list of paths to remove
    """
    if isinstance(file_paths, str):
        file_paths = [file_paths]

    for file_path in file_paths:
        if file_path and os.path.isfile(file_path):
            try:
                os.remove(file_path)
                print(f"Cleaned up: {file_path}")
            except Exception as e:
                print(f"Could not remove {file_path}: {str(e)}")