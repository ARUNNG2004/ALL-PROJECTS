def isgreaterrhan5(num):
    return num>5
list1=[1,2,3,4,5,6,7,8,9]
list1=list(filter(isgreaterrhan5, list1))
print(list1)