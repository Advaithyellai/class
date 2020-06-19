import tkinter as tk
import random
from PIL import ImageTk, Image
import tkinter.font as font

def saep():

    class hangmang:
        def __init__(self, root_2):
            root_2.destroy()
            self.root = tk.Tk()
            self.root.title("hangman")
            self.root.geometry('5000x1000')
            self.myfont = font.Font(size = 12, family = 'algerian')
            self.count = tk.IntVar()
            self.words = ['armadillo', 'beaver', 'chimpanzee', 'dolphin', 'earthworm', 'flamingo'\
                ,'gorilla', 'hedgehog', 'iguana', 'jaguar', 'kingfisher', 'llama', 'mangoose'\
                , 'otter', 'possum', 'rhea', 'salmon', 'turkey', 'vulture', 'woodpecker'\
                , '']
            self.word = self.words[random.randrange(0, len(self.words))]
            self.blank = ""
            self.listword = []

            for ele in self.word:
                self.listword += ele
            self.blank += self.listword[0]
            for loop in range(0, len(self.word)-1):
                self.blank = self.blank + " _"
            loop += 1

            tk.Label(self.root, text = " ", width = 100).grid(row = 0, column = 0)
            tk.Label(self.root, text = " ", height = 20).grid(row = 0, column = 1)
            self.counting = tk.Label(self.root, text = "wrongs: %s/6" %(self.count.get()), width = 25, height = 5, bg = 'green')
            self.counting.grid(row = 1, column = 1)
            self.counting['font'] = self.myfont
            self.blankp = tk.Label(self.root, text = self.blank, width = 25, height = 5, bg = 'orange', font = self.myfont)
            self.blankp.grid(row = 1, column = 2)
            self.blankp['font'] = self.myfont
            self.guest = tk.StringVar()
            self.guest.set('Guess animal or letter')
            self.guess = tk.Entry(self.root, textvariable = self.guest, width= 25)
            self.guess.grid(row = 2, column = 1)
            self.guess['font'] = self.myfont
            self.guess.bind('<Button>', self.guestsetting)
            self.guess.bind('<Return>', self.correct)
            self.rating = tk.Label(self.root, text = "You rate this game __ /10, scroll up & down", font = self.myfont, bg = 'turquoise')
            self.rating.grid(row = 3, column = 1)
            self.rater = tk.Scale(self.root, from_ = 1, to = 10, font = self.myfont, bg = 'chartreuse2', command = self.gers)
            self.rater.grid(row = 3, column = 2)
            if self.guess.get() == "":
                self.count.set(int(self.count.get())-1)
            self.root.mainloop()
        def gers(self, e):
            if self.rater.get() == 1:
                self.rating.configure(text = "); You rate this game 1 /10 ;(")
            elif self.rater.get() == 2:
                self.rating.configure(text = "You rate this game 2 /10 :-(")
            elif self.rater.get() == 3:
                self.rating.configure(text = "You rate this game 3 /10 :(")
            elif self.rater.get() == 4:
                self.rating.configure(text = "You rate this game 4 /10 ;-|")
            elif self.rater.get() == 5:
                self.rating.configure(text = "|; You rate this game 5 /10 ;|")
            elif self.rater.get() == 6:
                self.rating.configure(text = "You rate this game 6 /10 :-|")
            elif self.rater.get() == 7:
                self.rating.configure(text = "You rate this game 7 /10 :|")
            elif self.rater.get() == 8:
                self.rating.configure(text = "You rate this game 8 /10 :-)")
            elif self.rater.get() == 9:
                self.rating.configure(text = "You rate this game 9 /10 :)")
            elif self.rater.get() == 10:
                self.rating.configure(text = "[: You rate this game 10 /10 :]")
        def guestsetting(self, event):
            self.guest.set('')
        def correct(self, event):
            self.guest.set(self.guest.get().lower())
            self.guess.configure(textvariable = self.guest)
            
            if len(self.guess.get()) != 1:

                if self.guest.get() == self.word:
                    self.guest.set('congrats')
                    self.blankp.configure(text = "Congrats")
                    self.root.title('congrats')
                    self.counting.configure(text = self.word)
                    a = tk.Button(self.root, text = "Quit", height = 5, width = 25, bg = 'red',command = lambda : quit(), font = self.myfont)
                    a.grid(row = 2, column = 2)
                    b = tk.Button(self.root, text = "Replay", height = 5, width = 25, bg = 'slateGray3',command = lambda : self.__init__(self.root), font = self.myfont)
                    b.grid(row = 4, column = 1)
                else:
                    if len(self.guess.get()) != 0:
                        self.count.set(self.count.get()+1)
                        self.counting.configure(text = "wrongs: %s/6" %(self.count.get()))
                
                if self.count.get() >= 6:
                    self.guest.set('loser')
                    self.blankp.configure(text = "loser")
                    self.root.title('loser')
                    self.counting.configure(text = self.word)
                    a = tk.Button(self.root, text = "Quit", height = 5, width = 25, bg = 'red',command = lambda : quit(), font = self.myfont)
                    a.grid(row = 2, column = 2)
                    b = tk.Button(self.root, text = "Replay", height = 5, width = 25, bg = 'slateGray3',command = lambda : self.__init__(self.root), font = self.myfont)
                    b.grid(row = 4, column = 1)
                
                self.guest.set('')
            else:
                loop = 0
                blank_2 = ""
                if self.guess.get() in self.listword:
                    if self.guess.get() in list(self.blank):
                        self.count.set(int(self.count.get())+1)
                        self.counting.configure(text = "wrongs: %s/6" %(self.count.get()))
                        self.guest.set('')
                    else:
                        for ele in self.listword:
                            if ele == self.guess.get():
                                self.blank = self.blank.split(' ')
                                self.blank[loop] = ele
                                for ele_2 in self.blank:
                                    blank_2 += ele_2
                                    blank_2 += " "
                                self.blank = blank_2
                                blank_2 = ""
                            loop += 1
                        self.blankp.configure(text = self.blank)
                        self.guest.set('')
                else:
                    if len(self.guess.get()) != 0:
                        self.count.set(int(self.count.get())+1)
                        self.counting.configure(text = "wrongs: %s/6" %(self.count.get()))
                        self.guest.set('')
                if '_' in self.blank:
                    if self.count.get() >= 6:
                        self.guest.set('loser')
                        self.blankp.configure(text = "loser")
                        self.root.title('loser')
                        self.counting.configure(text = self.word)
                        a = tk.Button(self.root, text = "Quit", height = 5, width = 25, bg = 'red',command = lambda : quit(), font = self.myfont)
                        a.grid(row = 2, column = 2)
                        b = tk.Button(self.root, text = "Replay", height = 5, width = 25, bg = 'slateGray3',command = lambda : self.__init__(self.root), font = self.myfont)
                        b.grid(row = 4, column = 1)
                else:
                    self.guest.set('congrats')
                    self.blankp.configure(text = "Congrats")
                    self.root.title('congrats')
                    self.counting.configure(text = self.word)
                    a = tk.Button(self.root, text = "Quit", height = 5, width = 25, bg = 'red',command = lambda : quit(), font = self.myfont)
                    a.grid(row = 2, column = 2)
                    b = tk.Button(self.root, text = "Replay", height = 5, width = 25, bg = 'slateGray3',command = lambda : self.__init__(self.root), font = self.myfont)
                    b.grid(row = 4, column = 1)
                self.guest.set('')
    
    class cubegame:
        def __init__(self, root_2):
            self.root = tk.Tk()
            self.root.title('Cube')
            self.root.geometry('5000x1000')
            root_2.destroy()
            self.f = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
            self.d = ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']
            self.b = ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']
            self.t = ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']
            self.l = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
            self.r = ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']
            self.z = -1
            
            self.myfont = font.Font(root = self.root, size = 15, family = 'algerian', weight = "bold", overstrike = 1)
            self.myfont_2 = font.Font(root = self.root, size = 15, family = 'algerian', weight = 'bold')
            tk.Label(self.root, text = " ", height = 20).grid(row = 0, column = 1)
            tk.Label(self.root, text = " ", width = 100).grid(row = 1, column = 0)

            for x in range(2, 5):
                for y in range(2, 5):
                    self.z += 1
                    tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            
            self.moveer = tk.Label(self.root, text = "move = ", width = 12)
            self.moveer.grid(row = 1, column = 1)
            self.moveer['font'] = self.myfont_2
            self.w = tk.StringVar(self.root)
            self.ac = tk.Entry(self.root, text = self.w)
            self.ac.grid(row = 2, column = 1)
            self.a = tk.Label(self.root, text = "facing-black", fg = 'black', bg = 'red', width = 12)
            self.a.grid(row = 5, column = 1)
            self.a['font'] = self.myfont
            self.s = tk.Label(self.root, text = "on top-red", fg = 'red', bg = 'black', width = 12)
            self.s.grid(row = 6, column = 1)
            self.s['font'] = self.myfont
            self.ac.bind("<Return>", self.returning)
            self.rating = tk.Label(self.root, text = "You rate this game __ /10, scroll up & down", font = self.myfont_2, bg = 'turquoise')
            self.rating.grid(row = 8, column = 5)
            self.rater = tk.Scale(self.root, from_ = 1, to = 10, font = self.myfont, bg = 'chartreuse2', command = self.gers)
            self.rater.grid(row = 9, column = 5)
            self.root.mainloop()
        def gers(self, e):
            if self.rater.get() == 1:
                self.rating.configure(text = "); You rate this game 1 /10 ;(")
            elif self.rater.get() == 2:
                self.rating.configure(text = "You rate this game 2 /10 :-(")
            elif self.rater.get() == 3:
                self.rating.configure(text = "You rate this game 3 /10 :(")
            elif self.rater.get() == 4:
                self.rating.configure(text = "You rate this game 4 /10 ;-|")
            elif self.rater.get() == 5:
                self.rating.configure(text = "|; You rate this game 5 /10 ;|")
            elif self.rater.get() == 6:
                self.rating.configure(text = "You rate this game 6 /10 :-|")
            elif self.rater.get() == 7:
                self.rating.configure(text = "You rate this game 7 /10 :|")
            elif self.rater.get() == 8:
                self.rating.configure(text = "You rate this game 8 /10 :-)")
            elif self.rater.get() == 9:
                self.rating.configure(text = "You rate this game 9 /10 :)")
            elif self.rater.get() == 10:
                self.rating.configure(text = "[: You rate this game 10 /10 :]")
        def entering(self):
            self.z = -1
            move = self.w.get()
            move = move.upper()

            if move == "R":
                g, c, e = self.f[6], self.f[7], self.f[8]
                self.f[6], self.f[7], self.f[8] = self.d[2], self.d[1], self.d[0]
                self.d[0], self.d[1], self.d[2] = self.b[0], self.b[1], self.b[2]
                self.b[0], self.b[1], self.b[2] = self.t[8], self.t[7], self.t[6]
                self.t[6], self.t[7], self.t[8] = g, c, e
                h, i, j, k = self.r[0], self.r[7], self.r[8], self.r[1]
                self.r[0], self.r[7], self.r[8], self.r[1] = self.r[2], self.r[3], self.r[6], self.r[5]
                self.r[6], self.r[3], self.r[2], self.r[5] = h, k, j, i
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z+=1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "R'":
                g, c, e = self.f[6], self.f[7], self.f[8]
                self.f[6], self.f[7], self.f[8] = self.t[6], self.t[7], self.t[8]
                self.t[6], self.t[7], self.t[8] = self.b[2], self.b[1], self.b[0]
                self.b[0], self.b[1], self.b[2] = self.d[0], self.d[1], self.d[2]
                self.d[0], self.d[1], self.d[2] = e, c, g
                k,h,i,j = self.r[6], self.r[5], self.r[2], self.r[3]
                self.r[6], self.r[5], self.r[2], self.r[3] = self.r[8], self.r[1], self.r[0], self.r[7]
                self.r[0], self.r[1], self.r[7], self.r[8] = k, j, h, i
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z+=1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "L":
                g, c, e = self.f[0], self.f[1], self.f[2]
                self.f[0], self.f[1], self.f[2] = self.t[0], self.t[1], self.t[2]
                self.t[0], self.t[1], self.t[2] = self.b[8], self.b[7], self.b[6]
                self.b[6], self.b[7], self.b[8] = self.d[6], self.d[7], self.d[8]
                self.d[6], self.d[7], self.d[8] = e, c, g
                h, i, j, k = self.l[0], self.l[7], self.l[8], self.l[1]
                self.l[0], self.l[7], self.l[8], self.l[1] = self.l[2], self.l[3], self.l[6], self.l[5]
                self.l[6], self.l[3], self.l[2], self.l[5] = h, k, j, i
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "L'":
                g, c, e = self.f[0], self.f[1], self.f[2]
                self.f[0], self.f[1], self.f[2] = self.d[8], self.d[7], self.d[6]
                self.d[6], self.d[7], self.d[8] = self.b[8], self.b[7], self.b[6]
                self.b[6], self.b[7], self.b[8] = self.t[2], self.t[1], self.t[0]
                self.t[0], self.t[1], self.t[2] = g, c, e
                k,h,i,j = self.l[6], self.l[5], self.l[2], self.l[3]
                self.l[6], self.l[5], self.l[2], self.l[3] = self.l[8], self.l[1], self.l[0], self.l[7]
                self.l[0], self.l[1], self.l[7], self.l[8] = k, j, h, i
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "U":
                g, c, e = self.f[0], self.f[3], self.f[6]
                self.f[0], self.f[3], self.f[6] = self.r[2], self.r[1], self.r[0]
                self.r[0], self.r[1], self.r[2] = self.b[6], self.b[3], self.b[0]
                self.b[0], self.b[3], self.b[6] = self.l[6], self.l[7], self.l[8]
                self.l[6], self.l[7], self.l[8] = g, c, e
                h, i, j, k = self.t[0], self.t[7], self.t[8], self.t[1]
                self.t[0], self.t[7], self.t[8], self.t[1] = self.t[2], self.t[3], self.t[6], self.t[5]
                self.t[6], self.t[3], self.t[2], self.t[5] = h, k, j, i
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "U'":
                g, c, e = self.f[0], self.f[3], self.f[6]
                self.f[0], self.f[3], self.f[6] = self.l[6], self.l[7], self.l[8]
                self.l[6], self.l[7], self.l[8] = self.b[0], self.b[3], self.b[6]
                self.b[0], self.b[3], self.b[6] = self.r[2], self.r[1], self.r[0]
                self.r[0], self.r[1], self.r[2] = e, c, g
                k,h,i,j = self.t[6], self.t[5], self.t[2], self.t[3]
                self.t[6], self.t[5], self.t[2], self.t[3] = self.t[8], self.t[1], self.t[0], self.t[7]
                self.t[0], self.t[1], self.t[7], self.t[8] = k, j, h, i
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "D":
                g, c, e = self.f[2], self.f[5], self.f[8]
                self.f[2], self.f[5], self.f[8] = self.l[0], self.l[1], self.l[2]
                self.l[0], self.l[1], self.l[2] = self.b[8], self.b[5], self.b[2]
                self.b[2], self.b[5], self.b[8] = self.r[6], self.r[7], self.r[8]
                self.r[6], self.r[7], self.r[8] = g, c, e
                k,h,i,j = self.d[6], self.d[5], self.d[2], self.d[3]
                self.d[6], self.d[5], self.d[2], self.d[3] = self.d[8], self.d[1], self.d[0], self.d[7]
                self.d[0], self.d[1], self.d[7], self.d[8] = k, j, h, i
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "D'":
                g, c, e = self.f[2], self.f[5], self.f[8]
                self.f[2], self.f[5], self.f[8] = self.r[8], self.r[7], self.r[6]
                self.r[6], self.r[7], self.r[8] = self.b[8], self.b[5], self.b[2]
                self.b[2], self.b[5], self.b[8] = self.l[0], self.l[1], self.l[2]
                self.l[0], self.l[1], self.l[2] = g, c, e
                h, i, j, k = self.d[0], self.d[7], self.d[8], self.d[1]
                self.d[0], self.d[7], self.d[8], self.d[1] = self.d[2], self.d[3], self.d[6], self.d[5]
                self.d[6], self.d[3], self.d[2], self.d[5] = h, k, j, i
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "F":
                g, c, e = self.r[2], self.r[5], self.r[8]
                self.r[2], self.r[5], self.r[8] = self.t[2], self.t[5], self.t[8]
                self.t[2], self.t[5], self.t[8] = self.l[2], self.l[5], self.l[8]
                self.l[2], self.l[5], self.l[8] = self.d[2], self.d[5], self.d[8]
                self.d[2], self.d[5], self.d[8] = g, c, e
                h, i, j, k = self.f[0], self.f[7], self.f[8], self.f[1]
                self.f[0], self.f[7], self.f[8], self.f[1] = self.f[2], self.f[3], self.f[6], self.f[5]
                self.f[6], self.f[3], self.f[2], self.f[5] = h, k, j, i
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "F'":
                g, c, e = self.r[2], self.r[5], self.r[8]
                self.r[2], self.r[5], self.r[8] = self.d[2], self.d[5], self.d[8]
                self.d[2], self.d[5], self.d[8] = self.l[2], self.l[5], self.l[8]
                self.l[2], self.l[5], self.l[8] = self.t[2], self.t[5], self.t[8]
                self.t[2], self.t[5], self.t[8] = g, c, e 
                k,h,i,j = self.f[6], self.f[5], self.f[2], self.f[3]
                self.f[6], self.f[5], self.f[2], self.f[3] = self.f[8], self.f[1], self.f[0], self.f[7]
                self.f[0], self.f[1], self.f[7], self.f[8] = k, j, h, i
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "B":
                g, c, e = self.r[0], self.r[3], self.r[6]
                self.r[0], self.r[3], self.r[6] = self.t[0], self.t[3], self.t[6]
                self.t[0], self.t[3], self.t[6] = self.l[0], self.l[3], self.l[6]
                self.l[0], self.l[3], self.l[6] = self.d[0], self.d[3], self.d[6]
                self.d[0], self.d[3], self.d[6] = g, c, e
                h, i, j, k = self.b[0], self.b[7], self.b[8], self.b[1]
                self.b[0], self.b[7], self.b[8], self.b[1] = self.b[2], self.b[3], self.b[6], self.b[5]
                self.b[6], self.b[3], self.b[2], self.b[5] = h, k, j, i
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "B'":
                g, c, e = self.r[0], self.r[3], self.r[6]
                self.r[0], self.r[3], self.r[6] = self.d[0], self.d[3], self.d[6]
                self.d[0], self.d[3], self.d[6] = self.l[0], self.l[3], self.l[6]
                self.l[0], self.l[3], self.l[6] = self.t[0], self.t[3], self.t[6]
                self.t[0], self.t[3], self.t[6] = g, c, e
                k,h,i,j = self.b[6], self.b[5], self.b[2], self.b[3]
                self.b[6], self.b[5], self.b[2], self.b[3] = self.b[8], self.b[1], self.b[0], self.b[7]
                self.b[0], self.b[1], self.b[7], self.b[8] = k, j, h, i
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "M":
                g, c, e = self.f[3], self.f[4], self.f[5]
                self.f[3], self.f[4], self.f[5] = self.t[3], self.t[4], self.t[5]
                self.t[3], self.t[4], self.t[5] = self.b[5], self.b[4], self.b[3]
                self.b[5], self.b[4], self.b[3] = self.d[5], self.d[4], self.d[3]
                self.d[5], self.d[4], self.d[3] = g, c, e
                self.a.configure(text = "facing-{}".format(self.f[4]), fg = self.f[4], bg = self.t[4])
                self.s.configure(text = "on top-{}".format(self.t[4]), fg = self.t[4], bg = self.f[4])
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "M'":
                g, c, e = self.f[3], self.f[4], self.f[5]
                self.f[3], self.f[4], self.f[5] = self.d[5], self.d[4], self.d[3]
                self.d[5], self.d[4], self.d[3] = self.b[5], self.b[4], self.b[3]
                self.b[5], self.b[4], self.b[3] = self.t[3], self.t[4], self.t[5]
                self.t[3], self.t[4], self.t[5] = g, c, e
                self.a.configure(text = "facing-{}".format(self.f[4]), fg = self.f[4], bg = self.t[4])
                self.s.configure(text = "on top-{}".format(self.t[4]), fg = self.t[4], bg = self.f[4])
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "S":
                g, c, e = self.r[1], self.r[4], self.r[7]
                self.r[1], self.r[4], self.r[7] = self.t[1], self.t[4], self.t[7]
                self.t[1], self.t[4], self.t[7] = self.l[1], self.l[4], self.l[7]
                self.l[1], self.l[4], self.l[7] = self.d[1], self.d[4], self.d[7]
                self.d[1], self.d[4], self.d[7] = g, c, e
                self.a.configure(bg = self.t[4])
                self.s.configure(text = "on top-{}".format(self.t[4]), fg = self.t[4], bg = self.f[4])
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "S'":
                g, c, e = self.r[1], self.r[4], self.r[7]
                self.r[1], self.r[4], self.r[7] = self.d[1], self.d[4], self.d[7]
                self.d[1], self.d[4], self.d[7] = self.l[1], self.l[4], self.l[7]
                self.l[1], self.l[4], self.l[7] = self.t[1], self.t[4], self.t[7]
                self.t[1], self.t[4], self.t[7] = g, c, e
                self.a.configure(bg = self.t[4])
                self.s.configure(text = "on top-{}".format(self.t[4]), fg = self.t[4], bg = self.f[4])
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "E":
                g, c, e = self.f[1], self.f[4], self.f[7]
                self.f[1], self.f[4], self.f[7] = self.l[5], self.l[4], self.l[3]
                self.l[5], self.l[4], self.l[3] = self.b[1], self.b[4], self.b[7]
                self.b[1], self.b[4], self.b[7] = self.r[5], self.r[4], self.r[3]
                self.r[5], self.r[4], self.r[3] = e, c, g
                self.a.configure(text = "facing-{}".format(self.f[4]), fg = self.f[4], bg = self.t[4])
                self.s.configure(bg = self.f[4])
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "E'":
                g, c, e = self.f[1], self.f[4], self.f[7]
                self.f[1], self.f[4], self.f[7] = self.r[5], self.r[4], self.r[3]
                self.r[5], self.r[4], self.r[3] = self.b[1], self.b[4], self.b[7]
                self.b[1], self.b[4], self.b[7] = self.l[3], self.l[4], self.l[5]
                self.l[3], self.l[4], self.l[5] = e, c, g
                self.a.configure(text = "facing-{}".format(self.f[4]), fg = self.f[4], bg = self.t[4])
                self.s.configure(bg = self.f[4])
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "X":
                g, c, e = self.f[3], self.f[4], self.f[5]
                self.f[3], self.f[4], self.f[5] = self.d[5], self.d[4], self.d[3]
                self.d[5], self.d[4], self.d[3] = self.b[5], self.b[4], self.b[3]
                self.b[5], self.b[4], self.b[3] = self.t[3], self.t[4], self.t[5]
                self.t[3], self.t[4], self.t[5] = g, c, e
                g, c, e = self.f[6], self.f[7], self.f[8]
                self.f[6], self.f[7], self.f[8] = self.d[2], self.d[1], self.d[0]
                self.d[0], self.d[1], self.d[2] = self.b[0], self.b[1], self.b[2]
                self.b[0], self.b[1], self.b[2] = self.t[8], self.t[7], self.t[6]
                self.t[6], self.t[7], self.t[8] = g, c, e
                h, i, j, k = self.r[0], self.r[7], self.r[8], self.r[1]
                self.r[0], self.r[7], self.r[8], self.r[1] = self.r[2], self.r[3], self.r[6], self.r[5]
                self.r[6], self.r[3], self.r[2], self.r[5] = h, k, j, i
                g, c, e = self.f[0], self.f[1], self.f[2]
                self.f[0], self.f[1], self.f[2] = self.d[8], self.d[7], self.d[6]
                self.d[6], self.d[7], self.d[8] = self.b[8], self.b[7], self.b[6]
                self.b[6], self.b[7], self.b[8] = self.t[2], self.t[1], self.t[0]
                self.t[0], self.t[1], self.t[2] = g, c, e
                k,h,i,j = self.l[6], self.l[5], self.l[2], self.l[3]
                self.l[6], self.l[5], self.l[2], self.l[3] = self.l[8], self.l[1], self.l[0], self.l[7]
                self.l[0], self.l[1], self.l[7], self.l[8] = k, j, h, i
                self.a.configure(text = "facing-{}".format(self.f[4]), fg = self.f[4], bg = self.t[4])
                self.s.configure(text = "on top-{}".format(self.t[4]), fg = self.t[4], bg = self.f[4])
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "X'":
                g, c, e = self.f[6], self.f[7], self.f[8]
                self.f[6], self.f[7], self.f[8] = self.t[6], self.t[7], self.t[8]
                self.t[6], self.t[7], self.t[8] = self.b[2], self.b[1], self.b[0]
                self.b[0], self.b[1], self.b[2] = self.d[0], self.d[1], self.d[2]
                self.d[0], self.d[1], self.d[2] = e, c, g
                k,h,i,j = self.r[6], self.r[5], self.r[2], self.r[3]
                self.r[6], self.r[5], self.r[2], self.r[3] = self.r[8], self.r[1], self.r[0], self.r[7]
                self.r[0], self.r[1], self.r[7], self.r[8] = k, j, h, i
                g, c, e = self.f[0], self.f[1], self.f[2]
                self.f[0], self.f[1], self.f[2] = self.t[0], self.t[1], self.t[2]
                self.t[0], self.t[1], self.t[2] = self.b[8], self.b[7], self.b[6]
                self.b[6], self.b[7], self.b[8] = self.d[6], self.d[7], self.d[8]
                self.d[6], self.d[7], self.d[8] = e, c, g
                h, i, j, k = self.l[0], self.l[7], self.l[8], self.l[1]
                self.l[0], self.l[7], self.l[8], self.l[1] = self.l[2], self.l[3], self.l[6], self.l[5]
                self.l[6], self.l[3], self.l[2], self.l[5] = h, k, j, i
                g, c, e = self.f[3], self.f[4], self.f[5]
                self.f[3], self.f[4], self.f[5] = self.t[3], self.t[4], self.t[5]
                self.t[3], self.t[4], self.t[5] = self.b[5], self.b[4], self.b[3]
                self.b[5], self.b[4], self.b[3] = self.d[5], self.d[4], self.d[3]
                self.d[5], self.d[4], self.d[3] = g, c, e
                self.a.configure(text = "facing-{}".format(self.f[4]), fg = self.f[4], bg = self.t[4])
                self.s.configure(text = "on top-{}".format(self.t[4]), fg = self.t[4], bg = self.f[4])
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "Y":
                g, c, e = self.f[1], self.f[4], self.f[7]
                self.f[1], self.f[4], self.f[7] = self.r[5], self.r[4], self.r[3]
                self.r[5], self.r[4], self.r[3] = self.b[1], self.b[4], self.b[7]
                self.b[1], self.b[4], self.b[7] = self.l[3], self.l[4], self.l[5]
                self.l[3], self.l[4], self.l[5] = e, c, g
                g, c, e = self.f[2], self.f[5], self.f[8]
                self.f[2], self.f[5], self.f[8] = self.r[8], self.r[7], self.r[6]
                self.r[6], self.r[7], self.r[8] = self.b[8], self.b[5], self.b[2]
                self.b[2], self.b[5], self.b[8] = self.l[0], self.l[1], self.l[2]
                self.l[0], self.l[1], self.l[2] = g, c, e
                h, i, j, k = self.d[0], self.d[7], self.d[8], self.d[1]
                self.d[0], self.d[7], self.d[8], self.d[1] = self.d[2], self.d[3], self.d[6], self.d[5]
                self.d[6], self.d[3], self.d[2], self.d[5] = h, k, j, i
                g, c, e = self.f[0], self.f[3], self.f[6]
                self.f[0], self.f[3], self.f[6] = self.r[2], self.r[1], self.r[0]
                self.r[0], self.r[1], self.r[2] = self.b[6], self.b[3], self.b[0]
                self.b[0], self.b[3], self.b[6] = self.l[6], self.l[7], self.l[8]
                self.l[6], self.l[7], self.l[8] = g, c, e
                h, i, j, k = self.t[0], self.t[7], self.t[8], self.t[1]
                self.t[0], self.t[7], self.t[8], self.t[1] = self.t[2], self.t[3], self.t[6], self.t[5]
                self.t[6], self.t[3], self.t[2], self.t[5] = h, k, j, i
                self.a.configure(text = "facing-{}".format(self.f[4]), fg = self.f[4], bg = self.t[4])
                self.s.configure(text = "on top-{}".format(self.t[4]), fg = self.t[4], bg = self.f[4])
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "Y'":
                g, c, e = self.f[2], self.f[5], self.f[8]
                self.f[2], self.f[5], self.f[8] = self.l[0], self.l[1], self.l[2]
                self.l[0], self.l[1], self.l[2] = self.b[8], self.b[5], self.b[2]
                self.b[2], self.b[5], self.b[8] = self.r[6], self.r[7], self.r[8]
                self.r[6], self.r[7], self.r[8] = g, c, e
                k,h,i,j = self.d[6], self.d[5], self.d[2], self.d[3]
                self.d[6], self.d[5], self.d[2], self.d[3] = self.d[8], self.d[1], self.d[0], self.d[7]
                self.d[0], self.d[1], self.d[7], self.d[8] = k, j, h, i
                g, c, e = self.f[0], self.f[3], self.f[6]
                self.f[0], self.f[3], self.f[6] = self.l[6], self.l[7], self.l[8]
                self.l[6], self.l[7], self.l[8] = self.b[0], self.b[3], self.b[6]
                self.b[0], self.b[3], self.b[6] = self.r[2], self.r[1], self.r[0]
                self.r[0], self.r[1], self.r[2] = e, c, g
                k,h,i,j = self.t[6], self.t[5], self.t[2], self.t[3]
                self.t[6], self.t[5], self.t[2], self.t[3] = self.t[8], self.t[1], self.t[0], self.t[7]
                self.t[0], self.t[1], self.t[7], self.t[8] = k, j, h, i
                g, c, e = self.f[1], self.f[4], self.f[7]
                self.f[1], self.f[4], self.f[7] = self.l[5], self.l[4], self.l[3]
                self.l[5], self.l[4], self.l[3] = self.b[1], self.b[4], self.b[7]
                self.b[1], self.b[4], self.b[7] = self.r[5], self.r[4], self.r[3]
                self.r[5], self.r[4], self.r[3] = e, c, g
                self.a.configure(text = "facing-{}".format(self.f[4]), fg = self.f[4], bg = self.t[4])
                self.s.configure(text = "on top-{}".format(self.t[4]), fg = self.t[4], bg = self.f[4])
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "Z":
                g, c, e = self.r[0], self.r[3], self.r[6]
                self.r[0], self.r[3], self.r[6] = self.d[0], self.d[3], self.d[6]
                self.d[0], self.d[3], self.d[6] = self.l[0], self.l[3], self.l[6]
                self.l[0], self.l[3], self.l[6] = self.t[0], self.t[3], self.t[6]
                self.t[0], self.t[3], self.t[6] = g, c, e
                k,h,i,j = self.b[6], self.b[5], self.b[2], self.b[3]
                self.b[6], self.b[5], self.b[2], self.b[3] = self.b[8], self.b[1], self.b[0], self.b[7]
                self.b[0], self.b[1], self.b[7], self.b[8] = k, j, h, i
                g, c, e = self.r[2], self.r[5], self.r[8]
                self.r[2], self.r[5], self.r[8] = self.t[2], self.t[5], self.t[8]
                self.t[2], self.t[5], self.t[8] = self.l[2], self.l[5], self.l[8]
                self.l[2], self.l[5], self.l[8] = self.d[2], self.d[5], self.d[8]
                self.d[2], self.d[5], self.d[8] = g, c, e
                h, i, j, k = self.f[0], self.f[7], self.f[8], self.f[1]
                self.f[0], self.f[7], self.f[8], self.f[1] = self.f[2], self.f[3], self.f[6], self.f[5]
                self.f[6], self.f[3], self.f[2], self.f[5] = h, k, j, i
                g, c, e = self.r[1], self.r[4], self.r[7]
                self.r[1], self.r[4], self.r[7] = self.t[1], self.t[4], self.t[7]
                self.t[1], self.t[4], self.t[7] = self.l[1], self.l[4], self.l[7]
                self.l[1], self.l[4], self.l[7] = self.d[1], self.d[4], self.d[7]
                self.d[1], self.d[4], self.d[7] = g, c, e
                self.a.configure(bg = self.t[4])
                self.s.configure(text = "on top-{}".format(self.t[4]), fg = self.t[4], bg = self.f[4])
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "Z'":
                g, c, e = self.r[0], self.r[3], self.r[6]
                self.r[0], self.r[3], self.r[6] = self.t[0], self.t[3], self.t[6]
                self.t[0], self.t[3], self.t[6] = self.l[0], self.l[3], self.l[6]
                self.l[0], self.l[3], self.l[6] = self.d[0], self.d[3], self.d[6]
                self.d[0], self.d[3], self.d[6] = g, c, e
                h, i, j, k = self.b[0], self.b[7], self.b[8], self.b[1]
                self.b[0], self.b[7], self.b[8], self.b[1] = self.b[2], self.b[3], self.b[6], self.b[5]
                self.b[6], self.b[3], self.b[2], self.b[5] = h, k, j, i
                g, c, e = self.r[1], self.r[4], self.r[7]
                self.r[1], self.r[4], self.r[7] = self.d[1], self.d[4], self.d[7]
                self.d[1], self.d[4], self.d[7] = self.l[1], self.l[4], self.l[7]
                self.l[1], self.l[4], self.l[7] = self.t[1], self.t[4], self.t[7]
                self.t[1], self.t[4], self.t[7] = g, c, e
                g, c, e = self.r[2], self.r[5], self.r[8]
                self.r[2], self.r[5], self.r[8] = self.d[2], self.d[5], self.d[8]
                self.d[2], self.d[5], self.d[8] = self.l[2], self.l[5], self.l[8]
                self.l[2], self.l[5], self.l[8] = self.t[2], self.t[5], self.t[8]
                self.t[2], self.t[5], self.t[8] = g, c, e 
                k,h,i,j = self.f[6], self.f[5], self.f[2], self.f[3]
                self.f[6], self.f[5], self.f[2], self.f[3] = self.f[8], self.f[1], self.f[0], self.f[7]
                self.f[0], self.f[1], self.f[7], self.f[8] = k, j, h, i
                self.a.configure(text = "facing-{}".format(self.f[4]), fg = self.f[4], bg = self.t[4])
                self.s.configure(text = "on top-{}".format(self.t[4]), fg = self.t[4], bg = self.f[4])
                for x in range(2, 5):
                    for y in range(2, 5):
                        self.z += 1
                        tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            elif move == "exit":
                exit("bye")
        def returning(self, event):
            self.entering()
            self.w.set('')
    
    class cg:
        def __init__(self, root_2):
            root_2.destroy()
            self.counting = 60
            self.colours = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
            self.counter = 0
            self.words = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
            self.root = tk.Tk()
            self.root.title("Colour Game")
            self.root.geometry('1600x900')
            self.iv1 = tk.IntVar(self.root, 0)
            self.iv2 = tk.IntVar(self.root, 0)
            self.myfont = font.Font(size = 15, family = 'Algerian', weight = "bold")
            self.myfont_2 = font.Font(size = 18, family = 'Algerian', weight = "bold")
            self.myfont_4 = font.Font(size = 40)
            tk.Label(self.root, text = " ", width = 75).grid(row = 0, column = 0)
            self.rating = tk.Label(self.root, text = "You rate this game __ /10, scroll up & down", font = self.myfont, bg = 'turquoise')
            self.rating.grid(row = 1, column = 0)
            self.rater = tk.Scale(self.root, from_ = 1, to = 10, font = self.myfont, command = lambda e : self.gers(), bg = 'chartreuse2')
            self.rater.grid(row = 2, column = 0)
            tk.Label(self.root, text = "Game Description: Enter the colour of the self.words displayed below.", fg = 'grey', font = self.myfont).grid(row = 0, column = 1)
            tk.Label(self.root, text = "And keep in mind not to enter the word text itself", fg = 'grey', font = self.myfont).grid(row = 1, column = 1)
            self.score = tk.Label(self.root, text = "Your score : {}".format(self.counter), fg = 'forest green', font = self.myfont_2)
            self.score.grid(row = 2, column = 1)
            self.code = tk.Label(self.root, text = "   ",height = 4, font = self.myfont_4)
            self.code.grid(row = 3, column = 1)
            self.timer = tk.Label(self.root, text = "Game ends in : __", fg = 'gold2', font = self.myfont_2)
            self.timer.grid(row = 4, column = 1)
            tk.Label(self.root, text = "").grid(row = 5, column = 1)
            self.geser = tk.StringVar(self.root, "")
            self.ges = tk.Entry(self.root, textvariable = self.geser, width = 20, font = self.myfont, fg = 'khaki4')
            self.ges.grid(row = 6, column = 1)
            tk.Label(self.root, text = "", height = 13).grid(row = 7, column = 1)
            self.starter = tk.Button(self.root, text = "Start", width = 20, height = 3, font = self.myfont, bg = 'peach puff', command = self.lesgo)
            self.starter.grid(row = 8, column = 1)
            tk.Button(self.root, text = "Quit", width = 20, height = 3, font = self.myfont, bg = 'blue', command = lambda : quit()).grid(row = 7, column = 1)
            self.root.mainloop()
        def gers(self):
            if self.rater.get() == 1:
                self.rating.configure(text = "); You rate this game 1 /10 ;(")
            elif self.rater.get() == 2:
                self.rating.configure(text = "You rate this game 2 /10 :-(")
            elif self.rater.get() == 3:
                self.rating.configure(text = "You rate this game 3 /10 :(")
            elif self.rater.get() == 4:
                self.rating.configure(text = "You rate this game 4 /10 ;-|")
            elif self.rater.get() == 5:
                self.rating.configure(text = "|; You rate this game 5 /10 ;|")
            elif self.rater.get() == 6:
                self.rating.configure(text = "You rate this game 6 /10 :-|")
            elif self.rater.get() == 7:
                self.rating.configure(text = "You rate this game 7 /10 :|")
            elif self.rater.get() == 8:
                self.rating.configure(text = "You rate this game 8 /10 :-)")
            elif self.rater.get() == 9:
                self.rating.configure(text = "You rate this game 9 /10 :)")
            elif self.rater.get() == 10:
                self.rating.configure(text = "[: You rate this game 10 /10 :]")
        def lestart(self, event):

            if self.counting == 0:
                exit()

            a = self.ges.get()
            if a.lower() == self.colours[self.iv1.get()]:
                self.counter += 1
                self.score.configure(text = "Your score : {}".format(self.counter))
            
            self.geser.set('')
            self.colours = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
            self.words = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
            self.iv1.set(random.randint(0, len(self.colours)-1))
            self.iv2.set(random.randint(0, len(self.words)-1))
            self.code.configure(text = self.words[self.iv2.get()], fg = self.colours[self.iv1.get()])
        def lesgo(self):
            
            if self.counting == 60:
                self.geser.set('')
                self.colours = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
                self.words = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
                self.iv1.set(random.randint(0, 8))
                self.iv2.set(random.randint(0, 8))
                self.code.configure(text = self.words[self.iv1.get()], fg = self.colours[self.iv2.get()])
            
            self.ges.bind('<Return>', self.lestart)
            self.timer['text'] = "Game ends in : {}".format(self.counting)
            
            if self.counting > 0:
                self.counting = self.counting - 1
                self.root.after(1000, self.lesgo)
            
            if self.counting == 0:
                exit()
    
    class trr:
        def __init__(self, root_2):
            root_2.destroy()
            self.root = tk.Tk()
            self.root.geometry('1600x900')
            self.b = tk.Button(self.root, text = "Click to start")
            self.b.grid()
            self.b.bind('<Button>', self.dier)
            self.root.mainloop()
        def dctb(self):
            
            def cfbc(y):
                if y == 0:

                    if self.poloc.get() == self.plco2.get():
                        exit()
                    elif self.plco3.get() == self.poloc.get():
                        exit()
                    else:
                        self.io.destroy()
                        self.io2.destroy()
                        y = 4
                if y == 4:

                    self.io = tk.Label(self.root, image = self.pi2)
                    self.io2 = tk.Label(self.root,image = self.pi2)
                    self.rrnof = random.randrange(0, 3)
                    a = True

                    while a == True:
                        rnof2 = random.randrange(0, 3)

                        if rnof2 != self.rrnof:
                            a = False

                    self.io.grid(row = self.rrnof, column = y)
                    self.io2.grid(row = rnof2, column = y)
                    self.plco2.set(self.rrnof)
                    self.plco3.set(rnof2)
                self.io.grid(column = y)
                self.io2.grid(column = y)
                
                cfbcfbc(y)
            def cfbcfbc(y):
                self.root.after(225, cfbc, y-1)
            def ctlidky(event):

                if self.poloc.get() != 0:
                    self.poloc.set(self.poloc.get()-1)
                    loc.grid(row = self.poloc.get(), column = 0)
            def octlidky(event):

                if self.poloc.get() != 2:
                    self.poloc.set(self.poloc.get()+1)
                    loc.grid(row = self.poloc.get(), column = 0)
            
            self.poloc = tk.IntVar(self.root, 1)
            self.plco2 = tk.IntVar(self.root, 0)
            self.plco3 = tk.IntVar(self.root, 0)
            self.img = Image.open("C:\\Users\\Gayathri\\Downloads\\dino.jpg")
            self.img2 = Image.open("D:\\Advaith\\Code\\class\\pycode\\cactustrex.png")
            self.img = self.img.resize((160, 80))
            self.img2 = self.img2.resize((160, 80))
            self.pi =  ImageTk.PhotoImage(self.img)
            self.pi2 = ImageTk.PhotoImage(self.img2)
            y = 4
            
            for gsfidky in range(1, 3):
                tk.Label(self.root, text = "      ", height = 5, width = 20).grid(row = 3, column = gsfidky)
            
            tk.Label(self.root, text = "      ", height = 5, width = 20).grid(row = 0, column = 7)
            tk.Label(self.root, text = "      ", height = 5, width = 20).grid(row = 2, column = 7)
            tk.Label(self.root, text = "      ", height = 5, width = 20).grid(row = 1, column = 7)
            loc = tk.Label(self.root, image = self.pi, bg = 'black')
            loc.grid(row = 1, column = 0)
            self.root.bind('<space>', ctlidky)
            self.root.bind('<Down>', octlidky)
            self.root.bind('<Up>', ctlidky)
            self.root.after(750, cfbc, y)
        def dier(self, event):
            self.b.destroy()
            self.dctb()

    class kacg:
        def __init__(self, root_2):
            root_2.destroy() 
            self.xo = self.ro1 = self.ro2 = self.ro3 = self.co1 = self.co2 = self.co3 = self.di1 = self.di2 = 0
            self.root = tk.Tk()
            self.root.title("Knots And Crosses")
            self.myfont = font.Font(root = self.root, family = 'Algerian', size = 12, weight = "bold", overstrike = 1)
            self.b1 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = 'blue4', fg = 'lawn green', command = lambda : self.xoxo(self.b1))
            self.b1.grid(row = 0, column = 0)
            self.b2 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = 'blue4', fg = 'lawn green', command = lambda : self.xoxo(self.b2))
            self.b2.grid(row = 0, column = 1)
            self.b3 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = 'blue4', fg = 'lawn green', command = lambda : self.xoxo(self.b3))
            self.b3.grid(row = 0, column = 2)
            self.b4 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = 'blue4', fg = 'lawn green', command = lambda : self.xoxo(self.b4))
            self.b4.grid(row = 1, column = 0)
            self.b5 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = 'blue4', fg = 'lawn green', command = lambda : self.xoxo(self.b5))
            self.b5.grid(row = 1, column = 1)
            self.b6 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = 'blue4', fg = 'lawn green', command = lambda : self.xoxo(self.b6))
            self.b6.grid(row = 1, column = 2)
            self.b7 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = 'blue4', fg = 'lawn green', command = lambda : self.xoxo(self.b7))
            self.b7.grid(row = 2, column = 0)
            self.b8 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = 'blue4', fg = 'lawn green', command = lambda : self.xoxo(self.b8))
            self.b8.grid(row = 2, column = 1)
            self.b9 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = 'blue4', fg = 'lawn green', command = lambda : self.xoxo(self.b9))
            self.b9.grid(row = 2, column = 2)
            self.root.mainloop()
        def xoxo(self, value):
        
            if self.xo == 1:
                value.config(text = "o", command = lambda : print(end = ""))
                self.xo = 0
            elif self.xo == 0:
                value.config(text = "x", command = lambda : print(end = " "))
                self.xo = 1
            if value == self.b1:
                if self.b1['text'] == "x":
                    self.ro1 += 1
                    self.co1 += 1
                    self.di1 += 1
                else:
                    self.ro1 -= 1
                    self.co1 -= 1
                    self.di1 -= 1
            elif value == self.b2:
                if self.b2['text'] == "x":
                    self.ro1 += 1
                    self.co2 += 1
                else:
                    self.ro1 -= 1
                    self.co2 -= 1
            elif value == self.b3:
                if self.b3['text'] == "x":
                    self.ro1 += 1
                    self.co3 += 1
                    self.di2 += 1
                else:
                    self.ro1 -= 1
                    self.co3 -= 1
                    self.di2 -= 1
            elif value == self.b4:
                if self.b4['text'] == "x":
                    self.ro2 += 1
                    self.co1 += 1
                else:
                    self.ro1 -= 1
                    self.co1 -= 1        
            elif value == self.b5:
                if self.b5['text'] == "x":
                    self.ro2 += 1
                    self.co2 += 1
                    self.di2 += 1
                    self.di1 += 1
                else:
                    self.ro2 -= 1
                    self.co2 -= 1
                    self.di2 -= 1
                    self.di1 -= 1
            elif value == self.b6:
                if self.b6['text'] == "x":
                    self.ro2 += 1
                    self.co3 += 1
                else:
                    self.ro2 -= 1
                    self.co3 -= 1
            elif value == self.b7:
                if self.b7['text'] == "x":
                    self.ro3 += 1
                    self.co1 += 1
                    self.di2 += 1
                else:
                    self.ro3 -= 1
                    self.co1 -= 1
                    self.di2 -= 1
            elif value == self.b8:
                if self.b8['text'] == "x":
                    self.ro3 += 1
                    self.co2 += 1
                else:
                    self.ro3 -= 1
                    self.co2 -= 1
            else:
                if self.b9['text'] == "x":
                    self.ro3 += 1
                    self.co3 += 1
                    self.di1 += 1
                else:
                    self.ro3 -= 1
                    self.co3 -= 1
                    self.di1 -= 1
            
            ln = [self.ro1, self.ro2, self.ro3, self.co1, self.co2, self.co3, self.di1, self.di2]
            lb = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]
            a = 0
            
            for ele in lb:
                if ele['text'] != " ":
                    a += 1
            
            if a == 9:
                print(" ")
                exit("Tie")
            
            if 3 in ln:
                print(" ")
                exit("X won")
            elif -3 in ln:
                print(" ")
                exit("O won")   
    
    class boxes:

        def __init__(self, root_2):
            root_2.destroy()
            root = tk.Tk()
            root.title("dots and boxes")
            self.head = tk.Canvas(root, height = 180, width = 180)
            self.head.grid()
            self.counter = 0
            myfont = font.Font(root = root, family = 'Times', weight = 'bold')
            self.p1v = 0
            self.p2v = 0
            self.p1 = tk.Label(root, text = "Player1 - 0", bg = 'red', height = 3, width = 15, font = myfont)
            self.p2 = tk.Label(root, text = "Player2 - 0", bg = 'blue', height = 3, width = 15, font = myfont)
            self.p1.grid(column = 1, row = 0, sticky = 'n')
            self.p2.grid(column = 1, row = 0, sticky = 'n', pady = 75)
            for j in range(5):
                for i in range(5):
                    self.head.create_oval((40*i)+10, (40*j)+10, (40*i)+14, (40*j)+14, fill = 'green', tag = 'anoval')

            self.head.bind('<Button>', self.heady)
            root.mainloop()

        def nbm(self, coords, vorh, step):
            x1, y1, x2, y2 = coords
            a = []
            b = []

            if vorh == 'vertical':
                xm = (x1+x2)/2
                ym = (y1+y2)/2
                bm = [xm - 20, ym]
                am = [xm + 20, ym]
            elif vorh == 'horizontal':
                xm = (x1+x2)/2
                ym = (y1+y2)/2
                bm = [xm, ym - 20]
                am = [xm, ym + 20]
            
            for loop1 in self.head.find_enclosed(bm[0]-40, bm[1]-40, bm[0]+40, bm[1]+40):
                if loop1 > 25:
                    a.append(loop1)
            for loop2 in self.head.find_enclosed(am[0]-40, am[1]-40, am[0]+40, am[1]+40):
                if loop2 > 25:
                    b.append(loop2)
            if len(a) == 4:
                if step == 0:
                    self.head.create_text(bm[0], bm[1], text = "Player1", fill = 'red')
                    self.p1v += 1
                    self.p1.configure(text = "Player1 - {}".format(self.p1v))
                else:
                    self.p2v += 1
                    self.p2.configure(text = "Player2 - {}".format(self.p2v))
                    self.head.create_text(bm[0], bm[1], text = "Player2", fill = 'blue')
            if len(b) == 4:
                if step == 0:
                    self.p1v += 1
                    self.p1.configure(text = "Player1 - {}".format(self.p1v))
                    self.head.create_text(am[0], am[1], text = "Player1", fill = 'red')
                else:
                    self.p2v += 1
                    self.p2.configure(text = "Player2 - {}".format(self.p2v))
                    self.head.create_text(am[0], am[1], text = "Player2", fill = 'blue')
            if len(a) != 4 and len(b) != 4:
                if step == 0:
                    step = 1
                else:
                    step = 0
            return step

        def heady(self, event):
            x = (event.x-10)%40
            y = (event.y-10)%40
            exx = event.x-x
            eyy = event.y-y
            tagid = self.head.find_withtag('line')
            ftc = self.head.find_closest(event.x, event.y)
            if event.x < 10 or event.y < 10:
                return
            elif event.x > 180 or event.y > 180: 
                return
            if ftc[0] not in tagid:
                if x <= 8:
                    if y <= 8:
                        return
                    vh = 'vertical'
                    if self.counter == 1:
                        li = self.head.create_line(exx, eyy, exx, eyy+40, fill = 'blue', tags = 'line')
                    else:
                        li = self.head.create_line(exx, eyy, exx, eyy+40, fill = 'red', tags = 'line')
                    self.counter = self.nbm(self.head.coords(li), vh, self.counter)
                elif y <= 8:
                    vh = 'horizontal'
                    if self.counter == 1:
                        li = self.head.create_line(exx, eyy, exx+40, eyy, fill = 'blue', tags = 'line')
                    else:
                        li = self.head.create_line(exx, eyy, exx+40, eyy, fill = 'red', tags = 'line')
                    self.counter = self.nbm(self.head.coords(li), vh, self.counter)
    
    root_2.geometry('1600x900')
    locfb = ["arrow", "circle", "clock", "cross", "dotbox", "exchange", "fleur", "heart", "heart", "man", "mouse", "pirate", "plus", "shuttle", "sizing", "spider", "spraycan", "star", "target", "tcross", "trek", "watch"]
    myfont = font.Font(family="algerian", size=12, root = root_2, weight = "bold")

    tk.Label(root_2, text = " ", width = 85, height = 18).grid(row = 0, column = 0)
    
    tk.Button(root_2, text = "Click for Cube", command = lambda : cubegame(root_2), width = 20, height = 4, bg = 'red', cursor = locfb[random.randrange(0, len(locfb))], font = myfont).grid(row = 1, column = 1)
    
    tk.Button(root_2, text = "Click for Hangman", command = lambda : hangmang(root_2), width = 20, height = 4, bg = 'blue', cursor = locfb[random.randrange(0, len(locfb))], font = myfont).grid(row = 1, column = 2)
    
    tk.Button(root_2, text = "Click for color game", command = lambda : cg(root_2), width = 20, height = 4, bg = 'yellow', cursor = locfb[random.randrange(0, len(locfb))], font = myfont).grid(row = 2, column = 1)
    
    tk.Button(root_2, text = "Click for trex run", command = lambda : trr(root_2), width = 20, height = 4, bg = 'green', cursor = locfb[random.randrange(0, len(locfb))], font = myfont).grid(row = 2, column = 2)
    
    tk.Button(root_2, text = "Click for X and O", command = lambda : kacg(root_2), width = 20, height = 4, bg = 'orange', cursor = locfb[random.randrange(0, len(locfb))], font = myfont).grid(row = 3, column = 2)
    
    tk.Button(root_2, text = "Click for boxes", command = lambda : boxes(root_2), width = 20, height = 4, bg = 'pink', cursor = locfb[random.randrange(0, len(locfb))], font = myfont).grid(row = 3, column = 1)

root = tk.Tk()
fina = "minetdm"
a = 1
b = 0
root_2 = 0

def showing():
    global a

    if a == 1:
        shower.config(text = "Hide letters")
        password.config(show = "")

        a = 0
    elif a == 0:
        shower.config(text = "Show letters")
        
        a = 1

        password.config(show = "*")
def openinger(event):
    global root_2, root, a, b
    if passvar.get().lower() == fina:
        root_2 = tk.Tk()
        root.destroy()

        saep()
    else:
        shower.config(text = "Hide letters")
        password.config(show = "")
        
        a = 0
        b += 1
        
        passvar.set("no")
        
        if b == 6:
            exit("theif")

passvar = tk.StringVar(root, 'minetdm')
password = tk.Entry(root, textvariable = passvar, show = "*")
shower = tk.Button(root, text = "Show letters", command = showing)
shower.grid()
password.grid()
password.bind('<Return>', openinger)
root.mainloop()