import datetime

school_starts = datetime.date (2024, 1, 8) - datetime.date.today()

#convert to string to split at the comma otherwise will print days, 0:00:00 days
school_str = str(school_starts).split(',')


#after split only print the first half of list with [0]
print(f"School starts in {school_str[0]} days!!")
