"""
Today we'll just represent a Person with a dictionary.
Note: you do not have to use lambdas! can always just create new functions as needed
Remember:
* list.sort() will modify the original list
* sorted(list) will return a new list
* both functions take in a parameter called "key" that takes a function telling it how to compare each item
"""

import random
import string


def main():
    people = [
        {
            "first name": "Alice",
            "last name": "Smith",
            "phone": "123-456-1313",
            "age": 14,
        },
        {"first name": "Bob", "last name": "Two", "phone": "987-654-0000", "age": 17},
        {
            "first name": "David",
            "last name": "Brown",
            "phone": "222-153-8765",
            "age": 20,
        },
        {
            "first name": "Catherine",
            "last name": "Jones",
            "phone": "666-555-4444",
            "age": 15,
        },
        {"first name": "Bob", "last name": "One", "phone": "987-654-0000", "age": 17},
    ]

    print(assign_drivers_license(people))


# Part 2-1: Return people with everyone's age increased by 1


def age_plus_1(person):
    person["age"] += 1
    return person


def age_everyone(people):
    aged_people = list(map(age_plus_1, people))
    return aged_people


# Part 2-2:
# Return list of people with first name longer than 3 letters. Hint: use filter


def names_too_long(people):
    return list(filter(lambda person: len(person["first name"]) > 3, people))


# Part 2-3:
# For each person with first name longer than 3 letters, create a new field "nickname" for them that's the first 3 letters of their name. Return the modified list of people.
# Hint: use map() and names_too_long()


def assign_nicknames(people):
    def add_nickname(person):
        first_name = person["first name"]
        nickname = ""
        length = len(first_name)  # first name length
        for i in range(3):
            if i < length:
                nickname += first_name[i]
        # ^ gets first 3 letters of name and adds it to nickname
        # |
        person["nickname"] = nickname
        return person

    def add_nickname2(person):
        # input: one person
        # returns a person with nickname
        first_name = person["first name"]
        person["nickname"] = first_name[0:3]
        return person

    return list(map(add_nickname2, names_too_long(people)))


name = "Catherine"
before = name[:3]
after = name[3:]
print(before, after)


# Part 2-4:
# Create a function called "can_drive()" that returns a list of people who are over 16. Hint: use filter
def can_drive(people):
    return list(filter(lambda person: person["age"] > 16, people))


# Part 2-5:
# For each person who can drive (over 16), create a new field "driver license" for them that contains a random license ID (use the function I provided).
# Hint: use map() and can_drive()


def generate_license():
    return "".join(
        random.choice(string.ascii_uppercase + string.digits) for _ in range(7)
    )


def assign_drivers_license(people):
    def add_license(person):
        person["driver license"] = generate_license()
        return person

    return list(map(add_license, can_drive(people)))


#### Part 1 ####
# Sort people by first name


def return_first_name(person):
    return person["first name"]


def sort_by_first_name(people):
    people.sort(key=return_first_name)
    return people


#### Part 2 ####
# Sort people by age


def sort_by_age(people):
    def get_age(person):
        return person["age"]

    return sorted(people, key=get_age)


#### Part 3 ####
# Sort people by their first and last names combined


def return_full_name(person):
    return person["first name"] + person["last name"]


def sort_by_full_name(people):
    people.sort(key=return_full_name)
    return people


#### Part 4 ####
# Create an email for each person in "people". Emails are "{first name}.{last name}@gmail.com"
# Add the emails to the list of people and return that


def create_email(people):
    for person in people:
        email = f"{person['first name'].lower()}.{
            person['last name'].lower()}@gmail.com"
        person["email"] = email

    return people


main()


# def square(x):
#     return x*x


# original = {1, 2, 3, 4}
# new_l = map(square, original)
# print(list(new_l))


# def is_odd(x):
#     return x % 2 == 1


# odd_nums = list(filter(lambda x: x % 2 == 1, original))
# print(odd_nums)
