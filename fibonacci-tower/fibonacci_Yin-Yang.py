import turtle
turtle.colormode(255)
t=turtle.Turtle()
t.begin_fill()
t.fillcolor('black')
def Fibonacci (n):
    limit=4
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

    t.end_fill()
Fibonacci (1)
t.begin_fill()
t.fillcolor('white')
Fibonacci (1)
t.color('black')
Fibonacci (1)
