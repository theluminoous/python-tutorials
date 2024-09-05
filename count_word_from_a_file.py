file = open('myfile.txt','r')
# read = file.read()
# print(read)
count = 0
for line in file:
    words = line.split(" ")
    count += len(words) 
file.close()
print("Numbers are :", count)





