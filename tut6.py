az = ["Azhar","Saleem"]
for am in az:
    print(am)
    for i in am:
        print(i)
print("-------------------")

for num in range(1,10,3):
    print(num+1)
print("-------------------")

i=0
while(i<5):
    print(i)
    i= i+1
else:
    print("Number are printed")

z = int(input("Enter the value of Table :"))
for x in range(1,15):
    print(z," X" , x,"=", x * z)
    if(x==10):
      break
      print("Out of loop")




