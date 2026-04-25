import random

def play_game(round_number):
    print("\n" + "=*40")
    print(f"   NUMBER GUESSING GAME - ROUND {round_number}")
    print('='*40)

    max_number= 100 + (round_number - 1) * 50
    secret_number = random.randit(1, max_number)

    attempts = 0
    max_attempts = 7
    
    while attempts < max_number:
        try:
            guess = int(input(f"\nGuess a number (1 - {max_number}): "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        attempts += 1
        
        if guess < secret_number:
            print("Too low!")
             
        elif guess > secret_number:
            print("Too high!")

        else:
            print(f"WOW Correct! You guessed in {attempts} attempt(s)!")
            return True
        
    print("\n OOPS Game Over!")
    print(f"The correct number was: {secret_number}")
    return False

def main():
    round_nummber = 1

    while True:
       won = play_game(round_nummber)

    choice = input("\nDo you want to play again? (yes/no): ").lower()
        
    if choice != "yes":
            print("Thanks for playing!") 
            break
    
    round_nummber += 1

main()