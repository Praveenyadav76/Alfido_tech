import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("🎉 Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is? Let's find out!")

    while True:
        try:
            user_input = input("\n🔢 Your guess: ")
            user_guess = int(user_input)
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("🚫 Whoa! Your guess has to be between 1 and 100. Try again.")
                continue

            if user_guess < number_to_guess:
                print("📉 A bit too low. Give it another shot!")
            elif user_guess > number_to_guess:
                print("📈 A tad too high. Try again!")
            else:
                print(f"\n🎯 Nailed it! The number was {number_to_guess}.")
                print(f"👏 You got it in {attempts} tries. Great job!")
                break
        except ValueError:
            print("🤔 Hmm, that doesn’t look like a number. Please enter a valid number.")

if __name__ == "__main__":
    guess_the_number()
