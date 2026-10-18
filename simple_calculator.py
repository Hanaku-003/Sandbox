def div (number, by):
        return number/by

def X (number, by):
        return number*by

def minus (number, by):
        return number - by

def plus (number, by):
        return number+ by

    

numbers=["1:Addition","2:Subtraction","3:Multiplication","4:Division"]

for x in numbers:
          print(x)

choice =input("print the number of what do you want please: ")

a=int(input("enter first number :"))
b=int(input("enter second number :"))

result=None
if choice == "1":
    result= plus(a,b)
        
elif choice == "2":
    result= minus(a,b)
        

elif choice == "3":
    result= X(a,b)
       
    
elif choice == "4":
        while choice=="4" and b==0:
                print("please try again without 0 as a secound number")
                b=float(input("enter second number :"))
                result=div(a,b)
        else:
                result= div(a,b)
else:
    result="IDKا"
                
        
print("result is :",result)

extra=input ("to round your result, please print 'round'. only . else. just print'no'")
if extra.lower()=='round':
        print(round(result))
        print("thanks for trying")
elif extra.lower()=='no':
        print("thanks for trying")
        quit

