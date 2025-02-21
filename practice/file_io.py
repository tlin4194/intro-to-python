"""
Reading/writing a file
https://www.w3schools.com/python/python_file_open.asp
https://www.w3schools.com/python/python_file_write.asp 
"""


def main():
    write_nums_to_file("test1.txt", [1, 3, 2, 5, 0])
    write_nums_to_file("test2.txt", [2, 8, 3, 9, -1, -3])
    test1 = read_nums_file("test1.txt")
    test2 = read_nums_file("test2.txt")
    print(test1)
    print(test2)


def write_nums_to_file(filename, nums):
    """Write a given list of integers to a file called `{filename}.csv`"""
    # CSV format: each integer is separated by commas, all in 1 line.
    # Use "with" keyword, open() function and write() function
    # Note: There's no comma after the last integer

    ##### 1st Method without join() #####
    # last_num = nums.pop(-1)

    # with open(filename, "w") as file:
    #     for num in nums:
    #         file.write(f"{num}, ")

    #     file.write(f"{last_num}")

    ##### 2nd Method with join() #####
    nums_as_str = map(str, nums)
    x = ",".join(nums_as_str)
    with open(filename, "w") as file:
        file.write(x)


def read_nums_file(filename):
    """Read the comma separated integers from `{filename}.txt` and return the
    list of integers."""
    # Hints:
    # Use "with" keyword and open() function
    # Use split to separate list of numbers

    with open(filename, "r") as file:
        contents = file.read()

    string_numbers = contents.split(",")
    int_numbers = []

    for num in string_numbers:
        int_numbers.append(int(num))

    return int_numbers


main()
