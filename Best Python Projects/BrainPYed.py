storage = [0 for i in range(30000)]
index = 0
allow = True

print('''The code is arranged in a grid of slots, variables, that you can manipulate using 8 simple symbols. In these cells, there is a pointer, which denotes the active cell. This cell is the cell each activity is based on.
+ will increment the value of the cell at pointer position by one
- will decrement the value of the cell at pointer position by one
> will increment the pointer position by one (move right)
< will decrement the pointer position by one (move left)
. will output the cell at the pointer using the ASCII value of that number
, will allow you to enter an input into the cell at the pointer location
[ and ] will have the contents loop until the active cell is set to zero, if entered on zero, the contents are skipped
Everything else is ignored

''')
code = input("Enter BrainPYed code here: ")

balance = []
for i in code:
    if i == "[" or i == "]":
        balance.append(i)

for i in range(-(len(balance)//-2)):
    
    if len(balance) == 1:
        print("Error: Unable to run BrainPYed code because of inconsistant brackets")

        allow = False
        break
    elif balance[0] == "[" and balance[1] == "]":
        balance.pop(0)
        balance.pop(0)
        continue
    else:
        print("Error: Unable to run BrainPYed code because of inconsistant brackets")

        allow = False
        break

if allow == True:
    brackets = []
    for i in range(len(code)):
        if code[i] in "[]":
            brackets.append(i)

    for i in code:
        if i == "+":
            if storage[index] == 255:
                storage[index] = 0
            else:
                storage[index] += 1
            
        elif i == "-":
            if storage[index] == 0:
                storage[index] = 255
            else:
                storage[index] -= 1
            
        elif i == ">":
            index += 1
            
        elif i == "<":
            index -= 1
            
        elif i == ".":
            print(chr(storage[index]))
            
        elif i == ",":
            while True:
                ascii_input = input("Enter your input: ")
                if len(ascii_input) == 1:
                    storage[index] = ord(ascii_input)
                    break
                else:
                    print("Please only enter 1 character.")
            
        elif i == "[":
            print("Looping not implemented")
            
        elif i == ("]"):
            print("Looping not implemented")
