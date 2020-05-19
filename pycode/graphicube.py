# f = black = ['black0', 'black1', 'black2', 'black3', 'black4', 'black5', 'black6', 'black7', 'black8']
# d = orange = ['orange0', 'orange1', 'orange2', 'orange3', 'orange4', 'orange5', 'orange6', 'orange7', 'orange8']
# b = yellow = ['yellow0', 'yellow1', 'yellow2', 'yellow3', 'yellow4', 'yellow5', 'yellow6', 'yellow7', 'yellow8']
# t = red = ['red0', 'red1', 'red2', 'red3', 'red4', 'red5', 'red6', 'red7', 'red8']
# l = blue = ['blue0', 'blue1', 'blue2', 'blue3', 'blue4', 'blue5', 'blue6', 'blue7', 'blue8']
# r = green = ['green0', 'green1', 'green2', 'green3', 'green4', 'green5', 'green6', 'green7', 'green8']
# print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
# a = "aa"
# while a != "exit":
#     a = str(input("move =  "))
#     if a == "R":
#         g, c, e = f[6], f[7], f[8]
#         f[6], f[7], f[8] = d[2], d[1], d[0]
#         d[0], d[1], d[2] = b[0], b[1], b[2]
#         b[0], b[1], b[2] = t[8], t[7], t[6]
#         t[6], t[7], t[8] = g, c, e
#         h, i, j, k = r[0], r[7], r[8], r[1]
#         r[0], r[7], r[8], r[1] = r[2], r[3], r[6], r[5]
#         r[6], r[3], r[2], r[5] = h, k, j, i
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "R'":
#         g, c, e = f[6], f[7], f[8]
#         f[6], f[7], f[8] = t[6], t[7], t[8]
#         t[6], t[7], t[8] = b[2], b[1], b[0]
#         b[0], b[1], b[2] = d[0], d[1], d[2]
#         d[0], d[1], d[2] = e, c, g
#         k,h,i,j = r[6], r[5], r[2], r[3]
#         r[6], r[5], r[2], r[3] = r[8], r[1], r[0], r[7]
#         r[0], r[1], r[7], r[8] = k, j, h, i
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "L":
#         g, c, e = f[0], f[1], f[2]
#         f[0], f[1], f[2] = t[0], t[1], t[2]
#         t[0], t[1], t[2] = b[8], b[7], b[6]
#         b[6], b[7], b[8] = d[6], d[7], d[8]
#         d[6], d[7], d[8] = e, c, g
#         h, i, j, k = l[0], l[7], l[8], l[1]
#         l[0], l[7], l[8], l[1] = l[2], l[3], l[6], l[5]
#         l[6], l[3], l[2], l[5] = h, k, j, i
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "L'":
#         g, c, e = f[0], f[1], f[2]
#         f[0], f[1], f[2] = d[8], d[7], d[6]
#         d[6], d[7], d[8] = b[8], b[7], b[6]
#         b[6], b[7], b[8] = t[2], t[1], t[0]
#         t[0], t[1], t[2] = g, c, e
#         k,h,i,j = l[6], l[5], l[2], l[3]
#         l[6], l[5], l[2], l[3] = l[8], l[1], l[0], l[7]
#         l[0], l[1], l[7], l[8] = k, j, h, i
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "U":
#         g, c, e = f[0], f[3], f[6]
#         f[0], f[3], f[6] = r[2], r[1], r[0]
#         r[0], r[1], r[2] = b[6], b[3], b[0]
#         b[0], b[3], b[6] = l[6], l[7], l[8]
#         l[6], l[7], l[8] = g, c, e
#         h, i, j, k = t[0], t[7], t[8], t[1]
#         t[0], t[7], t[8], t[1] = t[2], t[3], t[6], t[5]
#         t[6], t[3], t[2], t[5] = h, k, j, i
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "U'":
#         g, c, e = f[0], f[3], f[6]
#         f[0], f[3], f[6] = l[6], l[7], l[8]
#         l[6], l[7], l[8] = b[0], b[3], b[6]
#         b[0], b[3], b[6] = r[2], r[1], r[0]
#         r[0], r[1], r[2] = e, c, g
#         k,h,i,j = t[6], t[5], t[2], t[3]
#         t[6], t[5], t[2], t[3] = t[8], t[1], t[0], t[7]
#         t[0], t[1], t[7], t[8] = k, j, h, i
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -" ,f, "\ncolour on top is - ", t)
#     elif a == "D":
#         g, c, e = f[2], f[5], f[8]
#         f[2], f[5], f[8] = r[8], r[7], r[6]
#         r[6], r[7], r[8] = b[8], b[5], b[2]
#         b[2], b[5], b[8] = l[0], l[1], l[2]
#         l[0], l[1], l[2] = g, c, e
#         h, i, j, k = d[0], d[7], d[8], d[1]
#         d[0], d[7], d[8], d[1] = d[2], d[3], d[6], d[5]
#         d[6], d[3], d[2], d[5] = h, k, j, i
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "D'":
#         g, c, e = f[2], f[5], f[8]
#         f[2], f[5], f[8] = l[0], l[1], l[2]
#         l[0], l[1], l[2] = b[8], b[5], b[2]
#         b[2], b[5], b[8] = r[6], r[7], r[8]
#         r[6], r[7], r[8] = g, c, e
#         k,h,i,j = d[6], d[5], d[2], d[3]
#         d[6], d[5], d[2], d[3] = d[8], d[1], d[0], d[7]
#         d[0], d[1], d[7], d[8] = k, j, h, i
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "F":
#         g, c, e = r[2], r[5], r[8]
#         r[2], r[5], r[8] = t[2], t[5], t[8]
#         t[2], t[5], t[8] = l[2], l[5], l[8]
#         l[2], l[5], l[8] = d[2], d[5], d[8]
#         d[2], d[5], d[8] = g, c, e
#         h, i, j, k = f[0], f[7], f[8], f[1]
#         f[0], f[7], f[8], f[1] = f[2], f[3], f[6], f[5]
#         f[6], f[3], f[2], f[5] = h, k, j, i
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "F'":
#         g, c, e = r[2], r[5], r[8]
#         r[2], r[5], r[8] = d[2], d[5], d[8]
#         d[2], d[5], d[8] = l[2], l[5], l[8]
#         l[2], l[5], l[8] = t[2], t[5], t[8]
#         t[2], t[5], t[8] = g, c, e 
#         k,h,i,j = f[6], f[5], f[2], f[3]
#         f[6], f[5], f[2], f[3] = f[8], f[1], f[0], f[7]
#         f[0], f[1], f[7], f[8] = k, j, h, i
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "B":
#         g, c, e = r[0], r[3], r[6]
#         r[0], r[3], r[6] = t[0], t[3], t[6]
#         t[0], t[3], t[6] = l[0], l[3], l[6]
#         l[0], l[3], l[6] = d[0], d[3], d[6]
#         d[0], d[3], d[6] = g, c, e
#         h, i, j, k = b[0], b[7], b[8], b[1]
#         b[0], b[7], b[8], b[1] = b[2], b[3], b[6], b[5]
#         b[6], b[3], b[2], b[5] = h, k, j, i
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "B'":
#         g, c, e = r[0], r[3], r[6]
#         r[0], r[3], r[6] = d[0], d[3], d[6]
#         d[0], d[3], d[6] = l[0], l[3], l[6]
#         l[0], l[3], l[6] = t[0], t[3], t[6]
#         t[0], t[3], t[6] = g, c, e
#         k,h,i,j = b[6], b[5], b[2], b[3]
#         b[6], b[5], b[2], b[3] = b[8], b[1], b[0], b[7]
#         b[0], b[1], b[7], b[8] = k, j, h, i
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "M":
#         g, c, e = f[3], f[4], f[5]
#         f[3], f[4], f[5] = t[3], t[4], t[5]
#         t[3], t[4], t[5] = b[5], b[4], b[3]
#         b[5], b[4], b[3] = d[5], d[4], d[3]
#         d[5], d[4], d[3] = g, c, e
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "M'":
#         g, c, e = f[3], f[4], f[5]
#         f[3], f[4], f[5] = d[5], d[4], d[3]
#         d[5], d[4], d[3] = b[5], b[4], b[3]
#         b[5], b[4], b[3] = t[3], t[4], t[5]
#         t[6], t[7], t[8] = g, c, e
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "S":
#         g, c, e = r[1], r[4], r[7]
#         r[1], r[4], r[7] = t[1], t[4], t[7]
#         t[1], t[4], t[7] = l[1], l[4], l[7]
#         l[1], l[4], l[7] = d[1], d[4], d[7]
#         d[1], d[4], d[7] = g, c, e
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "S'":
#         g, c, e = r[1], r[4], r[7]
#         r[1], r[4], r[7] = d[1], d[4], d[7]
#         d[1], d[4], d[7] = l[1], l[4], l[7]
#         l[1], l[4], l[7] = t[1], t[4], t[7]
#         t[1], t[4], t[7] = g, c, e
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "E":
#         g, c, e = f[1], f[4], f[7]
#         f[1], f[4], f[7] = r[5], r[4], r[3]
#         r[3], r[4], r[5] = b[1], b[4], b[7]
#         b[1], b[4], b[7] = l[5], l[4], l[3]
#         l[3], l[4], l[5] = e, c, g
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "E'":
#         g, c, e = f[1], f[4], f[7]
#         f[1], f[4], f[7] = l[3], l[4], l[5]
#         l[3], l[4], l[5] = b[1], b[4], b[7]
#         b[1], b[4], b[7] = r[5], r[4], r[3]
#         r[5], r[4], r[3] = e, c, g
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "X":
#         h, i, j, k = r[0], r[7], r[8], r[1]
#         r[0], r[7], r[8], r[1] = r[2], r[3], r[6], r[5]
#         r[6], r[3], r[2], r[5] = h, k, j, i
#         k,h,i,j = l[6], l[5], l[2], l[3]
#         l[6], l[5], l[2], l[3] = l[8], l[1], l[0], l[7]
#         l[0], l[1], l[7], l[8] = k, j, h, i
#         k, f, t, b, d = f, t, b, d, k
#     elif a == "X'":
#         h, i, j, k = l[0], l[7], l[8], l[1]
#         l[0], l[7], l[8], l[1] = l[2], l[3], l[6], l[5]
#         l[6], l[3], l[2], l[5] = h, k, j, i
#         k,h,i,j = r[6], r[5], r[2], r[3]
#         r[6], r[5], r[2], r[3] = r[8], r[1], r[0], r[7]
#         r[0], r[1], r[7], r[8] = k, j, h, i
#         k, f, d, b, t = f, d, b, t, k
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "Y":
#         pass
#     elif a == "Y'":
#         pass
#     elif a == "Z":
#         h, i, j, k = b[0], b[7], b[8], b[1]
#         b[0], b[7], b[8], b[1] = b[2], b[3], b[6], b[5]
#         b[6], b[3], b[2], b[5] = h, k, j, i
#         h, i, j, k = f[0], f[7], f[8], f[1]
#         f[0], f[7], f[8], f[1] = f[2], f[3], f[6], f[5]
#         f[6], f[3], f[2], f[5] = h, k, j, i
#         k, t, r, d, l = t, r, d, l, k
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "Z'":
#         k,h,i,j = b[6], b[5], b[2], b[3]
#         b[6], b[5], b[2], b[3] = b[8], b[1], b[0], b[7]
#         b[0], b[1], b[7], b[8] = k, j, h, i
#         h, i, j, k = f[0], f[7], f[8], f[1]
#         f[0], f[7], f[8], f[1] = f[2], f[3], f[6], f[5]
#         f[6], f[3], f[2], f[5] = h, k, j, i
#         k, t, l, d, r = t, l, d, r, k
#         print(" black = ", black,"\nred = ",  red,"\nyellow = ", yellow,"\norange = ", orange,"\nblue = ", blue,"\ngreen = ", green, "\nyou are facing -", f, "\ncolour on top is - ", t)
#     elif a == "exit":
#        exit()


