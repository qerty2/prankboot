# this is used to try out specific functions instead of randomly running one
# if you're looking for that, run main.py
import functions

print("This is designed to be used to call specific functions instead of running random ones for dev use. Check functions.py for list of options.")
while True:
    choice = input("What function do you want to run?: ")
    try:
        func=getattr(functions, choice)
        if callable(func):
            print(f"✅ Running {choice}\n")
            func()
            break
        else:
            print(f"❓ {choice} exists, but it isn't able to be called for some reason.\n")
            continue
    except AttributeError:
        print(f"❌ There is no function named {choice}\n")
        continue