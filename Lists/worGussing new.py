import random

def play_game():
    name = input("What is your name? ").strip().title()
    print(f"Good Luck, {name}! 🎉")

    names = ['hadi', 'yara', 'hasan', 'sara', 'osama']
    word = random.choice(names)

    print("\nGuess the name!\n")

    guesses = set()
    turns = 12

    while turns > 0:
        display = " ".join([char if char in guesses else "_" for char in word])
        print(display)

        if all(char in guesses for char in word):
            print("\n✅ You Win!")
            print(f"The name was: {word}")
            break

        guess = input("\nGuess a letter: ").lower().strip()

        if not guess or len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter one valid letter.")
            continue

        if guess in guesses:
            print("⚠️ You already guessed that letter.")
            continue

        guesses.add(guess)

        if guess not in word:
            turns -= 1
            print(f"❌ Wrong! You have {turns} guesses left.")
            if turns == 0:
                print("\n💀 You lose!")
                print(f"The correct name was: {word}")

# 🔁 تكرار اللعبة
while True:
    play_game()
    again = input("\nDo you want to play again? (y/n): ").lower().strip()
    if again != "y":
        print("👋 Thanks for playing! Bye!")
        break
