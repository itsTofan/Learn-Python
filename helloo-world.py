
friends = ['Taylor', 'Aan', 'Him', 'Alex']
for friend in friends:
    print ("Hi " + friend)

for i in range (10):
    print ("hello world")

name = "Brook"
print("Hello " + name)

print(4+5)
print(9*7)
print(1/3)
print(((1+2)*3)/4)

"""Data types, int string float"""
print(type("a"))
print(type(5))

#variable in container for data
lenght = 10
width =2
area = lenght * width
print("The area of the triangle is: " + str(area))


"""Functions"""
def greeting (name, department):
    print("Welcome, "+ name)
    print("You are part of " + department)

greeting("Andy", "IT")
greeting("Jack", "Accounting ")

"""Function with returning value"""
def area_triangle(base, height):
    return base*height/2

area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is:" + str(sum))

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

"""Function Reuse"""
def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Karen")
lucky_number("Bond")



"""Comparing things with If Else Statement, logical operator And Or Not, Modulo"""
print("big" > "small")
print("cat" == "dog")
#print(1 < "1") #type error
print(1 == "1")

print("Yellow" > "Cyan" and "Brown" > "Magenta")
print(25 > 50 or 1 != 2)
print (not 42 == "Answer")

def hint_username (username):
    if len(username) < 3:
        print("Invalid username. Must be at lesat 3 characters long.")
    elif len(username) > 15:
        print("Invalid username. Must be at most 15 characters long")
    else:
        print("Valid username.")

hint_username("Te")

def greater_value(x, y):
    if x > y:
        return x
    else:
       return y


print(((24 == 5*2) and (24 > 3*5) and (2*6 == 12)))

"""Looping"""
#While loops  While loops instruct your computer to 
#continuously execute your code based on the value of a condition
#initializing variable is important before using it
x = 0 #nitializing
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

def attempts(n):
    x = 1
    while x <= n:
        print("Attemp " + str(x))
        x += 1
    print("done")

attempts(5)

#infinite loops & how to breaks
while x !=0 and x % 2 == 0:
    x = x /2

#For loops 
for x in range (5):
    print(x)

friends = ['Taylor', 'Aan', 'Him', 'Alex'] #list of string
for friend in friends:
    print ("Hi " + friend)

values = [23, 52, 59, 37, 48]
sum =0
lenght = 0
for value in values:
    sum += value
    lenght += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/lenght))

#nested loops, loop inside loop
#common error 
for left in range(7):
    for right in range(left, 7):
        print("[]" + str(left) + "|" + str(right) + "]", end=" ")
    print()

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

# recursion  is the repeated application of the same procedure to 
# a smaller problem - russian nesting doll.
# Recursion lets us tackle complex problems by reducing 
# the problem to a simpler one.
#  in programming, recursion is a way of doing a repetitive 
# task by having a function call itself. 
def factorial(n):
    print("Factorial called with " + str(n))
    if n < 2:
        print("Returning 1")
        return 1
    result = n * factorial(n-1)
    print("Returning " + str(result) + " for factorial of " + str(n))
    return result

factorial(4)

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return 0

    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    return n + sum_positive_numbers(n - 1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

for x in range(10):
    for y in range(x):
        print(y)