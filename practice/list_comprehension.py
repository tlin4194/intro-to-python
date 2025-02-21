# Part 1: List/dictionary comprehension and argument unpacking
# Part 2: More list/dictionary iteration practice


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

    # get_phone_nums(people)
    # get_phone_nums2(people)
    # get_phone_nums4(people, "Alice", "Bob", "David")
    # print(create_phonebook(people))
    print(first_to_last_name(people))
    print(age_by_first_name(people))
    print(sum_of_all_ages(people))
    print(sum_of_some_ages(people, "Alice", "Bob", "David"))
    print(count_by_first_name(people))


# Part 1: Return phone numbers in a list
def get_phone_nums(people):
    # for i, person in enumerate(people):
    #     print(i, person["phone"])

    # numbers = [(i, person["phone"]) for i, person in enumerate(people)]

    return [person["phone"] for person in people]


# Part 1-2:
# Return phone numbers in a list, but ONLY for people who are over 16
# HINT: use list comprehension with if


def get_phone_nums2(people):
    return [person["phone"] for person in people if person["age"] > 16]


# Part 2:
# print the phone numbers for each person that gets passed in as argument
# don't need to return anything
# HINT: * turns all the arguments into a tuple you can use inside the function!


def get_phone_nums3(people, *names):
    print(names)
    for person in people:
        if person["first name"] in names:
            print(person["phone"])


def get_phone_nums4(people, *names):
    for name in names:
        # Assuming name is first name, we need to find the first matching person
        for person in people:
            if person["first name"] == name:
                print(person["phone"])


# Part 3
# Return a new dictionary with person's full name as key, phone number as value
# i.e. {"Alice Smith": "123-456-1313", "Bob One": "987-654-0000"}
# HINT: use dictionary comprehension


def create_phonebook(people):
    return {
        f'{person["first name"]} {person["last name"]}': person["phone"]
        for person in people
    }


# Part 4: Return a new dictionary with each person's first name mapped to their last name
# i.e. {"Alice": ["Smith"], "Bob": ["Two, "One"]}
def first_to_last_name(people):

    # return {person["first name"]: [person["last name"]] for person in people}
    names = {}
    for person in people:

        if person["first name"] in names:
            # if we've seen this first name before
            first_name_to_look_for = person["first name"]
            my_list = names[first_name_to_look_for]
            my_list.append(person["last name"])

        else:
            # if we've never seen this name before
            # 1. get the person's first name
            # 2. lookup the person's first name in the names dictionary and set it equal to an empty list
            # 3. Now we can append the last name into that empty list
            first_name_to_look_for = person["first name"]
            # empty list with first name in it
            names[first_name_to_look_for] = [person["last name"]]

    return names


# Part 5: Return a new dictionary with each first name mapped to a list of ages for people with that first name
# i.e. {"Alice": [14], "Bob": [17, 17] ....}
def age_by_first_name(people):
    pass


# Part 6: Create a list of everyone's age using list comprehension, and then return the sum of everyone's age.
# Hint: use sum(my_list) to get the sum of all items in a list of numbers.
def sum_of_all_ages(people):
    pass


# Part 7: Similar to sum_of_all_ages, but now I only want to sum the ages for specific first names I pass in.
# i.e: if names = ("Alice", "David"), then return 14+20 = 34
def sum_of_some_ages(people, *names):
    pass


# Part 8: Create a new dictionary with first name as key, and how many people have that first name as value.
# i.e. {"Alice": 1, "Bob": 2, "David": 1 ...}
def count_by_first_name(people):
    pass


main()
