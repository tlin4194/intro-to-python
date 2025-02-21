def print_row(width):
    print("#" * width)


def print_block(width, height):
    for _ in range(height):
        print_row(width)


def print_block2(width, height):
    for i in range(height):
        # printing a row
        for j in range(width):
            print("#", end="")
        # Add a new line at end of row
        print()


def print_triangle(height):
    # type here
    for i in range(height):
        i += 1
        print("#" * i)


print_triangle(5)
# print_block2(5, 5)


#
##
###
####
