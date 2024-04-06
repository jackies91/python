#Jackie Scott 12/12/23 Module 11.2

#Recursive function that accepts an integer argument, n, and prints the number of 1 up to and including n

#def to make recursive 
def recursive(num):
    #base condition so we don't run forever or recursion error, also ensures only positive numbers entered
    if num <= 0:  
        return
 #pass one less than what user inputs while invoking the function
    recursive(num -1)
#adding the print after so print shows couting up not down. put it after invoking function
    print(f'Recursive count is {num}')

#def iterative non-recursive, creating a for loop to loop within a function
def loop(number):
    #every loop will add 1 to the user input
    for n in range(1, number +1):
        print(f'Loop count is {n}')

input_test = int(input('Enter a positive number:  '))
#ensuring a postive number is entered for our loop, if yes then the "else" will pass the valid number to the 2 defs above
if input_test <= 0:
    print('Enter a positive valid number. ')

else:
    #passing the number to the recursive and loop defs
    print('Recursive method: ')
    recursive(input_test)
    print('-----------------------------------------------------------------------')
    print('For Loop method: ')
    loop(input_test)
