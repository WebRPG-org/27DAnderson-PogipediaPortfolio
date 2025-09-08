import winsound
from time import sleep

#Most errors should be fixed, maybe could later add commands to personalize some things, such as like /hz/ to change the hz value of the beep of /play/ using a variable named hz.

english_morse = {"A":".-","B":"-...","C":"-.-.","D":"-..","E":".","F":"..-.","G":"--.","H":"....","I":"..","J":".---","K":"-.-","L":".-..","M":"--","N":"-.","O":"---","P":".--.","Q":"--.-","R":".-.","S":"...","T":"-","U":"..-","V":"...-","W":".--","X":"-..-","Y":"-.--","Z":"--..","1":".----","2":"..---","3":"...--","4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----.","0":"-----","?":"..--..","!":"-.-.--",".":".-.-.-",",":"--..--",";":"-.-.-.",":":"---...","+":".-.-.","-":"-....-","/":"-..-.","=":"-...-", "(":"-.--.", ")":"-.--.-", "&":".-...", "_":"..--.-", "\"":".-..-.", "$":"...-..-", "@":".--.-.", "¿":"..-.-", "¡":"--...-"}
morse_english = {".-":"A","-...":"B","-.-.":"C","-..":"D",".":"E","..-.":"F","--.":"G","....":"H","..":"I",".---":"J","-.-":"K",".-..":"L","--":"M","-.":"N","---":"O",".--.":"P","--.-":"Q",".-.":"R","...":"S","-":"T","..-":"U","...-":"V",".--":"W","-..-":"X","-.--":"Y","--..":"Z",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6","--...":"7","---..":"8","----.":"9","-----":"0","..--..":"?","-.-.--":"!",".-.-.-":".","--..--":",","-.-.-.":";","---...":":",".-.-.":"+","-....-":"-","-..-.":"/","-...-":"=", "-.--.":"(", "-.--.-":")", ".-...":"&", "..--.-":"_", ".-..-.":"\"", "...-..-":"$", ".--.-.":"@", "..-.-":"¿", "--...-":"¡", "/": " ", "": " "}

print("This is a Two-Way Morse Code Translator. This can translate any of the standard 26 letters and the numbers 0 to 9. It will also translate question marks, exclamation points, periods/dots, commas, semi-colons, colons, pluses, minuses/dashes, forward slashes/fraction bars/alternative division signs, equals signs, paratheses, ampersands, underscores, quotation marks, dollar signs, at symbols, ¿ and ¡ to morse code. This morse code uses dots as: . and dashes as: - and uses spaces between letters and / between words. Any unknown characters or morse code will be printed as �. Entering /eng/ followed by English words will force the translation of English to Morse Code, specifically will prevent auto detection of morse code if you only include . and/or – and/or / in your text. Entering /play/ followed by morse code will beep out the morse code. If you only enter /eng/ or /play/, then it will still just translate to morse code. Plus, you can force English translation of commands using /eng/, and if /play/ if followed by text rather than morse code, it will act similar to /eng/, but can’t force Morse Code to English. Also, /play/ is only supported on windows because it uses winsound to beep. Also, enter /end/ to end the program. Lastly, to see these instructions again, enter /help/ or /?/.")

