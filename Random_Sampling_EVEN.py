import random

x=random.sample(range(100),4)

evens =[for n in x if n % 2 ==0]

print("Random ",x)
print("Even : ",evens)

