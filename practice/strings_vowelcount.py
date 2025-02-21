"""Count number of vowels in a string."""

import string

vowels = {"a", "e", "i", "o", "u"}


def vowelCount(input_str):
    count = 0
    for x in input_str.lower():
        if x in vowels:
            count += 1
    return count


def testVowelCount():
    print("Testing vowelCount()...", end="")
    assert vowelCount("abcdefg") == 2
    assert vowelCount("ABCDEFG") == 2
    assert vowelCount("") == 0
    assert vowelCount("This is a test.  12345.") == 4
    assert vowelCount(string.ascii_lowercase) == 5
    assert vowelCount(string.ascii_lowercase * 100) == 500
    assert vowelCount(string.ascii_uppercase) == 5
    assert vowelCount(string.punctuation) == 0
    assert vowelCount(string.whitespace) == 0
    print("Passed!")


testVowelCount()
