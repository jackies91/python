#Jackie Scott
#11/15/23
#Module 6.2 Tuple / redoing assignment for Module 12.2

#creating a tuple of random articles of clothing

#Initializing with values
clothes = ('shirt', 'socks', 'shorts', 'slacks', 'dress', 'undies', 'sweater', 'poncho', 'overalls', 'swimsuit', 'scarf', 'gloves', 'hat', 'tie', 'bra', 'nightgown', 'suit')

#Display the contents in a single statement.
print(clothes)

#Iterate through the collection displaying the output as a complete sentence using each value. Use the f-string format to control the output.
for i in clothes:
    print(f'Do you want me to wash your {i}? ')

#Repeat the output in reverse order using a different context string.
#Display the contents in a single statement.
print('\n\n----------Reversing----------\n\n')
print(clothes[::-1])

#Repeat the output in reverse order using a different context string.
for x in clothes[::-1]:
    print(f'No, do not wash my {x}.')