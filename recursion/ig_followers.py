class Person:
    def __init__(self, name):
        self.name = name
        self.follows = []

    def follow(self, person):
        """Add a person to the follow list."""
        self.follows.append(person)


def count_people_in_network(person, visited=None):
    """Recursively count all unique people in the network."""
    if visited is None:
        visited = set()

    # If this person has already been visited, don't count them again
    if person.name in visited:
        return 0

    # Mark this person as visited
    visited.add(person.name)

    # Count the current person (1) and recursively count the people they follow
    count = 1
    for followed_person in person.follows:
        count += count_people_in_network(followed_person, visited)

    return count


# Example usage:
if __name__ == "__main__":
    # Create people
    alice = Person("Alice")
    bob = Person("Bob")
    charlie = Person("Charlie")
    diana = Person("Diana")
    eddie = Person("Eddie")
    frances = Person("Frances")

    # Create follow relationships
    alice.follow(bob)
    alice.follow(charlie)
    alice.follow(eddie)
    bob.follow(charlie)
    charlie.follow(diana)
    diana.follow(alice)
    eddie.follow(frances)

    # Count people in Alice's network
    total_people = count_people_in_network(alice)
    print(f"Total people in the network: {total_people}")
