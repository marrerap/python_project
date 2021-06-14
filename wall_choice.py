def Wall(wall_option):
    if wall_option == 3:
        print("         --------Which Will You Choose?--------")
        wall_choice = int(input('''
        1. How do I escape form here?
        2. Why was I chosen for this? 
        3. Call the wall a loser back, grab phone then lodge it towards the wall.
        --> '''))
        if wall_choice == 1:
            print()
            print()
            print("The wall speaks to you. Clearing its throat causes the lighted room to flicker")
            print('"There is only one way out" the wall coughs. You wait for it to continue speaking.')
            print('The walls gasps like a dying person in a really bad movie looking for an Oscar.')
            print('You yell "Hello" and get no response in return... And')
            return True

        elif wall_choice == 2:
            print()
            print()
            print('The wall speaks to you. The room reverberates with each word spoken.')
            print('"You are here because you suck as a human being. Your heart is no longer')
            print('pure. Your actions are tainted with ulterior motive and your mom hates you...')
            print('LMAO"')
            return False 
        elif wall_choice == 3:
            print()
            print()
            print("You scream with laughter, telling the wall that he is the Loser!")
            print('You grab the phone to throw at the wall. You throw it watching the')
            print('phone dig its way deeper into the face the wall constructed. ')
            print('The face starts to look familiar and you realize it\'s actually ')
            print('your face. A pain starts forming just behind your nose. It gets worse')
            print('as the phone in the wall gets deeper... And')
            return True