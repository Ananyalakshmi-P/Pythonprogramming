import time
second=0
minutes=0
n=0
a=int(input("enter the count"))
while second<=a:
    print(second)
    time.sleep(1)
    second=second+1
    n=n+1
    if second==n*60:
        minute=(second)/60
        print(minute)