while True:

    constant_text = ""

    eng = 1
    
    play = 0

    print("")
    
    text = input("Enter Text/Morse Code Here: ")

    print("")

    if not text == "":
        if text[0] == "/" and text[1] == "p" and text[2] == "l" and text[3] == "a" and text[4] == "y" and text[5] == "/":
            if not text == "/play/":
                play = 1
                text = text[6:]

    characters = []

    is_morse = True

    if not text == "":
        if text[0] == "/" and text[1] == "e" and text[2] == "n" and text[3] == "g" and text[4] == "/":
            if not text == "/eng/":
                is_morse = False
                eng = 1
                text = text[5:]

    if text == "/end/" and eng == 0:
        break

    if text == "/help/" and not play == 1 and eng == 0 or text == "/?/" and not play == 1 and eng == 0:
        print("This is a Two-Way Morse Code Translator. This can translate any of the standard 26 letters and the numbers 0 to 9. It will also translate question marks, exclamation points, periods/dots, commas, semi-colons, colons, pluses, minuses/dashes, forward slashes/fraction bars/alternative division signs, equals signs, paratheses, ampersands, underscores, quotation marks, dollar signs, at symbols, ¿ and ¡ to morse code. This morse code uses dots as: . and dashes as: - and uses spaces between letters and / between words. Any unknown characters or morse code will be printed as �. Entering /eng/ followed by English words will force the translation of English to Morse Code, specifically will prevent auto detection of morse code if you only include . and/or – and/or / in your text. Entering /play/ followed by morse code will beep out the morse code. If you only enter /eng/ or /play/, then it will still just translate to morse code. Plus, you can force English translation of commands using /eng/, and if /play/ if followed by text rather than morse code, it will act similar to /eng/, but can’t force Morse Code to English. Also, /play/ is only supported on windows because it uses winsound to beep. Also, enter /end/ to end the program. Lastly, to see these instructions again, enter /help/ or /?/.")

    for i in range(len(text)):
        if text[i] == " " or text[i] == "-" or text[i] == "." or text[i] == "/":
            continue
        else:
            is_morse = False
            eng = 0
            break

    if is_morse == True and not text == "/help/" and not text == "/?/" or is_morse == True and eng == 0:
        constant_text = text
        eng_text = ""
        word = ""
        for i in text:
            if i == " ":
                try:
                    eng_text += morse_english[word]
                except KeyError:
                    eng_text += "�"
                word = ""
            elif i == "/":
                try:
                    eng_text += morse_english[word] + " "
                except KeyError:
                    eng_text += "�"
                word = ""
            else:
                word += i
        try:
            eng_text += morse_english[word]
        except KeyError:
            eng_text += "�"
        
        nospace_text = ""
        
        for i in range(len(eng_text)):
            if i == 0 or (eng_text[i] != " " or eng_text[i-1] != " "):
                nospace_text += eng_text[i]

        if not nospace_text == " ":
            if nospace_text[0] == " ":
                nospace_text = nospace_text[1:]
            if nospace_text[-1] == " ":
                nospace_text = nospace_text[:-1]
        else:
            nospace_text = "�"

        print(nospace_text)

        if play == 1:
            print("")
            print("Playing...")
            for i in range(len(constant_text)):
                if constant_text[i] == ".":
                    winsound.Beep(666, 222)
                if constant_text[i] == "-":
                    winsound.Beep(666, 777)
                if constant_text[i] == " ":
                    sleep(1.8)

    elif not text == "/help/" and not text == "/?/" or eng == 0:
        for i in range(0, len(text)):
            characters.append(text[i].upper())
            
        i = 0

        while i < len(characters):
            if characters[i].isalnum():
                i += 1
            elif characters[i] == " ":
                if i == 0 or characters[i-1] != " ":
                    i += 1
                else:
                    characters.pop(i)
            else:
                i += 1
        if characters[0] == " ":
            characters = characters[1:]
        if characters[-1] == " ":
            characters = characters[:-1]
            
    
        for i in range(len(characters)):
            
            if characters[i].capitalize() == " " or characters[i].capitalize() == "A" or characters[i].capitalize() == "B" or characters[i].capitalize() == "C" or characters[i].capitalize() == "D" or characters[i].capitalize() == "E" or characters[i].capitalize() == "F" or characters[i].capitalize() == "G" or characters[i].capitalize() == "H" or characters[i].capitalize() == "I" or characters[i].capitalize() == "J" or characters[i].capitalize() == "K" or characters[i].capitalize() == "L" or characters[i].capitalize() == "M" or characters[i].capitalize() == "N" or characters[i].capitalize() == "O" or characters[i].capitalize() == "P" or characters[i].capitalize() == "Q" or characters[i].capitalize() == "R" or characters[i].capitalize() == "S" or characters[i].capitalize() == "T" or characters[i].capitalize() == "U" or characters[i].capitalize() == "V" or characters[i].capitalize() == "W" or characters[i].capitalize() == "X" or characters[i].capitalize() == "Y" or characters[i].capitalize() == "Z" or characters[i] == "1" or characters[i] == "2" or characters[i] == "3" or characters[i] == "4" or characters[i] == "5" or characters[i] == "6" or characters[i] == "7" or characters[i] == "8" or characters[i] == "9" or characters[i] == "0" or characters[i] == "?" or characters[i] == "!" or characters[i] == "." or characters[i] == "," or characters[i] == ";" or characters[i] == ":" or characters[i] == "+" or characters[i] == "-" or characters[i] == "/" or characters[i] == "=" or characters[i] == "(" or characters[i] == ")" or characters[i] == "&" or characters[i] == "_" or characters[i] == "\"" or characters[i] == "$" or characters[i] == "@" or characters[i] == "¿" or characters[i] == "¡":
                if characters[i] == " ":
                    characters[i] = "/"
                else:
                    characters[i] = english_morse[characters[i]]
            else:
                characters[i] = "�"

        for i in range(len(characters)):
            print(characters[i], end=" ")
        
        print("")

