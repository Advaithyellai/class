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


from tkinter import Tk, mainloop, TOP, Button
from time import time
root = Tk() 
def helloer():
    print("hello")
button = Button(root, text = 'Geeks', command = root.after(5000, root.destroy)) 
button.pack(side = TOP, pady = 5) 
button_2 = Button(root, text = "hello", command = helloer)
button_2.pack()
mainloop()