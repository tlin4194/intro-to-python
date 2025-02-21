"""Tournament analysis using pandas library."""
import matplotlib.pyplot as plt
import pandas as pd


def main():
    data = pd.read_csv("tennis_tournament.csv")
    print(get_match_winners(data))
    break_points_df = break_points_analysis(data)
    print(break_points_df)
    plot_match_progression(data, match_id=1)


def get_match_winners(df: pd.DataFrame):
    """Returns a summary of the winner of each match."""
    match_results = df.groupby(
        "Match ID").last()  # Get the last recorded point for each match
    print(len(match_results))
    winners = match_results.apply(lambda row: row["Player 1 Name"] if row[
        "Player 1 Sets"] > row["Player 2 Sets"] else row["Player 2 Name"],
        axis=1)
    return winners


def break_points_analysis(df: pd.DataFrame):
    """Finds break points and calculates break point conversion rates."""
    break_points = []
    for _, row in df.iterrows():
        if row["Server"] == row["Player 1 Name"]:
            server_games = row["Player 1 Games"]
            opponent_games = row["Player 2 Games"]
            opponent_score = row["Player 2 Score"]
        else:
            server_games = row["Player 2 Games"]
            opponent_games = row["Player 1 Games"]
            opponent_score = row["Player 1 Score"]

        if opponent_score == "40" and opponent_games < server_games:
            break_points.append(row)

    return pd.DataFrame(break_points)


def plot_match_progression(df, match_id):
    """Plots the point-by-point progression of a given match."""
    match_df = df[df["Match ID"] == match_id]
    match_df.loc["Point Number"] = range(1, len(match_df) + 1)

    plt.plot(match_df["Point Number"], match_df["Player 1 Score"],
             label=str(match_df["Player 1 Name"]), marker="o")
    plt.plot(match_df["Point Number"], match_df["Player 2 Score"],
             label=str(match_df["Player 2 Name"]), marker="o")
    plt.xlabel("Point Number")
    plt.ylabel("Score Progression")
    plt.title(f"Match Progression for Match {match_id}")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
