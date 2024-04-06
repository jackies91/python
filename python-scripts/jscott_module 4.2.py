#Jackie Scott
#11/3/23
#Module 4.2

#This program uses a function to convert miles to kilometers

# Create a variable to control the loop.
another_trip = 'Y' 

#define the conversion ratio, there are 1.6 km in a mile
conversion = 1.609344   


#this function will calculate the conversion for miles to km
def convert_miles_to_km():      
     kilometers = miles * conversion
     return kilometers          
#returns the calculation to convert miles to km


#created a loop to account for if user enters upper or lower y
while another_trip.upper() == 'Y':    

#try look will run if user enters valid value     
    try:                                
        miles = float(input('Enter number of miles: '))     #get the miles from user
        print(f'{miles} miles is equal to {convert_miles_to_km():.2f} kilometers')  #displays the miles entered and calls the function to show calculated conversion to km
        another_trip = input('Do you want to convert another trip? (Enter y for yes): ') #determines if the loop will fire


#ensures a valid value was entered, in this case a number, if anything other than number entered, this expect will fire
    except ValueError:      
        print('Miles needs to be a number, try again')  #displays if anything other than a number was entered
        another_trip = input('Do you want to convert another trip? (Enter y for yes): ')     #determines if the loop will fire   

#ends the loop        
else:
    print('Thank you for using our program')