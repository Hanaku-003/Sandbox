import time
SE=0
m=SE//60
s=0
seconds=int(input("how much seconds?"))
while seconds!=SE:
        s = SE % 60
        m = SE // 60
        print(f"{m:02d}:{s:02d}")
        time.sleep(1)
        s+=1
        SE+=1
        m+=s//60
