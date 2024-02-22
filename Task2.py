import random

def number_guessing():
    print("Welcome to the number guessing game we have choose a number in between 1 to 100")
    secret_no = random.randint(1,100)
    attempt = 0
    while True:
        guess  = int(input("Enter the guess:"))
        attempt += 1
        if guess == secret_no :
            print(f"Congratulations you guessed the number in {attempt} attempts")
            break
        elif guess > secret_no:
            print("Your guess is too high!")
        else:
            print("Your guess is too low!")

if __name__ == "__main__":
    play_game = input("Do you want to play the game? (yes/no): ").lower()

    if play_game == "yes":
        number_guessing()
    else:
        print("MayBe Next Time")
