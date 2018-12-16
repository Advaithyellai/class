z = int(input("How many calculations do you want to make   "))
for x in range(z):
	print("1 = Addition")
	print("2 = Subtraction")
	print("3 = Multiplication")
	print("4 = division")
	print("5 = Average")
	print("6 = power ")
	print("7 = exit")
	a = int(input("Which of the following do you choose  "))
	if a == 7:
		exit()
	else:
		print("  ")
	b = int(input("Type a number   "))
	c = int(input("Type a 2nd number   "))
	if a == 1:
		print("The sum of ", b," and ", c, " is ", b+c)
	elif a == 2:
		print("The difference between ", b," and ", c, " is ", b-c)
	elif a == 3:
		print("The product of ", b," and ", c, " is ", b*c)
	elif a == 4:
		print("The quotient of ", b," and ", c, " is ", b/c)
	elif a==5:
		print("The average of ", b," and ", c, " is ", (b+c)/2)
	elif a == 6:
		print("the power of ", b, " and ", c, " is ", b^c)
	else:
		print("Sorry I can not help you")