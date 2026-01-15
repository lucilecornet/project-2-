#!/usr/bin/env python3
"""
Rock Paper Scissors Game
Play against the computer!
"""

import random
import sys

def get_computer_choice():
    """Randomly select rock, paper, or scissors for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def get_player_choice():
    """Get the player's choice with input validation."""
    while True:
        choice = input("\nChoose rock, paper, or scissors (or 'quit' to exit): ").lower().strip()

        if choice == 'quit':
            return None

        if choice in ['rock', 'paper', 'scissors']:
            return choice

        print("Invalid choice! Please choose rock, paper, or scissors.")

def determine_winner(player, computer):
    """Determine the winner of the round."""
    if player == computer:
        return "tie"

    winning_combinations = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }

    if winning_combinations[player] == computer:
        return "player"
    else:
        return "computer"

def display_result(player, computer, result):
    """Display the round result."""
    print(f"\nYou chose: {player}")
    print(f"Computer chose: {computer}")
    print("-" * 30)

    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win this round! 🎉")
    else:
        print("Computer wins this round!")

def play_game():
    """Main game loop."""
    print("=" * 40)
    print("  Welcome to Rock Paper Scissors!")
    print("=" * 40)
    print("\nRules:")
    print("  Rock beats Scissors")
    print("  Scissors beats Paper")
    print("  Paper beats Rock")

    player_score = 0
    computer_score = 0
    rounds = 0

    while True:
        player_choice = get_player_choice()

        if player_choice is None:
            break

        computer_choice = get_computer_choice()
        result = determine_winner(player_choice, computer_choice)

        display_result(player_choice, computer_choice, result)

        if result == "player":
            player_score += 1
        elif result == "computer":
            computer_score += 1

        rounds += 1

        print(f"\nScore - You: {player_score} | Computer: {computer_score}")

    # Final results
    print("\n" + "=" * 40)
    print("  Game Over!")
    print("=" * 40)
    print(f"Total rounds played: {rounds}")
    print(f"Final Score - You: {player_score} | Computer: {computer_score}")

    if player_score > computer_score:
        print("\n🏆 Congratulations! You won overall! 🏆")
    elif computer_score > player_score:
        print("\n💻 Computer won overall! Better luck next time!")
    else:
        print("\n🤝 It's an overall tie!")

    print("\nThanks for playing!")

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Thanks for playing!")
        sys.exit(0)
