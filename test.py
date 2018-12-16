# import time
# l = 200
# f = 200
# l=200
# ce=2
# e = 0
# a = 0
# c=0
# for lo in range(1, 11):
# 	e=e+1
# 	fs = int(input("How many fans do you want to buy    "))
# 	ls = int(input("How many lights do you want to buy  "))
# 	if fs > f:
# 		a=1
# 		print("sorry you cannot purchase", fs,"fans there are only", f,"fans left")
# 		print("do you want to buy", f, "fans")
# 		xfs = input(" ")
# 		if xfs == 'yes':
# 			f=0
# 		else:
# 			b=int(input("then how many do you want to buy "))
# 			f=f-b
# 	else:
# 		a=0
# 		print(" ")
# 	if ls > l:
# 		c=1
# 		print("sorry you cannot purchase", ls,"lights there are only", l,"light left")
# 		print("do you want to buy", l, "lights")
# 		xls = input(" ")
# 		if xls == 'yes':
# 			l=0
# 		else:
# 			d=int(input("then how many do you want to buy "))
# 			l=l-d
# 	else:
# 		c=0
# 		print(" ")
# 	print("Have a nice day  ")
# 	if c == 0:
# 		l = l - ls
# 	else:
# 		pass
# 	if a == 0:
# 		f=f-fs
# 	print("  ")
# 	if l <= 50:
# 		print("There are",l,"lights left, should I buy more  ")
# 		nl = input(" ")
# 		if nl == 'yes':
# 			nbl = int(input("How many lights should I buy  "))
# 			l = l+nbl
# 			if l > 200:
# 				thl = input("Sorry we cannot buy", nbl, "lights. But we can add", 200-(nbl-l), "lights. Do you agree  ")
# 				if thl == 'yes':
# 					l==200
# 				else:
					
# 		else:
# 			pass
# 	else:
# 		print("  ")
# 	if f <= 50:
# 		print("There are",f, "fans left, should I buy more  ")
# 		nf = input(" ")
# 		if nf == 'yes':
# 			f = 200
# 		else:
# 			pass
# 	else:
# 		print("  ")
# 	print("  ")
# 	if e == ce:
# 		choice = input("Do you want to exit the store  ")
# 		ce = ce + 2
# 		print(" ")
# 		if choice == 'yes':
# 			print("The current fans in the store are", f)
# 			print("The current lights in the store are", l)
# 			exit()
# 		else:
# 			pass 
a = int(input("Type a number(for factorial)  "))
b = 0
c = 1
for d in range(0, a):
	b = b+1
	c = b*c
if a != 0:
	print("The factorial of %d is %d" %(a, c))
else:
	print("The factorial of 0 is 0")