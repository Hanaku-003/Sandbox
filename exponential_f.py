n=0
def powpow(n):
    limit=int(input("put a limit" ))
    x=float(input("put in a number to put it to the power of n "))
    y=(x)**n
    print(y)
    while n!=limit:
        n+=1
        y=(x)**n
        print(y)
powpow(n)        
