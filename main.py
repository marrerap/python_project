import time 
import sys
from game_title import Title
from start_game import Start
from first_choice import First
from phone_choices import Phone
from window_choice import Window
from window_choice2 import Window2
from wall_choice import Wall



#-----------------------------------Game---Title---Screen---------------------------------------------------------------------------
# this is going to be the game title screen. this will run everytime the program is executed. 
continue_ = True

while continue_ == True:   
    Title()



    #----------------------------------------Start---The---Game--------------------------------------------------------------------------

    #this input is used to create the variable needed for the if/else statement built in the start game class.
    #i will use this to determine if the user wants to continue the game. the user will input a "y" or "n"
    time.sleep(1.5)
    game_start = input("> Do you want to try investigate this Instance of reality? (Y/N): ")

    # this will take the 'y' or 'n' and create an instance for the start_game class. this allows me to call the function 
    # I built in the Start class. without this i cannot run the next line of code which gives me my next bit of output. 
    start_yes = Start(game_start)


    #when I call call this attribute it will run the defined function in my Start class. It will output text based on the user's
    #input from the game_start question
    start_yes.start() 


    #-----------------------------------------Phone---Window---Wall----------------------------------------------------------------------
    # request which choice the user wants to make. do they want to choose the phone, window, wall. this will assign an
    # integer value to the first_choice variable.
    
    try:
        s = '''
            1.Do you reach for the phone?
            2.Do you head to the window to gaze into a star themed abyss?
            3.Do you check out the wall that is moving like waves in an ocean storm?'''
        for character in s:
                sys.stdout.write(character)
                sys.stdout.flush()
                time.sleep(.08)    
        first_choice = (int(input('''\n--> ''')))
    except ValueError:
        print('''
        Please select the options that were carefully listed for you.
        Don't make this more annoying than it needs to be ok...
        ''')
    except NameError:
        print('''
        Please select the options that were carefully listed for you.
        Don't make this more annoying than it needs to be ok...
        ''')

    # this call the First class function and create an instance that has the user's choice embedded in the instance
    try:
        user_choice = First(first_choice)


    # this will print the next prompt in the adventure based on the users choice of phone, wall, window.
    
        user_choice.phone_window_wall()
    # except NameError:
    #     print('''
    #     Please select the options that were carefully listed for you.
    #     Don't make this more annoying than it needs to be ok...
    #     ''')
        



        #take the first if statement for each choice's function and place. this will make returning true and false possible 

    #-------------------------------------Decision----Tree--------------------------------------------------------------------------------
    #--------------------------------------Phone----Choice's------------------------------------------------------------------------------
        if first_choice == 1:
            continue_ = Phone(first_choice)
            #Phone(first_choice)
            



        #-------------------------------------Window----Choice's------------------------------------------------------------------------------
        
        elif first_choice == 2:
            try:  
                s = '''
                1. Do you stay away from the window, hoping it remains closed?
                2. Do you walk towards the window, knowing you'll be pulled into an infinite void, ending your life"?'''
                for character in s:
                    sys.stdout.write(character)
                    sys.stdout.flush()
                    time.sleep(.1)
                window_choice = int(input("\n--> "))    
                if window_choice == 1:
                    continue_ = Window()
                elif window_choice == 2:            
                    continue_ = Window2()
            except ValueError:
                print('''
                ERROR CODE ID10T PLEASE ENTER A VALID CHOICE. 
                1 OR 2 ARE VALID CHOICES.. IN CASE YOU DIDN'T GET IT THE FIRST TIME.....           
                ''')
                print()
                print()
            
            
        



        #--------------------------------------Wall----Choice's-------------------------------------------------------------------------------
        elif first_choice == 3:
            continue_ = Wall(first_choice)
    except NameError:
        print('''
        Please select the options that were carefully listed for you.
        Don't make this more annoying than it needs to be ok...
        ''')
        
    
        
        
    












