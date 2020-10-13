# import tkinter as tk
# import random
# def callthiswhatevs(event):
#     if 'Motion' in str(event):
#         x, y = event.x, event.y
#         c.coords(rect, x, y)
#     else:
#         c.coords(rect, -10, -10)
# self.root = tk.Tk()
# self.root.geometry('500x500')
# c = tk.Canvas(self.root, width = 1600, height = 850, cursor = 'none')
# rr = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
# bit = rr[random.randrange(0, len(rr))]
# print(bit)
# rect = c.create_bitmap(-10, -10, bitmap = bit)
# c.bind('<Motion>', callthiswhatevs)
# c.bind('<Leave>', callthiswhatevs)
# c.grid()
# self.root.mainloop()

# import pyttsx3
# cump = pyttsx3.init()
# cump.setProperty('rate', 120)
# cump.setProperty('volume', 1)
# cump.runAndWait()

# from datetime import datetime
# a = datetime.self.now()
# b = "%z%Z\n%a = %A = %w\n%Y = %y / %b = %B = %m / %self.d\n%H = %I(24hrs) %p : %M : %S.%f\n%U(week no. first day of week is Sunday) = %W(Monday)\n%c | %x | %X | %%"
# print(a.strftime(b))


# DO NOT keep a = b = []
# you can keep a = b = 0 or a = b= "hi" but no a = b = []

# tk.Tk size  = 1600x900
# Canvas size = 795x1530

# import tkinter as tk
# self.root = tk.Tk()
# canvas = tk.Canvas(self.root)
# scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
# scrollable_frame = tk.Frame(canvas)
# scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
# canvas.create_window((0, 0), window=scrollable_frame, anchor = 'nw')
# canvas.configure(yscrollcommand=scrollbar.set)
# for i in range(50):
#     tk.Label(scrollable_frame, width = 20, text = "Label").grid()
# canvas.grid(row = 0, column = 0)
# scrollbar.grid(row = 0, column = 1, sticky = 'ns')
# self.root.mainloop()



import tkinter as tk
import random, math
from PIL import ImageTk, Image
from datetime import datetime

app = tk.Tk()
astroot = 0
root_2 = tk.Frame(app)

