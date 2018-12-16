import time
no = 21
user = input("What is your name ")
print("Hello %s!" %(user))
print("Welcome to my computer app 'The phocomp 1 app'.")
for x in range(0, 10):
	print("   ")
print("                  ^")
dps = input("Your device is empty(|). Do you want to download play store?  ")
while(True):
	if dps == 'yes':
		for i in range(0, 20):
			no = no - 21
			print("For downloading it you have to wait for %d seconds" %(no))
		end = 1
	else:
		dps = input("Your tab is empty. Do you want to download play store?(it is mandatory)  ")
	if end == 1:
		exit()
	else:
		pass
eps = input("Do you want to enter play store? ")
if eps == 'yes':
	print("You have entered play store. The apps in here are:- ")
	print("1 = Caluclater")
	print("2 = 'Speed game'")
	print("3 = guessing game")
	print()
