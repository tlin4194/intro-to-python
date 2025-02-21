"""String manipulation, sets, loops."""


def main():
    first_names = ["Alice", "Bob", "Catherine", "David"]
    last_names = ["Smith", "Lee", "Jones", "Brown"]
    print(combine_names(first_names, last_names))

    test1 = [2, 8, 3, 9, -1, -3]
    test2 = [1, 3, 2, 5, 0]
    print("Duplicates between lists: " + str(find_dups(test1, test2)))

    print(find_2nd_smallest(test1))
    print(find_2nd_smallest(test2))


def combine_names(first_names, last_names):
    """Return a list of full names (first and last names combined)"""
    # i.e. ["Alice Smith", "Bob Lee", "Catherine Jones", "David Brown"]
    full_names = []
    for i in range(len(first_names)):
        full_names.append(first_names[i] + " " + last_names[i])
    return full_names


def find_dups(list1, list2):
    """Return list of all duplicates between list1 and list2."""
    duplicates_within_list1 = set()
    duplicates_within_list2 = set()
    duplicates_between_lists = set()

    seen_list1 = set()
    for item in list1:
        if item in seen_list1:
            duplicates_within_list1.add(item)
        else:
            seen_list1.add(item)

    seen_list2 = set()
    for item in list2:
        if item in seen_list2:
            duplicates_within_list2.add(item)
        else:
            seen_list2.add(item)

    for item in list1:
        if item in list2:
            duplicates_between_lists.add(item)

    return duplicates_between_lists


def find_2nd_smallest(nums):
    """Return the 2nd smallest integer in nums.

    `nums` is a list of integers.
    """

    unique_nums = set(nums)
    unique_nums_list = list(unique_nums)
    unique_nums_list.sort()
    print(unique_nums_list)
    if len(unique_nums_list) > 1:
        return unique_nums_list[1]
    else:
        return None


main()
