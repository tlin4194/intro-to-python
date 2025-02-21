"""Analyzing a dataset of people's favorite restaurants
"""

from collections import defaultdict

# Dataset
data = [
    {
        "Name": "Mia",
        "Restaurant": "Olive Garden",
        "Cuisine": "Italian",
        "City": "New York",
        "Rating": 4.5,
        "Average Meal Cost ($)": 25,
        "Year Established": 1982,
    },
    {
        "Name": "Joey",
        "Restaurant": "Chipotle",
        "Cuisine": "Mexican",
        "City": "San Francisco",
        "Rating": 4.0,
        "Average Meal Cost ($)": 12,
        "Year Established": 1993,
    },
    {
        "Name": "Alex",
        "Restaurant": "Sushi Zen",
        "Cuisine": "Japanese",
        "City": "Los Angeles",
        "Rating": 4.8,
        "Average Meal Cost ($)": 35,
        "Year Established": 2005,
    },
    {
        "Name": "Sophia",
        "Restaurant": "BBQ Barn",
        "Cuisine": "Barbecue",
        "City": "Austin",
        "Rating": 4.7,
        "Average Meal Cost ($)": 28,
        "Year Established": 1932,
    },
    {
        "Name": "Zoey",
        "Restaurant": "Pasta Palace",
        "Cuisine": "Italian",
        "City": "Chicago",
        "Rating": 4.3,
        "Average Meal Cost ($)": 22,
        "Year Established": 1995,
    },
    {
        "Name": "Liam",
        "Restaurant": "Burger Haven",
        "Cuisine": "American",
        "City": "Miami",
        "Rating": 4.1,
        "Average Meal Cost ($)": 15,
        "Year Established": 2000,
    },
    {
        "Name": "Ralph",
        "Restaurant": "Curry House",
        "Cuisine": "Indian",
        "City": "Seattle",
        "Rating": 4.6,
        "Average Meal Cost ($)": 18,
        "Year Established": 2012,
    },
    {
        "Name": "Bella",
        "Restaurant": "Taco Fiesta",
        "Cuisine": "Mexican",
        "City": "Dallas",
        "Rating": 4.4,
        "Average Meal Cost ($)": 10,
        "Year Established": 2008,
    },
]

# Dataset
data2 = [
    {
        "Name": "Alice",
        "Restaurant": "Olive Garden",
        "Cuisine": "Italian",
        "City": "New York",
        "Rating": 4.5,
        "Average Meal Cost ($)": 25,
        "Year Established": 1982,
    },
    {
        "Name": "Bob",
        "Restaurant": "Chipotle",
        "Cuisine": "Mexican",
        "City": "San Francisco",
        "Rating": 4.0,
        "Average Meal Cost ($)": 12,
        "Year Established": 1993,
    },
    {
        "Name": "Charlie",
        "Restaurant": "Sushi Zen",
        "Cuisine": "Japanese",
        "City": "Los Angeles",
        "Rating": 4.8,
        "Average Meal Cost ($)": 35,
        "Year Established": 2005,
    },
    {
        "Name": "Diana",
        "Restaurant": "BBQ Barn",
        "Cuisine": "Barbecue",
        "City": "Austin",
        "Rating": 4.7,
        "Average Meal Cost ($)": 28,
        "Year Established": 2010,
    },
    {
        "Name": "Eve",
        "Restaurant": "Pasta Palace",
        "Cuisine": "Italian",
        "City": "Chicago",
        "Rating": 4.3,
        "Average Meal Cost ($)": 22,
        "Year Established": 1995,
    },
    {
        "Name": "Frank",
        "Restaurant": "Burger Haven",
        "Cuisine": "American",
        "City": "Miami",
        "Rating": 4.1,
        "Average Meal Cost ($)": 15,
        "Year Established": 2000,
    },
    {
        "Name": "Grace",
        "Restaurant": "Curry House",
        "Cuisine": "Indian",
        "City": "Seattle",
        "Rating": 4.6,
        "Average Meal Cost ($)": 18,
        "Year Established": 2012,
    },
    {
        "Name": "Hank",
        "Restaurant": "Taco Fiesta",
        "Cuisine": "Mexican",
        "City": "Dallas",
        "Rating": 4.4,
        "Average Meal Cost ($)": 10,
        "Year Established": 2008,
    },
]


