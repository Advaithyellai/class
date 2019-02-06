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
time.sleep(9)
print("Put your tongue in you fool")
eti = datetime.datetime.now()
difse = sti - eti
print("The time it took for the program to run is", difse)