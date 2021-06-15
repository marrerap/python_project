import time
import sys

def Phone(phone_option):
    try:    
        if phone_option == 1:
            s = '''
            1. Do you answer the phone in hopes of confronting the root cause of everything happening?
            2. Do you send the caller to voicemail and try to reach "911"?'''
            for character in s:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(.1)
            phone_choice = int(input('''\n--> '''))
            if phone_choice == 1:
                print()
                print()
                time.sleep(2)
                print('You press answer on the small led screen, raise the phone to your ear,')
                time.sleep(2)
                print("and say hello. You listen intently waiting for something on the other")
                time.sleep(2)
                print("side to say something.... ")
                time.sleep(2)
                print("You hear nothing on the other end and decide to hang up and try to make a")
                time.sleep(2)
                print('call.... And everything goes black... time to restart the game... you lose...')
                time.sleep(2)
                print()
                print()
                return True
                
            elif phone_choice == 2:
                print()
                print()
                time.sleep(2)
                print("You swipe the caller to voicemail. The room starts to vibrate and then stops.")
                time.sleep(2)
                print('You focus back on your phone and dial "911". An operator answers, Yet as you')
                time.sleep(2)
                print('try to reply, no sound comes from your mouth.... And everything goes black...')
                time.sleep(2)
                print('time to restart the game... you lose...')
                time.sleep(2)
                print()
                print()
                return True
            
    except ValueError:
        print('''
        I can see why you're stuck here... I don't even know you...
        but this is pathetic..... Press 1 or 2 chair warmer!!!
        ''')
        print()
        print()