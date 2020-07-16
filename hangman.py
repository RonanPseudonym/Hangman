import os, random, getch

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


while True:

    os.system("clear")

    indent = chooseIndent(47)

    print("\n"+indent+" _   _                                       ")
    print(indent+"| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
    print(indent+"| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print(indent+"|  _  | (_| | | | | (_| | | | | | | (_| | | | |")
    print(indent+"|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print(indent+"                   |___/                       ")

    print("\n"+str("Type 'play' to play, 'help' for help, 'quit'".center(os.get_terminal_size()[0])))
    print(str("to quit and 'credits' to display credits".center(os.get_terminal_size()[0])))

    while True:

        inp = input("\n"+indent+"> ").strip().lower()
        if inp == "play" or inp == "p":
            break
        elif inp == "quit" or inp == "q":
            print()
            quit()
        elif inp == "help" or inp == "h":
            print("\n"+indent+"Welcome to Hangman!")
            print(indent+"You play by guessing letters to find the word.")
            print(indent+"If you guess the word, you win.")
            print(indent+"If you guess incorrectly too many times, you lose.")
            print(indent+"That's all! Have fun 😉")
        elif inp == "credits" or inp == "c":
            print("\n"+indent+"Hangman is created by Ronan Underwood.")
            print(indent+"© CrypotoBabylon Games 2020")
        else:
            print("\n"+indent+"Unknown command")

    words, guessedLetters = [], []
    with open(os.path.join(directory,"words.txt")) as f:
        for line in f:
            words.append(line.strip().lower())


    print("\n"+indent+"Choose difficulty (easy, medium, hard)")
    while True:
        inp = input("\n"+indent+"> ").strip().lower()
        if inp == "easy":
            while True:
                word = str(random.choice(words))
                if len(word) == 6 or len(word) == 7:
                    break
        elif inp == "medium":
            while True:
                word = str(random.choice(words))
                if len(word) == 8 or len(word) == 9 or len(word) == 10:
                    break
        elif inp == "hard":
            while True:
                word = str(random.choice(words))
                if len(word) == 11 or len(word) == 12 or len(word) == 13:
                    break
        else:
            print("\n"+indent+"Unknown command")
        break

    turns = 0

    os.system("clear")

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
        print("\n"+showWord.center(os.get_terminal_size()[0]))

        if showWord.lower().replace(" ","") == word:
            print("\n"+indent+"===============")
            print("\n"+indent+"🎉 You won")
            print(indent+"The word was '"+word+"'")
            print(indent+"You got",turns,"letters wrong")
            input(indent+"Press [enter] to proceed")
            break

        if turns == 7:
            print("\n"+indent+"===============")
            print("\n"+indent+"💀 Game Over ")
            print(indent+"The word was '"+word+"'")
            input(indent+"Press [enter] to proceed")
            break

        print("\n\n")
        inp = getch.getch()
        inp = inp.lower().strip()
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
                print("\n"+indent+"\033[93mInvalid input\033[0m")
        else:
            os.system("clear")
            print("\n"+indent+"\033[93mAlready guessed\033[0m")
