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