# Functions
def average_rating(data):
    """What is the average restaurant rating across all entries?"""
    sum = 0
    for restaurant in data:
        sum += restaurant["Rating"]
    average = sum / len(data)
    return average


def cuisine_with_highest_avg_rating(data):
    """Which cuisine has the highest average rating?"""
    cuisine_average_rating = defaultdict(list)  # {cuisine: [rating1, rating2, ...]}
    for restaurant in data:
        cuisine_average_rating[restaurant["Cuisine"]].append(restaurant["Rating"])
    max_avg = 0
    best_cuisine = ""
    # go through each cuisine and calc the avg rating for each + keep track of the max avg we've seen so far
    for cuisine, ratings in cuisine_average_rating.items():
        average = sum(ratings) / len(ratings)
        if average > max_avg:
            max_avg = average
            best_cuisine = cuisine
    return best_cuisine


def restaurants_per_cuisine(data):
    """How many restaurants are there for each type of cuisine?"""
    # {cuisine: # of restaurants}
    # {"Japanese": 1}
    x = defaultdict(int)
    for restaurant in data:
        cuisine = restaurant["Cuisine"]  # string type
        x[cuisine] += 1
    return x


def oldest_restaurant(data):
    """Which restaurant is the oldest in the dataset?"""
    first_restaurant = data[0]
    oldest = first_restaurant["Year Established"]
    restaurant_name = first_restaurant["Restaurant"]
    for restaurant in data:
        if restaurant["Year Established"] < oldest:
            oldest = restaurant["Year Established"]
            restaurant_name = restaurant["Restaurant"]
    return restaurant_name


def most_popular_cuisine(data):
    """What is the most common cuisine based on frequency?"""
    # {cuisine: # of restaurants}
    frequency = restaurants_per_cuisine(data)
    most_frequent = 0
    most_frequent_cuisine = ""
    for cuisine, num_restaurants in frequency.items():
        if num_restaurants > most_frequent:
            most_frequent = num_restaurants
            most_frequent_cuisine = cuisine
    return most_frequent_cuisine


def average_meal_cost(data):
    """What is the average meal cost across all restaurants?"""
    pass


def city_with_highest_avg_rating(data):
    """What city has the most highly rated restaurants on average?"""
    pass


def highest_rated_restaurant(data):
    """Which restaurant has the highest rating?"""
    pass


def graph_restaurant_ratings(data):
    """Create a horizontal bar graph of restaurant ratings. Number of X = number of 0.1 rating points above 4, i.e. 4.1 rating = 1 X"""
    for restaurant in data:
        rating = restaurant["Rating"]
        if rating >= 4:
            smth = rating * 10
            num_of_x = smth % 10
            name = restaurant["Restaurant"]
            x = "X" * int(num_of_x)
            print(f"{name}\t{x}")
        else:
            print(restaurant["Restaurant"])


def graph_meal_costs(data):
    """Create a horizontal bar graph of average meal costs."""


# Main function to test all functions
def main():
    print("Average restaurant rating: ", average_rating(data))
    print(
        "Cuisine with the highest average rating: ",
        cuisine_with_highest_avg_rating(data),
    )
    print("Number of restaurants per cuisine: ", restaurants_per_cuisine(data))
    print("Oldest restaurant in the dataset: ", oldest_restaurant(data))
    print("Most common cuisine: ", most_popular_cuisine(data))
    print("Average meal cost ($): ", average_meal_cost(data))
    print(
        "City with the highest average restaurant rating: ",
        city_with_highest_avg_rating(data),
    )
    print("Highest-rated restaurant: ", highest_rated_restaurant(data))
    print("\nRestaurant Ratings Graph: ")
    graph_restaurant_ratings(data)
    print("\nMeal Costs Graph: ")
    graph_meal_costs(data)


# Run the main function
if __name__ == "__main__":
    main()
