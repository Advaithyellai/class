import datetime
import math
import time
import random
sti = datetime.datetime.now()
a = float(input("type your height             "))
b = float(input("type you weight              "))
c = float(input("type your age                "))
X = input("write a word                   ")
Y = input("type your name                 ")
Z = input("what is your favourite place   ")
e = int(a+b/c)
noc =0
now= 0
f = int(input("type a number                  "))
g = int(input("type another number            "))
d = input("Do you like watching football  ")
m = ("yes")
n = ("barcelona")
p = ("real madrid")
r = ("brazil")
t = ("5")
v = ("south africa")
none = "himalayas"
go = 0
year = int(input("Which YEAR were you born  "))
print("    1   ,     2  ,     3    ,     4    ,    5   ,    6    ,   7     ,    8   ,    9   ,    10   ,    11   ,    12   .")
print(" Jan = 1, Feb = 2, March = 3, April = 4, May = 5, June = 6, July = 7, Aug = 8, Sep = 9, Oct = 10, Nov = 11, Dec = 12.")
month = int(input("Which MONTH were you born(in number "))
day = int(input("Which DAY were you born  "))
mq = input("Are you good in maths ")
mq = mq.lower
w = int(input("type your height             "))
x = int(input("type you weight              "))
y = int(input("type your age                "))
z = input("write a word                   ")
aa = input("type your name                 ")
ab = input("what is your favourite place   ")
ac = int((w+x)/y)
ad = int(input("type a number                  "))
ae = int(input("type another number            "))
print("   ")
print("hi," + Y)
print("The length of your word, " + X +" is "+ str(len(X)) + " lettters long")
print("Your bmi = " + str(e-1))
if Z != none:
  print("Oh your favourite place is " + Z + ", my favourite place is himalayas")
else:
  print("Oh even my favourite place is himalayas ")
print("   ")
print("the sum of the 2 numbers is " + str(f+g))
print("the difference between the two numbers is " + str(f-g))
print("the quotient of the 2 numbers is " + str(f/g))
print("the product of the 2 numbes is " + str(f*g))
print("the average the two numbers is " + str(f+g/2))
print("   ")
if d == m:
    h = input("would you like to have a football quiz  ")
    if h == m:
      i = input("Q1. which team does lionel andres messi play for in europe club matches   ")
      i = i.lower()
      if i == n:
        print("correct answer")
        go = go + 1
        o = input("Q2. which team does christiano ronaldo play for in europian club matches  ")
        o = o.lower()
      else:
        print("wrong answer, it is Barcelona")
        o = input("Q2. which team does christiano ronaldo play for in europian club matches  ")
        o = o.lower()
      if o == p:
        go = go + 1
        print("correct answer")
        q = input(print("Q3. Which team in FIFA was the most succesful   "))
        q = q.lower()
      else:
        print("wrong answer, it is Real Madrid")
        q = input(print("Q3. Which team in FIFA was the most succesful   "))
        q = q.lower()
      if q == r:
        print("correct answer ")
        go = go + 1
        s = input(print("Q4. How many matches did france win in 2018 in numerals  "))
      else:
        print("wrong answer, it is Brazil   ")
        s = input(print("Q4. How many matches did france win in 2018 in numerals  "))
      if s == t:
        print("correct answer")
        go = go + 1
        u = input(print("Q5. where did 2010 world cup be held"))
        u = u.lower()
      else:
        print("wrong answer, it is 5")
        u = input(print("Q5. where did 2010 world cup be held  "))
        u = u.lower()
      if u == v:
        go = go + 1
        print("correct answer")
        print("cograts the quiz is over")
        print("Your score is ", go, " out of 5")
        print("The number of wrong answers are ", 5 - go)
        print("   ")
      else:
        print("wrong answer, it is south africa")
        print("congrats the quiz is over")
        print("Your score is ", go, " out of 5")
        print("The number of wrong answers are ", 5 - go)
        print("   ")
    else:
      j = input(print("do you watch ISL(ignore the none)  "))
      if j == m:
        print("oh even I watch ISL, my favourite team is goa")
        print("   ")
      else:
        k = input(print("do you atleast watch FIFA  "))
        if k == m:
          print("oh, even I watch FIFA my favourite player is ronaldo")
          print("   ")
        else:
          l = input(print("then do you watch clubs  "))
          if l == m:
            print("oh, I like Messi in clubs")
            print("   ")
          else:
            print("then what do you watch. You are not a football fan")
            print("   ")
