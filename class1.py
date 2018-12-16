# w, x, y, z, aa, ab... are known as variables. Variables are storages of something. If int is there it means that the storage                             is an integer. Else it is 
# a string. What ever is in the double quotes is going to be printed.
w = int(input("type your height             "))
x = int(input("type you weight              "))
y = int(input("type your age                "))
z = input("write a word                   ")
aa = input("type your name                 ")
ab = input("what is your favourite place   ")
ac = int((w+x)/y)
ad = int(input("type a number                  "))
ae = int(input("type another number            "))
bb = len(z)
# The command 'print' is for the computer to know that the things inside the brackets are going to be seen in the output. The things inside the double quotes are going to come as it
# is. But the things outside the double quotes are variables or numbers.
print("   ")
print("hi," + aa)
print("The length of your word, " + z +" is "+ str(len(z)) + " lettters long")
print("Your bmi = " + str(ac-1))
print("Oh your favourite place is " + ab + ", my favourite place is himalayas")
print("  ")
print("the sum of the 2 numbers is " + str(ad+ae))
print("the difference between the two numbers is " + str(ad-ae))
print("the quotient of the 2 numbers is " + str(ad/ae))
print("the product of the 2 numbes is " + str(ad*ae))
print("the average the two numbers is " + str((ad+ae)/2))
# If you want to see the output go to the left corner where "Type here to search" is there. Then type "Command Prompt" and when you see command prompt open it.
#  Then type Desktop\class1.py 