import random
nums=['1','2','3','4','5','6','7','8','9']
num=random.choice(nums)
num2=random.choice(nums)
tries=int(input("how many :"))
finich=False
false_ans= 0
correct= 0
tried= 0
def calcul_1(num,num2,tried,correct,false_ans,finich):
    
    answer=input(f"{num}+{num2}=...")
    
    while tried!=tries:
        
        if int(answer) ==(int(num)+int(num2)):    
            correct+=1
            tried+=1
            num=random.choice(nums)
            num2=random.choice(nums)
            
            if tried==tries:
                finich=True
                break
            else:
                return calcul_1(num,num2,tried,correct,false_ans,finich)
        else:
            if tried==tries:
                finich=True
                break
            else:
                false_ans+=1
                tried+=1
                num=random.choice(nums)
                num2=random.choice(nums)
                return calcul_1(num,num2,tried,correct,false_ans,finich)
   
    if finich :
        print(f"correct answers{correct}")
        print(f"incorrect answer{false_ans}")
        if false_ans>1:
            print(f"you are stupid .{false_ans} INCORRECT answers??!")
        elif false_ans==1:
            print(f"you are stupid .ONE INCORRECT answer??!")
        
calcul_1(num,num2,tried,correct,false_ans,finich)


