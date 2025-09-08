import random
import time

while True:
    
    playing = "None"
    
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    wordslist = ["other", "there", "which", "their", "about", "write", "would", "these", "thing", "could", "number", "sound", "people", "water", "first", "place", "where",]
    
    #old: parts = ["head", "body", "Left Leg", "Right Leg", "Left Arm", "Right Arm"]
    #old: hard_parts = ["head", "body", "Left Leg", "Right Leg", "Left Arm", "Right Arm", "Shirt", "Pants", "Socks", "Shoes", "Glasses", "Hat"]

    parts = ["6", "5", "4", "3", "2", "1"]
    hard_parts = ["12", "11", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
    
    parts_index = None

    correct_letters = []

    incorrect_letters = []
    
    guess = None
    gamemode = None
    word = None
    
    while True:
    
        gamemode = input("Enter gamemode [1 for default player vs player(s), 2 for player vs player(s) with more guesses, 3 for computer guesses word, 4 for computer makes lowercase letters password with less guess, 5 for computer makes lowercase letters password with more guess, 6 for computer makes pin, 7 for computer chooses a word from a predetermined list]: ")

        if gamemode == "1" or gamemode == "2" or gamemode == "3" or gamemode == "4" or gamemode == "5" or gamemode == "6" or gamemode == "7":
            break

    if gamemode == "1" or gamemode == "2":

        while True:

            print("")
            word = input("Please enter your word: ")

            if word == "":
                continue
            elif ' ' in word:
                continue
            elif word.isalpha() == False:
                continue
            else:
                word = word.lower()
                break

        for i in range(50):
            print("")

        while True:

            display_word = ""
            guess_word = ""
            
            for char in word:
                
                if char in correct_letters:
                    guess_word += char
                    display_word += char
                    display_word += " "
                else:
                    guess_word += "_"
                    display_word += "_ "

            print("The word is:", display_word)
            print("")


            if gamemode == "1":
                if guess_word == word:
                    break
                elif parts_index == None:
                    print("Parts are")
                elif parts_index == 6:
                    break
                else:
                    print("Parts are", *parts[0:parts_index], sep=", ")
            if gamemode == "2":
                if guess_word == word:
                    break
                elif parts_index == None:
                    print("Parts are")
                elif parts_index == 12:
                    break
                else:
                    print("Parts are", *hard_parts[0:parts_index], sep=", ")
            
            print("Remaining letters are: " + (str(letters)[1:-1]))

            print("Correct letters are: " + (str(correct_letters)[1:-1]))

            print("Incorrect letters are: " + (str(incorrect_letters)[1:-1]))

            print("")
        
            while True:
                guess = input("Other player(s), guess a letter: ")

                if len(guess) == 1 and guess.isalpha() == True:
                    guess = guess.lower()
                    break

            try:
                letters.remove(guess)
            
                if guess in word:

                    print("")
                    print("Word contains "+guess+".")
                    print("")

                    correct_letters.append(guess)
            
                elif guess not in word:

                    print("")
                    print("Word does not contain "+guess+".")
                    print("")

                    incorrect_letters.append(guess)

                    if parts_index == None:
                        parts_index = 1
                    else:
                        parts_index += 1

            except ValueError:
                print("")
                print("Letter already guessed or not valid.")
                print("")

        if gamemode == "2":
            if parts_index == 12:
                print("Parts are", *hard_parts[0:parts_index], sep=", ")
                print("Remaining letters are: " + (str(letters)[1:-1]))
                print("Correct letters are: " + (str(correct_letters)[1:-1]))
                print("Incorrect letters are: " + (str(incorrect_letters)[1:-1]))
                print("")
                print("Word maker wins, the word was \""+ word+"\".")
            elif guess_word == word:
                print("Parts are", *hard_parts[0:parts_index], sep=", ")
                print("Remaining letters are: " + (str(letters)[1:-1]))
                print("Correct letters are: " + (str(correct_letters)[1:-1]))
                print("Incorrect letters are: " + (str(incorrect_letters)[1:-1]))
                print("")
                print("Word guesser(s) wins, the word was \""+ word+"\".")

        print("")

        while True:
            playing = input("Play again? (Y/N): ")

            if playing.isdigit == True:
                continue
            elif playing.lower() == "yes" or playing.lower() == "y" or playing.lower() == "no" or playing.lower() == "n":
                break

        if playing.lower() == "no" or playing.lower() == "n":
            break
        
    if gamemode == "3":

        while True:

            print("")
            word = input("Please enter your word: ")

            if word == "":
                continue
            elif ' ' in word:
                continue
            elif word.isalpha() == False:
                continue
            else:
                word = word.lower()
                break

        for i in range(50):
            print("")

        while True:

            display_word = ""
            guess_word = ""
            
            for char in word:
                
                if char in correct_letters:
                    guess_word += char
                    display_word += char
                    display_word += " "
                else:
                    guess_word += "_"
                    display_word += "_ "

            print("The word is:", display_word)
            print("")
            
            if guess_word == word:
                break
            elif parts_index == None:
                print("Parts are")
            elif parts_index == 6:
                break
            else:
                print("Parts are", *parts[0:parts_index], sep=", ")
            
            print("Remaining letters are: " + (str(letters)[1:-1]))

            print("Correct letters are: " + (str(correct_letters)[1:-1]))

            print("Incorrect letters are: " + (str(incorrect_letters)[1:-1]))

            print("")

            time.sleep(2)
        
            
            computer_guess = (random.choice(letters))
            print("Computer guesses: "+computer_guess)
            time.sleep(2)

            try:
                letters.remove(computer_guess)
            
                if computer_guess in word:

                    print("")
                    print("Word contains "+computer_guess+".")
                    print("")

                    correct_letters.append(computer_guess)
            
                elif computer_guess not in word:

                    print("")
                    print("Word does not contain "+computer_guess+".")
                    print("")

                    incorrect_letters.append(computer_guess)

                    if parts_index == None:
                        parts_index = 1
                    else:
                        parts_index += 1

            except ValueError:
                print("")
                print("Letter already guessed or not valid.")
                print("")

        if parts_index == 6:
            print("Parts are", *parts[0:parts_index], sep=", ")
            print("Remaining letters are: " + (str(letters)[1:-1]))
            print("Correct letters are: " + (str(correct_letters)[1:-1]))
            print("Incorrect letters are: " + (str(incorrect_letters)[1:-1]))
            print("")
            print("You win, the word was \""+ word+"\".")
        elif guess_word == word:
            print("Parts are", *parts[0:parts_index], sep=", ")
            print("Remaining letters are: " + (str(letters)[1:-1]))
            print("Correct letters are: " + (str(correct_letters)[1:-1]))
            print("Incorrect letters are: " + (str(incorrect_letters)[1:-1]))
            print("")
            print("Computer wins, the word was \""+ word+"\".")

        print("")

        while True:
            playing = input("Play again? (Y/N): ")

            if playing.isdigit == True:
                continue
            elif playing.lower() == "yes" or playing.lower() == "y" or playing.lower() == "no" or playing.lower() == "n":
                break

        if playing.lower() == "no" or playing.lower() == "n":
            break

    if gamemode == "4" or gamemode == "5":

        computer_word = ""
            
        for i in range(random.randint(3,8)):
            computer_word += str(random.choice(letters))

        for i in range(50):
            print("")

        while True:

            display_word = ""
            guess_word = ""
            
            for char in computer_word:
                
                if char in correct_letters:
                    guess_word += char
                    display_word += char
                    display_word += " "
                else:
                    guess_word += "_"
                    display_word += "_ "

            print("The word is:", display_word)
            print("")

            if gamemode == "4":
                if guess_word == computer_word:
                    break
                elif parts_index == None:
                    print("Parts are")
                elif parts_index == 6:
                    break
                else:
                    print("Parts are", *parts[0:parts_index], sep=", ")
            if gamemode == "5":
                if guess_word == computer_word:
                    break
                elif parts_index == None:
                    print("Parts are")
                elif parts_index == 12:
                    break
                else:
                    print("Parts are", *hard_parts[0:parts_index], sep=", ")
            
            print("Remaining letters are: " + (str(letters)[1:-1]))

            print("Correct letters are: " + (str(correct_letters)[1:-1]))

            print("Incorrect letters are: " + (str(incorrect_letters)[1:-1]))

            print("")
        
            while True:
                guess = input("Player(s), guess a letter: ")

                if len(guess) == 1 and guess.isalpha() == True:
                    guess = guess.lower()
                    break

            try:
                letters.remove(guess)
            
                if guess in computer_word:

                    print("")
                    print("Word contains "+guess+".")
                    print("")

                    correct_letters.append(guess)
            
                elif guess not in computer_word:

                    print("")
                    print("Word does not contain "+guess+".")
                    print("")

                    incorrect_letters.append(guess)

                    if parts_index == None:
                        parts_index = 1
                    else:
                        parts_index += 1

            except ValueError:
                print("")
                print("Letter already guessed or not valid.")
                print("")

        if gamemode == "4":
            if parts_index == 6:
                print("Parts are", *parts[0:parts_index], sep=", ")
                print("Remaining letters are: " + (str(letters)[1:-1]))
                print("Correct letters are: " + (str(correct_letters)[1:-1]))
                print("Incorrect letters are: " + (str(incorrect_letters)[1:-1]))
                print("")
                print("Computer wins, the password was \""+ computer_word+"\".")
            elif guess_word == computer_word:
                print("Parts are", *parts[0:parts_index], sep=", ")
                print("Remaining letters are: " + (str(letters)[1:-1]))
                print("Correct letters are: " + (str(correct_letters)[1:-1]))
                print("Incorrect letters are: " + (str(incorrect_letters)[1:-1]))
                print("")
                print("Player(s) wins, the password was \""+ computer_word+"\".")
                
        if gamemode == "5":
            if parts_index == 12:
                print("Parts are", *hard_parts[0:parts_index], sep=", ")
                print("Remaining letters are: " + (str(letters)[1:-1]))
                print("Correct letters are: " + (str(correct_letters)[1:-1]))
                print("Incorrect letters are: " + (str(incorrect_letters)[1:-1]))
                print("")
                print("Computer wins, the password was \""+ computer_word+"\".")
            elif guess_word == computer_word:
                print("Parts are", *hard_parts[0:parts_index], sep=", ")
                print("Remaining letters are: " + (str(letters)[1:-1]))
                print("Correct letters are: " + (str(correct_letters)[1:-1]))
                print("Incorrect letters are: " + (str(incorrect_letters)[1:-1]))
                print("")
                print("Player(s) wins, the password was \""+ computer_word+"\".")

        print("")

        while True:
            playing = input("Play again? (Y/N): ")

            if playing.isdigit == True:
                continue
            elif playing.lower() == "yes" or playing.lower() == "y" or playing.lower() == "no" or playing.lower() == "n":
                break

        if playing.lower() == "no" or playing.lower() == "n":
            break
        
    

    if gamemode == "6":

        computer_word = ""

        print("")

        for i in range(random.randint(3,8)):
                computer_word += str(random.randint(0,9))

        for i in range(50):
            print("")

        while True:

            display_word = ""
            guess_word = ""
            
            for char in computer_word:
                
                if char in correct_letters:
                    guess_word += char
                    display_word += char
                    display_word += " "
                else:
                    guess_word += "_"
                    display_word += "_ "

            print("The number is:", display_word)
            print("")
            
            if guess_word == computer_word:
                break
            elif parts_index == None:
                print("Parts are")
            elif parts_index == 6:
                break
            else:
                print("Parts are", *parts[0:parts_index], sep=", ")
            
            print("Remaining numbers are: " + (str(numbers)[1:-1]))

            print("Correct numbers are: " + (str(correct_letters)[1:-1]))

            print("Incorrect numbers are: " + (str(incorrect_letters)[1:-1]))

            print("")
        
            while True:
                guess = input("Player(s), guess a number: ")

                if len(guess) == 1 and guess.isdigit() == True:
                    break

            try:
                numbers.remove(guess)
            
                if guess in computer_word:

                    print("")
                    print("Pin contains "+guess+".")
                    print("")

                    correct_letters.append(guess)
            
                elif guess not in computer_word:

                    print("")
                    print("Pin does not contain "+guess+".")
                    print("")

                    incorrect_letters.append(guess)

                    if parts_index == None:
                        parts_index = 1
                    else:
                        parts_index += 1

            except ValueError:
                print("")
                print("Number already guessed or not valid.")
                print("")

        if parts_index == 6:
            print("Parts are", *parts[0:parts_index], sep=", ")
            print("Remaining numbers are: " + (str(numbers)[1:-1]))
            print("Correct numbers are: " + (str(correct_letters)[1:-1]))
            print("Incorrect lnumbers are: " + (str(incorrect_letters)[1:-1]))
            print("")
            print("Computer wins, the pin was \""+  computer_word+"\".")
        elif guess_word == computer_word:
            print("Parts are", *parts[0:parts_index], sep=", ")
            print("Remaining numbers are: " + (str(numbers)[1:-1]))
            print("Correct numbers are: " + (str(correct_letters)[1:-1]))
            print("Incorrect numbers are: " + (str(incorrect_letters)[1:-1]))
            print("")
            print("Player(s) wins, the pin was \""+ computer_word+"\".")

        print("")

        while True:
            playing = input("Play again? (Y/N): ")

            if playing.isdigit == True:
                continue
            elif playing.lower() == "yes" or playing.lower() == "y" or playing.lower() == "no" or playing.lower() == "n":
                break

        if playing.lower() == "no" or playing.lower() == "n":
            break
        
    if gamemode == "7":

        computer_word = random.choice(wordslist)

        for i in range(50):
            print("")

        while True:

            display_word = ""
            guess_word = ""
            
            for char in computer_word:
                
                if char in correct_letters:
                    guess_word += char
                    display_word += char
                    display_word += " "
                else:
                    guess_word += "_"
                    display_word += "_ "

            print("The word is:", display_word)
            print("")

            if gamemode == "7":
                if guess_word == computer_word:
                    break
                elif parts_index == None:
                    print("Parts are")
                elif parts_index == 6:
                    break
                else:
                    print("Parts are", *parts[0:parts_index], sep=", ")
            
            print("Remaining letters are: " + (str(letters)[1:-1]))

            print("Correct letters are: " + (str(correct_letters)[1:-1]))

            print("Incorrect letters are: " + (str(incorrect_letters)[1:-1]))

            print("")
        
            while True:
                guess = input("Player(s), guess a letter: ")

                if len(guess) == 1 and guess.isalpha() == True:
                    guess = guess.lower()
                    break

            try:
                letters.remove(guess)
            
                if guess in computer_word:

                    print("")
                    print("Word contains "+guess+".")
                    print("")

                    correct_letters.append(guess)
            
                elif guess not in computer_word:

                    print("")
                    print("Word does not contain "+guess+".")
                    print("")

                    incorrect_letters.append(guess)

                    if parts_index == None:
                        parts_index = 1
                    else:
                        parts_index += 1

            except ValueError:
                print("")
                print("Letter already guessed or not valid.")
                print("")

        if gamemode == "7":
            if parts_index == 6:
                print("Parts are", *parts[0:parts_index], sep=", ")
                print("Remaining letters are: " + (str(letters)[1:-1]))
                print("Correct letters are: " + (str(correct_letters)[1:-1]))
                print("Incorrect letters are: " + (str(incorrect_letters)[1:-1]))
                print("")
                print("Computer wins, the password was \""+ computer_word+"\".")
            elif guess_word == computer_word:
                print("Parts are", *parts[0:parts_index], sep=", ")
                print("Remaining letters are: " + (str(letters)[1:-1]))
                print("Correct letters are: " + (str(correct_letters)[1:-1]))
                print("Incorrect letters are: " + (str(incorrect_letters)[1:-1]))
                print("")
                print("Player(s) wins, the password was \""+ computer_word+"\".")

        print("")

        while True:
            playing = input("Play again? (Y/N): ")

            if playing.isdigit == True:
                continue
            elif playing.lower() == "yes" or playing.lower() == "y" or playing.lower() == "no" or playing.lower() == "n":
                break

        if playing.lower() == "no" or playing.lower() == "n":
            break
        
    
    if playing.lower() == "no" or playing.lower() == "n":
        break

    print("")
