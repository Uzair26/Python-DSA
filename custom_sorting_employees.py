employees = [
    ("Alice", 25, 50000),
    ("Bob", 30, 60000),
    ("Charlie", 22, 40000)
]

age = sorted(employees,key = lambda x : x[1])
print(age)