import time
s=0
while s<30:
    if s<10:
         print(f"00:0{s}")
         time.sleep(1)
         s+=1
    elif s>=10:
        print(f"00:{s}")
        time.sleep(1)
        s+=1
