number=18
countofthen=1
while countofthen <=10:
    a=int(input("Enter the number "))
    if  a<18:
        print("Ho no negga enter panna number very lesss")
    elif a>18:
        print("neega enter panna nuber very big")
    elif a==18:
        print("yes your the winner")
        print("you have won in",countofthen,"life")
        break
    print(10-countofthen,"life's left")
    countofthen=countofthen+1