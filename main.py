from start_game import Start



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
game_start = input("> Do you want to try investigate this Instance of reality? (Y/N): ")

start = Start(game_start)

Start.start(start) 

# if game_start == "n" or game_start == "N":
#     print("Welp, if you never try, you never fail right?")
# elif game_start == "y" or game_start == "Y":
#     intro()
