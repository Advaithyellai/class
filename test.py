# a = int(input("Runs        - "))
# b = input("Overs       - ")
# e = int(input("Total overs - "))
# f = int(input("Wickets     - "))
# g = int(input("Target      - "))
# c = 0
# if "." in b:
#     c = 1
# b = b.split(".")
# if c == 0:
#     b.append('0')
# d = (a/int(b[0])+((int(b[1])/100*6)/10))
# if d/f*10 < e:
#     e = d/f*10
# print("run rate =", d)
# print("  ")
# print("projected score =", d*e)


# a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'\
#     ,'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
# b = input("number or word - ")
# if b == 'number':
#     c = input("number         - ")
#     c = c.split('2')
#     for d in c:
#         if d != '':
#             print(a[eval("0b0"+d)], end = "")
# elif b == 'word':
#     c = input("word           - ")
#     for d in c:
#         f = bin(a.index(d))
#         print(f[2:]+"2", end = "")


# import random
# import tkinter as tk
# root = tk.Tk()
# d = 0
# b = []
# f = ["arrow", "circle", "clock", "cross", "dotbox", "exchange", "fleur", "heart",\
#     "man", "mouse", "pirate", "plus", "shuttle", "sizing", "spider", "spraycan",\
#     "star", "target", "tcross", "trek", "watch"]
# while(d<4):
#     d += 1
#     a = ['blue', 'green', 'red', 'yellow']
#     c = a[random.randrange(0, 4)]
#     if c in b:
#         d -=1
#     else:
#         b.append(c)
#         e = f[random.randrange(0, len(f))]
#         tk.Label(root, text = c, cursor =e, bg = c).grid(row = d)
# root.mainloop()


import tkinter as tk
root = tk.Tk()
root.mainloop()