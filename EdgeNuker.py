import time
import os
from elevate import elevate

def is_elevated():
    return os.getuid() == 0

clear = lambda: os.system('cls')
print('''I as a creator(sggzhs) not responsible for any damages caused by this program. It is meant only to delete Edge and Edge Webview 2. Press Enter to proceed or close this application.''')
input()

if not is_elevated():
    print("Additional administrator privileges are required. Press enter to request.")
    input()
    try:
        elevate()
    except:
        print("Something gone wrong during request.")

try:
    print("Starting removal...")
    os.system("taskkill /IM msedgewebview2.exe /F")
    os.system("taskkill /IM msedge.exe /F")
    os.system("taskkill /IM zWebview2Agent.exe /F")
    os.system("del /F /Q \"C:\\Program Files (x86)\\Microsoft\\Edge")
    os.system("del /F /Q \"C:\\Program Files (x86)\\Microsoft\\EdgeCore")
    os.system("del /F /Q \"C:\\Program Files (x86)\\Microsoft\\EdgeUpdate")
    print("Removal completed succesfully! Press enter to close this program.")
except:
    print("Looks like removal has failed. Try restarting. Press enter to close.")
input()
