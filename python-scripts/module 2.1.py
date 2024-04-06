#determine which Countries fall under which Service Desk
service_desk_location = {
    'Emea Service Desk': 'Germay',
    'North America Service Desk': 'Mexico',
    'South America Service Desk': 'Argentina',
    'Global Service Desk':'High'
}


#Get user's location
user_location = input("Enter your country: ")

#Get user's priority level
priority = input('Enter the ticket priority level (High, Medium, Low): ')

#check user's location and route ticket to correct service desk
if user_location in service_desk_location:
    if priority in service_desk_location:
        print(f'Your ticket is being routed to the {service_desk_location} with', priority, 'level')
    else: 
        print('Your ticket is ')
else:
    print("Your location was not recognized. Your ticket is being routed to the Admin team for additional support.")
