import random

words = ["apple", "orange", "mango", "grape", "banana"]

word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6

print("===== HANGMAN GAME =====")

while attempts > 0 and "_" in guessed:

    print("\nWord:", " ".join(guessed))
    print("Attempts Left:", attempts)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
        print("Correct Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")

if "_" not in guessed:
    print("\nCongratulations! You won.")
    print("Word is:", word)
else:
    print("\nGame Over!")
    print("Correct Word:", word)
    