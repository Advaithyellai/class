no = int(input("Type a number  "))
b=1
x=0
if no == 0:
	print("The factorial of 0 is 0")
else:
	while(x<no+1):
		x=x+1
		b=b*x
	print("The factorial of",no,"is",b)