else:
  print("Oh, try watching some matches then you will like it")
  print("   ")
print("     ")
class Jungle:
    def __init__(self, name, vore, place, behavior, pred, prey):   
        self.animal = name
        self.vores = vore
        self.live = place
        self.behave = behavior
        self.predator = pred
        self.prey = prey
    def Name(self):
        print("\n Name: {} \n type: {} \n Position: {} \n Speciality: {} \n Prey: {} \n Predator: {}" .format(self.animal, self.vores, self.live, self.behave, self.prey, self.predator))
class Animal(Jungle):
    def __init__(self, name, vore, place, behavior, pred, prey):
        super().__init__(name, vore, place, behavior, pred, prey)
    def details(self):
        print("\n Name: {} \n type: {} \n Position: {} \n Speciality: {} \n Prey: {} \n Predator: {}" .format(self.animal, self.vores, self.live, self.behave, self.prey, self.predator))
printer_1 = Jungle('Worm', 'Herbivore', '3rd', 'Slow walker', 'Sparrow', 'Hawk')
printer_2 = Animal('Sparrow', 'Insectivore', '2nd', 'Fast digger', 'Hawk', 'Worm' )
printer_3 = Animal('Hawk', 'Carnivores', '1st', 'Super sight', 'Worms', 'Sparrow')
printer_1.Name()
printer_2.details()
printer_3.details()
print("     ")
if mq == "yes":
  maqu= input("Would you like a quiz of maths ")
  maqu=maqu.lower()
  if maqu == 'yes':
    stti= datetime.datetime.now()
    q1 = int(input("Q1. 13*7 "))
    if q1 == 91:
      noc = noc+1
      print("it is correct ")
      q2 = (input("Q2. 138/6 "))
    else:
      now = now +1
      print("it's wrong")
      q2 = int(input("Q2. 138/6 "))
    if q2 == 23:
      noc = noc+1
      print("It's correct ")
      q3 = int(input("Q3. 573 + 698"))
    else:
      now=now+1
      print("It's wrong")
      q3 = int(input("Q3. 573 + 698"))
    if q3 == 1271:
      noc=noc+1
      print("it's correct")
      q4 = int(input("Q4. 574 - 397"))
    else:
      now=now+1
      print("It's wrong")
      q4 = int(input("Q4. 574 - 397"))
    if q4 == 177:
      noc=noc+1
      print("it's correct")
      print("The no. of corrects you got is/are", noc)
      print("The no. of wrongs you got are/is", now)
      etti = datetime.datetime.now()
      print("The time you took is", etti-stti)
else:
  print("")
