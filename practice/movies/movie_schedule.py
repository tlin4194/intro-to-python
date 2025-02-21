import pandas as pd
from datetime import datetime, timedelta

# Global Constants
THEATER_OPENING_TIME = "10:00"
THEATER_CLOSING_TIME = "22:00"
NUMBER_OF_THEATERS = 3
CLEANING_TIME_MINUTES = 20


def load_movies():
    """Load movies data from a CSV file."""
    return pd.read_csv("movies.csv")


def calculate_showtimes(movies):
    """Generate a schedule for movies in theaters."""
    opening_time = datetime.strptime(THEATER_OPENING_TIME, "%H:%M")
    closing_time = datetime.strptime(THEATER_CLOSING_TIME, "%H:%M")
    cleaning_time = timedelta(minutes=CLEANING_TIME_MINUTES)

    schedule = []
    # Track movies to ensure each is shown
    unshown_movies = set(movies['Movie'])

    for theater in range(1, NUMBER_OF_THEATERS + 1):
        current_time = opening_time

        for _, movie in movies.iterrows():
            # Convert numpy.int64 to plain Python integer
            movie_duration = timedelta(
                minutes=int(movie['Duration (minutes)']))
            end_time = current_time + movie_duration

            # Ensure the movie ends before the theater closes
            if end_time <= closing_time:
                schedule.append({
                    "Theater": theater,
                    "Movie": movie['Movie'],
                    "Start Time": current_time.strftime("%H:%M"),
                    "End Time": end_time.strftime("%H:%M")
                })
                current_time = end_time + cleaning_time
                unshown_movies.discard(movie['Movie'])  # Mark movie as shown
            else:
                break  # No more movies can fit in this theater

    # Add unshown movies to the schedule
    for movie in unshown_movies:
        for theater in range(1, NUMBER_OF_THEATERS + 1):
            current_time = opening_time
            while current_time < closing_time:
                # Convert numpy.int64 to plain Python integer
                movie_duration = timedelta(minutes=int(
                    movies.loc[movies['Movie'] == movie, 'Duration (minutes)'].iloc[0]))
                end_time = current_time + movie_duration

                if end_time <= closing_time:
                    schedule.append({
                        "Theater": theater,
                        "Movie": movie,
                        "Start Time": current_time.strftime("%H:%M"),
                        "End Time": end_time.strftime("%H:%M")
                    })
                    break  # Stop once the movie is scheduled

    return schedule


def save_schedule(schedule):
    """Save the schedule to a CSV file."""
    df = pd.DataFrame(schedule)
    df.to_csv("schedule.csv", index=False)
    print("Schedule saved to 'schedule.csv'!")


def main():
    """Main function to generate the theater schedule."""
    movies = load_movies()
    schedule = calculate_showtimes(movies)
    save_schedule(schedule)


if __name__ == "__main__":
    main()
