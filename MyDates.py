
# Print out a date, given year, month, and day as numbers

# Setting up the lookup table
months = [
'January','February', 'March',
'April','May','June',
'July','August','September',
'October','November','December']

# A list with one ending for each number from 1 to 31
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
          + ['st', 'nd', 'rd'] + 7 * ['th'] \
          + ['st']

# Getting the input
year=input ("Year:")
month=input("Month :")
day=input("Day :")

# extracting the values
month_number=int(month)
day_number=int(day)

#looking up the database
month_name=months[month_number - 1]
print("month_name" + month_name)
ordinal = day+endings[day_number-1]

#Finally, print out the results
print(month_name+" "+ordinal+","+year)
