x=int(input("Enter the nuber for x:"))
y=int(input("Enter the nuber for x:"))
if x>y:
    min=x
else:
    min=y
while (1):
    if ((min%x==0)and(min%y==0)):
        print("Lcm is ",min)
        break