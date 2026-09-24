import time
import winsound
SE=0
m=SE//60
s=0
seconds=int(input("seconds="))+1
minutes=int(input("minutes="))
seconds+=minutes*60
while seconds!=SE :
        s = SE % 60
        m = SE // 60
        print(f"{m:02d}:{s:02d}")
        time.sleep(1)
        SE+=1

winsound.Beep(2000, 700)
print("TIME IS UP ")