class Asteroids:
    global astroot
        
    def __init__(self, root_2, app):
        app.title('Asteroids (An arcade game)')
        app.state('zoomed')
        self.root = tk.Canvas(app, bg = 'black', width = 1550, height = 800, cursor = 'none')

        self.side = 'left'

        self.reshoot = True
        self.selfstop = False
        self.orange = False
        self.red = False
        self.hearts = 3
        self.creation = []
        self.d = {}
        self.es = []

        app.bind('<Key>', self.pushed)
        app.bind('<1>', lambda e : self.pushed("space"))

        self.angle = 0
        self.duration = 7500
        self.stop = False
        self.once = False

        self.img = Image.open("images_for_gcpy\\rocket.png")
        self.img = self.img.resize((100, 100), Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(self.img.rotate(0))

        app.bind("<Motion>", self.move)
        app.bind("<Control_L> <w>", lambda e : app.destroy())

        self.root.after(15000, self.move, "Random")
        self.root.after(3000, self.attack, True, 3000)

        self.ball = self.root.create_image(775, 400, image = self.image)

        self.heart1 = self.root.create_rectangle(10, 10, 50, 50, fill = 'red')
        self.heart2 = self.root.create_rectangle(75, 10, 115, 50, fill = 'red')
        self.heart3 = self.root.create_rectangle(140, 10, 180, 50, fill = 'red')

        self.bbtg = self.root.create_rectangle(-10, -10, -2, -2, fill = "gray20")
        self.btg = self.root.create_text(-10, -10, text = "Back To Game", fill = "white", font = ("Informal roman", 24, 'bold'))

        self.besc = self.root.create_rectangle(-10, -10, -2, -2, fill = "gray20")
        self.esc = self.root.create_text(-10, -10, text = "Quit", fill = "white", font = ("Informal roman", 24, 'bold'))

        self.bret = self.root.create_rectangle(-10, -10, -2, -2, fill = "gray20")
        self.ret = self.root.create_text(-10, -10, text = "Return to Home Screen", fill = "white", font = ("Informal roman", 24, 'bold'))

        self.now = None
        self.sod = True

        self.root.grid()

    def attack(self, create = False, time = 0):

        if self.stop:
            self.creation.append(create)
            return

        if create == True:
            torf = random.randrange(0, 2)
            if torf:
                x = random.randrange(0, 1550)
                y = random.randrange(0, 2)
                if y: metior = self.root.create_oval(x-40, 760, x, 800, fill = "green", tag = "Metior")
                else: metior = self.root.create_oval(x-40, 0, x, 40, fill = "green", tag = "Metior")
            else:
                x = random.randrange(0, 800)
                y = random.randrange(0, 2)
                if y: metior = self.root.create_oval(1510, x-40, 1550, x, fill = "green", tag = "Metior")
                else: metior = self.root.create_oval(0, x-40, 40, x, fill = "green", tag = "Metior")
            if self.duration > 5000: self.duration -= 500
            else: self.orange = True
            self.root.after(self.duration, self.attack, True, self.duration)
            self.now = datetime.now()
            self.root.after(300, self.attack, metior, 300)
            return
        
        if self.root.itemcget(create, "tag") != "Metior": return

        attacker = self.root.coords(self.ball)
        shower = self.root.coords(create)
        attacker = [attacker[0]-10, attacker[1]-30]

        if shower[0] == attacker[0]: x = 0
        elif shower[0] > attacker[0]: x = -10
        else: x = 10
        
        if shower[1] == attacker[1]: y = 0
        elif shower[1] > attacker[1]: y = -10
        else: y = 10

        self.root.coords(create, shower[0]+x, shower[1]+y, shower[2]+x, shower[3]+y)
        shower = self.root.coords(create)
        cball = self.root.coords(self.ball)
        things = self.root.find_enclosed(cball[0]-60, cball[1]-60, cball[0]+60, cball[1]+60)
        
        if len(things) > 0:
            for ele in things:
                if self.root.itemcget(ele, 'tag') == "Metior":
                    self.hearts -= 1
                    h1 = self.root.create_text(775, 100, text = "-1 Heart", fill = '#00FFFF', font = ("Algerian", 15, 'bold'))
                    self.root.after(3000, self.root.delete, h1)
                    if self.hearts == 2: self.root.itemconfigure(self.heart3, fill = 'black')
                    elif self.hearts == 1: self.root.itemconfigure(self.heart2, fill = 'black')
                    elif self.hearts == 0: exit("Game Over")
                    self.root.coords(ele, -100, 0, -100, 0)
                    self.root.itemconfigure(ele, tag = "torn")

        self.root.after(300, self.attack, create, 300)

    def movit(self, obj, dist = None, time = 0):
        if self.stop:
            self.d[obj] = dist
            return

        coords = self.root.coords(obj)
        
        x = (coords[0]+coords[2])/2
        y = (coords[1]+coords[3])/2
        
        self.root.coords(obj, x+dist[0]-5, y+dist[1]-5, x+dist[0]+5, y+dist[1]+5)

        met = self.root.find_withtag("Metior")

        objc = self.root.coords(obj)

        if objc[0] > 1550 or objc[2] < 0 or objc[1] > 800 or objc[3] < 0:
            self.root.coords(obj, -100, -250, -100, -250)
            self.root.itemconfigure(obj, tag = 'torn')
            return

        for ast in met:
            coords = self.root.coords(ast)

            if coords[0] < objc[0] and coords[2] > objc[2] and coords[1] < objc[1] and coords[3] > objc[3]:
                if self.root.itemcget(ast, 'fill') == "green" and self.orange and not self.red:
                    self.root.itemconfigure(ast, fill = 'orange')
                    self.sod = self.red = True
                elif self.root.itemcget(ast, 'fill') == "green" or self.root.itemcget(ast, 'fill') == "self.orange" and not self.sod:
                    self.root.itemconfigure(ast, fill = 'red')
                    self.sod = True
                    self.red = False
                elif not self.sod:
                    self.root.coords(ast, -250, -250, -250, -250)
                    self.root.itemconfigure(ast, tag = "Broke")
                self.root.delete(obj)
                return

        self.root.after(100, self.movit, obj, dist, 100)

    def pushed(self, e, time = 0):

        e2 = e

        if e != 'space' and e != 10: e = e.keysym
        
        if self.stop and e != "Escape":
            self.es.append(e2)
            return

        if e == 10:
            self.reshoot = True
            return
            
        x0, y0 = self.root.coords(self.ball)
        if e == 'a':
            self.side = 'left'
            self.root.coords(self.ball, x0-15, y0)
        elif e == 'd':
            self.side = 'right'
            self.root.coords(self.ball, x0+15, y0)
        elif e == 'w':
            self.side = 'up'
            self.root.coords(self.ball, x0, y0-15)
        elif e == 's':
            self.side = 'down'
            self.root.coords(self.ball, x0, y0+15)
        
        elif e == "Escape" and not self.stop:
            self.stop = True
            self.root['cursor'] = 'arrow'
            self.root.coords(self.bbtg, 620, 250, 930, 350)
            self.root.coords(self.btg, 775, 300)
            
            self.root.coords(self.besc, 620, 350, 930, 450)
            self.root.coords(self.esc, 775, 400)

            self.root.coords(self.bret, 620, 450, 930, 550)
            self.root.coords(self.ret, 775, 500)

            if not self.once:
                self.once = True
                self.root.tag_bind(self.bret, "<Button>", self.switch)
                self.root.tag_bind(self.bbtg, "<Button>", lambda e : self.root.event_generate("<Escape>"))
                self.root.tag_bind(self.besc, "<Button>", lambda e : app.quit())

        elif e == "Escape":
            self.root['cursor'] = 'none'

            for ele in self.creation:
                self.attack(ele)

            for key, val in self.d.items():
                if self.root.itemcget(key, 'tag') != 'torn': self.movit(key, val)

            for ele in self.es:
                self.pushed(ele)

            self.root.coords(self.bbtg, -10, -10, -2, -2)
            self.root.coords(self.btg, -10, -10)
            
            self.root.coords(self.besc, -10, -10, -2, -2)
            self.root.coords(self.esc, -10, -10)
            
            self.root.coords(self.bret, -10, -10, -2, -2)
            self.root.coords(self.ret, -10, -10)

            self.root.after(10000, self.)
            self.root.after(10, self.switch, 10)

        elif e == 'space' and self.reshoot:
            self.reshoot = False
            
            if self.angle > 360:
                ang = self.angle//360
                self.angle = (360*ang)/self.angle
            elif self.angle < 0:
                self.angle = 360 + self.angle

            x = (50*math.cos(math.radians(self.angle+90)))+x0
            y = (50*math.sin(math.radians(self.angle+90)))+y0

            y = y0-(y-y0)

            shoot = self.root.create_oval(x-5, y-5, x+5, y+5, fill = 'yellow', tag = "Shoot")

            fdist = [0, 0]
            dist = [x-x0, y-y0]

            if dist[0] < 0:
                dist[0] = 0-dist[0]
                fdist[0] = 1
            
            if dist[1] < 0:
                dist[1] = 0-dist[1]
                fdist[1] = 1
            
            total = dist[0] + dist[1]
            total = 15/total
            dist[1] = total*dist[1]
            dist[0] = total*dist[0]
            
            if fdist[0] == 1: dist[0] = 0-dist[0]

            if fdist[1] == 1: dist[1] = 0-dist[1]

            self.sod = False
            self.movit(shoot, dist)
            self.root.after(900, self.pushed, 10, 900)

    def move(self, event):
        if self.stop: return

        if event == "Random":
            ran = random.randrange(0, 10)
            if ran == 0:
                if self.hearts == 1: self.root.itemconfigure(self.heart2, fill = 'red')
                elif self.hearts == 2: self.root.itemconfigure(self.heart3, fill = 'red')
                self.hearts += 1
                h1 = self.root.create_text(775, 100, text = "+1 Heart", fill = '#000fff000', font = ("Algerian", 15, 'bold'))
                self.root.after(3000, self.root.delete, h1)
            self.root.after(15000, self.move, "Random")
            return
        app.unbind("<Motion>")
        x = event.x-775
        self.angle -= x/3
        self.angle %= 360
        if self.stop: return
        self.image = ImageTk.PhotoImage(self.img.rotate(self.angle))

        self.root.itemconfig(self.ball, image = self.image)
        app.event_generate('<Motion>', warp = True, x = 775, y = 400)
        app.bind("<Motion>", self.move)

    def switch(self, event):
        """Switches between root and root_2\n\nParameters are - None"""
        global hroot
        
        if event == 10:
            self.stop = False
            return

        # makes a global variable the self.root and ungrids it. Grids the home screen
        hroot = self.root
        root_2.grid()
        
        app.title('Home screen')
        app.configure(bg = root_2.cget('bg'))
        
        self.root.grid_remove()

Asteroids(root_2, app)

app.mainloop()