# import tkinter as tk
# root_2 = tk.Tk()
# def blehbleh(event):
#     root = tk.Tk()
#     C = tk.Canvas(root, height = 65, width = 110, bg = 'black')
#     C.grid()
#     if a.get() == '0':
#         coords = [10, 10, 15, 15]
#         C.create_oval(coords, fill="red")
#     elif a.get() == '1':
#         coords = [10,10, 60,60]
#         C.create_oval(coords, fill="red")
#     elif a.get() == '2':
#         coords = [10, 10, 60, 60]
#         C.create_arc(coords, start=0, extent=180, fill="red")
#     elif a.get() == '3':
#         coords = [40,40, 20,20, 60,20, 40,40]
#         C.create_polygon(coords, fill = 'red')
#     elif a.get() == '4':
#         coords = [20,40, 20,10, 60,10, 60,40, 20,40]
#         C.create_polygon(coords, fill = 'red')
#     elif a.get() == '5':
#         coords = [10,30, 30,10, 50,30, 50,60, 10,60, 10,30]
#         C.create_polygon(coords, fill = 'red')
#     elif a.get() == '6':
#         coords = [20,10, 10,20, 20,30, 30,30, 40,20, 30,10, 20,10]
#         C.create_polygon(coords, fill = 'red')
#     elif a.get() == '7':
#         coords = [35,10, 20,20, 20,30, 30,40, 40,40, 50,30, 50,20, 35,10]
#         C.create_polygon(coords, fill = 'red')
#     elif a.get() == '8':
#         coords = [30,10, 20,20, 20,30, 30,40, 40,40, 50,30, 50,20, 40,10, 30,10]
#         C.create_polygon(coords, fill = 'red')
#     elif a.get() == '9':
#         coords = [25,5, 15,10, 8,20, 12,33, 20,40, 30,40, 38,33, 42,20, 35,10, 25,5]
#         C.create_polygon(coords, fill = 'red')
#     elif a.get() == '10':
#         coords = [20,5, 12,10, 8,20, 12,33, 20,40, 30,40, 38,33, 42,20, 38,10, 30,5, 20,5]
#         C.create_polygon(coords, fill = 'red')
#     else:
#         a.set('Error')
# tk.Label(root_2, text = "Number(0-10)=").grid(row = 0, column = 0)
# a = tk.StringVar()
# b = tk.Entry(root_2, text = a)
# b.grid(row = 0, column = 1)
# b.bind('<Return>', blehbleh)
# root_2.mainloop()



