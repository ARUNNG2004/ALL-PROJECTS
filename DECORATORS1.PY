# def func1():
#     print("Subscribe Now!")

# func2=func1
# del func1
# func2()

# def funcreturner(num):
#     if num==0:
#         return print
#     if num==1:
#         return int 

# a=funcreturner(1)
# print(a)

# def funcexecter(func):
#     func("This is the print statement ")

# funcexecter(print)

def dec1(func):
    def execution():
        print("execution")
        func()
        print("executed")
    return execution
@dec1
def arun():
    print("i a subscribers ")

# subscribers=dec1(arun)
arun()