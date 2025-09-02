def gen_even():
    n = 0
    while True:
        yield n
        n += 2

even = gen_even()

# print first 10 even numbers
for _ in range(10):
    print(next(even), end=" ")
