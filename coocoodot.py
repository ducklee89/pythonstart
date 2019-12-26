import module
from module import person1
import datetime

module.greeting("hoohoo")


a = module.person1["country"]

print(a)

print(person1["name"])

x = datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))
