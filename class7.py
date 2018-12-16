word = input("Type a sentence  ")
word = word.lower()
alpha =['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', ' ']
count =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for ind in word:
	try:
		position = alpha.index(ind)
		count[position]=count[position]+1
	except Exception as ex:
		print("Not found ")
	if position == 26:
	 	print("space is in place ", position) 
	else:
		print(ind, " is in place ", position)
for i in range(0,27):
	if i == 26:
		print("The number of spaces is ", count[26])	
	else:
		print("The number of ", alpha[i], " is ", count[i])