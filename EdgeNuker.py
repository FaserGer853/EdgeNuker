import time
import os

os.system('echo 3 | sudo tee /proc/sys/vm/drop_caches >/dev/null 2>&1')
clear = lambda: os.system('cls')
print("Programm ready to execute")
time.sleep(2)
clear()
os.system("pause")
clear()
print("Are you sure to run this program?")
time.sleep(2)
clear()
os.system("pause")
clear()
print("The creator (sggzhs) of this software is not responsible for the damage caused")
time.sleep(2)
clear()
os.system("pause")
clear()

print("You can safely remove the edge files now.")
print("Close the program when you will finish.")
while True:
    try:
        os.system("taskkill /IM msedgewebview2.exe /F")
        os.system("taskkill /IM msedge.exe /F")
        os.system("taskkill /IM zWebview2Agent.exe /F")
        os.system("del /F /Q \"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\119.0.2151.44\\EBWebView\\x86\\EmbeddedBrowserWebView.dll")
        os.system("del /F /Q \"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\119.0.2151.44\\EBWebView\\x64\\EmbeddedBrowserWebView.dll")
    except Exception:
        pass
