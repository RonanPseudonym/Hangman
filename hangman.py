import os, random

os.system("clear")

directory = os.path.dirname(os.path.realpath(__file__))

def chooseIndent(num):
    indentNum = int(os.get_terminal_size()[0]-num)//2
    indent = str(" "*indentNum)
    return indent

indent = chooseIndent(16)

noose = '''----------------
'''+indent+'''|              |'''


letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","v","n","o","p","q","r","s","t","u","v","w","x","y","z"]

hangman = [
    indent+'''|
'''+indent+'''|
'''+indent+'''|
'''+indent+'''|
    ''',

    indent+'''|              O
'''+indent+'''|
'''+indent+'''|
'''+indent+'''|
    ''',

    indent+'''|              O
'''+indent+'''|              |
'''+indent+'''|
'''+indent+'''|
    ''',

    indent+'''|              O
'''+indent+'''|             \|
'''+indent+'''|
'''+indent+'''|
    ''',

    indent+'''|              O
'''+indent+'''|             \|/
'''+indent+'''|
'''+indent+'''|
    ''',

    indent+'''|              O
'''+indent+'''|             \|/
'''+indent+'''|              |
'''+indent+'''|
    ''',

    indent+'''|              O
'''+indent+'''|             \|/
'''+indent+'''|              |
'''+indent+'''|             /
    ''',
    indent+'''|              O
'''+indent+'''|             \|/
'''+indent+'''|              |
'''+indent+'''|             / \\
    '''
]

indent = chooseIndent(47)

print("\n"+indent+" _   _                                       ")
print(indent+"| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
print(indent+"| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
print(indent+"|  _  | (_| | | | | (_| | | | | | | (_| | | | |")
print(indent+"|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
print(indent+"                   |___/                       ")

print("\n"+indent+"Would you like to play?")

while True:

    while True:

        inp = input("\n"+indent+"> ").strip().lower()
        if inp == "yes" or inp == "y":
            break
        elif inp == "no" or inp == "n":
            print()
            quit()
        else:
            print("\n"+indent+"Unknown command")

    words, guessedLetters = [], []
    with open(os.path.join(directory,"words.txt")) as f:
        for line in f:
            words.append(line.strip().lower())

    os.system("clear")

    word = str(random.choice(words))

    turns = 0

    # =====================================================

    print()
    print()

    indent = chooseIndent(16)

    while True:
        showWord = ""

        for i in range(0, len(word)):
            if word[i] in str(guessedLetters):
                showWord = showWord + word[i].upper() + " "
            else:
                showWord = showWord + "_ "

        print("\n"+indent+""+noose+"\n"+hangman[turns])
        for i in range(0, 6):
            row = []
            for j in range(0, 6):
                if not (i*6)+j > 26:
                    if letters[(i*6)+j] in guessedLetters:
                        if letters[(i*6)+j].lower() in word.lower(): row.append("".join(letters[((i*6)+j)].upper()))
                        else:                                        row.append("\033[91m"+"".join(letters[((i*6)+j)].upper())+"\033[0m")
                    else:
                        row.append("-")
            print(indent+""+"  ".join(row))
        print("\n"+indent+""+showWord)

        if showWord.lower().replace(" ","") == word:
            print("\n"+indent+"===============")
            print("\n"+indent+"You won!")
            print(indent+"The word was '"+word+"'")
            print(indent+"You got",turns,"letters wrong")
            break

        if turns == 7:
            print("\n"+indent+"===============")
            print("\n"+indent+"Game Over")
            print(indent+"The word was '"+word+"'")
            break

        inp = input("\n\n"+indent+"> ").lower().strip()
        if inp not in guessedLetters:
            if inp in letters:
                if inp in word:
                    os.system("clear")
                    print("\033[32m"+"\n"+indent+"Correct"+"\033[0m")
                else:
                    turns += 1
                    os.system("clear")
                    print("\033[91m"+"\n"+indent+"Incorrect"+"\033[0m")
                    # guessedLetters.append("\033[91m"+inp+"\033[0m") #Red text
                guessedLetters.append(inp)
            else:
                os.system("clear")
                print("\n"+indent+"Please type one letter")
        else:
            os.system("clear")
            print("\n"+indent+"You've already guessed that letter")
    print("\n"+indent+"Would you like to play again?")
