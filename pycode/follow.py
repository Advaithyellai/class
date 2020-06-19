import tkinter as tk
def callthiswhatevs(event):
    x, y = event.x, event.y
    c.coords(rect, x - 10, y - 10, x + 10, y + 10)
root = tk.Tk()
root.geometry('500x500')
c = tk.Canvas(root, width = 1600, height = 850, bg = 'black')
rect = c.create_rectangle(0, 0, 0, 0, fill = 'blue')
c.bind('<Motion>', callthiswhatevs)
c.grid()
root.mainloop()