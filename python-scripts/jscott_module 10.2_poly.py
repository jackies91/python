#Jackie Scott 12/8/23 Module 10.2 
#This program will gather and manage employee information

#Create super class for employee, the blueprint 
class Employee:
    def __init__(self, name, gender, pay_rate, employee_number):
        self.name = name
        self.gender = gender
        self.rate = pay_rate
        self.number = employee_number

#setters or mutator for attributes
    def set_name(self, name):
        self.name = name
    def set_gender(self, gender):
        self.gender = gender
    def set_rate(self, pay_rate):
        self.rate = pay_rate
    def set_number(self, employee_number):
        self.number = employee_number

#getters or accessors for attributes
    def get_name(self):
        return self.name
    def get_gender(self):
        return self.gender
    def get_rate(self):
        return self.rate
    def get_number(self):
        return self.number


#create class to inherit employee class information but add shift information
class ProductionWorker(Employee):
    def __init__(self, name, gender, pay_rate, employee_number, shift_number):
        super().__init__(name, gender, pay_rate, employee_number)
        self.shift_number = shift_number
        
    #mutator for attribute
    def set_shift_numbert(self, shift_number):
        self.shift_number = shift_number
    
    #getters
    def get_shift_number(self):
        return self.shift_number
   


#create main class that will inherit employee and productionworker classes and create information
class Main:
     #add workers info so no user input is required
     def run(self):
        employee1 = Employee('John Smith', 'Male', 25.00, 123456)
        employee2 = Employee('Jackie Scott', 'Female', 30.00, 789456)

        prodworker1 = ProductionWorker('Daniel Scott', 'Male', 27.00, 456987, 2)
        prodworker2 = ProductionWorker('Gus Garcia', 'Male', 15.00, 741258, 1)

        #display information for each employee
        self.display_employee(employee1)
        self.display_employee(employee2)
        self.display_employee(prodworker1)
        self.display_employee(prodworker2)
#print all employee information formatted to show in different lines 
     def display_employee(self, Employee):
         print(
        f"\nEmployee Name: {Employee.get_name()} "
        f"\nEmployee Gender: {Employee.get_gender()} "
        f"\nEmployee Payrate: {Employee.get_rate():.2f}/hour "
        f"\nEmployee Number: {Employee.get_number()}" 
        f"\n{'Employee Shift: ' + str(Employee.get_shift_number()) if isinstance(Employee, ProductionWorker) else ''}"
        )
       

#create an instance for main class
main_instance = Main()

#run
main_instance.run()