import random
import time
import tkinter as tk
root = tk.Tk()
def entering(move):
    global f, t, r, l, d, b
    z = -1
    if move == "R":
        g, c, e = f[6], f[7], f[8]
        f[6], f[7], f[8] = d[2], d[1], d[0]
        d[0], d[1], d[2] = b[0], b[1], b[2]
        b[0], b[1], b[2] = t[8], t[7], t[6]
        t[6], t[7], t[8] = g, c, e
        h, i, j, k = r[0], r[7], r[8], r[1]
        r[0], r[7], r[8], r[1] = r[2], r[3], r[6], r[5]
        r[6], r[3], r[2], r[5] = h, k, j, i
        for x in range(1, 4):
            for y in range(0, 3):
                z+=1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "R'":
        g, c, e = f[6], f[7], f[8]
        f[6], f[7], f[8] = t[6], t[7], t[8]
        t[6], t[7], t[8] = b[2], b[1], b[0]
        b[0], b[1], b[2] = d[0], d[1], d[2]
        d[0], d[1], d[2] = e, c, g
        k,h,i,j = r[6], r[5], r[2], r[3]
        r[6], r[5], r[2], r[3] = r[8], r[1], r[0], r[7]
        r[0], r[1], r[7], r[8] = k, j, h, i
        for x in range(1, 4):
            for y in range(0, 3):
                z+=1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "L":
        g, c, e = f[0], f[1], f[2]
        f[0], f[1], f[2] = t[0], t[1], t[2]
        t[0], t[1], t[2] = b[8], b[7], b[6]
        b[6], b[7], b[8] = d[6], d[7], d[8]
        d[6], d[7], d[8] = e, c, g
        h, i, j, k = l[0], l[7], l[8], l[1]
        l[0], l[7], l[8], l[1] = l[2], l[3], l[6], l[5]
        l[6], l[3], l[2], l[5] = h, k, j, i
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "L'":
        g, c, e = f[0], f[1], f[2]
        f[0], f[1], f[2] = d[8], d[7], d[6]
        d[6], d[7], d[8] = b[8], b[7], b[6]
        b[6], b[7], b[8] = t[2], t[1], t[0]
        t[0], t[1], t[2] = g, c, e
        k,h,i,j = l[6], l[5], l[2], l[3]
        l[6], l[5], l[2], l[3] = l[8], l[1], l[0], l[7]
        l[0], l[1], l[7], l[8] = k, j, h, i
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "U":
        g, c, e = f[0], f[3], f[6]
        f[0], f[3], f[6] = r[2], r[1], r[0]
        r[0], r[1], r[2] = b[6], b[3], b[0]
        b[0], b[3], b[6] = l[6], l[7], l[8]
        l[6], l[7], l[8] = g, c, e
        h, i, j, k = t[0], t[7], t[8], t[1]
        t[0], t[7], t[8], t[1] = t[2], t[3], t[6], t[5]
        t[6], t[3], t[2], t[5] = h, k, j, i
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "U'":
        g, c, e = f[0], f[3], f[6]
        f[0], f[3], f[6] = l[6], l[7], l[8]
        l[6], l[7], l[8] = b[0], b[3], b[6]
        b[0], b[3], b[6] = r[2], r[1], r[0]
        r[0], r[1], r[2] = e, c, g
        k,h,i,j = t[6], t[5], t[2], t[3]
        t[6], t[5], t[2], t[3] = t[8], t[1], t[0], t[7]
        t[0], t[1], t[7], t[8] = k, j, h, i
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "D":
        g, c, e = f[2], f[5], f[8]
        f[2], f[5], f[8] = l[0], l[1], l[2]
        l[0], l[1], l[2] = b[8], b[5], b[2]
        b[2], b[5], b[8] = r[6], r[7], r[8]
        r[6], r[7], r[8] = g, c, e
        k,h,i,j = d[6], d[5], d[2], d[3]
        d[6], d[5], d[2], d[3] = d[8], d[1], d[0], d[7]
        d[0], d[1], d[7], d[8] = k, j, h, i
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "D'":
        g, c, e = f[2], f[5], f[8]
        f[2], f[5], f[8] = r[8], r[7], r[6]
        r[6], r[7], r[8] = b[8], b[5], b[2]
        b[2], b[5], b[8] = l[0], l[1], l[2]
        l[0], l[1], l[2] = g, c, e
        h, i, j, k = d[0], d[7], d[8], d[1]
        d[0], d[7], d[8], d[1] = d[2], d[3], d[6], d[5]
        d[6], d[3], d[2], d[5] = h, k, j, i
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "F":
        g, c, e = r[2], r[5], r[8]
        r[2], r[5], r[8] = t[2], t[5], t[8]
        t[2], t[5], t[8] = l[2], l[5], l[8]
        l[2], l[5], l[8] = d[2], d[5], d[8]
        d[2], d[5], d[8] = g, c, e
        h, i, j, k = f[0], f[7], f[8], f[1]
        f[0], f[7], f[8], f[1] = f[2], f[3], f[6], f[5]
        f[6], f[3], f[2], f[5] = h, k, j, i
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "F'":
        g, c, e = r[2], r[5], r[8]
        r[2], r[5], r[8] = d[2], d[5], d[8]
        d[2], d[5], d[8] = l[2], l[5], l[8]
        l[2], l[5], l[8] = t[2], t[5], t[8]
        t[2], t[5], t[8] = g, c, e 
        k,h,i,j = f[6], f[5], f[2], f[3]
        f[6], f[5], f[2], f[3] = f[8], f[1], f[0], f[7]
        f[0], f[1], f[7], f[8] = k, j, h, i
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "B":
        g, c, e = r[0], r[3], r[6]
        r[0], r[3], r[6] = t[0], t[3], t[6]
        t[0], t[3], t[6] = l[0], l[3], l[6]
        l[0], l[3], l[6] = d[0], d[3], d[6]
        d[0], d[3], d[6] = g, c, e
        h, i, j, k = b[0], b[7], b[8], b[1]
        b[0], b[7], b[8], b[1] = b[2], b[3], b[6], b[5]
        b[6], b[3], b[2], b[5] = h, k, j, i
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "B'":
        g, c, e = r[0], r[3], r[6]
        r[0], r[3], r[6] = d[0], d[3], d[6]
        d[0], d[3], d[6] = l[0], l[3], l[6]
        l[0], l[3], l[6] = t[0], t[3], t[6]
        t[0], t[3], t[6] = g, c, e
        k,h,i,j = b[6], b[5], b[2], b[3]
        b[6], b[5], b[2], b[3] = b[8], b[1], b[0], b[7]
        b[0], b[1], b[7], b[8] = k, j, h, i
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "M":
        g, c, e = f[3], f[4], f[5]
        f[3], f[4], f[5] = t[3], t[4], t[5]
        t[3], t[4], t[5] = b[5], b[4], b[3]
        b[5], b[4], b[3] = d[5], d[4], d[3]
        d[5], d[4], d[3] = g, c, e
        a.configure(text = "facing - {}".format(f[4]), fg = f[4], bg = t[4])
        s.configure(text = "on top - {}".format(t[4]), fg = t[4], bg = f[4])
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "M'":
        g, c, e = f[3], f[4], f[5]
        f[3], f[4], f[5] = d[5], d[4], d[3]
        d[5], d[4], d[3] = b[5], b[4], b[3]
        b[5], b[4], b[3] = t[3], t[4], t[5]
        t[3], t[4], t[5] = g, c, e
        a.configure(text = "facing - {}".format(f[4]), fg = f[4], bg = t[4])
        s.configure(text = "on top - {}".format(t[4]), fg = t[4], bg = f[4])
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "S":
        g, c, e = r[1], r[4], r[7]
        r[1], r[4], r[7] = t[1], t[4], t[7]
        t[1], t[4], t[7] = l[1], l[4], l[7]
        l[1], l[4], l[7] = d[1], d[4], d[7]
        d[1], d[4], d[7] = g, c, e
        a.configure(bg = t[4])
        s.configure(text = "on top - {}".format(t[4]), fg = t[4], bg = f[4])
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "S'":
        g, c, e = r[1], r[4], r[7]
        r[1], r[4], r[7] = d[1], d[4], d[7]
        d[1], d[4], d[7] = l[1], l[4], l[7]
        l[1], l[4], l[7] = t[1], t[4], t[7]
        t[1], t[4], t[7] = g, c, e
        a.configure(bg = t[4])
        s.configure(text = "on top - {}".format(t[4]), fg = t[4], bg = f[4])
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "E":
        g, c, e = f[1], f[4], f[7]
        f[1], f[4], f[7] = l[5], l[4], l[3]
        l[5], l[4], l[3] = b[1], b[4], b[7]
        b[1], b[4], b[7] = r[5], r[4], r[3]
        r[5], r[4], r[3] = e, c, g
        a.configure(text = "facing - {}".format(f[4]), fg = f[4], bg = t[4])
        s.configure(bg = f[4])
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "E'":
        g, c, e = f[1], f[4], f[7]
        f[1], f[4], f[7] = r[5], r[4], r[3]
        r[5], r[4], r[3] = b[1], b[4], b[7]
        b[1], b[4], b[7] = l[3], l[4], l[5]
        l[3], l[4], l[5] = e, c, g
        a.configure(text = "facing - {}".format(f[4]), fg = f[4], bg = t[4])
        s.configure(bg = f[4])
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "X":
        g, c, e = f[3], f[4], f[5]
        f[3], f[4], f[5] = d[5], d[4], d[3]
        d[5], d[4], d[3] = b[5], b[4], b[3]
        b[5], b[4], b[3] = t[3], t[4], t[5]
        t[3], t[4], t[5] = g, c, e
        g, c, e = f[6], f[7], f[8]
        f[6], f[7], f[8] = d[2], d[1], d[0]
        d[0], d[1], d[2] = b[0], b[1], b[2]
        b[0], b[1], b[2] = t[8], t[7], t[6]
        t[6], t[7], t[8] = g, c, e
        h, i, j, k = r[0], r[7], r[8], r[1]
        r[0], r[7], r[8], r[1] = r[2], r[3], r[6], r[5]
        r[6], r[3], r[2], r[5] = h, k, j, i
        g, c, e = f[0], f[1], f[2]
        f[0], f[1], f[2] = d[8], d[7], d[6]
        d[6], d[7], d[8] = b[8], b[7], b[6]
        b[6], b[7], b[8] = t[2], t[1], t[0]
        t[0], t[1], t[2] = g, c, e
        k,h,i,j = l[6], l[5], l[2], l[3]
        l[6], l[5], l[2], l[3] = l[8], l[1], l[0], l[7]
        l[0], l[1], l[7], l[8] = k, j, h, i
        a.configure(text = "facing - {}".format(f[4]), fg = f[4], bg = t[4])
        s.configure(text = "on top - {}".format(t[4]), fg = t[4], bg = f[4])
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "X'":
        g, c, e = f[6], f[7], f[8]
        f[6], f[7], f[8] = t[6], t[7], t[8]
        t[6], t[7], t[8] = b[2], b[1], b[0]
        b[0], b[1], b[2] = d[0], d[1], d[2]
        d[0], d[1], d[2] = e, c, g
        k,h,i,j = r[6], r[5], r[2], r[3]
        r[6], r[5], r[2], r[3] = r[8], r[1], r[0], r[7]
        r[0], r[1], r[7], r[8] = k, j, h, i
        g, c, e = f[0], f[1], f[2]
        f[0], f[1], f[2] = t[0], t[1], t[2]
        t[0], t[1], t[2] = b[8], b[7], b[6]
        b[6], b[7], b[8] = d[6], d[7], d[8]
        d[6], d[7], d[8] = e, c, g
        h, i, j, k = l[0], l[7], l[8], l[1]
        l[0], l[7], l[8], l[1] = l[2], l[3], l[6], l[5]
        l[6], l[3], l[2], l[5] = h, k, j, i
        g, c, e = f[3], f[4], f[5]
        f[3], f[4], f[5] = t[3], t[4], t[5]
        t[3], t[4], t[5] = b[5], b[4], b[3]
        b[5], b[4], b[3] = d[5], d[4], d[3]
        d[5], d[4], d[3] = g, c, e
        a.configure(text = "facing - {}".format(f[4]), fg = f[4], bg = t[4])
        s.configure(text = "on top - {}".format(t[4]), fg = t[4], bg = f[4])
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "Y":
        g, c, e = f[1], f[4], f[7]
        f[1], f[4], f[7] = r[5], r[4], r[3]
        r[5], r[4], r[3] = b[1], b[4], b[7]
        b[1], b[4], b[7] = l[3], l[4], l[5]
        l[3], l[4], l[5] = e, c, g
        g, c, e = f[2], f[5], f[8]
        f[2], f[5], f[8] = r[8], r[7], r[6]
        r[6], r[7], r[8] = b[8], b[5], b[2]
        b[2], b[5], b[8] = l[0], l[1], l[2]
        l[0], l[1], l[2] = g, c, e
        h, i, j, k = d[0], d[7], d[8], d[1]
        d[0], d[7], d[8], d[1] = d[2], d[3], d[6], d[5]
        d[6], d[3], d[2], d[5] = h, k, j, i
        g, c, e = f[0], f[3], f[6]
        f[0], f[3], f[6] = r[2], r[1], r[0]
        r[0], r[1], r[2] = b[6], b[3], b[0]
        b[0], b[3], b[6] = l[6], l[7], l[8]
        l[6], l[7], l[8] = g, c, e
        h, i, j, k = t[0], t[7], t[8], t[1]
        t[0], t[7], t[8], t[1] = t[2], t[3], t[6], t[5]
        t[6], t[3], t[2], t[5] = h, k, j, i
        a.configure(text = "facing - {}".format(f[4]), fg = f[4], bg = t[4])
        s.configure(text = "on top - {}".format(t[4]), fg = t[4], bg = f[4])
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "Y'":
        g, c, e = f[2], f[5], f[8]
        f[2], f[5], f[8] = l[0], l[1], l[2]
        l[0], l[1], l[2] = b[8], b[5], b[2]
        b[2], b[5], b[8] = r[6], r[7], r[8]
        r[6], r[7], r[8] = g, c, e
        k,h,i,j = d[6], d[5], d[2], d[3]
        d[6], d[5], d[2], d[3] = d[8], d[1], d[0], d[7]
        d[0], d[1], d[7], d[8] = k, j, h, i
        g, c, e = f[0], f[3], f[6]
        f[0], f[3], f[6] = l[6], l[7], l[8]
        l[6], l[7], l[8] = b[0], b[3], b[6]
        b[0], b[3], b[6] = r[2], r[1], r[0]
        r[0], r[1], r[2] = e, c, g
        k,h,i,j = t[6], t[5], t[2], t[3]
        t[6], t[5], t[2], t[3] = t[8], t[1], t[0], t[7]
        t[0], t[1], t[7], t[8] = k, j, h, i
        g, c, e = f[1], f[4], f[7]
        f[1], f[4], f[7] = l[5], l[4], l[3]
        l[5], l[4], l[3] = b[1], b[4], b[7]
        b[1], b[4], b[7] = r[5], r[4], r[3]
        r[5], r[4], r[3] = e, c, g
        a.configure(text = "facing - {}".format(f[4]), fg = f[4], bg = t[4])
        s.configure(text = "on top - {}".format(t[4]), fg = t[4], bg = f[4])
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "Z":
        g, c, e = r[0], r[3], r[6]
        r[0], r[3], r[6] = d[0], d[3], d[6]
        d[0], d[3], d[6] = l[0], l[3], l[6]
        l[0], l[3], l[6] = t[0], t[3], t[6]
        t[0], t[3], t[6] = g, c, e
        k,h,i,j = b[6], b[5], b[2], b[3]
        b[6], b[5], b[2], b[3] = b[8], b[1], b[0], b[7]
        b[0], b[1], b[7], b[8] = k, j, h, i
        g, c, e = r[2], r[5], r[8]
        r[2], r[5], r[8] = t[2], t[5], t[8]
        t[2], t[5], t[8] = l[2], l[5], l[8]
        l[2], l[5], l[8] = d[2], d[5], d[8]
        d[2], d[5], d[8] = g, c, e
        h, i, j, k = f[0], f[7], f[8], f[1]
        f[0], f[7], f[8], f[1] = f[2], f[3], f[6], f[5]
        f[6], f[3], f[2], f[5] = h, k, j, i
        g, c, e = r[1], r[4], r[7]
        r[1], r[4], r[7] = t[1], t[4], t[7]
        t[1], t[4], t[7] = l[1], l[4], l[7]
        l[1], l[4], l[7] = d[1], d[4], d[7]
        d[1], d[4], d[7] = g, c, e
        a.configure(bg = t[4])
        s.configure(text = "on top - {}".format(t[4]), fg = t[4], bg = f[4])
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "Z'":
        g, c, e = r[0], r[3], r[6]
        r[0], r[3], r[6] = t[0], t[3], t[6]
        t[0], t[3], t[6] = l[0], l[3], l[6]
        l[0], l[3], l[6] = d[0], d[3], d[6]
        d[0], d[3], d[6] = g, c, e
        h, i, j, k = b[0], b[7], b[8], b[1]
        b[0], b[7], b[8], b[1] = b[2], b[3], b[6], b[5]
        b[6], b[3], b[2], b[5] = h, k, j, i
        g, c, e = r[1], r[4], r[7]
        r[1], r[4], r[7] = d[1], d[4], d[7]
        d[1], d[4], d[7] = l[1], l[4], l[7]
        l[1], l[4], l[7] = t[1], t[4], t[7]
        t[1], t[4], t[7] = g, c, e
        g, c, e = r[2], r[5], r[8]
        r[2], r[5], r[8] = d[2], d[5], d[8]
        d[2], d[5], d[8] = l[2], l[5], l[8]
        l[2], l[5], l[8] = t[2], t[5], t[8]
        t[2], t[5], t[8] = g, c, e 
        k,h,i,j = f[6], f[5], f[2], f[3]
        f[6], f[5], f[2], f[3] = f[8], f[1], f[0], f[7]
        f[0], f[1], f[7], f[8] = k, j, h, i
        a.configure(text = "facing - {}".format(f[4]), fg = f[4], bg = t[4])
        s.configure(text = "on top - {}".format(t[4]), fg = t[4], bg = f[4])
        for x in range(1, 4):
            for y in range(0, 3):
                z += 1
                tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
    elif move == "exit":
       exit()
