# import tkinter as tk
# import random
# import time
# root = tk.Tk()
# root.title('monopoly with CPU')
# def highestroll(event):
#     a = []
#     for loop1 in range(0, 4):
#         b = random.randrange(1, 6)
#         a.append(b)
#     D1.configure(text = a[0])
#     D2.configure(text = a[1])
#     D1.after(1000, func = R1.configure(text = "CPU's roll"))
#     D2.after(1000, func = D1.configure(text = a[2]))
#     D2.after(100, func = D2.configure(text = a[3]))
#     c = a[0] + a[1]
#     d = a[2] + a[3]
#     e = max(d, c)
#     if e == d:
#         R1.destroy
#         R2 = tk.Button(root, text = "Roll", height = 2, width = 15)
#         R2.grid(row = 2, column = 1)
#     else:
#         R1.destroy
#         R2 = tk.Button(root, text = "Roll", height = 2, width = 15)
#         R2.grid(row = 2, column = 1)
#         a = random.randrange(1, )
#     return
# a = random.randrange(1, 4)
# b = random.randrange(1, 4)
# while(a == b):
#       b = random.randrange(1, 4)
# c = ['blue', 'green', 'yellow', 'red']
# pl = c[a]
# cpu = c[b]
# lpl = tk.Label(root, text = "Your colour "+pl, bg = pl)
# lcl = tk.Label(root, text = "CPU's colour "+cpu, bg = cpu)
# tk.Label(root, text = " ").grid(row = 1, column = 1)
# lpl.grid(row = 4, column = 4)
# lcl.grid(row = 4, column = 5)
# D1 = tk.Label(root, text = 'dice 1', height = 6, width = 15, bg = 'black', fg = 'white', font=("Courier", 12))
# D2 = tk.Label(root, text = 'dice 2', height = 6, width = 15, bg = 'black', fg = 'white', font=("Courier", 12))
# R1 = tk.Button(root, text = "ROLL", height = 2, width = 15)
# lpl.after(4000, func = lpl.destroy)
# lcl.after(4000, func = lcl.destroy)
# D1.grid(row = 1, column = 1)
# D2.grid(row = 1, column = 2)
# R1.grid(row = 2, column = 1)
# R1.bind('<Button>', highestroll)
# root.mainloop()


# import tkinter as tk
# root = tk.Tk()
# import random
# def correct(event):
#     global guess
#     loop = 0
#     blank_2 = ""
#     if guess in listword:
#         for ele in listword:
#             if ele == guess:
#                 blank = blank.split(' ')
#                 blank[loop] = ele
#                 for ele_2 in blank:
#                     blank_2 += ele_2
#                     blank_2 += " "
#                 blank = blank_2
#                 blank_2 = ""
#             loop += 1
#     print(blank)
#     if '_' in blank:
#         guess = input("Guess again  ")
#     else:
#         print("Congrats")
# words = ['armadillo', 'beaver', 'chimpanzee', 'dolphin', 'earthworm', 'flamingo', 'gorilla', 'hippopotamus', 'iguana', 'jaguar', 'kingfisher', 'llama', 'mangoose', 'otter', 'possum', 'rhea', 'salmon', 'turkey', 'viper', 'woodpecker']
# word = words[random.randrange(0, len(words))]
# blank = ""
# listword = []
# for ele in word:
#     listword += ele
# blank += listword[0]
# for loop in range(0, len(word)-1):
#     blank = blank + " _"
# print(blank)
# guess = input(" ")
# root.mainloop()


# import tkinter as tk
# root = tk.Tk()
import random
print("WELCOME TO MY GAME OF HANGMAN! The rules are similar to hangman")
count = 0
def correct(guess, blank, count):
    loop = 0
    blank_2 = ""
    if guess in listword:
        for ele in listword:
            if ele == guess:
                blank = blank.split(' ')
                blank[loop] = ele
                for ele_2 in blank:
                    blank_2 += ele_2
                    blank_2 += " "
                blank = blank_2
                blank_2 = ""
            loop += 1
    print(blank)
    if '_' in blank:
        if guess in listword:
            if guess not in blank:
                print("you already guessed that")
                print("We will spare you and take away no tries")
            else:
                print("no")
        else:
            count += 1
        if count == 6:
            print("😭 😢 loser 😢 😭")
            print("word was", word)
            exit("😉 🌝 THANKS FOR PLAYING 🌝 😉")
        print("tries:", count)
        guess = input("Guess again  ")
        if guess == "":
            count = count - 1
        correct(guess, blank, count)
    else:
        print("Congrats")
        exit("😉 🌝 THANKS FOR PLAYING 🌝 😉")
        print("tries", count)
words = ['armadillo', 'beaver', 'chimpanzee', 'dolphin', 'earthworm', 'flamingo', 'gorilla', 'hedgehog', 'iguana', 'jaguar', 'kingfisher', 'llama', 'mangoose', 'otter', 'possum', 'rhea', 'salmon', 'turkey', 'vulture', 'woodpecker']
word = words[random.randrange(0, len(words))]
blank = ""
listword = []
for ele in word:
    listword += ele
blank += listword[0]
for loop in range(0, len(word)-1):
    blank = blank + " _"
print("tries:", count, ", if you have 6 tries you are out. BE WARNED!!!")
print(blank)
guess = input("guess ")
if guess == "":
    count = count - 1
correct(guess, blank, count)
# root.mainloop()