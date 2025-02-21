"""Analyzing a dataset of people's favorite movies."""

from collections import defaultdict


# Dataset
data = [
    {
        "Name": "Alice",
        "Movie": "The Avengers",
        "Genre": "Action",
        "Release Year": 2012,
        "Rating": 5,
        "Duration (min)": 143,
        "Box Office ($M)": 158,
    },
    {
        "Name": "Bob",
        "Movie": "Finding Nemo",
        "Genre": "Animation",
        "Release Year": 2003,
        "Rating": 4,
        "Duration (min)": 100,
        "Box Office ($M)": 94,
    },
    {
        "Name": "Charlie",
        "Movie": "The Dark Knight",
        "Genre": "Action",
        "Release Year": 2008,
        "Rating": 5,
        "Duration (min)": 152,
        "Box Office ($M)": 105,
    },
    {
        "Name": "Diana",
        "Movie": "Frozen",
        "Genre": "Animation",
        "Release Year": 2013,
        "Rating": 4,
        "Duration (min)": 102,
        "Box Office ($M)": 127,
    },
    {
        "Name": "Eve",
        "Movie": "Inception",
        "Genre": "Sci-Fi",
        "Release Year": 2010,
        "Rating": 5,
        "Duration (min)": 148,
        "Box Office ($M)": 83,
    },
    {
        "Name": "Frank",
        "Movie": "Interstellar",
        "Genre": "Sci-Fi",
        "Release Year": 2014,
        "Rating": 4,
        "Duration (min)": 169,
        "Box Office ($M)": 101,
    },
    {
        "Name": "Grace",
        "Movie": "Toy Story",
        "Genre": "Animation",
        "Release Year": 1995,
        "Rating": 5,
        "Duration (min)": 81,
        "Box Office ($M)": 73,
    },
    {
        "Name": "Hank",
        "Movie": "Avengers: Endgame",
        "Genre": "Action",
        "Release Year": 2019,
        "Rating": 5,
        "Duration (min)": 181,
        "Box Office ($M)": 798,
    },
]

# https://sharepad.io/live/0Acwcb7 -> restaurant dataset
# Functions


def average_rating(data):
    """What is the average rating of all movies?"""
    # ratings = []
    # for item in data:
    #    ratings.append(item["Rating"])

    ratings = [item["Rating"] for item in data]
    average = sum(ratings) / len(data)
    return average


def genre_with_highest_avg_rating(data):
    """Which genre has the highest average rating?"""
    seen = defaultdict(list)
    for movie in data:
        seen[movie["Genre"]].append(movie["Rating"])

    # get avg rating of each genre
    # seen = {"Action": [4, 5, 4, 4], "Romance": [3, 5, 2]}
    # genre = "Action"
    # ratings = [4, 5, 4, 4]
    averages = defaultdict(list)
    for genre, ratings in seen.items():
        average = sum(ratings) / len(ratings)
        averages[average].append(genre)
    # print(averages)
    max_average = max(averages.keys())
    # print(max_average)
    return averages[max_average]


def movies_per_genre(data):
    """How many movies from each genre are in the dataset?"""
    # {genre: count}
    # genres = {}
    genres = defaultdict(int)
    for movie in data:
        genres[movie["Genre"]] += 1
    return genres


def oldest_movie(data):
    """Which movie is the oldest in the dataset?

    ("Release Year")
    """
    oldest_movie = data[0]["Movie"]
    oldest_year = data[0]["Release Year"]
    for movie in data:
        if movie["Release Year"] < oldest_year:
            oldest_year = movie["Release Year"]
            oldest_movie = movie["Movie"]
    return oldest_movie


def most_popular_genre(data):
    """What is the most popular movie genre based on frequency?"""
    number_of_movies = movies_per_genre(data)
    max_count = 0
    max_genre = ""
    for genre, count in number_of_movies.items():
        if count > max_count:
            max_count = count
            max_genre = genre
    return max(number_of_movies, key=lambda genre: number_of_movies[genre])


def average_duration(data):
    """What is the average duration of movies?"""
    pass


def total_box_office(data):
    """What is the total box office revenue of all movies?"""
    total = 0
    for movie in data:
        total += movie["Box Office ($M)"]
    return total


def highest_box_office_movie(data):
    """Which movie had the highest box office revenue?"""
    pass


def graph_movie_ratings(data):
    """Create a horizontal bar graph of the movie ratings.

    Each row should print the movie name first, then an "x" for each
    point in the rating.
    """
    for movie in data:
        print(movie["Movie"], end="\t\t")
        [print("x", end="") for item in range(movie["Rating"])]
        print()


def graph_box_office(data):
    """Create a horizontal bar graph of the movie ratings.

    Each row should print the movie name first, then an "x" for each 10
    million in box office, rounded to the nearest 10 million
    """
    pass


# Main function to test all functions


def main():
    print("Average rating of all movies:", average_rating(data))
    print("Genre with the highest average rating:", genre_with_highest_avg_rating(data))
    print("Number of movies per genre:", movies_per_genre(data))
    print("Oldest movie in the dataset:", oldest_movie(data))
    print("Most popular movie genre based on frequency:", most_popular_genre(data))
    print("Average duration of movies (minutes):", average_duration(data))
    print("Total box office revenue ($M):", total_box_office(data))
    print("Movie with the highest box office revenue:", highest_box_office_movie(data))
    graph_movie_ratings(data)


# Run the main function
if __name__ == "__main__":
    main()
