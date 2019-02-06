ak = int(input("type a number  "))
sumx=1
for al in range(1, ak + 1):
	sumx = sumx * al
	print(sumx)
of = open("tes.txt", "a")
rw = input("Type a random word  ")
rn = int(input("Type a number   "))
null = 0
while (null < rn):
	null = null + 1
	of.write(rw)
	of.write("%d\r\n" % (null))
of.close()