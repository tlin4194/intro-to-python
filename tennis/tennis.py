"""Tracking live points results from a tennis tournament.

Reference data: https://github.com/JeffSackmann/tennis_slam_pointbypoint/blob/master/2024-wimbledon-points.csv
"""

import csv
from collections import defaultdict


def main():
    filename = "tennis_tournament.csv"
    data = load_csv(filename)
    # print(data)
    for match_id in ["1", "2", "3", "4"]:
        print(current_winning_player(data, match_id=match_id))
    print(get_rankings(data))
    # print(f"The highest ranked player is: {best_player}")


def load_csv(filename):
    """Load the tennis match data from a CSV file into a list of
    dictionaries."""
    with open(filename, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def current_winning_player(data, match_id=""):
    """For each match ID, return the name of the player who is leading."""
    # Find the last row with current match_id so we can get the latest scores
    for i in range(len(data) - 1, -1, -1):
        row = data[i]
        current_match_id = row["Match ID"]
        if current_match_id == match_id:  # current row is this match
            # Compare sets
            # Compare games
            # Comparing the current score to find who's winning
            if row["Player 1 Sets"] > row["Player 2 Sets"]:
                return row["Player 1 Name"]
            elif row["Player 2 Sets"] > row["Player 1 Sets"]:
                return row["Player 2 Name"]
            elif row["Player 1 Games"] > row["Player 2 Games"]:
                return row["Player 1 Name"]
            elif row["Player 2 Games"] > row["Player 1 Games"]:
                return row["Player 2 Name"]
            elif row["Player 1 Score"] > row["Player 2 Score"]:
                return row["Player 1 Name"]
            elif row["Player 2 Score"] > row["Player 1 Score"]:
                return row["Player 2 Name"]
            return None  # it's a tie
    # if match_id is not in file
    return "Match hasn't started yet"


def get_rankings(data):
    """Return list of players in order of their ranking based on matches
    won."""
    players = defaultdict(int)  # {name of player: number of matches won}}

    # step 1: figure out how many matches each player has won
    # loop through the data, look at each row
    # If someone has 2 sets won, add 1 to their # of matches won
    for row in data:
        # print(row)
        if row["Player 1 Sets"] == "2":  # if player 1 won the match
            winner = row["Player 1 Name"]
            loser = row["Player 2 Name"]
            print(f"{winner} has won")
            players[winner] += 1
            players[loser] = players[loser]
        elif row["Player 2 Sets"] == "2":  # if player 2 won the match
            winner = row["Player 2 Name"]
            loser = row["Player 1 Name"]
            print(f"{winner} has won")
            players[winner] += 1
            players[loser] = players[loser]

    print(players)
    # step 2: Sort the list of players by the number of matches they have won
    return sorted(players, key=lambda k: players[k], reverse=True)


if __name__ == "__main__":
    main()
