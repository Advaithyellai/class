# import tkinter as tk
# import random
# def callthiswhatevs(event):
#     if 'Motion' in str(event):
#         x, y = event.x, event.y
#         c.coords(rect, x, y)
#     else:
#         c.coords(rect, -10, -10)
# root = tk.Tk()
# root.geometry('500x500')
# c = tk.Canvas(root, width = 1600, height = 850, cursor = 'none')
# rr = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
# bit = rr[random.randrange(0, len(rr))]
# print(bit)
# rect = c.create_bitmap(-10, -10, bitmap = bit)
# c.bind('<Motion>', callthiswhatevs)
# c.bind('<Leave>', callthiswhatevs)
# c.grid()
# root.mainloop()

# import pyttsx3
# cump = pyttsx3.init()
# cump.setProperty('rate', 120)
# cump.setProperty('volume', 1)
# cump.runAndWait()

# from datetime import datetime
# a = datetime.now()
# b = "%z%Z\n%a = %A = %w\n%Y = %y / %b = %B = %m / %d\n%H = %I(24hrs) %p : %M : %S.%f\n%U(week no. first day of week is Sunday) = %W(Monday)\n%c | %x | %X | %%"
# print(a.strftime(b))


# DO NOT keep a = b = []
# you can keep a = b = 0 or a = b= "hi" but no a = b = []

# tk.Tk size  = 1600x900
# Canvas size = 795x1530

# import tkinter as tk
# root = tk.Tk()
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
# root.mainloop()



import tkinter as tk
import random

app = tk.Tk()
app.title('Asteroids (An arcade game)')
root = tk.Canvas(app, bg = 'black', width = 500, height = 500)
side = 'left'
reshoot = True

def attack(create = False):
    if create == True:
        torf = random.randrange(0, 2)
        if torf:
            x = random.randrange(0, 500)
            y = random.randrange(0, 2)
            if y: metior = root.create_oval(x-40, 460, x, 500, fill = "white")
            else: metior = root.create_oval(x-40, 0, x, 40, fill = "white")
        else:
            x = random.randrange(0, 500)
            y = random.randrange(0, 2)
            if y: metior = root.create_oval(460, x-40, 500, x, fill = "white")
            else: metior = root.create_oval(0, x-40, 40, x, fill = "white")
        root.after(10000, attack, True)
        root.after(300, attack, metior)
        return
    attacker = root.coords(ball)
    shower = root.coords(create)
    attacker = [attacker[0]+43, attacker[1]-43]

    if shower[0] == attacker[0]: x = 0
    elif shower[0] > attacker[0]: x = -5
    else: x = 5
    
    if shower[1] == attacker[1]: y = 0
    elif shower[1] > attacker[1]: y = -5
    else: y = 5

    root.coords(create, shower[0]+x, shower[1]+y, shower[2]+x, shower[3]+y)

    root.after(300, attack, create)

def movit(obj, s = None):
    coords = root.coords(obj)
    if s:
        if s == 'left': coords = [coords[0]-5, coords[1], coords[0]+15, coords[1]+20]
        elif s == 'right': coords = [coords[0]+5, coords[1], coords[0]+25, coords[1]+20]
        elif s == 'up': coords = [coords[0], coords[1]-5, coords[0]+20, coords[1]+15]
        elif s == 'down': coords = [coords[0], coords[1]+5, coords[0]+20, coords[1]+25]
        root.coords(obj, coords[0], coords[1], coords[2], coords[3])
        root.after(100, movit, obj, s)
        return

    if side == 'left': coords = [coords[0]-10, coords[1], coords[0]+10, coords[1]+20]
    elif side == 'right': coords = [coords[0]+10, coords[1], coords[0]+30, coords[1]+20]
    elif side == 'up': coords = [coords[0], coords[1]-10, coords[0], coords[1]-30]
    elif side == 'down': coords = [coords[0], coords[1]+10, coords[0]+20, coords[1]+30]
    
    root.coords(obj, coords[0], coords[1], coords[2], coords[3])
    root.after(100, movit, obj, side)

def pushed(e):
    global side, reshoot
    if e == 10:
        reshoot = True
        return
    e = e.keysym
    x0, y0 = root.coords(ball)
    if e == 'Left':
        side = 'left'
        root.coords(ball, x0-10, y0)
    elif e == 'Right':
        side = 'right'
        root.coords(ball, x0+10, y0)
    elif e == 'Up':
        side = 'up'
        root.coords(ball, x0, y0-10)
    elif e == 'Down':
        side = 'down'
        root.coords(ball, x0, y0+10)
    elif e == 'space' and reshoot:
        reshoot = False
        shoot = root.create_oval(x0+43, y0-43, x0+63, y0-63, fill = 'gold')
        movit(shoot)
        root.after(900, pushed, 10)

app.bind('<Key>', pushed)

p4 = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\think_emoji.png")
# p4 = p4.subsample(3, 3)

root.after(3000, attack, True)
ball = root.create_image(250, 250, image = p4)

root.grid()
app.mainloop()