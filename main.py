# if you're just trying to check out the functions, use tester.py
import random
import sys
import functions

def main(): # runs one of the functions in functions.py
    funcs = [
        func for name, func in vars(functions).items()
        if callable(func) and not name.startswith("__")
    ]
    random.choice(funcs)()

def startup(): # rolling 1 in 4 chance to run the main script
    run = random.randint(1,4)
    if run == 1:
        main()
    else:
        sys.exit()
startup()