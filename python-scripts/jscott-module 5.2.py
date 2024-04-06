#Jackie Scott
#11/8/23
#Module 5.2 Data File 

#This program prompts user for their information to write on a data file


def main():

    #prompt user for information
    file_name = input('Enter the file name: ')
    user_name = input('Enter your name: ')
    street_address = input('Enter your address: ')
    phone_num = input('Enter your phone number: ')


#using with open to ensure the file auto closes after we are done, using 'w' mode since file does not exist, the f string will create the file name with the input for vaiable user_name
    with open(f'{file_name}data.txt', 'w') as file:
    
    #the file.write is what will actually write to the new file, we seperate the variables with commas  
        file.write(f'{user_name}, {street_address}, {phone_num}')

#using with open to auto close but this time 'r' mode to simply read what was written to the file, using the same f string variable since we do not know what the file will be named
    with open(f'{file_name}data.txt', 'r') as file:

#this will display the entire contents of the file
        user_data = file.read()
        print(f"\nContents of {file_name} data.txt:  {user_data}")

#call the main function this will check if the script is being ran as the main program or if it is being imported, in this case the main program
if __name__ == "__main__":
    main()