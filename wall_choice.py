import time
import sys

def Wall(wall_option):
    try:    
        if wall_option == 3:
            print()
            print()
            print("         --------Which Will You Choose?--------")        
            s = '''
            1. How do I escape form here?
            2. Why was I chosen for this? 
            3. Call the wall a loser back, grab phone then lodge it towards the wall.'''
            for character in s:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(.1)
            wall_choice = int(input('''\n--> '''))
            if wall_choice == 1:
                print()
                print()
                time.sleep(2)
                print("The wall speaks to you. Clearing its throat causes the lighted room to flicker")
                time.sleep(2)
                print('"There is only one way out" the wall coughs. You wait for it to continue speaking.')
                time.sleep(2)
                print('The walls gasps like a dying person in a really bad movie looking for an Oscar.')
                time.sleep(2)
                print('You yell "Hello" and get no response... And everything goes black...')
                time.sleep(2)
                print('time to restart the game... you lose')
                return True

                

            elif wall_choice == 2:
                print()
                print()
                time.sleep(2)
                print('The wall speaks to you. The room reverberates with each word spoken.')
                time.sleep(2)
                print('"You are here because you suck as a human being. Your heart is no longer')
                time.sleep(2)
                print('pure. Your actions are tainted with ulterior motive and your mom hates you...')
                time.sleep(2)
                print('LMAO...Loser, try again..."')
                return True 
            elif wall_choice == 3:
                print()
                print()
                time.sleep(2)
                print("You scream with laughter, telling the wall that he is the Loser!")
                time.sleep(2)
                print('You grab the phone to throw at the wall. You throw it watching the')
                time.sleep(2)
                print('phone dig its way deeper into the face the wall constructed. ')
                time.sleep(2)
                print('The face starts to look familiar and you realize it\'s actually ')
                time.sleep(2)
                print('your face. A pain starts forming just behind your nose. It gets worse')
                time.sleep(2)
                print('as the phone in the wall gets deeper... And your face explodes...')
                time.sleep(2)
                print('time to restart... you lose...')
                return True
            
    except ValueError:
        print('''
                You're a special kind of special aint'cha buddy...smh...
                Alright man, you got three choices now, use context clue and figure it out...
                ''')
