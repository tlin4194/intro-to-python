class Employee:
    def __init__(self, name):
        self.name = name
        self.team_members = []

    def add_team_member(self, team_member):
        """Add a team_member to this manager's team."""
        self.team_members.append(team_member)


def count_employees(employee):
    """Recursively count the number of employees under a given manager."""
    count = 1  # Count the current employee
    for team_member in employee.team_members:
        count += count_employees(team_member)  # Recursively count team_members
    return count


# Example usage:
if __name__ == "__main__":
    # Create employees
    ceo = Employee("CEO")
    manager1 = Employee("Manager1")
    manager2 = Employee("Manager2")
    employee1 = Employee("Employee1")
    employee2 = Employee("Employee2")
    employee3 = Employee("Employee3")
    intern1 = Employee("Intern1")
    intern2 = Employee("Intern2")

    # Create reporting relationships
    ceo.add_team_member(manager1)
    ceo.add_team_member(manager2)
    manager1.add_team_member(employee1)
    manager1.add_team_member(employee2)
    manager2.add_team_member(employee3)
    employee2.add_team_member(intern1)
    employee3.add_team_member(intern2)

    # Count all employees starting from the CEO
    total_employees = count_employees(ceo)
    print(f"Total employees in the company: {total_employees}")