print("Welcome to my amazing game (Not like Advaith.Basireddy's)")
print("This game is about story telling")
d = input("What's your name  ")
j = input("What do you want to name your charecter   ")
print("Choose your weponry,", d)
print("1. No weapon")
print("2. Daggers")
print("3. Bow")
print("4. Sword")
print("5. Gun")
a = int(input("Choose your bloody weapon  "))
if a < 100:
    print("Ok. %d is chosen " %(a))
    print("Which shield do you choose")
    b = int(input("1 = metal, 2 = wooden, 3 = no shield.  "))
    if b ==1:
        print("Ok, it is %s" %('metal'))
    elif b == 2:
        print("Ok, it is wooden")
    else:
        print("Ok, no weapon")
    if b != 3:
        print("1. Square shaped")
        print("2. Diamond shaped")
        print("3. Rectangluar shaped")
        print("4. Ovalar shaped")
        c = int(input("What do you want to choose  "))
        print("Ok. %d is chosen" %(c))
    print("Now the story BEGINS!")
    print("You were born in an alien planet and you were sent to Earth at the age 2")
    print("You had super powers before")
    print("But your arch enemy took them all. But he couldn't kill you")
    print("Because you were too strong")
    print("Now, he wants to rule Earth")
    print("The world depends on you,", j)
    print("No one should speak 'his' name. We call him 'human-evil'")
    print("Human-evil's name is Ad-A-Adv-Advaith.Basireddy")
    print("If you speak human-evils name 5 times you you will be cursed")
    time.sleep(5)
    print("Oh no human-evils minion's minion is coming. Tata bye-bye!")
    print("1 = Call your best friend as back up(he will come in 1 min)")
    print("2 = Fight with her")
    print("3 = Run away")
    print("4 = Call your company as back up(2 min & 10 persons)")
    print("5 = Let her kill you")
    print("6 = Tell human-evil's name 5 times")
    e = int(input("What do you choose  "))
    if e == 1:
        print("Oh no she's asking you to fight with her")
        print("1 = Fight with her")
        print("2 = Run away")
        print("3 = Let her kill you")
        f = int(input("What do you do  "))
        if f == 1:
            print("Ok. Fight")
            time.sleep(5)
            print("Now you win and back up comes and arrests her")
        elif f == 2:
            print("Now you run of far and you see your back up")
            print("1.= Go with him and fight her")
            print("2.= Ask him to run with you")
            print("3.= Ask him only to fight her")
            g = int(input("What do you do  "))
            if g == 1:
                print("Ok. Fighting")
                time.sleep(2)
                print("Now your best friend dies")
                print("1 Run away")
                print("2 Keep fighting")
                h = int(input("Choose one  "))
                if h == 1:
                    print("Now you see a 'HUMAN-EVIL'!")
                    print("He kills you")
                    print("Thanks for playing this", d)
                    print("This is the end of version 1.0")
                    exit("Tata bye-bye")
                elif h == 2:
                    print("Ok. Fighting")
                    time.sleep(5)
                    print("You win!")
                else:
                    print("Try again!")
                    exit()
            elif g == 2:
                print("Now you see a 'HUMAN-EVIL'!")
                print("He kills you and her")
                print("Thanks for playing this", d)
                print("This is the end of version 1.0")
                exit("Tata bye-bye")
            else:
                print("He says,'Ok, you stay here.'")
                print("And he goes to fight her")
                print("Now you see a 'HUMAN-EVIL'!")
                print("He kills you")
                print("Thanks for playing this", d)
                print("This is the end of version 1.0")
                exit("Tata bye-bye")
        else:
            print("Now you are stabbed and in 5 seconds you'll be killed")
            time.sleep(5)
            print("Now your best friend comes and sees this and kills her")
            print("He takes you to the hospital")
            print("The doctors say that because you are not from Earth they don't know your organs")
            print("Now you see a 'HUMAN-EVIL'!")
            print("He kills you")
            print("Thanks for playing this", d)
            print("This is the end of version 1.0")
            exit("Tata bye-bye")
    elif e == 2:
        print("Ok. Fighting")
        time.sleep(2)
        print("She stabs your leg and gets a shock cause you are an alien")
        print("Now she's down for a few mins")
        print("1 = Call your friend as back up(2 min)")
        print("2 = Call your company as back up(4 min)")
        print("3 = Let her wake up and kill you(5 min)")
        i = int(input("Which one  "))
        if i == 1:
            print("You pick your phone and call him")
            print("He tells,'Ok I'll reach there in 2 min, google maps'.")
            time.sleep(2)
            print("Now, human-evil sees him")
            print("He fights hi, but he looses. Then human-evil kills him")
            print("Now, she gets up from her shock and shots you")
            print("Now you are dead")
            print("Thanks for playing this", d)
            print("This is the end of version 1.0")
            exit("Tata bye-bye")
        elif i == 2:
            print("You pick your phone and call them")
            print("They tell,'Ok I'll reach there in 4 min, google maps'.")
            time.sleep(4)
            print("Now, human-evil sees them")
            print("Now, they fight against them")
            print("Then they stab human-evil's knee")
            print("Human-evil fell and your company is running to you")
            print("Now, they have arrived to save you")
            print("Now, she gets up from the shock")
            print("Now Your crew kills her")
        else:
            time.sleep(5)
            print("Now she kills you")
            print("Thanks for playing this", d)
            exit()
    elif e == 3:
        print("Ok. Running")
        print("You will take 5 sec to run away")
        time.sleep(5)
        print("Now your arch enemie is in front ")
        print("What do you do")
        print("1. Fight him")
        print("2. Run back and fight his minion")
        print("3. Call for help(2 min)")
        print("4. Die on spot")
        k = int(input("Which one do you choose  "))
        if k == 1:
            print("Ok fighting")
            time.sleep(5)
            print("Oh! You died")
            print("I forgot to warn you, he is stronger")
            print("Thanks for playing this", d)
            exit("Tata, bye-bye")
        elif k==2:
            print("Ok. Running back")
            time.sleep(2)
            print("I forgot to warn you, he is faster")
            print("He has caught you and killed you")
            print("Thanks for playing this", d)
            exit("Tata, bye-bye")
        elif k==3:
            print("Ok. You pick your phone and call help")
            print("But human-evil kills you before they come")
            print("Thanks for playing this", d)
            exit("Tata, bye-bye")
        else:
            print("Ok. Dying")
            print("Thanks for playing this", d)
            exit("Tata, bye-bye")
    elif e == 4:
        print("Oh no she's asking you to fight with her")
        print("1 = Fight with her")
        print("2 = Run away")
        print("3 = Let her kill you")
        f = int(input("What do you do  "))
        if f == 1:
            print("Ok. Fight")
            time.sleep(5)
            print("Now you win and back up comes and arrests her")
        elif f == 2:
            print("Now you run of far and you see your back up")
            print("1.= Go with him and fight her")
            print("2.= Ask him to run with you")
            print("3.= Ask him only to fight her")
            g = int(input("What do you do  "))
            if g == 1:
                print("Ok. Fighting")
                time.sleep(2)
                print("Now your best friend dies")
                print("1 Run away")
                print("2 Keep fighting")
                h = int(input("Choose one  "))
                if h == 1:
                    print("Now you see a 'HUMAN-EVIL'!")
                    print("He kills you")
                    print("Thanks for playing this", d)
                    print("This is the end of version 1.0")
                    exit("Tata bye-bye")
                elif h == 2:
                    print("Ok. Fighting")
                    time.sleep(5)
                    print("You win!")
                else:
                    print("Try again!")
                    exit()
            elif g == 2:
                print("Now you see a 'HUMAN-EVIL'!")
                print("He kills you and her")
                print("Thanks for playing this", d)
                print("This is the end of version 1.0")
                exit("Tata bye-bye")
            else:
                print("He says,'Ok, you stay here.'")
                print("And he goes to fight her")
                print("Now you see a 'HUMAN-EVIL'!")
                print("He kills you")
                print("Thanks for playing this", d)
                print("This is the end of version 1.0")
                exit("Tata bye-bye")
        else:
            print("Now you are stabbed and in 5 seconds you'll be killed")
            time.sleep(5)
            print("Now your best friend comes and sees this and kills her")
            print("He takes you to the hospital")
            print("The doctors say that because you are not from Earth they don't know your organs")
            print("Now you see a 'HUMAN-EVIL'!")
            print("He kills you")
            print("Thanks for playing this", d)
            print("This is the end of version 1.0")
            exit("Tata bye-bye")
    elif e == 5:
        print("Ok. Killing")
        time.sleep(2)
        print("Thanks for playing this game", d)
        exit("Tata, bye-bye")
    elif e == 6:
        print("Ok telling")
        time.sleep(2)
        print("Now human-evil's minion's minion informed human-evil and he comes")
        print("1. Run away")
        print("2. Fight with him")
        print("3. Die on spot")
        k = int(input("Which one  "))
        if k == 1:
            print("Ok. Running")
            time.sleep(2)
            print("Because you are unlucky you trip on a stone and fall")
            print("Now human-evil catches you and kills you")
            print("Thanks for playing %s/%s" %(d, j))
            exit("Tata, bye-bye")
        elif k == 2:
            print("Ok, fighting")
            time.sleep(2)
            print("Because you are unlucky he kills you")
            print("Thanks for playing %s/%s" %(d, j))
            exit("Tata, bye-bye")
        else:
            print("Ok, killing")
            time.sleep(5)
            print("Thanks for playing %s/%s" %(d, j))
            exit("Tata, bye-bye")
    else:
        print("Sorry cant help with that")
