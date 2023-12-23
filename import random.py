import random

def generate_birthday_wish(name):
    wishes = [
        f"Happy Birthday, {name}! May your day be filled with joy and laughter.",
        f"Wishing a fantastic birthday to {name}! May this year bring you success and happiness.",
        f"Happy Birthday, {name}! May all your dreams and wishes come true.",
        f"Warmest wishes on your birthday, {name}! May the coming year be your best one yet.",
        f"Sending lots of love and birthday cheer to {name}! Have a wonderful day!",
        f"May this birthday be the beginning of a year filled with new adventures for {name}. Happy Birthday!",
        f"Happy Birthday, {name}! May your day be as special as you are.",
        f"Wishing you a day full of love, laughter, and all the things you enjoy, {name}. Happy Birthday!",
    ]

    return random.choice(wishes)

def birthday_guess_game():
    print("Welcome to the Birthday Wish Guessing Game!")
    print("Mirabel Ojo, can you guess whose birthday it is?")
    
    # Get user input
    guessed_name = input("Enter a name: ")

    # Generate a birthday wish
    birthday_wish = generate_birthday_wish(guessed_name)

    # Display the birthday wish
    print("\nBirthday Wish:")
    print(birthday_wish)

if __name__ == "__main__":
    birthday_guess_game()
