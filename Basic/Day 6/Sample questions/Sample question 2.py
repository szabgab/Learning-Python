a=int(input("Please enter a number "))
while(True):
    if(a%2==0):
        a=a/2
    else:
        a=3*a+1
    if(a==1):
        break
