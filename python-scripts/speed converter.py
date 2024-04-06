#this script converts kph to mph 
#starting at 60 kph - 130 kph
#increments of 10 will be displayed

start_speed = 60
end_speed = 131
increment = 10
conversion_mph = 0.6214

#print table headings
print('KPH\tMPH')
print('-----------------')

#print speeds
for kph in range (start_speed, end_speed, increment):
    mph = kph * conversion_mph
    print(f'{kph}\t{mph:.1f}')