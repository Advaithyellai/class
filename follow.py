import tkinter as tk
import time
def callback(event):
    x, y = event.x, event.y
    print(x, y)
    c.coords(rect, x - 10, y - 10, x + 10, y + 10)
root = tk.Tk()
root.geometry('500x500')
root.configure(bg='red')
c = tk.Canvas(root, width = 1510, height = 200)
rect = c.create_rectangle(0, 0, 0, 0, fill = 'blue')
c.bind('<Motion>', callback)
c.pack()
root.mainloop()