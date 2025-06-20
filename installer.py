# ngl I wrote the main functions and had ChatGPT write the logic for the installer (except for administrator and file paths) cause im lazy
# todo: rewrite
import os, sys, ctypes, shutil

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    params = ' '.join([f'"{arg}"' for arg in sys.argv])
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)
    sys.exit()

print("Welcome!\nBe advised; this will make the script start up automatically when your computer does and can be EXTREMELY annoying.")

startup_path = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\main.py"

while True:
    status = input("Type install to install, or remove to remove: ").lower().strip()
    if status not in ("install", "remove"):
        print("Invalid option, try again.\n")
        continue

    elif status == "install":
        input("Are you sure? Press Enter to continue: ")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        source = os.path.join(script_dir, "main.py")
        target = startup_path

        try:
            shutil.copy(source, target)
            print("Installed successfully!")
        except Exception as e:
            print(f"Failed to install: {e}")
        break

    elif status == "remove":
        try:
            if os.path.exists(startup_path):
                os.remove(startup_path)
                print("Removed successfully!")
            else:
                print("No installed file found to remove.")
        except Exception as e:
            print(f"Failed to remove: {e}")
        break
