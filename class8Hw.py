pb ={'Advaith': 7337454037, \
'Mahesh': 9885266007, \
'Gayathri': 9848140153 }
co =0
ts =0
ce = 0
nl = int(input("How many changes do you want to make to the phone book "))
print("   ", "  ")
for l in range(0, nl):
	print("The phone book has these numbers", pb)
	print("1 = Add a number")
	print("2 = delete a number")
	print("3 = find a number ")
	print("4 = List All the numbers")
	print("5 = Number of numbers ")
	print("6 = Reverse Alphabetic Order of the names")
	print("7 = Alphabetic Order of the names")
	print("8 = Exit the phone book")
	b = int(input("Which of the following do you choose "))
	if b==1:
	 		nam = input("What is your name ")
	 		pn = int(input("what is your phone number "))
	 		pb[nam]=pn
	 		print(pb)
	 		co = co+1
	 		print(" ")
	elif b==2:
		dn = input("which number do you want to delete ")
		del pb[dn]
		print("After",dn,"is deleted the phone book is ",pb)
		print(" ")
		co = co+1
	elif b==3:
		fn = input("whoose number do you want to find ")
		print(fn,"'s number is",pb[fn])
		print(" ")
		ts=ts+1
	elif b==4:
		for keys, values in pb.items():
			print("The name is", keys, "and the number is", values)
			print(" ")
		print(pb)
		ts=ts+1
		print(" ")
	elif b==5:
		print("The number of numbers are",len(pb))
		print(pb)
		print(" ")
		ts=ts+1
	elif b==6:
		so = pb.sort()
		re = so.reverse()
		print(re)
		print(" ")
		ts=ts+1
	elif b==7:
		sor = pb.sort()
		print(sor)
		print(" ")
		ts=ts+1
	elif b==8:
		print("the number of changes made are", co)
		print("the number of things seen are", ts)
		print(" ")
		exit()
		ce = 1
	else:
		print("Sorry I cannot help you")
		print("")
		l=l-1
if ce == 0:
	print("the number of changes made are", co)
	print("the number of things seen are", ts)
	print("  ")
else:
	print(" ")