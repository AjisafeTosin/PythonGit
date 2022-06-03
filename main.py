import random
def main():
    user_action = input("Enter a choice (P, R, S): ")
    possible_actions = ["P", "R", "S"]
    computer_action = random.choice(possible_actions)
    if user_action in possible_actions:
        
        print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
        if user_action == computer_action:
            print(f"Both players selected {user_action}. It's a tie!")
            main()
        elif user_action == "R":
            if computer_action == "S":
                print("Rock smashes scissors! You win!")
            else:
                print("Paper covers rock! You lose.")
        elif user_action == "P":
            if computer_action == "R":
                print("Paper covers rock! You win!")
            else:
                print("Scissors cuts paper! You lose.")
        elif user_action == "S":
            if computer_action == "P":
                print("Scissors cuts paper! You win!")
            else:
                print("Rock smashes scissors! You lose.")
    
    else:
        print("Invalid Entry kindly Enter 'P','R','S'")
        main()

main()