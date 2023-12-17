import requests
import json
import discord
import aiohttp
import asyncio
import threading
import os

import http.server
import socketserver

class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Ok!")

port = 8080

httpd = socketserver.TCPServer(("", port), MyHandler)
print(f"Serving on port {port}")

async def main():
      while True:
          response = requests.get("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer")
          data = response.text

          json_data = json.loads(data)
          version = json_data["clientVersionUpload"]

          with open('version.txt', 'r') as file:
              saved_version = file.read()

          if version != saved_version:
              with open('version.txt', 'w') as file:
                  file.write(version)

              url = os.environ['WEBHOOK']

              async with aiohttp.ClientSession() as session:
                  webhook = discord.Webhook.from_url(url, session=session)

                  embed = discord.Embed.from_dict({
                      "title": f"Roblox Client has been updated to {version}.",
                      "color": 16711680,
                      "footer": {
                          "text": "Made by alexelmejor2017",
                          "icon_url": "https://cdn.discordapp.com/avatars/868534218442043412/3533157f851315f8696c607722f9fe3e.webp?size=128"
                      }
                  })

                  payload = {
                      "content": " @everyone **UPDATE DETECTED**",
                      "embeds": [embed]
                  }

                  await webhook.send(**payload)

          await asyncio.sleep(300)

if __name__ == "__main__":
    server_thread = threading.Thread(target=httpd.serve_forever)
    server_thread.start()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
