import random


def get_user_choice():
    choices = ['rock', 'paper', 'scissors']
    user_choice = ''
    while user_choice not in choices:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice not in choices:
            print("Invalid choice. Please try again.")
    return user_choice


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    """Determine the winner based on the user's and computer's choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return "User"
    else:
        return "Computer"


def display_result(user_choice, computer_choice, winner):
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie")
    elif winner == "user":
        print("You win")
    else:
        print("You lose")


def play_again():

    while True:
        x = input("Do you want to play again?(yes/no): ").lower()
        if x == 'yes':
            return True
        elif x == 'no':
            return False
        else:
            print("Invalid choice")


def main():
    user_score = 0
    computer_score = 0
    print("Welcome to Rock, Paper, Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)
        if winner == "User":
            user_score += 1
        elif winner == "Computer":
            computer_score += 1
        print(f"\nScores: You - {user_score}, Computer - {computer_score}")
        if not play_again():
            print("Final scores: You - {}, Computer - {}".format(user_score, computer_score))
            break


if __name__ == "__main__":
    main()