#Jackie Scott
#10/30/23
#Module 3.2 Loops

#This program will utilize a while to determine how long it takes for an investment to double at a given interest rate.
#The input will be an annualized interest rate and the initial investment amount, and the output is the number of years it takes an investment to double.


#Get interest rate
interest = float(input ('Enter interest rate: ' ))

#Get investment amount
investment = float(input('Enter initial investment amount:  '))

#create variable to keep track of time
years = 0

#create variable to keep track of the balance
balance = investment

#convert interest to decimal 
dec_interest = interest/100

#while loop calculation that stops once investment is doubled
while balance <= investment*2: #the loop will continue as long as the balance is less than double the investment
     balance += balance * dec_interest #updating balance after multiplying by the interest given
     years += 1  #keeps track of the years 

#results 
print(f'Your investment will double in {years} years.')