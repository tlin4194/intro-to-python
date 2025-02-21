"""Writing your first class!"""


class Car:
    # This is an example of a class. Car has to be capitalized.

    # This is an init function that gets called automatically when you create an INSTANCE of the CLASS
    def __init__(self, price, color, make, model):
        if not isinstance(price, int) or price < 0:
            # Checks if price is a positive integer
            raise ValueError("Invalid price")
        if make not in ["Toyota", "Honda", "Ford", "Lexus"]:
            raise ValueError("Invalid make")
        # these are instance variables - specific info for each car I create
        self.price = price
        self.color = color
        self.make = make
        self.model = model

    def __str__(self):
        return f"This {
            self.color}  {
            self.make}  {
            self.model}  car costs {
            self.price}."

    def beep(self, num_beeps):
        print("Beep " * num_beeps)


# This is how you create an instance of the Car class
my_car = Car(10000, "silver", "Toyota", "Camry")
print(my_car)
my_car.beep(3)


# Your turn
# Create a class that represents a person. The person has first name, last name, an email, phone number, and an outfit.
# Person() has some functions:
# __str__: return their first and last name
# talk: prints a string you want them to say as argument
# go_to: takes in a place to go to as argument (string). Print "{first_name} {last_name} is going to {place}."
# change outfit: takes in a tuple of clothes as strings. i.e. ("white shirt", "jeans", "sneakers")

# Then create a couple of people and try calling some of the functions.


class Person:

    # parameter: input to your function from the perspective of your function
    # arguents: what you put into the parameter
    # variable: some unknown quantity with a name
    def __init__(self, first_name, last_name, email, phone_number, outfit):
        # instance variable
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.outfit = outfit

    def __str__(self):
        # anytime we convert a person to a string, use this
        return f"{self.first_name} {self.last_name}"

    def talk(self, sentence):
        print(sentence)

    def go_to(self, place):
        print(f"{self.first_name} {self.last_name} is going to {place}.")

    def change_outfit(self, new_outfit):
        self.outfit = new_outfit
        print(
            f"{self.first_name} {
                self.last_name} changed outfit to {self.outfit}."
        )


class Student(Person):
    def __init__(self, first_name, last_name, subjects, school):
        super().__init__(
            first_name, last_name, None, None, ("shirt", "skirt", "sneakers")
        )
        self.school = school
        self.subjects = subjects

    def __str__(self):
        # anytime we convert a person to a string, use this
        return (
            f"{self.first_name} {self.last_name} takes {self.subjects} at {self.school}"
        )


student1 = Student("Alice", "Smith", "Algebra 2, English, Biology", "SHS")
print(student1)

person1 = Person(
    "Alice",
    "Smith",
    "alicesmith@gmail.com",
    "425-777-5725",
    ("shirt", "skirt", "flats"),
)
person2 = Person("Bob", "the Builder", "bobthebuilder@gmail.com", "911", ("pajamas",))
person3 = Person(
    "Ariana",
    "Greenblatt",
    "arianagreenblatt@gmail.com",
    "333-333-333",
    ("hoodie", "sweats", "socks"),
)

print(person1)
person1.talk("Hello, world!")
person1.go_to("Paris")
person1.change_outfit(("dress", "heels"))
print()

print(person2)
person2.talk("Can we fix it?")
person2.go_to("the construction site")
person2.change_outfit(("flannel shirt", "overalls", "boots"))
print()

print(person3)
person3.talk("Have a good day!")
person3.go_to("school")
person3.change_outfit(("tank top", "jeans", "sneakers"))
