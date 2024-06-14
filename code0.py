print('hi\n')
print("hello there")
print("""General
Kenobi
wow""")
print("'hi'\n")
print('"hi"\n')

name = "John"   # This is a string variable
age = 35        # This is an integer variable
price = 35.5    # This is a float variable
boolean = True  # This is a boolean variable
untrue = False    # This is a boolean variable
empty = None    # This is a None variable

print(name, 'is', age, 'years old') # This will not throw an error

print('print', type(name)) # shows the type of the variable
year = '2020'
print('print', type(year)) # shows the type of the variable
year = int(year) # converts year to an integer
print('print', type(year)) # shows the type of the variable

quantity = 3
print('print', type(quantity)) # shows the type of the variable
quantity = str(quantity) # converts quantity to a string
print('print', type(quantity)) # shows the type of the variable

#you cant turn string into an integer if it is not a number
'''quantity1 = 'hello'
print('print', type(quantity1)) # shows the type of the variable
quantity1 = int(quantity1) # converts quantity to a string
print('print', type(quantity1)) # shows the type of the variable'''

name, age = 'John', 35

a,b = 5,2
c = a / b
d = 3 + 2 * 2
print(c + d) # addition
