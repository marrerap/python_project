


def Window(window_option):
    if window_option ==2:
        window_choice = int(input('''
        1. Do you stay away from the window, hoping it remains closed?
        2. Do you walk towards the window, knowing you'll be pulled into an infinite void, ending your life"?
        --> '''))

        if window_choice == 1:
            print()
            print()        
            print('As you walk back to the center of the room, the windows opens.')
            print('The vacuum held back by the window is now sucking you towards it')
            print('You start squating, desperately reaching for anything to grab onto')
            print('realizing there is nothing to grasp, you are sucked out ... And')
            return True
        elif window_choice == 2:
            print()
            print()
            print('For some reason the idea of ending it all seems to be the best option')
            print('Why continue this game you\'re bored of.')
            print('You rush to the window, it opens as fast as you run to it.')
            print("You go to jump through the opening... And")
            return True
