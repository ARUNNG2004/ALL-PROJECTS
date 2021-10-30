# a=-1
# b=1
# n=int(input("Enter no. of terms: "))
# i=0
# sum=0
# Fibo=[]
# while i<n:
#     s= a + b
#     Fibo.append(s)
#     sum+=s
#     a = b
#     b = s
#     i+=1
# print("Fibonacci series upto "+ str(n) +" terms is : " + str(Fibo))
# print("The sum of Fibonacci series: ",sum)
# def fiob(x):
#     a=0
#     b=1
   
#     for i in range(2,x):
#         c=a+b
#         a=b
#         b=c
#         print(c,end=" ")
# fiob(int(input("Enter the number:")))
# p=-1
# c=1
# a=int(input("Enter the number:"))
# for i in range(1,a+1):
#     a=p+c
#     print(a,end=",")
#     p=c
#     c=a
# i=6
# while i>0:
#     for i in range(1,i-1):
#         print(i,end='\t')
#     print('\n')
#     i=i+1
i=6
while i>0:
    for j in range(1,i):
        print(j,end="\t")
    print("\n")
    i+=-1
    
# while true:
#     for i in range(5,0,-1):
#         for j in range(1,i+1):
#             print(j,end="")
#         print()
#     else:
#         break