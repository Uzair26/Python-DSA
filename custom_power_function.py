

def my_power(base,exp):
    if exp ==0 :
        return 1
   
    
    return base * my_power(base,exp-1)


base=int(input("enter a base : "))
exp=int(input("enter a exp : "))

print(my_power(base,exp))
    