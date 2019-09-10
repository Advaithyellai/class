z = 0
a = 0
change = 0
search = 0
print("Welcome to my bookstore")
lof = ['Tinkle', 'Amar Chitra Khatha', 'Harry Potter and the Chamber of Secrets', 'Harry Potter and the Deathly Hallows' , 'Geronimo Stilton and the Kingdom of Fantasy' , 'Agatha Christie', 'Science and Nature' , 'Famous Five']
print("The list of the books of the store is :  ")
print(lof)
while (True):
	a = a + 1
	print("  ")
	print("1 = Add a Book")  
	print("2 = Delete a Book")
	print("3 = Find a Book")
	print("4 = List All the Books")
	print("5 = Number of Books ")
	print("6 = Reverse Alphabetic Order of the Books")
	print("7 = Alphabetic Order of the Books")
	print("8 = Exit the Store")
	b = int(input("Which of the following do you choose  "))
	if b == 1:
		change = change + 1
		print("  ")
		c = input("Which book do you want to add  ")
		lof.append(c)
		print("After ", c, " is added, the list is ", lof)
	elif b == 2:
		change = change + 1
		print("  ")
		d = input("Which of the following book do you want to remove ")
		lof.remove(d)
		print("After ", d, " is removed, the Store is ", lof)
	elif b == 3:
		search = search + 1
		print("  ")
		e = input("Which book do you want to find   ")
		try:
			d = lof.index(c)
			print("It is in place ", lof.index(e) + 1)
		except Exception as k:
			print("You will find it if you put correct capitals or if you add it")
			print("The books you can find are ")
		print(lof)
	elif b == 4:
		search = search + 1
		print("  ")
		print("The list is ")
		for charecter in lof:
			print(charecter)
	elif b == 5:
		search = search + 1
		print("  ")
		print("The number of books in the store is ", len(lof))
		print(lof)
	elif b == 6:
		search = search + 1
		lof.sort()
		lof.reverse()
		print("  ")
		print("The reverse alphabetic order of the books is ", lof)
	elif b == 7:
		search = search + 1
		lof.sort()
		print("  ")
		print("The alphabetic order of the books is ", lof)
	elif b == 8:
		z = 1
		print("  ")
		print("The number of changes made to the store = ", change)
		print("The number of the things you searched is " , search)
		print("The current store is = ", lof)
		exit()
		print("  ")
	else:
		print("Sorry I cannot help you ")