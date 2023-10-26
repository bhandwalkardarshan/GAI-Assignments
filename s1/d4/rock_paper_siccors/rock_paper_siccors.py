import random

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    return computer_choice

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "draw"
    elif user_choice == "rock" and computer_choice == "paper":
        return "computer"
    elif user_choice == "rock" and computer_choice == "scissors":
        return "user"
    elif user_choice == "paper" and computer_choice == "rock":
        return "user"
    elif user_choice == "paper" and computer_choice == "scissors":
        return "computer"
    elif user_choice == "scissors" and computer_choice == "rock":
        return "computer"
    elif user_choice == "scissors" and computer_choice == "paper":
        return "user"

def update_score(winner, scores):
    if winner == "user":
        scores["user"] += 1
    elif winner == "computer":
        scores["computer"] += 1
    else:
        scores["draw"] += 1
    return scores

def display_score(scores):
    print("\nScore:\nUser: {}\nComputer: {} \nDraw: {}".format(scores["user"], scores["computer"], scores["draw"]))

def play_again():
    user_choice = input("Do you want to play again? (yes or no): ").strip().lower()
    if user_choice == "yes":
        return True
    elif user_choice == "no":
        return False

def main():
    scores = {'user': 0, 'computer': 0, 'draw': 0}
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        scores = update_score(winner, scores)
        display_score(scores)
        if play_again() == False:
            break
    
    print("Thank you for playing Rock, Paper, Scissors!")

if __name__ == "__main__":
    main()
    
