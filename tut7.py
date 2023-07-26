from math import pi
def azhar(rad):
    vol = (4/3*pi*rad**3)
    # print("the volume is sphare is : ",vol)

voli = int(input("Enter the Radius of Sphare :"))
azhar(voli)

daa = 12
azhar(daa)

def pakistan(a, b):  #Parameters
    sum = a+b
    mul = a*b
    sub = a-b
    div = a/b
    print("Sum of A + B is :",sum)
    print("Sum of A + B is :",sub)
    print("Sum of A + B is :",mul)
    print("Sum of A + B is :",div)

pakistan(45,78)      #Arguments 

marks = [34, 45, "Azhar"]
print(marks)
print(marks[2])
print(marks[0])
print(marks[1])



