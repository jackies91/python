# This program will calculate and display student cumulative GPA.

# First create our class to store student information about themselves, class credits, and points
class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.total_credits = 0
        self.total_points = 0
        # initialize total credits and points

    # This def will help tally the total credits and points as well as calculate GPA
    def add_courses(self, credits, points):
        self.total_credits += credits
        self.total_points += points * credits

    # This def will check if the total credits entered are greater than zero,
    # if so, it will calculate GPA by dividing the total from above def by total credits
    def calculate_gpa(self):
        if self.total_credits == 0:
            return 0.0
        return self.total_points / self.total_credits

    # To display the calculations and student input
    def display_gpa(self):
        print(f"{self.first_name} {self.last_name}'s Cumulative GPA: {self.calculate_gpa():.2f}")


# Now we can write our code to use the class we created above, Student
def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')

    student = Student(first_name, last_name)

    # Creating our loop and validating that user input is good since we can not divide by zero.
    while True:
        try:
            credits = float(input('Enter your total class credits or "0" to exit: '))
            if credits == 0:
                break

            points = float(input('Enter total grade points: '))
            student.add_courses(credits, points)

        except ValueError:
            print('Enter only numbers greater than Zero')

    student.display_gpa()

main()
