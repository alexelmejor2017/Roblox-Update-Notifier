# Roblox Update Notifier

This is a program I made in Python a while ago which, after a set delay, it notifies the user through a Discord Webhook if Roblox has updated. It supports almost every version of Roblox, including Windows, Mac, Android and iOS.

# How it works

The logic is very simple. The program runs in a loop with a delay of 300 seconds (or 5 minutes) by default. After which period it will check the current version number on different platforms, and if the version number is different from the one saved in the text file, it will assume roblox has updated, therefore it will overwrite it and send a message through a webhook. I have decided to store the versions in text files because in case the VPS went offline, the version would be saved and once it came back online it wouldnt send false update alerts.

# How to setup

1. Download Python 3.9 or higher (I suggest always using the latest version)
2. Download the repository and extract everything in a folder
3. In that folder open a command prompt and type the command `pip install -r requirements.txt`
4. Run the file bot.py

**IMPORTANT:** Ensure that the names of the files remain unchanged, otherwise the program may not work properly
