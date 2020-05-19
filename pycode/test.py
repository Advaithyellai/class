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

# print("task one")
# a = input("Text - ")
# b = list(a)
# e 
# print(b)
# for c in range(0, len(b)):
#     if d == 1:
#         if b[c] != ' ':
            
#     if b[c] == ' ':
#         d = 1

print("   ")
a = input("Text(no syntax) - ")
b = list(a)
d = ""
e = []
for ele in b:
    if ele == ' ':
        c = 1
if c == 0:
    a += ' '
    b = list(a)
    b[-1] = b[0]
    b.remove(b[0])
    c = ""
    for ele in b:
        c += ele
    c += "ay"
    print(c)
elif c == 1:
    for el in b:
        d += el
    d = d.split(' ')
    for elem in d:
        print(elem)
        elem += ' '
        f = list(elem)
        print(f)
        f[-1] = f[0]
        print(f)
        b.remove(b[0])
        print(f)
        h = ""
        for eleme in elem:
            h += eleme
            print(f)
        h += "ay "
        print(f)
        e.append(f)
        g = ""
        i = ""
        for elemen in e:
            for
            g += elemen
            print(g)
        print(g)
        exit()