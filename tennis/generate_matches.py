import csv
import random
from datetime import datetime, timedelta

# Tennis point progression
POINTS = ["0", "15", "30", "40", "AD"]
BEST_OF = 3  # Best-of-three sets match


def main():
    """Main function to generate and save a simulated tennis match."""
    matches = [
        ("Alice", "Bob", None),
        ("Charlie", "Dave", 50),
        ("Eve", "Frank", None),
        ("Alice", "Bob", 30),
    ]
    all_matches_data = []

    for i, match in enumerate(matches):
        player1, player2, max_num_points = match
        print(max_num_points)
        match_data = generate_match(
            i+1, player1, player2, max_num_points, BEST_OF)
        all_matches_data.extend(match_data)

    save_to_csv(all_matches_data, "tennis_tournament.csv")


def generate_match(match_id, player1, player2, max_num_points=None, best_of=3):
    """
    Simulates a tennis match until either:
    1. The specified number of points (max_num_points) is reached.
    2. A player wins the match (best-of-three or best-of-five sets).
    """
    match_data = []

    # Initial match state
    player1_score, player2_score = "0", "0"
    player1_games, player2_games = 0, 0
    player1_sets, player2_sets = 0, 0
    server = random.choice([player1, player2])  # Randomize initial server
    start_time = datetime.now()

    points_played = 0
    while (not max_num_points or points_played < max_num_points) and not is_match_over(
            player1_sets, player2_sets, best_of):
        timestamp = start_time + timedelta(
            seconds=len(match_data) *
            random.randint(30, 90))  # Simulate time progression

        # Randomly decide who wins the point
        point_winner = random.choice([player1, player2])

        # Update scores with correct AD and Deuce handling
        player1_score, player2_score = update_score(player1_score,
                                                    player2_score,
                                                    point_winner == player1)

        # Check for game win
        annotation = check_game_status(player1, player2, player1_score,
                                       player2_score, player1_games,
                                       player2_games)

        if annotation == f"{player1} wins game":
            player1_games += 1
            player1_score, player2_score = "0", "0"  # Reset scores after game win
        elif annotation == f"{player2} wins game":
            player2_games += 1
            player1_score, player2_score = "0", "0"  # Reset scores after game win

        # Check for set win (6 games needed with 2-game lead)
        if player1_games >= 6 and player1_games - player2_games >= 2:
            annotation += f" | {player1} wins set"
            player1_sets += 1
            player1_games, player2_games = 0, 0  # Reset games after set win
        elif player2_games >= 6 and player2_games - player1_games >= 2:
            annotation += f" | {player2} wins set"
            player2_sets += 1
            player1_games, player2_games = 0, 0  # Reset games after set win

        # Stop match if a player has won the required number of sets
        if is_match_over(player1_sets, player2_sets, best_of):
            annotation += f" | {player1 if player1_sets >
                                player2_sets else player2} wins match"

        # Change server every game
        if player1_score == "0" and player2_score == "0":
            server = player1 if server == player2 else player2  # Alternate server

        # Append match data row
        match_data.append([
            timestamp.strftime("%Y-%m-%d %H:%M:%S"), match_id, player1,
            player2, server, player1_score, player2_score, player1_games,
            player2_games, player1_sets, player2_sets, annotation
        ])

        points_played += 1  # Increase points played count

    return match_data


def update_score(player1_score, player2_score, player1_wins_point):
    """Updates the score based on who won the point.

    Handles normal point progression, game-winning scenarios, and Deuce
    resets.
    """
    if player1_wins_point:  # Player 1 wins the point
        if player1_score == "40" and player2_score not in ["40", "AD"]:
            return "Game", player2_score  # Player 1 wins the game immediately
        elif player1_score == "40" and player2_score == "40":
            return "AD", "40"  # Player 1 gains Advantage
        elif player1_score == "AD":
            return "Game", player2_score  # Player 1 wins from Advantage
        elif player2_score == "AD":
            return "40", "40"  # Reset to Deuce
        return next_score(player1_score), player2_score
    else:  # Player 2 wins the point
        if player2_score == "40" and player1_score not in ["40", "AD"]:
            return player1_score, "Game"  # Player 2 wins the game immediately
        elif player2_score == "40" and player1_score == "40":
            return "40", "AD"  # Player 2 gains Advantage
        elif player2_score == "AD":
            return player1_score, "Game"  # Player 2 wins from Advantage
        elif player1_score == "AD":
            return "40", "40"  # Reset to Deuce
        return player1_score, next_score(player2_score)


def next_score(current_score):
    """
    Returns the next score in the sequence: 0 -> 15 -> 30 -> 40.
    """
    if current_score == "0":
        return "15"
    elif current_score == "15":
        return "30"
    elif current_score == "30":
        return "40"
    return current_score  # Should not reach here


def check_game_status(player1, player2, score1, score2, games1, games2):
    """Determines the annotation for the current point."""
    if score1 == "40" and score2 == "40":
        return "Deuce"
    elif score1 == "AD":
        return f"Advantage {player1}"
    elif score2 == "AD":
        return f"Advantage {player2}"
    elif score1 == "Game":
        return f"{player1} wins game"
    elif score2 == "Game":
        return f"{player2} wins game"
    return ""


def is_match_over(player1_sets, player2_sets, best_of):
    """Checks if the match has been won by either player.

    - Best of 3: First to 2 sets
    - Best of 5: First to 3 sets
    """
    required_sets = best_of // 2 + 1
    return player1_sets >= required_sets or player2_sets >= required_sets


def save_to_csv(match_data, filename="tennis_tournament.csv"):
    """Saves match data to a CSV file."""
    headers = [
        "Timestamp", "Match ID", "Player 1 Name", "Player 2 Name", "Server",
        "Player 1 Score", "Player 2 Score", "Player 1 Games", "Player 2 Games",
        "Player 1 Sets", "Player 2 Sets", "Annotations"
    ]

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(match_data)


if __name__ == "__main__":
    main()
