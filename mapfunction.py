# numbers=["33","45","1","2","3"]
# print(type(numbers[0]))
# number[0]=int (number[0])
# print(number[0])
# for i in  range(len(numbers)):
#     numbers[i]=int(numbers[i])
# print(type(numbers[0]))
# print(numbers)
# numbers=["33","45","1","2","3"]
# numbers=list(map(int,numbers))
# print(type(numbers[4]))
def square(a):
    return a*a

num=[1,2,3,4,5,6,7,8,9,10]
for i in num:
    print(i)
# num=list(map(lambda a:a*a, num))    
num=list(map(square,num))
for i in num:
    print(i)