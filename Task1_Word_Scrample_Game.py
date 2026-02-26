import random

print("===== WORD SCRAMBLE GAME =====")

words = ["python", "computer", "keyboard", "security", "network", "programming"]

while True:
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))

    print("\nUnscramble the word:", scrambled)

    attempts = 3

    while attempts > 0:
        guess = input("Your guess: ").lower()

        if guess == word:
            print("🎉 Correct! You guessed the word.")
            break
        else:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

    if attempts == 0:
        print(f"Out of attempts! The correct word was: {word}")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing! 👋")
        break