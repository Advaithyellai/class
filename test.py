import time
import random
scor = 0
print("Hi! Let's see how lucky you are")
name = input("What's your name  ")
class Players:
    def __init__(self, first, last, position, score):
        self.firstname = first
        self.surname = last
        self.play = position
        self.point = score
    def greeting(self):
        print("Hi I am %s and my last name is %s and I play as %s, I am %s points" %(self.firstname, self.surname, self.play, self.point))
plr_1 = Players('Advaith   ', 'Yellai   ', 'Center Defence Mid,  ', 11)
plr_2 = Players('Wojciech  ', 'Szczresny', 'Goalkeeper,          ', 5)
plr_3 = Players('Christiano', 'Ronaldo  ', 'Right Forward,       ', 10)
plr_4 = Players('Paula     ', 'Dybala   ', 'Left Forward,        ', 6)
plr_5 = Players('Miralem   ', 'Pjanic   ', 'Center Attack mid,   ', 7)
plr_6 = Players('Douglas   ', 'Costa    ', 'Right Wing,          ', 9)
plr_7 = Players('Emre      ', 'Can      ', 'Left Wing,           ', 8)
plr_8 = Players('Medhi     ', 'Benatia   ', 'Right front defence,', 4)
plr_9 = Players('Leornado  ', 'Bonicci   ', 'Left front defence, ', 3)
plr_10 = Players('Joao     ', 'Cancelo   ', 'Right back defence, ', 2)
plr_11 = Players('Giorgio  ', 'Chiellini ', 'Left back defence,  ', 1)
print("You're going to be given a random player. Each player is a few points")
print("It's starting")
rand = random.randrange(1, 1000)
press = int(input("Type %s to continue  " %(rand)))
if press == rand:
    pass
else:
    exit("Next time press a random number")
for lop in range(0, 5):
    print("Spinning.", end = '\r')
    time.sleep(1)
    print("Spinning..", end = '\r')
    time.sleep(1)
    print("Spinning...", end = '\r')
    time.sleep(1)
    ran = random.randrange(1, 11)
    if ran == 1:
        plr_1.greeting()
        print("You are lucky, very lucky you got 11 points")
        scor += 11
    elif ran == 2:
        plr_2.greeting()
        print("You are average, you got 5 points")
        scor += 5
    elif ran == 3:
        plr_3.greeting()
        print("You are lucky, very lucky you got 10 points")
        scor += 10
    elif ran == 4:
        plr_4.greeting()
        print("You are above average, you got 6 points")
        scor += 6
    elif ran == 5:
        plr_5.greeting()
        print("You are above average, you got 7 points")
        scor += 7
    elif ran == 6:
        plr_6.greeting()
        print("You are lucky, you got 9 points")
        scor += 9
    elif ran == 7:
        plr_7.greeting()
        print("You are lucky, you got 8 points")
        scor += 8
    elif ran == 8:
        plr_8.greeting()
        print("You are average, you got 4 points")
        scor += 4
    elif ran == 9:
        plr_9.greeting()
        print("You are below average you got 3 points")
        scor += 3
    elif ran == 10:
        plr_10.greeting()
        print("You are below average you got 2 points")
        scor += 2
    elif ran == 11:
        plr_11.greeting()
        print("You are unlucky you got 1 points")
        scor += 1
    else:
        pass
    time.sleep(5)
    print("  ")
    print("  ")
print("Your score is", scor)
print("Check a file named football.txt there will be all the scores played")
opening, ope = open('football.txt' , 'a'), open('foot.txt', 'a')
opening.write("name = %s, score = %d" %(name, scor), end = '\n')
ope.write("name = %s, score = %d" %(name, scor), end = '\n')
opening.close()
ope.close()
print("name = %s score = %d" %(name, scor))
print("Tata, Bye-bye")