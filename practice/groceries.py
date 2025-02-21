"""Suppose that you're in the habit of making a list of items you need from the
grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one's input to a program). Then output the user's grocery list formatted as follows:
* All uppercase, user's input is case-insensitive
* Sorted alphabetically by item
* Prefixing each line with the number of times the user inputted that item
* No need to pluralize the items

Example:
My Grocery List:
apple
apple
banana
milk
banana
tomato

2 APPLE
2 BANANA
1 MILK
1 TOMATO
"""

my_dict = {"a": 1, "b": 2}
my_dict["c"] = 0
my_dict["a"] = 2
print(my_dict["a"])

def main():
    g_list = {}
    print("If you want to stop adding things to your cart, hit enter")
    while True:
        x = input("Item: ").upper()
        if x == "":
            print_list(g_list)
            break
        else:                   # valid item to add
            if x in g_list:     # we've already seen this input (duplicates)
                g_list[x] += 1  # increment count for that item
            else:               # first time we've seen this input
                g_list[x] = 1   # set count to 1


def print_list(g_list):
    print("This is the final list")
    s = sorted(g_list.keys())
    for x in s:
        print(f"{x}:  {g_list[x]}")
    
main()
