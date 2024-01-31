### PATCHED

So, Replit decided to make an update so you can't run a Replit 24/7 for free anymore. Soon I will update this GitHub with a tutorial on another host, stay tuned.



### What is this

This is a bot that every 5 minutes it will check the current version of the Roblox Client, if the version changes then it will send a message to the specified webhook.

### How to set this up

1. Create a Replit and Import from GitHub.
2. At the bottom left corner, where it says "Tools" look for "Secrets" and click on that.
3. A window called "Secrets" should pop up, click "New Secret".
4. Where it says "Key" write "WEBHOOK" and in the value enter your webhook url.
5. Then click "Add Secret".
6. Then, run your replit.
7. A Web Server should come up, just click on the button specified in the image below.
![image](https://github.com/alexelmejor2017/Roblox-Update-Notifier/assets/74315786/a2ff2335-60c8-41be-a524-9ec614f1f62a)
8. It will take you to your replit web server, copy the url.
9. Create an account and/or login to https://uptimerobot.com.
10. Create a New Monitor, where it says "Monitor Type" select HTTPS.
11. At "Friendly Name" just type wathever you want.
12. At "URL OR IP" type the Web Server url you just copied.
13. At "Monitoring Interval" place it on 5 minutes.
14. Then click "Create Monitor"

And there you have it folks, your own bot that notifies you when Roblox updates.

### I got the error "OSError: [Errno 98] Address already in use"
![image](https://github.com/alexelmejor2017/Roblox-Update-Notifier/assets/74315786/78896311-fbe8-4a88-b039-50821742867d)

That's a bug, I will try to fix it, but for now you can either wait around 15-30 seconds and then boot it back on and it should work or go to the shell and type "kill 1", then wait a few seconds for the replit to reconnect, boot again and it will be fixed.
