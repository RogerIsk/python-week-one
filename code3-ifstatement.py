x = 11
if x > 0:
    print('x is Positive')
else:
    print('x is Negative')


if x > 0 and x < 10:
    print('x is between 0 and 10')
else:
    print('x is not between 0 and 10')


#nested if statement
if x > 0:
    if x%2 == 0: # checking if x is even or odd
        print('x is Positive and Even')
    else:
        print('x is Positive and Odd')
else:
    print('x is not Positive')


x = 5
if x > 0 and x < 10:
    print('x is Positive and less than 10')
elif x > 10:
    print('x is Positive and greater than 10')
elif x > 100:
    print('x is Positive and greater than 100')
else:
    print('x is Negative')


gym_member = ['John', 'Doe', 25, 1.75, 80]
member = input('Enter member name: ')

if member in gym_member:
    print('Member is in the list')
else:
    join = input('Member not in the list. Do you want to add the member? (y/n): ')
    if join == 'y':
        print('Member added to the list')
    else:
        print('get out of here')

price = 1200
budget = 1000
is_laptop_available = True

if budget > price and is_laptop_available == True:
    print('Buy the laptop')
elif budget > price and is_laptop_available == False:
    print('Laptop not available')
elif budget < price and is_laptop_available == True:
    print('Budget is not enough')
else:
    print('Budget is not enough and Laptop not available')

username = input('Enter username: ')
if not username:
    email = 'admin@python.py'
else:
    email = username + '@python.py'
print(email)

print('$'*15)
num = -256

if num:
    print('Number is not 0')
elif num and num < 0:
    print('Number is Negative')
else:
    print('Number is 0')

#for loops

for i in range(5): # stop
    print(i)
for i in range(5,10): # start, stop
    print(i)
for i in range(5,10,2): # start, stop, step - stepping on every 2nd number (2)
    print(i)

for i in range(5): # nested for loop
    for j in range(2):
        print(i,j)

for i in range(20,10,-1): # start, stop, step - stepping backwards / countdaown
    print(i)

#iterables
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

my_string = 'Python is ok'
for chat in my_string:
    print(chat)

for i in range(20):
    if i % 3 == 0:
        pass
    else:
        print(i)

for i in range(20):
    if i == 10:
        break
    else:
        print(i)

for i in range(5):
    for j in range(5):
        if i == 2:
            break
        else:
            print(i,j)