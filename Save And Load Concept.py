import os

print("/Start/ = Play New Game")
print("/Save/ = Save Current Game")
print("/Load/[Save Code] = Load Saved Game")
print("/User_Save/[User] = Enter Save User")
print("/User_Load/[User] = Load Save User")
print("/Help/ or /?/ = Display Help Menu Again")
print("/End/ = End Program")
print("")

while True:
    save = input("Enter Command: ")

    path1 = "C:\\Users\\"+save[11:]+"\\Desktop"
    path2 = "C:\\Users\\"+save[11:]+"\\Desktop\\Save_For_Game.txt"

    print("")

    if save.lower() == "/start/":
        print("Game Started")
    
    elif save.lower() == "/save/":
        print("Keep This Save Code Safe: [Save Code]")

    elif save[0] == "/" and save.lower()[1] == "l" and save.lower()[2] == "o" and save.lower()[3] == "a" and save.lower()[4] == "d" and save[5] == "/" and not save.lower() == "/load/":
        print("Game Loaded From Save")

    elif save[0] == "/" and save.lower()[1] == "u" and save.lower()[2] == "s" and save.lower()[3] == "e" and save.lower()[4] == "r" and save[5] == "_" and save.lower()[6] == "s" and save.lower()[7] == "a" and save.lower()[8] == "v" and save.lower()[9] == "e"  and save[10] == "/" and not save.lower() == "/user_save/":
        if os.path.exists(path1):
            with open("C:\\Users\\"+save[11:]+"\\Desktop\\Save_For_Game.txt", "w") as file:
                file.write("[Save_Code]")
            print("Game Saved To File")
        else:
            print("Invalid User")

    elif save[0] == "/" and save.lower()[1] == "u" and save.lower()[2] == "s" and save.lower()[3] == "e" and save.lower()[4] == "r" and save[5] == " " and save.lower()[6] == "s" and save.lower()[7] == "a" and save.lower()[8] == "v" and save.lower()[9] == "e"  and save[10] == "/" and not save.lower() == "/user_save/":
        if os.path.exists(path1):
            with open("C:\\Users\\"+save[11:]+"\\Desktop\\Save_For_Game.txt", "w") as file:
                file.write("[Save_Code]")
            print("Game Saved To File")
        else:
            print("Invalid User")
    
    elif save[0] == "/" and save.lower()[1] == "u" and save.lower()[2] == "s" and save.lower()[3] == "e" and save.lower()[4] == "r" and save[5] == "_" and save.lower()[6] == "l" and save.lower()[7] == "o" and save.lower()[8] == "a" and save.lower()[9] == "d"  and save[10] == "/" and not save.lower() == "/user_load/":
        if os.path.exists(path2):
            if os.path.isfile(path2):
                with open("C:\\Users\\"+save[11:]+"\\Desktop\\Save_For_Game.txt") as file:
                    print("Game Loaded From Save:", file.read())
        else:
            print("No Save")

    elif save[0] == "/" and save.lower()[1] == "u" and save.lower()[2] == "s" and save.lower()[3] == "e" and save.lower()[4] == "r" and save[5] == " " and save.lower()[6] == "l" and save.lower()[7] == "o" and save.lower()[8] == "a" and save.lower()[9] == "d"  and save[10] == "/" and not save.lower() == "/user_load/":
        if os.path.exists(path2):
            if os.path.isfile(path2):
                with open("C:\\Users\\"+save[11:]+"\\Desktop\\Save_For_Game.txt") as file:
                    print("Game Loaded From Save:", file.read())
        else:
            print("No Save")
            
    elif save.lower() == "/help/" or save == "/?/":
        print("/Start/ = Play New Game")
        print("/Save/ = Save Current Game")
        print("/Load/[Save Code] = Load Saved Game")
        print("/User_Save/[User] = Enter Save User")
        print("/User_Load/[User] = Load Save User")
        print("/Help/ or /?/ = Display Help Menu Again")
        print("/End/ = End Program")
        
    elif save.lower() == "/end/":
        break

    else:
        print("Invalid Command")

    print("")
