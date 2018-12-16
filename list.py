los=[]
for x in range(1,10+1):
	a = input("Write a word  ")
	los.append(a)
print(los)
b = input("which word do you want to find   ")
print(los.index(b))
print(len(los))
los.reverse()
print(los)
los.sort()
print(los)