import random

def play_game():
    words = {
        "python": "Programming language",
        "apple": "A fruit",
        "tiger": "Wild animal",
        "india": "A country",
        "computer": "Electronic device"
    }

    word = random.choice(list(words.keys()))
    hint = words[word]

    guessed = []
    wrong = 0

    stages = [
        "",
        " O ",
        " O \n | ",
        " O \n/| ",
        " O \n/|\\",
        " O \n/|\\\n/ ",
        " O \n/|\\\n/ \\"
    ]

    print("\nHangman Game")
    print("Hint:", hint)

    while wrong < 6:
        display = ""

        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print("\nWord:", display)
        print(stages[wrong])

        if "_" not in display:
            print("You Won!")
            break

        guess = input("Enter a letter: ").lower()

        if guess in guessed:
            print("Already guessed")
            continue

        guessed.append(guess)

        if guess not in word:
            wrong += 1
            print("Wrong Guess")

    if wrong == 6:
        print(stages[wrong])
        print("You Lost")
        print("The word was:", word)

# Main loop to replay
while True:
    play_game()
    again = input("\nDo you want to play again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing! ")
        break
