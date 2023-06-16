
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

#Data structure
#String
name = "Andry"
color = 'blue'
#place = "cambridge' - error
pet = "" # empty string
pet = "looooooooooooooooooooooooooooooong cat"
print ("Name: " + name + ", Favorite color: " + color)
print ("example" * 3)
print(len(name)) #lenght of string
#String indexing
name = "Jaylen"
print (name[1]) #string start from index 0
print (name[0])
print (name[len(name)-1])
print (name[-1]) #print from the last char
print (name[-2])
#substring / slice
color = "Orange"
print(color[1:4])
fruit = "Pineapple"
print(fruit[:4]) # from index 0 to first 4 char
print(fruit[4:]) # from index 4 to onward

#create new string - string is immutable meaning cannot modified
message = 'A kong string with a silly typo'
#message[2] = "l" #error not support item assingment
new_message = message[0:2] + "l" + message[3:]
print(new_message)
pet = "Cats & Dogs"
print(pet.index("&"))
print("Dragons" in pet) #to check if word dragaon in variable pet - False
print("Cats" in pet) #True

def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

print (pet.upper())
print (pet.lower())
answer = 'YES'
if answer.lower() == "yes":
    print("User said Yes")

print(" YES ".strip()) #delete white space first index and last
print(" YES  ".lstrip()) #delete white space left
print(" YES  ".rstrip()) #delete white space right
print ("The number times e occurs in this string is".count("e"))

#format string
name = "Manny"
number = len(name) * 3
print ("Hello {}, your lucky number is {}".format(name, number))
print("Your lucky number is {number}, {name}".format(name=name, number=len(name)*3))

price = 7.500
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

def to_celcius(x):
    return (x-32)*5/9

for x in range(0, 101, 10):
    print("{:>3} F | {:>6.2f} C".format(x, to_celcius(x)))

#data type - List - collection of data.
#list is mutable it mean can change it value
x = ["Now", "we", "are", "cooking!"]
print(type(x))
print(x)
print(len(x))

print("are" in x)
print("is" in x)
print(x[0])
print(x[3])
#print(x[4]) #error
print(x[1:3])
print(x[:2])
print(x[2:])

Fruits = ["Pineapple", "Banana", "Apple", "Melon"]
Fruits.append("Kiwi")
print(Fruits)
Fruits.insert(0, "Orange") #insert at index 0
print(Fruits)
Fruits.remove("Melon")
print(Fruits)
#Fruits.remove("Pear") #error
Fruits.pop(3) #remove at index 3
print(Fruits)
Fruits[2] = "Strawberry"
print(Fruits)


#Tuples is a sequence of element of any type that immutable
#like return function, tuple can be unpack
fullname = ('Grace', 'M', 'Hopper')
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

result = convert_seconds(5000)
print(type(result))
print(result)
hours, minutes, seconds = result
print(hours, minutes, seconds)
hours, minutes, seconds = convert_seconds(1000)
print(hours, minutes, seconds)

#loop over list or tuple
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)

print("Total characters: {}, Average lenght: {}".format(chars, chars/len(animals)))

winners = ["Ashley", "Dylan", "Reese"]
#enumerate function to tuple of each element
for index, person in enumerate(winners):
    print("{} {}".format(index + 1, person))

def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result

print(full_emails([("andry@example.com", "Andry Six"), ("shane@example.com","Shane Penel")]))

multiples = []
for x in range (1,11):
    multiples.append(x*7)
print(multiples)
#list comprehension let us create new list based on sequences or ranges
multiples = [x*7 for x in range(1, 11)]
print(multiples)

languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
lenghts = [len(language) for language in languages]
print(lenghts)

z = [x for x in range(0, 101) if x % 3 == 0]
print(z)


#Dictionaries - the data inside dictionaries take the form of pairs of keys and values
x = {}
print(type(x))
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)
print(file_counts["txt"])
print(file_counts["jpg"])
file_counts["cfg"] = 8
print(file_counts)
del file_counts["cfg"]
print(file_counts)

for extension in file_counts:
    print(extension)

for ext, ammount in file_counts.items():
    print("There are {} files with the .{} extension".format(ammount, ext))

print(file_counts.keys())
print(file_counts.values())
for value in file_counts.values():
    print(value)

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result

