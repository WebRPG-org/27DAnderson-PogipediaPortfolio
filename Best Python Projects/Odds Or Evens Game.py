import random

games = -1
set_run_false = False
running1 = True

while running1 == True:

    scoreboard = [0, 0]

    running2 = True
    
    while running2 == True:
        play = input("How many times would you like to play (1, 3, 5, infinite)? ")
        
        if play == "1" or play == "3" or play == "5" or play.lower() == "infinite":
            print("✓")
            running2 = False
        else:
            print("✗")
    if play.lower() == "infinite":
        print("")
        print("Enter End, Stop, or Finish at any time to end game.")
        play = 999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

    play = int(play)
    
    for i in range(0, play):

        print("")
        print("")
        print("Game " + str(i + 1) + ":")
        print("")

        running3 = True
        while running3 == True:
        
            choice = input("Pick odds or evens: ")
            
            if choice.lower() == "stop" and play > 5 or choice.lower() == "end" and play > 5 or choice.lower() == "finish" and play > 5:
                set_run_false = True
                
            if set_run_false == True:
                break
            if choice.lower() == "odds" or choice.lower() == "evens" or choice.lower() == "odd" or choice.lower() == "even":
                print("✓")
                running3 = False
            else:
                print("✗")

        running4 = True
        while running4 == True:

            if set_run_false == True:
                break
            
            playerNum = input("How many fingers do you throw (1-5)? ")

            if playerNum.lower() == "stop" and running1 == True and play > 5 or playerNum.lower() == "end" and running1 == True and play > 5 or playerNum.lower() == "finish" and running1 == True and play > 5:
                set_run_false = True

            if set_run_false == True:
                break

            if playerNum.isdigit() == True:
                playerNum = int(playerNum)
                if playerNum > 0 and playerNum < 6:
                    print("✓")
                    playerNum = int(playerNum)
                    running4 = False
                else:
                    print("✗")
            else:
                print("✗")
            games = i
        if set_run_false == True:
            running1 = False
            break
        
        print("")

        computerNum = random.randint(1, 5)

        print("Computer throws:", computerNum)

        total = playerNum + computerNum

        print("Total fingers are:", total)

        if choice.lower() == "odds" and total % 2 == 1 or choice.lower() == "odd" and total % 2 == 1:
            print("Player wins!")
            scoreboard[0] += 1
        elif choice.lower() == "evens" and total % 2 == 0 or choice.lower() == "even" and total % 2 == 0:
            print("Player wins!")
            scoreboard[0] += 1
        else:
            print("Computer wins!")
            scoreboard[1] += 1

        print("")
        print("Player:", scoreboard[0])
        print("Computer:", scoreboard[1])
        
    running1 = False

print("")

if play > 5:
    if scoreboard[0] > scoreboard[1]:
        print("Player wins " + str(scoreboard[0]) + " out of " + str(games + 1) + " games.")
    elif scoreboard[1] > scoreboard[0]:
        print("Computer wins " + str(scoreboard[1]) + " out of " + str(games + 1) + " games.")
    elif scoreboard[0] == scoreboard[1]:
        print("Player and Computer tied " + str(scoreboard[0]) + " to " + str(scoreboard[1]) + " out of " + str(games + 1) + " games.")
else:
    if scoreboard[0] > scoreboard[1]:
        print("Player wins " + str(scoreboard[0]) + " out of " + str(play) + " games.")
    elif scoreboard[1] > scoreboard[0]:
        print("Computer wins " + str(scoreboard[1]) + " out of " + str(play) + " games.")