else:
    print("Sorry can't help")
    print("Thanks for playing this game", d)
    exit("Tata, bye-bye")
print("Congrats!")
print("Now you go to a training school")
print("There are 2 trained professionals, pick one to coach you")
print("1 = Kris = swords(attack and defence)")
print("2 = Bablu = shield(attack and defence)")
l = int(input("Pick a coach for you "))
if l == 1:
    n = '____________'
    print("Ok training")
    print("He'll train in 12 days(in our world 12 seconds)")
    time.sleep(1)
    for m in range(0, 12):
        n = list(n)
        time.sleep(1)
        n[m] = '-'
        n = str(n)
        print(n, end="\r")
    print("Done training")
    print("You know-;")
    print("sword shield, sword block, sword clash, cut arrow, sword throw, sword jump and sword slash")
    print("Oh no :[")
    print("A minion of human-evil found out that you were in this school")
    print("He's coming your way")
    print("1 - run far away")
    print("2 - stay and fight")
    print("3 - Tell human-evils name 5 times")
    o = int(input("What is your decision   "))
    if o == 1:
        print("Ok. Running")
        print("You will jump out of the window and jump")
        time.sleep(5)
        print("Ohhh! No, human-evil is in front of you")
        print("1 <fight him>")
        print("2 <run away>")
        print("3 <die>")
        p = int(input("What do you do   "))
        if p == 1:
            print("Ok fighting")
            time.sleep(2)
            print("He kills you")
            print("Thanks for playing this %s or %s" %(d, j))
            exit("Tata, bye-bye")
        elif p==1:
            print("Ok running")
            time.sleep(2)
            print("He is faster than you")
            print("He catches you and kills you")
            print("Thanks for playing this %s or %s" %(d, j))
            exit("Tata, bye-bye")
        else:
            print("Ok dying")
            time.sleep(2)
            print("He kills you")
            print("Thanks for playing this %s or %s" %(d, j))
            exit("Tata, bye-bye")
    elif o == 2:
        print("Ok staying")
        time.sleep(8)
        print("Now his minion comes and fights with all of you")
        time.sleep(2)
        print("He injures you and dies because Rishik kills him")
        print("They take you to a hospital")
        print("The doctors say that you can't recover")
        print("Because you are an alien")
        print("Now you die")
        print("Thanks for playing this %s or %s" %(d, j))
        exit("Tata, bye-bye")
    else:
        print("Ok telling")
        time.sleep(2)
        print("told")
        print("Now theres an Earthquake and you die in it")
        print("Thanks for playing %s or %s" %(d, j))
        exit("Tata, bye-bye")
