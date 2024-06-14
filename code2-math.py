a = 5
b = 2
c = -3

print(a + b) # addition
print(a - b) # subtraction
print(a * b) # multiplication
print(a / b) # division

print(a ** b) # exponentiation - 5^2=25
print(a % b) # modulus - 2:5=2(1) - shows only the remainder which is 1
print(a // b) # floor division - divides and rounds down to the nearest whole number 2:5=2(1)
print(abs(c)) # absolute value -3=3

print(min([a,b,c])) # minimum value - shows only the minimum value/smallest number
print(max([a,b,c])) # maximum value - shows only the maximum value/biggest number

firstname = 'John'
lastname = 'Doe'
print(firstname + ' ' + lastname) # concatenation - joins the two strings together
firstname = firstname + ' ' + lastname
print(firstname) # concatenation - joins the two strings together

x = 5
x += 3 # x=x+3
print(x)

y = 5
y *= 4 # y=y*4
print(y)

z = 5
z-= 2 # z=z-2
print(z)

w=10
w%=2 # w=w%2
print(w)

# we can write any math problem in this short form

var1 = 5
var2 = 3
# every time we compare the result is boolean
print(var1 == var2) # checking if they are equal
print(var1 != var2) # checking if they are not equal
print(var1 > var2) # checking if var1 is greater than var2
print(var1 < var2) # checking if var1 is less than var2
print(var1 >= var2) # checking if var1 is greater than or equal to var2
print(var1 <= var2) # checking if var1 is less than or equal to var2