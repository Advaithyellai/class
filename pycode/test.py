import time
import tkinter as tk

# root = tk.Tk()
# root.geometry('1600x900')
# root.title("Dots and Boxes")
# To do: maze, clock, calendar, google, cleaner, notes, maps, contacts, ultimate banking [ listboxes ], mango tree

# root_2 = tk.Tk()
# def blehbleh(event):
#     C = tk.Canvas(root_2, height = 65, width = 110, bg = 'black')
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
# tk.Label(root, text = "Number(0-10)=").grid(row = 0, column = 0)
# a = tk.StringVar(root)
# b = tk.Spinbox(root, text = a, from_ = 0, to = 10)
# b.grid(row = 0, column = 1)
# b.bind('<Return>', blehbleh)
# root_2.mainloop()



# canvas = tk.Canvas(root)
# scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
# scrollable_frame = tk.Frame(canvas)
# scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
# canvas.create_window((0, 0), window=scrollable_frame, anchor = 'nw')
# canvas.configure(yscrollcommand=scrollbar.set)
# for i in range(50):
#     tk.Label(scrollable_frame, width = 20, text = "Label").grid()
# canvas.grid(row = 0, column = 0)
# scrollbar.grid(row = 0, column = 1, sticky = 'ns')

# class clock:
#     def __init__(self, root_2):
#         root_2.destroy()
#         root = tk.Tk()
#         tk.Button(root, text = " Alarm ", bg = '')
#         root.mainloop()
#     def timering(self):
#         pass
#     def alarming(self):
#         pass
#     def stopingwatch(self):
#         pass

# root_2 = tk.Tk()
# clock(root_2)
# root.mainloop()

b = 500
a = 500
e = 0
print("you should enter below 1000 and above 0")
print("if it takes me 11 tries to guess yvofejvioejou win and I will give 100 rs")
print("else you give me 10 rs")
c = int(input("What is your number  "))
if c > 0 and c < 1000:
    d = True
else:
    exit("You should enter below 1000 and above 0")
while d == True:
    e += 1
    if e == 11:
        exit("You beat me :(")
    if e == 1:
        if a > c:
            b = 0
        elif a < c:
            b = 500
            a = 1000
        else:
            d = False
    else:
        f = round((a+b)/2)
        if f > c:
            a = f
        elif f < c:
            b = f
        else:
            d = False
if a == c:
    print("It is {} I guessed in {} try / tries".format(a, e))
elif f == c:
    print("It is {} i guessed in {} try / tries".format(int(f), e))
elif b == c:
    print("It is {} I guessed in {} try / tries".format(b, e))
else:
    print("Sorry, some kind of error came")