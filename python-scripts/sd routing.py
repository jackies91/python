#determine which Countries fall under which Service Desk
emea_service_desk = ['Germay', 'United Kingdom', 'France', 'Italy']
north_america_sd = ['Mexico', 'United States', 'Canada']
south_america_sd = ['Argentina', 'Brazil', 'Chile', 'Peru']

#Get user's location
user_location = input("Enter your country")

#check user's location and route ticket to correct service desk
if user_location in emea_service_desk:
    print('Your ticket is being routed to the Emea Service Desk')
elif user_location in north_america_sd:
    print('Your ticket is being routed to the North America Service Desk')
elif user_location in south_america_sd:
    print('Your ticket is being routed to the South America Service Desk')
else:   #this was in case someone put in a country you don't have defined, a fail save
    print("Your location was not recognized. Your ticket is being routed to the Admin team for additional support.")