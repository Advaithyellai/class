import datetime
import time
import random

wl = 0
div = 0
fll = 0
no = 21
end = 0
go = 0
exfl = 0
opfl = 4
wl = 0
loa = []
noc = 0
load = []
loeo = [':)', ':(', ':|', ':]', ':[', ':}', ':{', ':>', ':<', ':D']
doeo = {':)':1, ':(': 2, ':|':3, ':]':4, ':[':5, ':}':6, ':{':7, ':>':8, ':<':9, ':D':10}
mat = 0
mq = 'yes'
now = 0

user = input("What is your name ")
print("Hello %s!" %(user))
print("Welcome to my computer app 'The phocomp 1' app.")

print(" ")
print("Notifications - 0__________battery - 100% ")
for x in range(0, 10):
	print("   ")
dps = input("Your device is empty(^). Do you want to download play store?  ")

while(exfl < 10):
	if dps == 'yes':
		print("For downloading it you have to wait for 5 seconds")
		time.sleep(5)
		print("It has DOWNLOADED! :] ")
		exfl = 10
	else:
		dps = input("Your tab is empty. Do you want to download play store?(it is mandatory)  ")

print("You have entered play store. The apps in here are:- ")
print("1 = Caluclater")
print("2 = Guessing game")
print("3 = Math game")
print("There is no exit")
gd =int(input("Which one do you choose(1, 2 or 3)  "))
try:
	if gd == 1:
		print("Ok. Downloading in 5 seconds")
		time.sleep(5)
		print("It has DOWNLOADED! :]")
		print("You have entered Caluclater")
		z = int(input("How many calculations do you want to make   "))
		while(wl < z):
			wl = wl + 1
			print("1 = Addition")
			print("2 = Subtraction")
			print("3 = Multiplication")
			print("4 = division")
			print("5 = Average")
			print("6 = power ")
			print("7 = exit")
			a = int(input("Which of the following do you choose  "))
			if a == 1:
				adin = int(input("How many numbers do you want to add  "))
				for bbla in range(0, adin):
					bblla = int(input("Type a number  "))
					load.append(bblla)
				ssol = sum(load)
				print("The sum of", load, "is", ssol)
			elif a == 2:
				so = int(input("Type the first number  "))
				st = int(input("Type another number    "))
				print("The difference between %f and %f is %f" %(so, st, so-st))
			elif a == 3:
				sfo = int(input("Type a number  "))
				sfot = int(input("Type a number  "))
				print("The product of %d and %d is %d" %(sfo, sfot, sfo*sfot))
			elif a == 4:
				sso = int(input("Type a number "))
				ssot = int(input("Type another number "))
				print("The quotient of ", sso," and ", ssot, " is ", sso/ssot)
			elif a == 5:
				ain = int(input("How many numbers do you want the Average of  "))
				for bla in range(0, ain):
					blla = int (input ("Type a number  "))
					loa.append(blla)
				sol = sum(loa)
				solo = len(loa)
				solot = sol /solo
				print("The average of", loa ,"is", solot)
			elif a == 6:
				sto = int(input("Type a number  "))
				sfo = int(input("Type a 2nd number  "))
				print("the power of ", sto, " and ", sfo, " is ", pow(sto, sfo))
			elif a == 7:
				print(" ")
				wl = z
			else:
				print("Sorry I can not help you")
				print("  ")

	elif gd == 2:
		print("Ok. Downloading in 5 seconds")
		time.sleep(5)
		print("It has DOWNLOADED! :]")
		print("You have entered Guessing game ")
		print("Levels = -1-  2  3  4  5")
		print("You will have to guess the numbers 1 - 10")
		ggno = int(random.randrange(1, 10))
		while(wl < 4):
			wl = wl + 1
			fll = fll+1
			print("You have %d guesses left" %(opfl))
			opfl = opfl-1
			gno = int(input("Guess the number I thought  "))
			if ggno > gno:
				print("Guess more  ")
			elif ggno < gno:
				print("Guess lesser ")
			elif ggno == gno:
				print("CONGRATULATIONS! You have done it. :-]")
				go = 1
				wl = 4
			else:
				pass
		if go == 1:
			print("It took you %d guesses to break it" %(fll))
		else:
			print("Oh no! :-[ The answer is ", ggno)
		egg = input("Do you want to exit this game  ")
		egg = egg.lower()
		if egg == 'yes':
			print("Ok, Exitng.")
		else:
			print("Levels = 1 -2- 3  4  5")
			print("You will now have to guess the numbers 1 - 100")
			ggno = int(random.randrange(1, 100))
			opfl = 10
			fll = 0
			go = 0
			while(wl < 10):
				wl = wl + 1
				fll = fll+1
				print("You have %d guesses left" %(opfl))
				opfl = opfl-1
				gno = int(input("Guess the number I thought  "))
				if ggno > gno:
					print("Guess more  ")
				elif ggno < gno:
					print("Guess lesser ")
				elif ggno == gno:
					print("CONGRATULATIONS! You have done it. :-]")
					go = 1
					wl = 10
				else:
					pass
			if go == 1:
				print("It took you %d guesses to brake it" %(fll))
			elif go == 0:
				print("Oh no! :-[ The answer is ", ggno)
			else:
				pass
			eegg = input("Do you want to exit this game  ")
			eegg = eegg.lower()
			if eegg == 'yes':
				print("Ok, Exitng.")
			else:
				print("Levels = 1  2 -3-  4  5")
				print("You will now have to guess the emojis ", doeo)
				ggo = int(random.randrange(1, 10))
				ggno = loeo[ggo]
				opfl = 4
				wl = 0
				go = 0
				while(wl < 4):
					wl = wl + 1
					fll = fll+1
					print(":) = 1 , :( = 2 , :| = 3 , :] = 4 , :[ = 5 , :} = 6 , :{ = 7 , :> = 8 , :< = 9 and :D = 10")
					print("You have %d guesses left" %(opfl))
					opfl = opfl-1
					gno = int(input("Guess the number of emoji I thought  "))
					if gno < ggo:
						print("Guess more  ")
					elif gno < ggo:
						print("Guess lesser ")
					elif gno == ggo:
						print("CONGRATULATIONS! You have done it. :-]")
						print("It is", ggno)
						go = 1
						wl = 4
					else:
						pass
				if go == 1:
					print("It took you %d guesses to brake it" %(fll))
				elif go == 0:
					print("Oh no! :-[ The answer is ", ggno)
					eeegg = input("Do you want to exit this game  ")
					eeegg = eeegg.lower()
				else:
					pass
				if eeegg == 'yes':
					print("Ok, Exitng.")
				else:
					print("Sorry we have 3 levels available till now. We have to exit")

	elif gd == 3:
		print("Ok. Downloading in 5 seconds")
		time.sleep(5)
		print("It has DOWNLOADED! :]")
		print("You have entered Math game ")
		print("Levels -1-  2  3  4  5")
		if mq == "yes":
			maqu= 'YES'
			maqu=maqu.swapcase()
			if maqu == 'yes':
				while(mat < 5):
					mat = mat +1
					fmn = random.randrange(2, 10)
					smn = random.randrange(11, 20)
					stti= datetime.datetime.now()
					q1 = int(input("Q1. %d*%d " %(fmn, smn)))
					if q1 == fmn*smn:
						noc = noc+1
						print("it is correct ")
						while(div < 1):
							fdn = random.randrange(101, 399)
							sdn = random.randrange(2, 10)
							if fdn%sdn == 0:
								div = 1
							else:
								pass
						q2 = int(input("Q2. %d/%d " %(fdn, sdn)))
					else:
						now = now +1
						print("it's wrong")
						print("it is correct ")
						while(div < 1):
							fdn = random.randrange(101, 399)
							sdn = random.randrange(2, 10)
							if fdn%sdn == 0:
								div = 1
							else:
								pass
						q2 = int(input("Q2. %d/%d " %(fdn, sdn)))
					if q2 == fdn/sdn:
						noc = noc+1
						print("It's correct ")
						fan = random.randrange(501, 999)
						san = random.randrange(501, 999)
						q3 = int(input("Q3. %d + %d" % (fan, san)))
					else:
						now=now+1
						print("It's wrong")
						fan = random.randrange(501, 999)
						san = random.randrange(501, 999)
						q3 = int(input("Q3. %d + %d" %(fan, san)))
					if q3 == fan + san:
						noc=noc+1
						print("it's correct")
						fsn = random.randrange(501, 999)
						ssn = random.randrange(101, 499)
						q4 = int(input("Q4. %d - %d " %(fsn, ssn)))
					else:
						now=now+1
						print("It's wrong")
						fsn = random.randrange(501, 999)
						ssn = random.randrange(101, 499)
						q4 = int(input("Q4. %d - %d " %(fsn, ssn)))
					if q4 == fsn - ssn:
						noc=noc+1
						print("it's correct")
					else:
						now = now+1
						print("It's wrong")
					print("The no. of corrects you got is/are", noc)
					print("The no. of wrongs you got are/is", now)
					etti = datetime.datetime.now()
					estti = etti-stti
					print("The time you took is", estti)
					print("Look at this file known as 'mathtime.txt'. There will be the time taken by all the people who played this game")
					otf = 'mathtime.txt'
					of = open(otf)
					of.write(user)
					of.write(", the time you took is %f ," %(estti))
					of.write("%s got %d corrects " %(user, noc))
					of.close()
					dywe = input("Do you want to exit this game  ")
					dywe = dywe.lower()
					if dywe == 'yes':
						print("Ok, exiting")
						mat = 5
					else:
						pass

	else:
		pass