print(count_letters("aaaaa"))
print(count_letters("superman"))
print(count_letters("very long string with lot of letters"))

"""The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values. 
Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).
"""
def email_list(domains):
    emails = []
    for domain, users in domains.items():
	    for user in users:
                emails.append(user + "@" + domain)
    return emails

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

"""The groups_per_user function receives a dictionary, which contains group names with the list of users. 
sers can belong to multiple groups. Fill in the blanks to return a dictionary with the users as keys and a list of their groups as values. 
"""
def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for group, users in group_dictionary.items():
		# Now go through the users in the group
		for user in users:
			# Now add the group to the the list of
			if user not in user_groups:
				user_groups[user] = []
			user_groups[user].append(group)

# groups for this user, creating the entry
# in the dictionary if necessary

	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

""""""
wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

"""The add_prices function returns the total price of all of the groceries in the  dictionary. 
Fill in the blanks to complete this function.
"""
def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for item, price in basket.items():
		total += price
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
	# Limit the return value to 2 decimal places
	return round(total, 2)  

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59, 
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44

#week 4 assingment
#1 Fill in the blank to complete the “first_character” function. This function should return 
# the first character of any string passed in.  Complete the string operation needed in this 
# function so that input like "Hello, World" will produce the output "H".

def first_character(string):
    # Complete the return statement using a string operation.
    return string[0] 


print(first_character("Hello, World")) # Should print H
print(first_character("Python is awesome")) # Should print P
print(first_character("Keep going")) # Should print K

#2. Complete the for loop and string method needed in this function so that a function call like 
# "alpha_length("This has 1 number in it")" will return the output "17". This function should:
"""accept a string through the parameters of the function;
iterate over the characters in the string;
determine if each character is a letter 
(counting only alphabetic characters; numbers, punctuation, and spaces should be ignored);
increment the counter;
return the count of letters in the string."""

def alpha_length(string):
    character = ""
    count_alpha = 0
    # Complete the for loop sequence to iterate over "string".
    for char in string: 
        # Complete the if-statement using a string method. 
        if char.isalpha():
            count_alpha += 1  
    return count_alpha
 
print(alpha_length("This has 1 number in it")) # Should print 17
print(alpha_length("Thisisallletters")) # Should print 16
print(alpha_length("This one has punctuation!")) # Should print 21

"""
3. Consider the following scenario about using Python lists: 
A professor gave his two assistants, Aniyah and Imani, the task of keeping an attendance list of students 
in the order they arrived in the classroom. Aniyah was the first one to note which students arrived, and then Imani took over. After class, they each entered their lists into the computer and emailed them to the professor. 
The professor wants to combine the two lists into one and sort it in alphabetical order. 
Complete the code by combining the two lists into one and then sorting the new list. This function should:
accept two lists through the function’s parameters;,
combine the two lists;
sort the combined list in alphabetical order;
return the new list. 
"""
def alphabetize_lists(list1, list2):
  new_list = [] # Initialize a new list.
  new_list= list1 + list2 # Combine the lists.
  new_list.sort() # Sort the combined lists.
  return new_list 


Aniyahs_list = ["Jacomo", "Emma", "Uli", "Nia", "Imani"]
Imanis_list = ["Loik", "Gabriel", "Ahmed", "Soraya"]


print(alphabetize_lists(Aniyahs_list, Imanis_list))
# Should print: ['Ahmed', 'Emma', 'Gabriel', 'Imani', 'Jacomo', 'Loik', 'Nia', 'Soraya', 'Uli']

"""
4.
Question 4
 Fill in the blank to complete the “even_numbers” function. This function should use a list
comprehension to create a list of even numbers using a conditional if statement with the 
modulo operator to test for numbers evenly divisible by 2. The function receives two variables 
and should return the list of even numbers that occur between the “first” and “last” variables
exclusively (meaning don’t modify the default behavior of the range to exclude the “end” value
in the range). For example, even_numbers(2, 7) should return [2, 4, 6].  
"""
def even_numbers(first, last):
  return [num for num in range(first, last+1) if num % 2 ==0]

