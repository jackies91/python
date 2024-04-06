#Jackie Scott
#10/18/23
#Module 1.3 calculate cost of fiber install

#This code will calculate the cost of installing fiber cable

#Display a welcome message for your program.
print("Welcome to Fast Fiber Internet")

#Get the number of feet of fiber optic to be installed from the user.
feet_fiber = float(input("Enter the number of feet of fiber optic cable you will need installed:"))

#Multiply the total cost as the number of feet times .87.
fiber_cost = feet_fiber * 0.87

#Display the calculated information and company name.
print("The total cost of your fiber optic cable installed by Fast Fiber Internet is $",fiber_cost)

input("Press Enter to exit")
                
