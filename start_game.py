import time



class Start:
    def __init__(self, start_choice):
       self.start_choice = start_choice
       
      
    
    def start(self):
        try:    
            if self.start_choice == "n" or self.start_choice  == "N":
                return (f"Welp, if you never try, you never fail right?")
            elif self.start_choice == "y" or self.start_choice == "Y":
                print("***************************************************************")
                print()
                print()
                print()
                print("                    *WWWOOOOOSSSSSHHHHH*")
                time.sleep(1.5)
                print("        (The world around you has fully materialized)")
                print()
                print()
                time.sleep(2)
                print('You come to realize that you are in a bright, cube shaped room.')
                time.sleep(2)
                print('An instantaneous rush of cold air wraps around you like plastic')
                time.sleep(2)
                print('surrounding vacuum sealed meat. Goosebumps fill your skin down')
                time.sleep(2)
                print('to your fingertips and suddenly you begin to fear for your life.')
                time.sleep(2)
                print()
                print()
                print()
                print('The room vibrates, goes dark, then illuminates. There is now a')
                time.sleep(2)
                print('phone in front of you, a window to nowhere, and one of the walls')
                time.sleep(2)
                print('looks as if it\'s made of a liquid-like material. ')
                time.sleep(2)
                print('Now that you have shaken off the initial shock of being lost, you')
                time.sleep(2)
                print("you decide to attempt to figure a way out of this f**^&%n room!")
                print()
                print()
                print()
                print()
            
               
        except ValueError:
            print('''
                Ok, I see I need to remind you that there are only 2 options...
                Press either Y or N, ok bud.
                ''')    
