import os

os.system('echo 3 | sudo tee /proc/sys/vm/drop_caches >/dev/null 2>&1')
print("You can now remove the files. Close the programm when done.")
while True:
    os.system("taskkill /IM msedgewebview2.exe /F")
    os.system("taskkill /IM msedge.exe /F")
    os.system("taskkill /IM zWebview2Agent.exe /F")
    os.system("del /F /Q \"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\119.0.2151.44\\EBWebView\\x86\\EmbeddedBrowserWebView.dll")
    os.system("del /F /Q \"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\119.0.2151.44\\EBWebView\\x64\\EmbeddedBrowserWebView.dll")
