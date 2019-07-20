# import tkinter as tk
# import time
# st = ''
# root = tk.Tk()
# a = tk.Label(root)
# a.grid()
# def newvsold():
#     global st
#     et = time.strftime("%d - %m - %Y   %H : %M : %S")
#     if et != st:
#         st = et
#         a.configure(text = st)
#     a.after(900, newvsold)
# newvsold()
# root.mainloop()
import tkinter as tk
import time
def callback(event):
    x, y = event.x, event.y
    c.coords(rect, x - 10, y - 10, x + 10, y + 10)
root = tk.Tk()
root.configure(bg='red')
c = tk.Canvas(root, width = 1510, height = 700)
rect = c.create_rectangle(0, 0, 0, 0, fill = 'blue')
c.bind('<Motion>', callback)
c.pack()
root.mainloop()