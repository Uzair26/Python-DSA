import time
num= int(input("enter the number : "))
start = time.time()

sum=0
for i in range(num+1):
    sum=sum+i


end=time.time()

print("Loop method ",end-start,"seconds")