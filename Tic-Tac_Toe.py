import random

while True:
    p1 = None
    p2 = None
    
    gamemode = None

    board = {"1":"_", "2":"_", "3":"_", "4":"_", "5":"_", "6":"_", "7":"_", "8":"_", "9":"_",}

    spots = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "end"]
    comp = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    while True:
        gamemode = input("Enter gamemode [1 for player vs player, 2 for player vs computer, 0 or end for leave]: ")
        if gamemode == "1" or gamemode == "2" or gamemode == "0" or gamemode == "end":
            break
    if gamemode == "0" or gamemode == "end":
        break
    if gamemode == "1":
        print(board["1"], end=' ')
        print(board["2"], end=' ')
        print(board["3"])
        print(board["4"], end=' ')
        print(board["5"], end=' ')
        print(board["6"])
        print(board["7"], end=' ')
        print(board["8"], end=' ')
        print(board["9"])

        while True:

            p1 = None
            p2 = None
            
            while True:
            
                p1 = input("Place x on spot: ")
                if p1 in spots:
                    spots.remove(p1)
                    break
            if p1 == "0" or p1 == "end":
                break
            board[p1] = "x"
            print(board["1"], end=' ')
            print(board["2"], end=' ')
            print(board["3"])
            print(board["4"], end=' ')
            print(board["5"], end=' ')
            print(board["6"])
            print(board["7"], end=' ')
            print(board["8"], end=' ')
            print(board["9"])

            while True:
                
                p2 = input("Place o on spot: ")
                if p2 in spots:
                    spots.remove(p2)
                    break
            if p2 == "0" or p1 == "end":
                break
            board[p2] = "o"
            print(board["1"], end=' ')
            print(board["2"], end=' ')
            print(board["3"])
            print(board["4"], end=' ')
            print(board["5"], end=' ')
            print(board["6"])
            print(board["7"], end=' ')
            print(board["8"], end=' ')
            print(board["9"])
            if p1 == "0" or p1 == "end" or p2 == "0" or p2 == "end":
                break
            
    if gamemode == "2":
        print(board["1"], end=' ')
        print(board["2"], end=' ')
        print(board["3"])
        print(board["4"], end=' ')
        print(board["5"], end=' ')
        print(board["6"])
        print(board["7"], end=' ')
        print(board["8"], end=' ')
        print(board["9"])

        while True:

            p1 = None
            p2 = None
            
            while True:
            
                p1 = input("Place x on spot: ")
                if p1 == "0" or p1 == "end":
                    break
                if p1 in spots:
                    spots.remove(p1)
                    comp.remove(p1)
                    break
            if p1 == "0" or p1 == "end":
                break
            board[p1] = "x"
            print(board["1"], end=' ')
            print(board["2"], end=' ')
            print(board["3"])
            print(board["4"], end=' ')
            print(board["5"], end=' ')
            print(board["6"])
            print(board["7"], end=' ')
            print(board["8"], end=' ')
            print(board["9"])

            p2 = random.choice(comp)
            spots.remove(p2)
            comp.remove(p2)
            print("Computer chooses:", p2)
                
            board[p2] = "o"
            print(board["1"], end=' ')
            print(board["2"], end=' ')
            print(board["3"])
            print(board["4"], end=' ')
            print(board["5"], end=' ')
            print(board["6"])
            print(board["7"], end=' ')
            print(board["8"], end=' ')
            print(board["9"])
            if p1 == "0" or p1 == "end" or p2 == "0" or p2 == "end":
                break

    while True:     
        play = input("Would you like to play again? ")
        if play.lower() == "no" or play.lower() == "n" or play.lower() == "yes" or play.lower() == "y":
            break
    if play.lower() == "no" or play.lower() == "n":
        break
