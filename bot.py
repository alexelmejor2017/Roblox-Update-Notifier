import requests
import discord
import aiohttp
import asyncio
import json
from bs4 import BeautifulSoup
import random
import colorama
from colorama import Fore, Style

colorama.init()

cycle_count = 0

async def check_web_version():
    try:
        response = requests.get("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer", timeout=10)
        data = response.text
        json_data = json.loads(data)
        version = json_data["clientVersionUpload"]
        print(f"Web version checked: {version}")
        return version
    except Exception as e:
        print(f"Error checking web version: {e}")
        return None

async def check_mac_version():
    try:
        response = requests.get("https://clientsettingscdn.roblox.com/v2/client-version/MacPlayer", timeout=10)
        data = response.text
        json_data = json.loads(data)
        version = json_data["clientVersionUpload"]
        print(f"Mac version checked: {version}")
        return version
    except Exception as e:
        print(f"Error checking mac version: {e}")
        return None

async def check_android_version():
    try:
        response = requests.get("https://apkpure.net/roblox-android/com.roblox.client", timeout=10)
        soup = BeautifulSoup(response.content, "html.parser")
        latest_version_div = soup.find(string=lambda text: "What's new in the latest" in text)
        if latest_version_div:
            version = latest_version_div.split()[-1]
            print(f"Android version checked: {version}")
            return version
        print("Android version could not be found.")
        return None
    except Exception as e:
        print(f"Error checking android version: {e}")
        return None

async def check_ios_version():
    try:
        url = 'https://apps.apple.com/us/app/roblox/id431946152'
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        version_tag = soup.find('p', class_='l-column small-6 medium-12 whats-new__latest__version')
        if version_tag:
            version = version_tag.text.strip().replace('Version ', '')
            print(f"iOS version checked: {version}")
            return version
        print("iOS version could not be found.")
        return None
    except Exception as e:
        print(f"Error checking iOS version: {e}")
        return None

async def process_updates(platform, version, saved_version):
    url = "" ## PUT YOUR WEBHOOK HERE
    async with aiohttp.ClientSession() as session:
        webhook = discord.Webhook.from_url(url, session=session)
        embed = discord.Embed.from_dict({
            "title": f"Roblox {platform} Version has been updated to {version}",
            "description": f"Old Version: ``{saved_version}``\nNew Version: ``{version}``",
            "color": 16711680,
            "footer": {
                "text": "Made by alexelmejor2017",
            }
        })
        await webhook.send(content=f" @everyone **{platform} UPDATE DETECTED**", embed=embed)
        print(f"{platform} Update Detected!")

async def main():
    global cycle_count
    print("\n" + Fore.BLUE + "Update Notifier Started" + Style.RESET_ALL)
    while True:
        cycle_count += 1

        web_version = await check_web_version()
        mac_version = await check_mac_version()
        android_version = await check_android_version()
        ios_version = await check_ios_version()

        with open('web_version.txt', 'r') as file:
            saved_web_version = file.read().strip() or "null"
        
        with open('mac_version.txt', 'r') as file:
            saved_mac_version = file.read().strip() or "null"

        with open('android_version.txt', 'r') as file:
            saved_android_version = file.read().strip() or "null"

        with open('ios_version.txt', 'r') as file:
            saved_ios_version = file.read().strip() or "null"

        tasks = []
        if web_version and web_version != saved_web_version:
            tasks.append(process_updates("WEB", web_version, saved_web_version))
            with open('web_version.txt', 'w') as file:
                file.write(web_version)

        if mac_version and mac_version != saved_mac_version:
            tasks.append(process_updates("MAC", mac_version, saved_mac_version))
            with open('mac_version.txt', 'w') as file:
                file.write(mac_version)

        if android_version and android_version != saved_android_version:
            tasks.append(process_updates("ANDROID", android_version, saved_android_version))
            with open('android_version.txt', 'w') as file:
                file.write(android_version)

        if ios_version and ios_version != saved_ios_version:
            tasks.append(process_updates("iOS", ios_version, saved_ios_version))
            with open('ios_version.txt', 'w') as file:
                file.write(ios_version)

        if tasks:
            await asyncio.gather(*tasks)

        print("\n" + Fore.GREEN + f"Version check cycle {cycle_count} complete. Sleeping for 300 seconds..." + Style.RESET_ALL)
        await asyncio.sleep(300)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(main())
