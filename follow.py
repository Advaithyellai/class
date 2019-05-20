import tkinter as tk
import time
# def callback(event):
#     x, y = event.x, event.y
#     print(x, y)
#     c.coords(rect, x - 10, y - 10, x + 10, y + 10)
root = tk.Tk()
# root.geometry('500x500')
# root.configure(bg='red')
# c = tk.Canvas(root, width = 1510, height = 200)
# rect = c.create_rectangle(0, 0, 0, 0, fill = 'blue')
# c.bind('<Motion>', callback)
# c.pack()
no = 0
n = 0.0
def fun():
    global no, n
    if no == 10:
        time.sleep(10)
        print(10/n)
        no = 0
    time.sleep(0.1)
    n+=0.1
    no += 1
b = tk.IntVar()
tk.Entry(root, text = b)
tk.Button(root, text = " Click Me ", command = fun,height = 5, width = 20).grid()
root.mainloop()