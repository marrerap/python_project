from game_title import Title
from start_game import Start
from first_choice import First
from phone_choices import Phone
from window_choice import Window
from wall_choice import Wall
#-----------------------------------Game---Title---Screen---------------------------------------------------------------------------
# this is going to be the game title screen. this will run everytime the program is executed. 

Title()



#----------------------------------------Start---The---Game--------------------------------------------------------------------------

#this input is used to create the variable needed for the if/else statement built in the start game class.
#i will use this to determine if the user wants to continue the game. the user will input a "y" or "n"
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
first_choice = (int(input('''
    1.Do you reach for the phone?
    2.Do you head to the window to gaze into a star themed abyss?
    3.Do you check out the wall that is moving like waves in an ocean storm?
    --> ''')))

# this call the First class function and create an instance that has the user's choice embedded in the instance
user_choice = First(first_choice)


# this will print the next prompt in the adventure based on the users choice of phone, wall, window.
user_choice.phone_window_wall()




    

#-------------------------------------Decision----Tree--------------------------------------------------------------------------------
#--------------------------------------Phone----Choice's------------------------------------------------------------------------------

Phone(first_choice)



#-------------------------------------Window----Choice's------------------------------------------------------------------------------

Window(first_choice)



#--------------------------------------Wall----Choice's-------------------------------------------------------------------------------

Wall(first_choice)












