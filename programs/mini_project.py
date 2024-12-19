import random

def multi_player_dice_roll():
    print("Welcome to the Simplified Multi-Player Dice Roll Game!")
    
    num_players = int(input("Enter the number of players: "))
    scores = [0] * num_players

    while True:
        try:
            rounds = int(input("How many rounds do you want to play? (or '0' to quit): "))
            if rounds == 0:
                print("Thank you for playing!")
                break

            for round_number in range(1, rounds + 1):
                print(f"\n--- Round {round_number} ---")
                
                for player in range(num_players):
                    print(f"\nPlayer {player + 1}'s turn:")
                    guess = int(input("Guess the total result of 2 dice (2 to 12): "))
                    while guess < 2 or guess > 12:
                        guess = int(input("Invalid number! Please guess a number between 2 and 12: "))

                    roll_result_1 = random.randint(1, 6)
                    roll_result_2 = random.randint(1, 6)
                    total_roll = roll_result_1 + roll_result_2
                    print(f"You rolled: {roll_result_1} and {roll_result_2} (Total: {total_roll})")

                    if total_roll == guess:
                        print(f"Player {player + 1}: You guessed it right!")
                        scores[player] += 1 
                    else:
                        print(f"Player {player + 1}: Sorry, you guessed wrong.")

                print("\nScores after this round:")
                for player in range(num_players):
                    print(f"Player {player + 1}: {scores[player]} points")

            max_score = max(scores)
            winners = [i + 1 for i, score in enumerate(scores) if score == max_score]

            if len(winners) > 1:
                print(f"\nIt's a tie between players: {', '.join(map(str, winners))} with {max_score} points!")
            else:
                print(f"\nPlayer {winners[0]} wins with {max_score} points!")

        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    multi_player_dice_roll()
