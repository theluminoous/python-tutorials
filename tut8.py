li = [12,56,78,34,6,8,34,6,57,34]
# li.append(0)
# li.sort()
li.reverse()
print(li)

tup = ("Pakistan", "America", "England")
temp = list(tup)
temp.append("Russia")
temp.pop(0)
tup = tuple(temp)
print(tup)
