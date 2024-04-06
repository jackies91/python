#Jackie Scott
#10/24/23
#Module 2.2 calculate cost of fiber install, bulk discount

#This code will calculate the cost of installing fiber cable with a bulk discount

#Display a welcome message for your program.
print("Welcome to Fast Fiber Internet")

#Get the number of feet of fiber optic to be installed from the user.
feet_fiber = float(input("Enter the number of feet of fiber optic cable you will need installed:"))

#Initialize fiber_cost variable to store the cost.
fiber_cost = 0.0

#List with highest footage first as python fires in the order it is scripted and once a condition is met the script stops. This ensures we look through every condition possible to get the most accurate calculation.
if feet_fiber >= 500:                #If they purchase more than 500 feet, they will be charged $.50 per foot
    fiber_cost = feet_fiber * .50 
elif feet_fiber >= 250:              #If the user purchases more than 250 feet, they will be charged $.70 per foot
    fiber_cost = feet_fiber * .70 
elif feet_fiber >= 100:              #If the user purchases more than 100 feet, they are charged $.80 per foot.
    fiber_cost = feet_fiber * .80
else:
    fiber_cost = feet_fiber * 0.87   #A base price in case the conditions above are not met. I used the rate from Module 1.3 assignment

#Display the calculated information and company name.
print(f"The total cost of your fiber optic cable installed by Fast Fiber Internet is ${fiber_cost:.2f}")