import random
a = int(random.randrange(1,100))
gameon = 0
guesses = 10
print("You have 10 guesses to answer ")
for x in range(1, 10+1):
	b = int(input("Guess a number which is lesser than the number I thought  "))
	print("You have ", guesses-x , " guesses left ")
	if b < a:
		print("Guess more  ")
	elif b>a:
		print("Guess lesser ")
	else:
		print("correct answer")
		gameon=1
		break

if gameon==1:
	print("You win ")
else:
	print("You loose")

print("the correct answer is ", a)