def returning(event):
    entering(w.get())
    w.set('')
def algorithming(event):
    w.set('')
def shufling(event):
    p = ["R", "R'", "L", "L'", "U", "U'", "D", "D'", "F", "F'", "B", "B'", "M", "M'", "E", "E'", "S", "S'"]
    for o in range(0, 15):
        n = random.randrange(0, len(p))
        entering(p[n])
        time.sleep(1)
f = black = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
d = orange = ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']
b = yellow = ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']
t = red = ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']
l = blue = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
r = green = ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']
z = -1
for x in range(1, 4):
    for y in range(0, 3):
        z += 1
        tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge").grid(row = y, column = x)
tk.Label(root, text = "move = ").grid(row = 0, column = 0)
w = tk.StringVar()
ac = tk.Entry(root, text = w)
ac.grid(row = 1, column = 0)
tk.Label(root, text = "algorithm = ").grid(row = 2, column = 0)
ab = tk.Entry(root)
ab.grid(row = 3, column = 0)
a = tk.Label(root, text = "facing - black", fg = 'black', bg = 'red')
a.grid(row = 4, column = 0)
s = tk.Label(root, text = "on top - red", fg = 'red', bg = 'black')
s.grid(row = 5, column = 0)
ab.bind("<Return>", algorithming)
ac.bind("<Return>", returning)
q = tk.Button(root, text = "Shuffle", bg = t[4], fg = 'black')
q.grid(row = 6, column = 0)
q.bind("<Button>", shufling)
root.mainloop()