n=1
while n<=10:
    print(n,end='\t')
    n=n+1
def solution(n):
    for i in range(1,n+1):
        print(i)
solution(100)
# using to find summ of nature numbers down
import math 
def findsum(n):
    return math.floor((n*(n+1))/2)
print(findsum(10))
a=int(input("Enter the number "))
b=(a*(a+1))/2
print(b)
n=int(input("Enter the number "))
sum1=0
for i in range(1,n+1):
    sum1=sum1+i
print("sum of",n,"is",sum1)
