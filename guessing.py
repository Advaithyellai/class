import random
am = int(random.randrange(1,100))
gameon = 0
guesses = 10
print("You have 10 guesses to answer ")
for ao in range(1, 10+1):
	guesses = guesses -1
	an = int(input("Guess the number which I thought  "))
	print("You have ", guesses , " guesses left ")
	if an < am:
		print("Guess more  ")
	elif an > am:
		print("Guess lesser ")
	else:
		print("correct answer")
		gameon=1
		break

if gameon==1:
	print("You win ")
else:
	print("You loose")
print("the correct answer is ", am)