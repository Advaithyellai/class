a = input ("Type a word  ")
b = a[:: - 1]
a = a.lower()
b = b.lower()
print("The reverse string of",a ," is ", a[:: -1])
if a == b:
	print("Yes ", a, " is a pallidrom ")
else:
	print("No ", a, " is not a pallidrom  ")