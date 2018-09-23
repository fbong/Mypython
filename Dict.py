# value pair within a value pair

people = {
    'Alice': {'phone': '2341', 'addr': 'Foo drive 23'},
    'Beth': {'phone': '9102', 'addr': 'Bar street 42'},
    'Cecil': {'phone': '3158', 'addr': 'Baz avenue 90'}
}

# Descriptive labels for the phone number and address. These will be used
# when printing the output.
# Simple Dictionary
labels = {'phone': 'phone number', 'addr': 'address'}

# Are we looking for a phone number or an address?
name = input('Name: ')
request = input('Phone number (p) or address (a)? ')

# Use the correct key:

if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# Only try to print information if the name is a valid key in
# our dictionary:

if name in people:
    #   print.(name, labels[key], people[name][key] % "%s's %s is %s." )
    print(name, labels[key], people[name][key])
