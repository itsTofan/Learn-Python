#making a script to list which user using which machine

#event class contain the date when the event happened, the name of the
#machine where it happened, the user involved and the event type
"""numbers = [4, 6, 2, 7, 1]
numbers.sort()                                  #sort list without making new list
print(numbers)

names = ["Carlos", "Ray", "Alex", "Kelly"]
print(names)
print(sorted(names))                            #sort list and copy to new list
print(names)
print(sorted(names, key=len))
"""

class Event:
    def __init__(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user

def get_event_date(event):
    return event.date

def current_user(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout" and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    user_list = ""
    for machine, users in machines.items():
        if len(users) > 0:
            user_list - ", ".join(users)
            print("{}: {}".format(machine, user_list))
events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-23 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-21 11:24:35', 'login', 'myworkstation.local', 'chris')
]

users = current_user(events)
print(users)


#exercise
class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
    def up(self):
        if self.current < self.top:
            self.current += 1
    def down(self):
        if self.current > self.bottom:
            self.current -= 1
    def go_to(self, floor):
        if self.bottom <= floor <= self.top:
            self.current = floor
    def __str__(self): # to set default function of print of this class
        return "Current floor: {}".format(self.current)

elevator = Elevator(-1, 10, 0)
elevator.up() 
print(elevator.current) #should output 1
elevator.down() 
print(elevator.current) #should output 0
elevator.go_to(10) 
print(elevator.current) #should output 10
# Go to the top floor. Try to go up, it should stay. Then go down.
elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current) # should be 9
# Go to the bottom floor. Try to go down, it should stay. Then go up.
elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1
elevator.go_to(5)
print(elevator)



#exercise 2 inheritance
class Animal:
    name = ""
    category = ""
    
    def __init__(self, name):
        self.name = name
    
    def set_category(self, category):
        self.category = category

class Turtle(Animal):
    category = "reptile"

class Snake(Animal):
    category = "reptile"

class Zoo:
    def __init__(self):
        self.current_animals = {}
    
    def add_animal(self, animal):
        self.current_animals[animal.name] = animal.category
    
    def total_of_category(self, category):
        result = 0
        for animal in self.current_animals.values():
            if animal  == category:
                result += 1
        return result

zoo = Zoo()

turtle = Turtle("Turtle") #create an instance of the Turtle class
snake = Snake("Snake") #create an instance of the Snake class

zoo.add_animal(turtle)
zoo.add_animal(snake)

print(zoo.total_of_category("reptile")) #how many zoo animal types in the reptile category

#Assessment - Object-oriented programming
"""
In this exercise, we'll create a few classes to simulate a server that's taking connections from 
the outside and then a load balancer that ensures that there are enough servers to serve those connections.
To represent the servers that are taking care of the connections, we'll use a Server class. 
Each connection is represented by an id, that could, for example, be the IP address of the computer 
connecting to the server. For our simulation, each connection creates a random amount of load in the server, 
between 1 and 10.
"""
#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        self.connections[connection_id] = connection_load
        # Add the connection to the dictionary with the calculated load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        if connection_id in self.connections:
            del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = sum(self.connections.values())
        # Add up the load for each of the connections
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
#End Portion 1#

server = Server()
server.add_connection("192.168.1.1")

print(server.load())
server.close_connection("192.168.1.1")
print(server.load())


class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        self.connections[connection_id] = server
        server.add_connection(connection_id)

    def close_connection(self, connection_id):
        """Closes the connection on the server corresponding to connection_id."""
        if connection_id in self.connections:
            server = self.connections[connection_id]
            del self.connections[connection_id]
            server.close_connection(connection_id)

    def avg_load(self):
        """Calculates the average load of all servers"""
        total_load = 0
        for server in self.servers:
            total_load += server.load()
        average_load = total_load / len(self.servers)
        return average_load

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        if self.avg_load() > 50:
            new_server = Server()
            self.servers.append(new_server)

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random() * 10 + 1
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        if connection_id in self.connections:
            del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = sum(self.connections.values())
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())
    
l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())
l.servers.append(Server())
print(l.avg_load())
l.close_connection("fdca:83d2::f20d")
print(l.avg_load())
for connection in range(20):
    l.add_connection(connection)
print(l)
print(l.avg_load())

#final project
def get_event_date(event):
    return event.date

def current_users(events):
    events.sort(key=get_event_date)
    machines = {}
    for event in events:
        if event.machine not in machines:
            machines[event.machine] = set()
        if event.type == "login":
            machines[event.machine].add(event.user)
        elif event.type == "logout" and event.user in machines[event.machine]:
            machines[event.machine].remove(event.user)
    return machines

def generate_report(machines):
    for machine, users in machines.items():
        if len(users) > 0:
            user_list = ", ".join(users)
            print("{}: {}".format(machine, user_list))

class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user

events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)
generate_report(users)