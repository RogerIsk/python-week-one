# Binary Code
print('*'*10)
num = 10
bin_num = bin(num)
print(bin_num)
simple = '/' 
ascii = ord(simple) # string to binary
print(bin(ascii))

binary = '101110'
decimal = int(binary, 2) # 1*2^5 + 0*2^4 + 1*2^3 + 1*2^2 + 1*2^1 + 0*2^0 = 46
print(decimal)

# logical operators for binary

a = 0b1101
b = 0b1000
print(bin(a & b)) # 0b1000 - 8
print(bin(a | b)) # 0b1101 - 13

# Logical Operators

#'and'  Returns True if both statements are true                    - exanple: x < 5 and x < 10
#'or'   Returns True if one of the statements is true               - example: x < 5 or x < 4
#'not'  Reverse the result, returns False if the result is true     - example: not(x < 5 and x < 10)

c = True
d = False
e = True
print(c and d) # False
print(c or d) # True
print(not e) # False
print(c or d and e) # True
print(c and d or e) # True

budget = 1200
price = 1000
laptop_available = True
print('#'*15)
print(budget > price and laptop_available) # True
print('#'*15)
username1 = input("Enter username: ")
password1 = input("Enter password: ")
print(username1 == 'admin' and password1 == 'admin123') # True

x = [1,2,3,4,5]
y = x
z = [1,2,3,4,5]
print(x == y) # True
print(x == z) # True
print(x is y) # True
print(x is z)     # id(x) == id(z) - False       because they are not in the same memory / not the same object / different id
print(x is not z) # id(x) != id(z) - True
print(id(x))
print(id(y))
print(id(z))
print('#'*15)

f = 5
g = 5
print(id(f))
print(id(g))
print(f is g) # True

# when 'is' is used numbers and strings are the same but tables and lists are not the same

#membership keyword
gymmembers = ['John', 'Jane', 'Jack', 'Jill']
print('John' in gymmembers) # True - 'in' checks if the value is in the list
print('John' not in gymmembers) # False - 'not in' checks if the value is not in the list
print('Solomon' in gymmembers) # False
print('Solomon' not in gymmembers) # True

mystring = 'dont do that'
print('dont' in mystring) # True
print('dont' not in mystring) # False