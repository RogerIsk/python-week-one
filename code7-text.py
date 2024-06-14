my_text = 'Hello, World!'
text2 = 'Lorem ipsum dolor sit amet, consectetur \nadipiscing elit.'
print(my_text)
print(text2)

item = 'apple'
price = 2.5
quantity = 3
string = 'the ' +str(quantity) + ' ' + item + 's cost ' + str(price*quantity) + ' dollars'
print(string)

string2 = f"the {quantity} {item}s cost {price*quantity} dollars"
print(string2)

string3 = 'the {} {}s cost {} dollars'.format(quantity, item, price*quantity)
print(string3)


from math import pi
area = 4*pi
result = f'The area of a circle with radius 2 is {area:.3f}'
print(result)

text3 = 'Hello, World!'
for char in text3:
    print(char)

print(len(text3))
print(f'there are {len(text3)} characters present in {text3}')
list = ['a', 1, 2, 3, 4, 8, 9]
print(len(list))

def check_len(string):
    return len(string) < 10
   
post = 'This is'
if check_len(post):
    print('The string is too short')
    

string4 = 'Hello, World!' #converts into uppercase
print(string4.upper())
string5 = 'Hello, World!' #converts into lowercase
print(string5.lower())