except Exception as ex:
	print(" ")
	print(" ")

print("Notifications - 1_______Batttery - 5%")
if gd == 1:
	print("  _______     _______")
	print(" | PLAY  |___| CALUC |")
	print(" | STORE |___| LATER |")
	print("  --------    -------  ")
	for x in range(1, 5):
		print("  ")
elif gd == 2:
	print("  _______     ___________")
	print(" | PLAY  |___| GUESSING |")
	print(" | STORE |___| GAME     |")
	print("  --------    -----------  ")
	for x in range(1, 5):
		print("  ")
elif gd == 3:
	print("  _______     _______")
	print(" | PLAY  |___| MATH |")
	print(" | STORE |___| GAME |")
	print("  --------    -------  ")
	for x in range(1, 5):
		print("  ")
else:
	for z in range(0, 5):
		print(" ")
		print(" ")
print("                     :|       ____")
print("LOW BATTERY SHUTTING DOWN!:! |___|")
print("This is the end of version 1.0")
print("THANK YOU FOR USING IT! ")
print(":+ := :[ :] :{ :} :< :> :-| ;| ;-| :0 :| :( :) :& :$ :# :! :B :c :C :D :E :I :J :K :l :N :o :O :S :x :X :z :Z ")
print("These are all the emojis I know(^).")