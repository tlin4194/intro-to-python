"""
Palindrome Checker

Write a Python function that checks if a given string is a palindrome. A palindrome is a string that reads the same backward as forward.

Example:
For input "radar", the output should be True.
For input "hello", the output should be False.
"""


def main():
    test = ["hello", "radar", "ababbaba"]
    for t in test:
        print(is_palindrome(t))


def is_palindrome(s):
    for i in range(len(s) // 2):
        # print(f"{i=}, {s[i]=}")
        if s[i] != s[len(s) - 1 - i]:
            return False
    # didn't find any mismatches
    return True


main()
