def main ():
    intro()

    cups_needed = int(input('Enter the number of cups:  '))

    #convert
    cups_to_ounces(cups_needed)

    #intro function displays
def intro():
    print('This program converts measurements')
    print('in cups to fluid ounces. For your')
    print('reference the formula is: ')
    print('1 cup = 8 fluid ounces')
    print()

#cups_to_ounces funaction accepts a number of cups & displays equivalent number of ounces
def cups_to_ounces(cups):
    ounces = cups * 8
    print(f'That converts to {ounces} ounces')

#call main function
main()