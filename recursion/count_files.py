files = [
    "File 1",
    [
        "File 2",
        [
            "File 3",
            "File 4",
        ],
        "File 5",
        "File 6"
    ],
    "File 7",
    [
        "File 8",
        "File 9"
    ],
    "File 10"
]


def main():
    print(count_files(files))


def count_files(folder):
    """Recursively counts and returns the number of leaf items in a
    (potentially nested) list."""
    count = 0
    for item in folder:                 # For each item in the current folder
        if isinstance(item, list):      # Check if this item is actually a subfolder
            count += count_files(item)  # Recursive call
        else:
            count += 1                  # Base case

    return count


main()
