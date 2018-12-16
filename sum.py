ak = int(input("type a number  "))
sumx=1
for al in range(1, ak + 1):
	sumx = sumx * al
	print(sumx)
f = open("tes.txt", "a")
a = input("Type a random word  ")
b = int(input("Type a number   "))
i = 0
while (i < b):
	i = i + 1
	f.write(a)
	f.write("%d\r\n" % (i))
f.close()
print(1 == 1)
