# for i in range(1,20):
#     print("i is now {}".format(i))
#
# number = "9,223,372,036,854,775,807"
# for i in range(0, len(number)):
#     print(number[i])
# removes the commas

number = "9,223,372,036,854,775,807"
cleanedNumber = ''

# for loops stop at one tick before the end of range
#for i in range(0, len(number)):
for i in range(len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)

print(f"The number is {newNumber} ")