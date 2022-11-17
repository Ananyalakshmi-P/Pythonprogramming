import time
second=0
minute=0
a=int(input("enter the count"))
while second<=a:
    print(second)
    time.sleep(1)
    second=second+1
    if second>=60:
        minute=second/60
        print(minute,"minute")

