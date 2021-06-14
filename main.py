from start_game import Start
from phone import Phone


# def intro():
#     print()
#     print()
#     print()
#     print("                    *WWWOOOOOSSSSSHHHHH*")
#     print("        (The world around you has fully materialized)")
#     print()
#     print()

print()
print()
print('                  ------|||||--|||||------')
print('                  |                      |')
print('                  |  Instance  Override  |')
print('                  |                      |')
print('                  ------|||||--|||||------')
print()
print()
print("        (DARKNESS SURROUNDS YOU...NO LIGHT IS SIGHT!)")
print()
print("                     ------------------              ")
print()
print('                   ... Where...am...I?')
print('  "HEEEELLLLLOOOOO!!!" Hmph, I have no idea what is going on...')
print()
print()
print("            You know something isn't quite right.")



#this input is used to create the variable needed for the if/else statement built in the start game class.
game_start = input("> Do you want to try investigate this Instance of reality? (Y/N): ")
#this variable will 
start = Start(game_start)
#this is similar to print the statement below
Start.start(start) 








phone = (int(input('''
            1.Do you reach for the phone?
            2.Do you head to the window to gaze into star themed abyss?
            3.Do you check out the wall that is moving like waves in an ocean storm?
            ''')))

phone_choice = Phone(phone)


























































# if game_start == "n" or game_start == "N":
#     print("Welp, if you never try, you never fail right?")
# elif game_start == "y" or game_start == "Y":
#     intro()
