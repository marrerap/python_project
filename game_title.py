import time
import sys

def Title():
    print()
    print()
    print('                  ------|||||--|||||------')
    print('                  |                      |')
    print('                  |  Instance  Override  |')
    print('                  |                      |')
    print('                  ------|||||--|||||------')
    print()
    print()
    time.sleep(1.5)
    print("        (DARKNESS SURROUNDS YOU...NO LIGHT IS SIGHT!)")
    print()
    time.sleep(1.5)
    print("                     ------------------              ")
    print()
    s = '                    ... Where...am...I?\n'
    for character in s:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.1)
    s1 = '  "HEEEELLLLLOOOOO!!!" Hmph, I have no idea what is going on...'
    for character in s1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.1)
    print()
    print()
    time.sleep(1.5)
    print("            You know something isn't quite right.")