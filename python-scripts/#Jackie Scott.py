#Jackie Scott
#12/3/23
#Module 9.2

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Get user input for a person
user_name = input("Enter the person's name: ")
user_age = int(input("Enter the person's age: "))  # Assuming age is an integer

# Create an instance of the Person class with user input
user_person = Person(user_name, user_age)

# Call the say_hello method
user_person.say_hello()
