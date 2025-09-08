import random

print("Welcome to the number guess")
print("Think of a number between 1-100, and I'll guess it!")

guess = 50
guesses = []
limit = [1, 100]
num = "None"

while not num.lower() == "c" and not num.lower() == "correct":

    guess = random.randint(limit[0], limit[1])
    while guess in guesses:
        guess = random.randint(limit[0], limit[1])
    guesses.append(guess)

    print("")
    print(limit)
    print("I guess... " + str(guess))
    print("say 'h' if I need to guess higher")
    print("'l' to guess lower")

    while True:
        
        num = input("'c' if I'm correct!    ")
        if num == "h" or num == "l" or num == "c" or num == "lower" or num == "higher" or num == "correct":
            break
    
    if num == "h" or num == "higher":
        limit[0] = guess
    elif num == "l" or num == "lower":
        limit[1] = guess
    elif num == "c" or num == "correct":
        print("I knew I'd find it! Your number was " + str(guess))

    if limit[0] + 1 == limit[1]:
        print("")
        if num == "l" or num == "lower":
            print("Liar, your number couldn't be lower than " + str(guess) + ", so it should be:  " + str(guess))
        elif num == "h" or num == "higher":
            print("Liar, your number couldn't be higher than " + str(guess) + ", so it should be:  " + str(guess))
        number_range = "c"
        break
    if limit[0] == limit[1]:
        print("")
        if num == "l" or num == "lower":
            print("Liar, your number couldn't be lower than " + str(guess) + ", so it should be:  " + str(guess))
        elif num == "h" or num == "higher":
            print("Liar, your number couldn't be higher than " + str(guess) + ", so it should be:  " + str(guess))
        number_range = "c"
        break
