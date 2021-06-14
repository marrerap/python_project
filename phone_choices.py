

def Phone(phone_option):
    if phone_option == 1:
        phone_choice = int(input('''
        1. Do you answer the phone in hopes of confronting the root cause of everything happening?
        2. Do you send the caller to voicemail and try to reach "911"?
        --> '''))
        if phone_choice == 1:
            print()
            print()
            print('You press answer on the small led screen, raise the phone to your ear,')
            print("and say hello. You listen intently waiting for something on the other")
            print("side to say something.... ")
            print("You hear nothing on the other end and decide to hang up and try to make a")
            print('call.... And')
            print()
            print()
            return True
        elif phone_choice == 2:
            print()
            print()
            print("You swipe the caller to voicemail. The room starts to vibrate and then stops.")
            print('You focus back on your phone and dial "911". An operator answers, Yet as you')
            print('try to reply, no sound comes from your mouth.... And')
            print()
            print()
            return True