print(even_numbers(4, 14)) # Should print [4, 6, 8, 10, 12]
print(even_numbers(0, 9))  # Should print [0, 2, 4, 6, 8]
print(even_numbers(2, 7))  # Should print [2, 4, 6]

"""
5.
Question 5
Fill in the blanks to complete the “endangered_animals” function. 
This function accepts a dictionary containing a list of endangered animals (keys) and
 their remaining population (values).  For each key in the given “animal_dict” dictionary, 
 format a string to print the name of the animal, with one animal name per line.
"""
def endangered_animals(animal_dict):
    result = ""
    # Complete the for loop to iterate through the key and value items 
    # in the dictionary.    
    for animal, num in animal_dict.items():
        # Use a string method to format the required string.
        result += "{}\n".format(animal)
    return result


print(endangered_animals({"Javan Rhinoceros":60, "Vaquita":10, "Mountain Gorilla":200, "Tiger":500}))

# Should print:
# Javan Rhinoceros
# Vaquita
# Mountain Gorilla
# Tiger

"""Question 6
Consider the following scenario about using Python dictionaries and lists: 
Tessa and Rick are hosting a party. Before they send out invitations, they want to add all of the people 
they are inviting to a dictionary so they can also add how many guests each friend is bringing to the party.  
Complete the function so that it accepts a list of people, then iterates over the list and adds all of 
the names (elements) to the dictionary as keys with a starting value of 0. Tessa and Rick plan to update 
these values with the number of guests their friends will bring with them to the party. Then, print the new dictionary.
This function should:
accept a list variable named “guest_list” through the function’s parameter;
add the contents of the list as keys to a new, blank dictionary;
assign each new key with the value 0;
print the new dictionary.
"""
def setup_guests(guest_list):
    # loop over the guest list and add each guest to the dictionary with
    # an initial value of 0
    result = {} # Initialize a new dictionary 
    for guest in guest_list: # Iterate over the elements in the list 
        result[guest] = 0  
         # Add each list element to the dictionary as a key with 
        # the starting value of 0
    return result

guests = ["Adam","Camila","David","Jamal","Charley","Titus","Raj","Noemi","Sakira","Chidi"]

print(setup_guests(guests))
# Should print {'Adam': 0, 'Camila': 0, 'David': 0, 'Jamal': 0, 
# 'Charley': 0, 'Titus': 0, 'Raj': 0, 'Noemi': 0, 'Sakira': 0, 'Chidi': 0}

"""
7.
Question 7
Use a dictionary to count the frequency of numbers in the given “text” string. Only numbers should be counted. 
Do not count blank spaces, letters, or punctuation. Complete the function so that input like "1001000111101" 
will return a dictionary that holds the count of each number that occurs in the string  {'1': 7, '0': 6}. 
This function should: 
accept a string “text” variable through the function’s parameters;
initialize an new dictionary;
iterate over each text character to check if the character is a number’
count the frequency of numbers in the input string, ignoring all other characters;
populate the new dictionary with the numbers as keys, ensuring each key is unique, and 
assign the value for each key with the count of that number;
return the new dictionary.
"""
def count_numbers(text):
  # Initialize a new dictionary.
  dictionary = {} 
  # Complete the for loop to iterate through each "text" character.
  for char in text:
    # Complete the if-statement using a string method to check if the
    # character is a number.
    if char.isdigit():
      # Complete the if-statement using a logical operator to check if 
      # the number is not already in the dictionary.
      if char not in dictionary:
          dictionary[char] = 0
      dictionary[char] += 1
           # Use a dictionary operation to add the number as a key
           # and set the initial count value to zero.
      # Use a dictionary operation to increment the number count value 
      # for the existing key.
  return dictionary

print(count_numbers("1001000111101"))
# Should be {'1': 7, '0': 6}

print(count_numbers("Math is fun! 2+2=4"))
# Should be {'2': 2, '4': 1}

print(count_numbers("This is a sentence."))
# Should be {}

print(count_numbers("55 North Center Drive"))
# Should be {'5': 2}

car_makes = ["Ford", "Volkswagen", "Toyota"]
car_makes.remove("Ford")
print(car_makes)

teacher_names = {"Math": "Aniyah Cook", "Science": "Ines Bisset", "Engineering": "Wayne Branon"}
print(teacher_names.values())

colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)
