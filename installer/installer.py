# installs the script to the startup folder
# if you just want to try out the functions without installing check tester.py

import os
import sys
import ctypes
import subprocess
import shutil

# making script run with administrator, as you need those perms to add / remove stuff from startup
if not ctypes.windll.shell32.IsUserAnAdmin():
    script = os.path.abspath(sys.argv[0])
    params = subprocess.list2cmdline([script] + sys.argv[1:])
    rc = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
    if rc <= 32:
        raise RuntimeError(f"Failed to make administrator, error code: {rc}")
    sys.exit()

path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup"
item_path = "prankboot.exe"
delete_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\prankboot.exe"

def install():
    try:
        shutil.copy(item_path, path)
        print("\n✅ Installed successfully!")
        input("Press enter to finish: ")
        sys.exit()
    except PermissionError:
        print("\n❌ Permission error, please try closing and re-running the script")
        input("Press enter to exit: ")
        sys.exit()
    except FileNotFoundError:
        print("\n❌ EXE missing. Please re-download the release")
        input("Press enter to exit: ")
        sys.exit()

def remove():
    try:
        os.remove(delete_path)
        print("\n✅ Uninstalled successfully!")
        input("Press enter to finish: ")
        sys.exit()
    except PermissionError:
        print("\n❌ Permission error, please try closing and re-running the script")
        input("Press enter to exit: ")
        sys.exit()
    except FileNotFoundError:
        print("\n❌ prankboot is not installed.")
        input("Press enter to exit: ")
        sys.exit()


print("Welcome!")
while True:
    choice = input("Type install to install, and remove to remove: ").strip().lower()

    if choice not in ["install", "remove"]:
        print("Invalid choice, try again.\n")
        continue

    elif choice == "install":
        install()
        break

    elif choice == "remove":
        remove()
        break