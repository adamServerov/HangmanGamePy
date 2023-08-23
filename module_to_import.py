import random

lWords = ["python", "java", "swift", "javascript"]
winCount = 0
lostCount = 0


def play():
    randomWord = "".join(random.choice(lWords))
    nAttempts = 8
    global  winCount,lostCount
    word = ["-"] * len(randomWord)
    print(''.join(word))
    userGuessedLettters = list('')
    userWrongTry = list('')
    while nAttempts != 0:
        letter = input(f"Input a letter:")
        if len(letter) > 1 or letter == "":
            print("Please, input a single letter.")
            word = ''.join(word)
        elif not letter.isalpha() or not letter.islower():
            print("Please, enter a lowercase letter from the English alphabet.")
            word = ''.join(word)
        elif letter not in randomWord and letter not in userWrongTry:
            nAttempts -= 1
            print("That letter doesn't appear in the word.")
            word = ''.join(word)
            userWrongTry.append(letter)
        elif letter in userWrongTry:
            print("You've already guessed this letter.")
            word = ''.join(word)
        elif letter in randomWord and letter in userGuessedLettters:
            nAttempts -= 1
            print("You've already guessed this letter.")
            word = ''.join(word)
        else:
            userGuessedLettters.append(letter)
            temp = list(word)
            for i in range(len(randomWord)):
                if randomWord[i] == letter:
                    temp[i] = letter

            word = ''.join(temp)
        print(f"\n{word}")

        if nAttempts == 0 and "-" in word:
            lostCount += 1
            print("You lost!")
            menu()
            break
        elif not "-" in word:
            winCount += 1

            print(f"You guessed the word {word}!")
            print("You survived!")
            menu()
            break



def result():
    print(f"You won: {winCount} times.")
    print(f"You lost: {lostCount} times.")
    menu()


def menu():
    dimPut = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    if dimPut == "play":
        play()
    elif dimPut == "results":
        result()
    else:
        quit()


print("H A N G M A N")
menu()
