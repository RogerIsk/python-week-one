def greet():
    print("Hello, World!")


greet()


def user():
    return "Hello there!"


hello = user()
print(hello)


def greet(name):
    return "hello " + name


name = "John"
print(greet(name))
name2 = "Jane"
hello2 = greet(name2)
print(hello2)
print(greet("John"))


def add(a, b):
    return a + b


result = add(3, 5)
print(result)


def multiply(a, b):
    return a * b


result = multiply(3, 5)
print(result)


def make_email(username):
    if username:
        email = username + "@gmail.com"
    else:
        email = "admingmail.com"
    return email


name = input("Enter your username: ")
email = make_email(name)
print(email)


def login(username, password):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username == "admin" and password == "admin":
        return "Login successful"
    else:
        return "Login failed"


def is_even1(number):
    if number % 2 == 0:
        return True
    return False


def is_even2(number):
    if number % 2 == 0:
        return True
    else:
        return False


def is_even3(number):
    return number % 2 == 0


print(is_even1(3))


def iseven(number):
    for i in range(1, number):
        if i % 2 == 0:
            print(i)

number = int(input("Enter a number: "))
iseven(number)