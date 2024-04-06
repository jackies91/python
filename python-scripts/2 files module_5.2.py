#Jackie Scott
#11/8/23
#Module 5.2 Data File 

#This program prompts user for their information to write on a data file

def main():
    
    #prompt user for information
    file_name = input("Enter file name: ")
    user_name = input("Enter your name: ")
    street_address = input("Enter your street address: ")
    phone_number = input("Enter your phone number: ")


#opening multiples with one with statement, "w" mode since files do not exist
#the f string will create the file name with the input for vaiable file_name
#the seconde file follow step 7 naming, <your first name> data.txt

    with open(f"{file_name}.txt", "w") as infile, open('jackiedata.txt', 'w') as outfile:

#the ".write" is what will actually write to the file, we seperate the variables with commas  
        infile.write(f"{user_name},{street_address},{phone_number}")
        outfile.write(f"{user_name},{street_address},{phone_number}")


#using "with open" to auto close but this time "r" mode to simply read what was written to the file, using the same f string variable since we do not know what the file will be named
    with open(f'{file_name}.txt', 'r') as file:

#this will display the entire contents of the file
        user_data = file.read()
        print(f"Contents of {file_name}:\n{user_data}")

#good to just check that the information was written to the second file
    with open('jackiedata.txt', 'r') as file:
        content = file.read()
        print(f"Contents of jackiedata.txt:\n{content}")


#call the main function this will check if the script is being ran as the main program or if it is being imported, in this case the main program
if __name__ == "__main__":
    main()

