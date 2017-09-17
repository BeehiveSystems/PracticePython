from datetime import datetime
from datetime import timedelta

name = input("What is your name? ")
name = name.title()
age = input("%s, what is your age? " % (name))

now = datetime.now().year
birth = now - int(age)
print("You were born in %s." % (birth))

elderly = birth + 100
print("You will turn 100 in %s." % (elderly))
