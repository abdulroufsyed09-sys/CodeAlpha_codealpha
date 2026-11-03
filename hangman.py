import random

words = ["python","program","keyword","internet","computer"]
word = random.choice(words)

guessed = []
wrong = 0
max_wrong = 6

print("===========================================")
print("HANGMAN")
print("===========================================")

while wrong < max_wrong:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nword:",display)

    if "_" not in display:
        print("You win! the game!! The word was",word)
        break

    print("Wrong guess left:",max_wrong-wrong)
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter..")
    elif guess in guessed:
        print("You already guessed that..")
    else:
        guessed.append(guess)
        if guess in word:
            print("Correct")
        else:
            wrong += 1
            print("Wrong!")
else:
    print ("\nGame over! The Word was",word)

