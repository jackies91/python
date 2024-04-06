#Jackie Scott
#12/1/23
#Module 7.2 Strings

#a program that acquires a String containing a person’s first, middle, and last names, and then display their first, middle, and last initials. For example, if the user enters John William Smith, the program should display J. W. S.

def main():
    #ask user for their full name in one line
    full_name = input('Enter your full name, First, Middle, and Last: ')

    #split up the entered name that the user entered 
    initials = full_name.split()

#create a loop to go through each element in initals
    for x in initials:

#loop through using end so each element has the needed dot at the end and displays everything in a single line
#use .upper to ensure the initials are in uppercase in the case it was not entered that way 
        print(x[0].upper(), end='.')

if __name__ == "__main__":
    main()