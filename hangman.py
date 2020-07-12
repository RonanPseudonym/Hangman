import os, random

os.system("clear")

directory = os.path.dirname(os.path.realpath(__file__))

noose = '''----------------
        |              |'''

letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","v","n","o","p","q","r","s","t","u","v","w","x","y","z"]

hangman = [
    '''        |
        |
        |
        |
    ''',

    '''        |              O
        |
        |
        |
    ''',

    '''        |              O
        |              |
        |
        |
    ''',

    '''        |              O
        |             \|
        |
        |
    ''',

    '''        |              O
        |             \|/
        |
        |
    ''',

    '''        |              O
        |             \|/
        |              |
        |
    ''',

    '''        |              O
        |             \|/
        |              |
        |             /
    ''',
    '''        |              O
        |             \|/
        |              |
        |             / \\
    '''
]

print("\n\t _   _                                       ")
print("\t| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
print("\t| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
print("\t|  _  | (_| | | | | (_| | | | | | | (_| | | | |")
print("\t|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
print("\t                   |___/                       ")

print("\n\tWould you like to play?")

while True:

    while True:

        inp = input("\n\t> ").strip().lower()
        if inp == "yes" or inp == "y":
            break
        elif inp == "no" or inp == "n":
            print()
            quit()
        else:
            print("\n\tUnknown command")

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

    while True:
        showWord = ""

        for i in range(0, len(word)):
            if word[i] in str(guessedLetters):
                showWord = showWord + word[i].upper() + " "
            else:
                showWord = showWord + "_ "

        print("\n\t"+noose+"\n"+hangman[turns])
        for i in range(0, 6):
            row = []
            for j in range(0, 6):
                if not (i*6)+j > 26:
                    if letters[(i*6)+j] in guessedLetters:
                        if letters[(i*6)+j].lower() in word.lower(): row.append("".join(letters[((i*6)+j)].upper()))
                        else:                                        row.append("\033[91m"+"".join(letters[((i*6)+j)].upper())+"\033[0m")
                    else:
                        row.append("-")
            print("\t"+"  ".join(row))
        print("\n\t"+showWord)

        if showWord.lower().replace(" ","") == word:
            print("\n\t===============")
            print("\n\tYou won!")
            print("\tThe word was '"+word+"'")
            print("\tYou got",turns,"letters wrong")
            break

        if turns == 7:
            print("\n\t===============")
            print("\n\tGame Over")
            print("\tThe word was '"+word+"'")
            break

        inp = input("\n\n\t> ").lower().strip()
        if inp not in guessedLetters:
            if inp in letters:
                if inp in word:
                    os.system("clear")
                    print("\033[32m"+"\n\tCorrect"+"\033[0m")
                else:
                    turns += 1
                    os.system("clear")
                    print("\033[91m"+"\n\tIncorrect"+"\033[0m")
                    # guessedLetters.append("\033[91m"+inp+"\033[0m") #Red text
                guessedLetters.append(inp)
            else:
                os.system("clear")
                print("\n\tPlease type one letter")
        else:
            os.system("clear")
            print("\n\tYou've already guessed that letter")
    print("\n\tWould you like to play again?")