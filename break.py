start_point=int(input("enter the start point"))
end_point=int(input("enter the end point"))

for i in range(start_point,end_point+1):
    if i%10==0:
        break
    else:
        print(i)

