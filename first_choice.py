import time
import sys
class First:
    def __init__(self, choice):
        self.choice = choice




    def phone_window_wall(self):
        try:    
            if self.choice == 1:
                print()
                print()
                print()
                time.sleep(2)
                print("As you approach the, phone it starts to ring. It startles you")
                time.sleep(2)
                print("The caller id shows a bunch of characters, no name or phone")
                time.sleep(2)
                print('number for the caller. You wonder if the caller is the one who is')
                time.sleep(2)
                print('behind your current predicament. You notice the phone has full')
                time.sleep(2)
                print('reception! You think to yourself "I sure wish I remembered anyone\'s ')
                time.sleep(2)
                print("phone number... So, what do you do now?")
                print()
                print()

            elif self.choice == 2:
                print()
                print()
                print()
                time.sleep(2)
                print("You decide to walk to the window. The window starts to look more")
                time.sleep(2)
                print("distorted the closer you get. The window cracks open slightly ")
                time.sleep(2)
                print("as you continue to step forward and air in the room escapes through")
                time.sleep(2)
                print('the vacuum on the other side of it. You go to step back and the')
                time.sleep(2)
                print("window shuts and is no longer distorted. As you observe this weird")
                time.sleep(2)
                print("series of events, you realize the window reacts to your conscious ")
                time.sleep(2)
                print('decisions and actions regarding it. So the question is, what do you do:')         

            elif self.choice == 3:
                print()
                print()
                print()
                print()
                time.sleep(2)
                print("As you turn towards the mysteriously wavy wall, it acknowledges your")
                time.sleep(2)
                print('decision to walk towards it. A face manifests in the constantly')
                time.sleep(2)
                print("moving waves creasing what would be a flat wall in a normal world.")
                time.sleep(2)
                print('The wall\'s mouth begins to move as if it wants to speak, and says')
                time.sleep(2)
                print('"Hello Loser, I am the all-knowing entity that has placed you here."')
                time.sleep(2)
                print('"I will allow you to ask one of two questions...."')
                
                s = '''
                -- How does one escape from this crazy world?\n
                -- Why, of all people, were you the one to be chosen for this experience.
                '''
                for character in s:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(.1)
            
        except ValueError:
            print('''
                AAhem!!!(violent throat clear) I'm pretty sure this game is rated "Mature"....
                Whats your excuse for not paying attention to detail??? Enter 1, 2 or 3..... 
                ''')
        except NameError:
            print('''
                AAhem!!!(violent throat clear) I'm pretty sure this game is rated "Mature"....
                Whats your excuse for not paying attention to detail??? Enter 1, 2 or 3..... 
                ''')