elif l == 2:
    q = '____________'
    print("Ok training")
    print("He'll train in 12 days(in our world 12 seconds)")
    time.sleep(1)
    for r in range(0, 12):
        q = str(q)
        print(q, end = "\r")
        time.sleep(1)
        q = list(q)
        q[r] = '-'
    print("Done training")
    print("You know-;")
    print("sword shield, shield block, shield strike, cut arrow, shield throw, shield jump and shield slash")
    print("Oh no :[")
    print("A minion of human-evil found out that you were in this school")
    print("He's coming your way")
    print("1 - run far away")
    print("2 - stay and fight")
    print("3 - Tell human-evils name 5 times")
    s = int(input("What is your decision   "))
    if s == 1:
        print("Ok. Running")
        print("You will jump out of the window and jump")
        time.sleep(5)
        print("Ohhh! No, human-evil is in front of you")
        print("1 <fight him>")
        print("2 <run away>")
        print("3 <die>")
        p = int(input("What do you do   "))
        if p == 1:
            print("Ok fighting")
            time.sleep(2)
            print("He kills you")
            print("Thanks for playing this %s or %s" %(d, j))
            exit("Tata, bye-bye")
        elif p==1:
            print("Ok running")
            time.sleep(2)
            print("He is faster than you")
            print("He catches you and kills you")
            print("Thanks for playing this %s or %s" %(d, j))
            exit("Tata, bye-bye")
        else:
            print("Ok dying")
            time.sleep(2)
            print("He kills you")
            print("Thanks for playing this %s or %s" %(d, j))
            exit("Tata, bye-bye")
    elif s == 2:
        print("Ok staying")
        time.sleep(8)
        print("He has come")
        print("Now you are fighting")
        time.sleep(2)
        print("You win")
        print("This is the only way to win")
        print("Congrats! :}")
    else:
        print("Ok telling")
        time.sleep(2)
        print("told")
        print("Now theres an Earthquake and you die in it")
        print("Thanks for playing %s or %s" %(d, j))
        exit("Tata, bye-bye")
print("Now before he dies he kill Kris")
print("human-evil's minion sent a message in his phone to human-evil")
print("It will be sent in 1 month(game's time)")
print("1 = Try to break it")
print("2 = Ignore it")
t = int(input("Choose it  "))
if t == 1:
    print("Ok you chose to break it")
