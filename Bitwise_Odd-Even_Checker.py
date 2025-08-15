num=int(input("enter a number : "))
# Bitwise check: num & 1
# If the last bit is 1 → odd, else even
if num & 1:
    print(f"{num} is odd")
else:
    print(f"{num} is even")