f = white = ['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']
d = orange = ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']
b = yellow = ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']
t = red = ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']
l = blue = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
r = green = ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']
print(" white = ", white,"\n red = ",  red,"\n yellow = ", yellow,"\n orange = ", orange,"\n blue = ", blue,"\n green = ", green, "\n you are facing -", f, "\n colour on top is - ", t)
a = "aa"
while a != "exit":
    a = str(input("move "))
    if a == "R":
        a, c, e = f[6], f[7], f[8]
        f[6], f[7], f[8] = d[2], d[1], d[0]
        d[0], d[1], d[2] = b[0], b[1], b[2]
        b[0], b[1], b[2] = t[8], t[7], t[6]
        t[6], t[7], t[8] = a, c, e
        g,h,i,j = r[0], r[1], r[5], r[3]
        r[0], r[1], r[5], r[3] = r[6], j, h, r[7]
        r[8], r[6], r[7], r[2] = r[2],r[8],i,g
        print(" white = ", white,"\n red = ",  red,"\n yellow = ", yellow,"\n orange = ", orange,"\n blue = ", blue,"\n green = ", green, "\n you are facing -", f, "\n colour on top is - ", t)
    elif a == "L":
        a, c, e = f[0], f[1], f[2]
        f[0], f[1], f[2] = t[0], t[1], t[2]
        t[0], t[1], t[2] = b[8], b[7], b[6]
        b[6], b[7], b[8] = d[6], d[7], d[8]
        d[6], d[7], d[8] = e, c, a
        g,h,i,j = l[0], l[1], l[5], l[3]
        l[0], l[1], l[5], l[3] = l[6], j, h, l[7]
        l[8], l[6], l[7], l[2] = l[2],l[8],i,g
        print(" white = ", white,"\n red = ",  red,"\n yellow = ", yellow,"\n orange = ", orange,"\n blue = ", blue,"\n green = ", green, "\n you are facing -", f, "\n colour on top is - ", t)
    elif a == "U":
        a, c, e = f[0], f[3], f[6]
        f[0], f[3], f[6] = r[2], r[1], r[0]
        r[0], r[1], r[2] = b[0], b[3], b[6]
        b[0], b[3], b[6] = l[6], l[7], l[8]
        l[6], l[7], l[8] = a, c, e
        g,h,i,j = l[0], l[1], l[5], l[3]
        t[0], t[1], t[5], t[3] = t[6], j, h, t[7]
        t[8], t[6], t[7], t[2] = t[2],t[8],i,g
        print(" white = ", white,"\n red = ",  red,"\n yellow = ", yellow,"\n orange = ", orange,"\n blue = ", blue,"\n green = ", green, "\n you are facing -", f, "\n colour on top is - ", t)
    elif a == "F":
        a, c, e = r[2], r[5], r[8]
        r[2], r[5], r[8] = t[2], t[5], t[8]
        t[2], t[5], t[8] = l[2], l[5], l[8]
        l[2], l[5], l[8] = d[2], d[5], d[8]
        d[2], d[5], d[8] = a, c, e
        g,h,i,j = l[0], l[1], l[5], l[3]
        l[0], l[1], l[5], l[3] = l[6], j, h, l[7]
        l[8], l[6], l[7], l[2] = r[2],r[8],i,g
        print(" white = ", white,"\n red = ",  red,"\n yellow = ", yellow,"\n orange = ", orange,"\n blue = ", blue,"\n green = ", green, "\n you are facing -", f, "\n colour on top is - ", t)
    elif a == "R'":
        a, c, e = f[6], f[7], f[8]
        f[6], f[7], f[8] = t[6], t[7], t[8]
        t[6], t[7], t[8] = b[2], b[1], b[0]
        b[0], b[1], b[2] = d[0], d[1], d[2]
        d[0], d[1], d[2] = e, c, a
        g,h,i,j = l[0], l[1], l[5], l[3]
        l[0], l[1], l[5], l[3] = l[6], j, h, l[7]
        l[8], l[6], l[7], l[2] = r[2],r[8],i,g
        g,h,i,j = l[0], l[1], l[5], l[3]
        l[0], l[1], l[5], l[3] = l[6], j, h, l[7]
        l[8], l[6], l[7], l[2] = r[2],r[8],i,g
        print(" white = ", white,"\n red = ",  red,"\n yellow = ", yellow,"\n orange = ", orange,"\n blue = ", blue,"\n green = ", green, "\n you are facing -", f, "\n colour on top is - ", t)
    elif a == "L'":
        a, c, e = f[0], f[1], f[2]
        f[0], f[1], f[2] = d[8], d[7], d[6]
        d[6], d[7], d[8] = b[8], b[7], b[6]
        b[6], b[7], b[8] = t[2], t[1], t[0]
        t[0], t[1], t[2] = a, c, e
        print(" white = ", white,"\n red = ",  red,"\n yellow = ", yellow,"\n orange = ", orange,"\n blue = ", blue,"\n green = ", green, "\n you are facing -", f, "\n colour on top is - ", t)
    elif a == "U'":
        a, c, e = f[0], f[3], f[6]
        f[0], f[3], f[6] = l[6], l[7], l[8]
        l[6], l[7], l[8] = b[0], b[3], b[6]
        b[0], b[3], b[6] = r[2], r[1], r[0]
        r[0], r[1], r[2] = e, c, a
        print(" white = ", white,"\n red = ",  red,"\n yellow = ", yellow,"\n orange = ", orange,"\n blue = ", blue,"\n green = ", green, "\n you are facing -" ,f, "\n colour on top is - ", t)
    elif a == "F'":
        a, c, e = r[2], r[5], r[8]
        r[2], r[5], r[8] = d[2], d[5], d[8]
        d[2], d[5], d[8] = l[2], l[5], l[8]
        l[2], l[5], l[8] = t[2], t[5], t[8]
        t[2], t[5], t[8] = a, c, e 
        print(" white = ", white,"\n red = ",  red,"\n yellow = ", yellow,"\n orange = ", orange,"\n blue = ", blue,"\n green = ", green, "\n you are facing -", f, "\n colour on top is - ", t)
    else:
        print("error")