else:
    print("Ok ignored")
    print("When you are going Bablu thinks you are a spy of human-evil")
    print("Then he kills you by stabbing your stomach while going")
    print("Thanks for playing %s or %s" %(d, j))
u ={'*':'a', '&':'b', ')':'c', '(':'d', '^':'e', '@':'f', '%':'g', \
    '#':'h', '!':'i', '$':'j', ',':'k', '/':'l', '|':'m', '}':'n', \
    ']':'o', ':':'p', '[':'q', '`':'r', '~':'s', '-':'t', '_':'u', \
    '+':'v', '=':'w', '<':'x', '?':'y', '>':'z'}
print("The thing is written as -; (] !- @!@-^^} (*?~ *@-^` -]||]`]= for human-evil")
print("Bablu said that the only way to crack it is to get it from human-evil's secret hide out")
print("Then another person asks ,'But where is his hide out'")
print("Then Bablu answers ,'No one knows except human-evil and his minions know it'")
print("Then another person tells,'Ok we'll kidnap one")
print("1=[Agree]")
print("2=[Disagree and kill them all]")
print("3=[Run away]")
v = int(input("Choose one  "))
if v == 1:
    d = d.lower()
    x = list(d)
    y = (len(d)-1)
    if x[y] == 'a':
        print("Good girl :D")
    elif x[y] == 'e':
        print("Good girl :D")
    elif x[y] == 'i':
        print("Good girl :D")
    elif x[y] == 'o':
        print("Good girl :D")
    elif x[y] == 'u':
        print("Good girl :D")
    else:
        print("Good Boy :>")
        "".join(d)
elif v == 2:
    print("When you disagree they shoot you")
    print("thanks for playing this", d, "or", j)
    exit("Tata, bye-bye")
else:
    print("When you run they shoot you")
    print("thanks for playing this", d, "or", j)
    exit("Tata, bye-bye")
print("Now you and your crew go to search for them")
print("You overcome across a house where there are 3 people training in martial arts")
print("And 1 person reading a book")
print("One can be your patner")
print("1st person # Shield #")
print("2nd person # Sword #")
print("3rd person # ninja blades #")
print("4th person # Super smart #")
z = int(input("Choose your patner  "))
print("Ok")
print("You will continue walking")
time.sleep(2)
print("The you see a couple of guards")
aa = int(input("1-bring 'em down, 2-die, 3-run  "))
if aa == 1:
    print("Ok trying")
    time.sleep(2)
    print("You got half down and your patner got the other half")
    print("You go in")
    print("You see a minion of human-evil")
    print("What do you do")
    ab = int(input("1-bring him down, 2-die, 3-run  "))
    if ab != 1:
        print("Ok")
        if ab ==2:
            print("dead")
        else:
            print("He shoots you while you are running")
        print("Thanks for playing %s or %s" %(d, j))
        exit("Tata, bye-bye")
    else:
        print("You bring him down")
        print("Now only 5 members including you and your patner are left in your crew")
elif aa ==2:
    print("dead")
    print("Thanks for playing %s or %s" %(d, j))
else:
    print("Your patner killed you")
    print("Because he doubted you")
print("You go deeper inside")
print("You see ")
time.sleep(2)
print("...HUMAN-EVIL...")
print("1 = fight him")
print("2 = Die on spot")
print("3 = Run away")
ac = int(input("What is your unanimous decision "))
if ac == 1:
    print("Ok fighting")
    time.sleep(5)
    if z == 1:
        print("You killed him :~}")
        print("You and your patner won")
    else:
        print("You died")
        print("Cause you couldn't co-ordinate well")
        print("If you had chosen shield as your patner you would win")
        print("Thanks for playing this %s or %s" %(d, j))
        exit("Tata, bye-bye")
elif a == 2:
    print("Dead")
    print("Thanks for playing this %s or %s" %(d, j))
    exit("Tata, bye-bye")
else:
    print("Now human-evil shoots you while you are running")
    print("Thanks for playing this %s or %s" %(d, j))
    exit("Tata, bye-bye")
