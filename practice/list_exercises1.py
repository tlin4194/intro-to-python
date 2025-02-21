def main():
    my_list = [10, 2, -1, 5, 7, 8, 6, 11]
    # feel free to add test cases in main
    test_a = [-1, 2, 5, -3, 0, 6, 2, -1]
    test_b = [5, 7, 2, 0, -5]
    # print(filter_even_numbers(test_a))
    # print(filter_even_numbers(test_b))
    print(remove_duplicates(test_a))
    # test your other functions


def sum_of_list(l):
    # return sum of the list
    sums = 0
    for i in l:
        sums += i
    return sums


def get_max(l):
    # return biggest number in the list
    current_max = l[0]
    for i in l:
        if i > current_max:
            current_max = i
    return current_max


def count_occurrences(l, element):
    # return the number of times a specific element is in the list
    count = 0
    for i in l:
        if i == element:
            count += 1
    return count


def filter_even_numbers(l):
    # return the list without any of the even numbers
    # for i in l:
    #    if i % 2 != 0: # is even
    #       return i
    # or

    final_list = []
    for i in l:
        if i % 2 != 0:
            final_list.append(i)
    return final_list


def find_x(l, element):
    # find element in the list, and return the index where it is. If element is not in the list, return None
    for i in range(len(l)):
        if l[i] == element:
            return i
    return None


def remove_duplicates(l):
    # return the list without any duplicates
    newlist = []
    for i in l:
        if i not in newlist:
            newlist.append(i)
    return newlist


main()
