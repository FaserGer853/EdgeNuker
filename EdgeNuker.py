import subprocess
import time
import os

print("Programm ready to execute")
time.sleep(2)
os.system("clear")
os.system("pause")
os.system("clear")
print("Are you sure to run this program?")
time.sleep(2)
os.system("clear")
os.system("pause")
os.system("clear")
print("The creator of this software is not responsible for the damage caused")
time.sleep(2)
os.system("clear")
os.system("pause")
os.system("clear")

print("You can safely remove the edge files now.")
print("Close the program when you will finish.")
while True:
    try:
        a = open(f"C:\Program Files (x86)\Microsoft\Edge\Application\119.0.2151.44\EBWebView\x86\EmbeddedBrowserWebView.dll")
        b = open(f"C:\Program Files (x86)\Microsoft\Edge\Application\119.0.2151.44\EBWebView\x64\EmbeddedBrowserWebView.dll")
        os.system("taskkill /IM msedgewebview2.exe /F")
        os.system("taskkill /IM zWebview2Agent.exe /F")
        os.remove(a)
        os.remove(b)
    except Exception:
        pass