print("Woo-hoo")
print("You and your patner co-ordinated amazingly")
print("Now you find a note in human-evil's pocket")
print("It has the code to the secret code")
print("1 -Crack it-")
print("2 -Ignore it-")
ad = int(input("What to do  "))
if ad == 1:
    ag = time.time()
    print("Ok picked")
    print("It says -;")
    print(u)
    print("The code is -;")
    print("(] !- @!@-^^} (*?~ *@-^` -]||]`]=")
    ae = 0
    while(ae < 1000):
        ae = ae+1
        print(u)
        af = input("What is the code  ")
        af = af.lower()
        if af == "do it fifteen days after tommorow":
            print("It is correct!")
            print("Bravo!")
            print("You are super intelligent")
            ah = time.time()
            print("You cracked it in %d guesses" %(ae))
            print("You took", int(ah-ag),"seconds")
            ae = 1000
        else:
            print("It's wrong")
else:
    print("Ok ignored")
    print("Now you got your super powers back")
    print("Thanks for playing this %s or %s" %(d, j))
    exit("Tata, bye-bye")
print("Now you got your super powers back")
u ={'*':'a', '&':'b', ')':'c', '(':'d', '^':'e', '@':'f', ';':'g', \
    '#':'h', '!':'i', '$':'j', ',':'k', '/':'l', '|':'m', '}':'n', \
    ']':'o', ':':'p', '[':'q', '`':'r', '~':'s', '-':'t', '_':'u', \
    '+':'v', '=':'w', '<':'x', '?':'y', '>':'z'}
print(u)
print("-#*},~ @]` :/*?!}; %s ]` %s" %(d, j))
exit("-*-* &?^ &?^")
senc =[2233, 2323, 3223, 2332, 3232, 3322]
senn =['Advaith.Y', 'Advaith.B', 'Daiwik', 'Tanishq', 'Vidit', 'Ganesh']
recc =[4455, 4545, 5445, 4554, 5454, 5544]
recn =['Advaith.Y', 'Advaith.B', 'Daiwik', 'Tanishq', 'Vidit', 'Ganesh']
bal = 1000

class Trans:
    def __init__(self, tran, sencar, reccar):
        self.trs = tran
        self.a_1 = sencar
        self.a_2 = reccar
        try:
            self.senca = senc.index(sencar)
            self.senna = senn[self.senca]
            self.recca = recc.index(reccar)
            self.recna = recn[self.recca]

        except Exception as ex:
            print("Sorry,", ex)

    def transact(self):
        if(self.trs < bal):
            print("You sent $%s to %s" %(self.trs, self.recna))
            print("Your name is %s and account number is **** and place is %s" %(self.senna, self.senca+1))
        else:
            print("Enna daa rascala! Emiti raa dunnepothu! Qya bey howle!")

acc_1 = int(input("What is your account number           "))
acc_2 = int(input("What's the reciever's account number  "))
acc_3 = int(input("How much money do you want to send    "))

trans_1 = Trans(acc_3, acc_1, acc_2)
trans_1.transact()
print("hi, " + aa)
print("The length of your word, " + z +" is "+ str(len(z)) + " lettters long")
print("Your bmi = " + str(ac-1))
print("Oh your favourite place is " + ab + ", my favourite place is himalayas")
print("  ")
print("the sum of the 2 numbers is " + str(ad+ae))
print("the difference between the two numbers is " + str(ad-ae))
print("the quotient of the 2 numbers is " + str(ad/ae))
print("the product of the 2 numbes is " + str(ad*ae))
print("the average the two numbers is " + str((ad+ae)/2))
print("   ")
name=input("Type a sentence  ")
af = input("What charecter do you need   ")
howmany = 0
for ch in name:
  if ch == af:
    howmany=howmany+1
print("The no. of charecters are ", howmany)
print("   ")
ag =float(input("type a number  ")) 
ah =float(input("type another number  "))
ai =int(input("type another number   "))
aj = 0
print("The number ", ag , "to the power of ", ah , " is ", pow(ag, ah))
print("the random number from 1 - 100 = " , random.randrange(1, 100))
print("the absolute value of " + str(ag) + " is "+ str(abs(ag)))
print("the ceiling value of " + str(ag) + " is " + str(math.ceil(ag)))
print("the floor value of " + str(ag) + " is " + str(math.floor(ag)))
for bb in range(1, ai+1):
  pass
  aj = aj + 1
  print(aj)
print("I am done")
print("  ")
ak = int(input("type a number  "))
sumx=1
for al in range(1, ak + 1):
  sumx = sumx * al
  print(sumx)
