
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