#object-oriented programming - a flexible, powerful paradigm where classes represent and define concepts,
#while objects are instances of claseses.
#the attrubutes are the characteristics associated to a type
#the method are the functions associated to a type

print(type(0))
print(type(""))
print(dir("")) #print attribute and class method associate with the type
#help("") #print documentiation of the method and how to use

#create new class of Apple - recomend using Capital letter
class Apple:
    pass

class Apple:
    color = ""
    flavor = ""

jonagold = Apple()
jonagold.color = "red"
jonagold.flavor = "sweet"
print(jonagold.color.upper())   #Dot notation access any of the abilities the object might have(method) or
print(jonagold.flavor)  #information it might store (attributes)

golden = Apple()
golden.color = "Yellow"
golden.flavor = "Soft"

# “If you have an apple and I have an apple and we exchange these apples then
# you and I will still each have one apple. But if you have an idea and I have
# an idea and we exchange these ideas, then each of us will have two ideas.”
# George Bernard Shaw

class Person:
    apples = 0
    ideas = 0

johanna = Person()
johanna.apples = 1
johanna.ideas = 1

martin = Person()
martin.apples = 2
martin.ideas = 1

def exchange_apples(you, me):
#Here, despite G.B. Shaw's quote, our characters have started with       #different amounts of apples so we can better observe the results. 
#We're going to have Martin and Johanna exchange ALL their apples with #one another.
#Hint: how would you switch values of variables, 
#so that "you" and "me" will exchange ALL their apples with one another?
#Do you need a temporary variable to store one of the values?
#You may need more than one line of code to do that, which is OK. 
    temp1 = you.apples
    temp2 = me.apples
    you.apples = temp2
    me.apples = temp1
    return you.apples, me.apples
    
def exchange_ideas(you, me):
    #"you" and "me" will share our ideas with one another.
    #What operations need to be performed, so that each object receives
    #the shared number of ideas?
    #Hint: how would you assign the total number of ideas to 
    #each idea attribute? Do you need a temporary variable to store 
    #the sum of ideas, or can you find another way? 
    #Use as many lines of code as you need here.
    temp1 = you.ideas
    temp2 = me.ideas
    you.ideas = temp2
    me.ideas = temp1
    return you.ideas, me.ideas

exchange_apples(johanna, martin)
print("Johanna has {} apples and Martin has {} apples".format(johanna.apples, martin.apples))
exchange_ideas(johanna, martin)
print("Johanna has {} ideas and Martin has {} ideas".format(johanna.ideas, martin.ideas))


##################
# define a basic city class
class City:
	name = ""
	country = ""
	elevation = 0 
	population = 0

# create a new instance of the City class and
# define each attribute
city1 = City()
city1.name = "Cusco"
city1.country = "Peru"
city1.elevation = 3399
city1.population = 358052

# create a new instance of the City class and
# define each attribute
city2 = City()
city2.name = "Sofia"
city2.country = "Bulgaria"
city2.elevation = 2290
city2.population = 1241675

# create a new instance of the City class and
# define each attribute
city3 = City()
city3.name = "Seoul"
city3.country = "South Korea"
city3.elevation = 38
city3.population = 9733509

def max_elevation_city(min_population):
	# Initialize the variable that will hold 
# the information of the city with 
# the highest elevation 
	return_city = City()

	# Evaluate the 1st instance to meet the requirements:
	# does city #1 have at least min_population and
	# is its elevation the highest evaluated so far?
	if city1.population>min_population:
		return_city = city1
	# Evaluate the 2nd instance to meet the requirements:
	# does city #2 have at least min_population and
	# is its elevation the highest evaluated so far?
	elif city2.population>min_population:
		return_city = city2
	# Evaluate the 3rd instance to meet the requirements:
	# does city #3 have at least min_population and
	# is its elevation the highest evaluated so far?
	elif city3.population>min_population:
		return_city = city3

	#Format the return string
	if return_city.name:
		return ("{}, {}".format(return_city.name, return_city.country))
	else:
		return ""

print(max_elevation_city(100000)) # Should print "Cusco, Peru"
print(max_elevation_city(1000000)) # Should print "Sofia, Bulgaria"
print(max_elevation_city(10000000)) # Should print ""


#############################
class Furniture:
	color = ""
	material = ""

table = Furniture()
table.color = "brown"
table.material = "wood"

couch = Furniture()
couch.color = "red"
couch.material = "leather"

def describe_furniture(piece):
	return ("This piece of furniture is made of {} {}".format(piece.color, piece.material))

print(describe_furniture(table)) 
# Should be "This piece of furniture is made of brown wood"
print(describe_furniture(couch)) 
# Should be "This piece of furniture is made of red leather"


#method introduction
#instance variable is a variable that have different values for differrent instances of the same class
class Piglet:
	"""Represents a piglet that can say their name"""
	name = "piglet"
	years = 0
	def speak(self):
		"""Outputs a message including the name of the piglet"""
		print("Oink! I'm {}!".format(self.name))
	def pig_years(self):
		"""Converts the current age to equivalent pig years"""
		return self.years * 18
        
help(Piglet)
hamlet = Piglet()
hamlet.name = "Hamlet"
hamlet.speak()
hamlet.years = 2
print(hamlet.pig_years())

petunia = Piglet()
petunia.name = "petunia"
petunia.speak()
petunia.years = 4
print(petunia.pig_years())


#constructor of the class is the method that's called when you call the name of the class
#always start with init -- special method
class Apple:
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor
	def __str__(self): # to set default function of print of this class
		return "This apple is {} and its flavor is {}".format(self.color, self.flavor)

jonagold = Apple("red", "sweet")
print(jonagold)

#documenting function
#docstring a brief text that explains what something does
def to_seconds(hours, minutes, seconds):
	"""return the amount of seconds in the given hours, minutes and seconds"""
	return hours*3600+minutes*60+seconds
help(to_seconds)


#Inheritance 
class Fruit:
	def __init__(self, color, flavor):
		self.color = color
		self.flavor = flavor

class Apple(Fruit):
	pass

class Grape(Fruit):
	pass

granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")
print(granny_smith.flavor)
print(carnelian.color)

class Animal:
	sound = ""
	def __init__(self, name):
		self.name = name
	def speak(self):
		print("{sound} I'm {name}! {sound}".format(name=self.name, sound=self.sound))

class Piglet(Animal):
	sound = "Oink"

hamlet = Piglet ("Hamlet")
print(hamlet.speak())

class Cow(Animal):
	sound = "Mooooo"

milky = Cow("Milky White")
print(milky.speak())

#Composition - 
class Repository:
	def __init__(self):
		self.packages = {}
	def add_package(self, package):
		self.packages[package.name] =  package
	def total_size(self):
		result = 0
		for package in self.package.values():
			results += package.size
		return result
	
#module used to organize functions, classes and other data together in a structured way
#python standard library using import
import random
import datetime
print(random.randint(1,10))
now = datetime.datetime.now()
print(now)
print(now.year)
print(now + datetime.timedelta(days=28))