print("  ")
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
print("   ")
ap = int(input("How many calculations do you want to make   "))
for aq in range(ap):
  print("1 = Addition")
  print("2 = Subtraction")
  print("3 = Multiplication")
  print("4 = division")
  print("5 = Average")
  print("6 = power ")
  print("7 = exit")
  ar = int(input("Which of the following do you choose  "))
  at = int(input("Type a number   "))
  au= int(input("Type a 2nd number   "))
  if ar == 1:
    print("The sum of ", at," and ", au, " is ", at+au)
  elif ar == 2:
    print("The difference between ", at," and ", au, " is ", at-au)
  elif ar == 3:
    print("The product of ", at," and ", au, " is ", at*au)
  elif ar == 4:
    print("The quotient of ", at," and ", au, " is ", at/au)
  elif ar==5:
    print("The average of ", at," and ", au, " is ", (at+au)/2)
  elif ar == 6:
    print("the power of ", at, " and ", au, " is ", at^au)
  elif ar == 7:
    exit()
  else:
    print("Sorry I can not help you")
print("   ")
aaa = 0
while (aaa < 10):
  aaa = aaa + 1
  print("hello", a)
print("  ")
los=[]
for x in range(1,10+1):
  a = input("Write a word  ")
  los.append(a)
print(los)
b = input("which word do you want to find   ")
print(los.index(b))
print(len(los))
los.reverse()
print(los)
los.sort()
print(los)
print("  ")
a = 0
aa= int(input("How many changes do you want to make in the bookstore   "))
z = 0
y = aa
lof = ['Tinkle', 'Amar Chitra Khatha', 'Harry Potter and the Chamber of Secrets', 'Harry Potter and the Deathly Hallows' , 'Geronimo Stilton and the Kingdom of Fantasy' , 'Agatha Christie', 'Science and Nature' , 'Famous Five']
print("The list of the books of the store is :  ")
print(lof)
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
  print("  ")
  c = input("Which book do you want to add  ")
  lof.append(c)
  print("After ", c, " is added, the list is ", lof)
elif b == 2:
  print("  ")
  d = input("Which of the following book do you want to remove ")
  lof.remove(d)
  print("After ", d, " is removed, the Store is ", lof)
elif b == 3:
  print("  ")
  e = input("Which book do you want to find   ")
  print("It is in place ", lof.index(e) + 1)
  print(lof)
elif b == 4:
  print("  ")
  print("The list is ")
  for charecter in lof:
    print(charecter)
elif b == 5:
  print("  ")
  print("The number of books in the store is ", len(lof))
  print(lof)
elif b == 6:
  lof.sort()
  lof.reverse()
  print("  ")
  print("The reverse alphabetic order of the books is ", lof)
elif b == 7:
  lof.sort()
  print("  ")
  print("The alphabetic order of the books is ", lof)
elif b == 8:
  z = 1
  print("  ")
  print("The number of changes made to the store = ", a-1)
  print("The current store is = ", lof)
  a = 10
else:
  print("Sorry I cannot help you ")
  y = y + 1
if z == 0:
  print("  ")
  print("The number of changes made to the store = ", aa)
  print("The current store is = ", lof)
else:
  print("  ")
st = time.time()
dob = datetime.datetime(year, month, day)
today = datetime.datetime.now()
age = today - dob
a = datetime.timedelta(days = 365)
b = age/a
e = math.floor(b)
d = (b - e)*12
f = 18 - e
print("Your age is %d[years] %d[months]." %(b, d))
print("The no. of years left to get your license is :", f)
et = time.time()
i = et - st
print("The time taken for this program to run = %s[seconds]. " %(i))
print("  ")
print("I know ten things about you you you you you you you you you you you yoo you you you")
print("1. that you are a human")
print("2. that you are reading this")
print("4. you were to lazy to read all the ' you's ' ")
print("5. you didn't realize that there was a 'yoo' in it ")
print("6. you just looked back to see if there was a 'yoo")
print("6. you are laughing at this ")
print("7. you didn't realize that number 3. was missing")
print("8. you just looked back to see number 3")
print("9. you are laughing at this ")
print("10. you can't say the letter 'P' without putting your tongue in") 
time.sleep(2)
print("Put your tongue in you fool")
eti = datetime.datetime.now()
difse = sti - eti
print("The time it took for the program to run is", difse)