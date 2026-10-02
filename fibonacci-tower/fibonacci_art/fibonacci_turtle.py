import turtle
turtle.colormode(255)
t=turtle.Turtle()
t.color(75, 0, 130)
def Fibonacci (n):
    limit=4 
    tries=0    
    n_2=n
    print(n)
    print(n_2)
    t.circle(n/100,90)
    t.circle(n_2/100,90)
    while True :
        n+=n_2
        n_2+=n
        print(n)
        print(n_2)
        t.circle(n/100,90)
        t.circle(n_2/100,90)
        if n >10**limit:
            break


Fibonacci (1)
