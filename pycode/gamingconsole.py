import tkinter as tk
import random
import tkinter.font as font
def hangmang():
    global root
    root.destroy()
    def guestsetting(event):
        guest.set('')
    def correct(event):
        global guess, word, guest, blankp, counting, root, listword, blank, count, myfont
        guest.set(guest.get().lower())
        guess.configure(textvariable = guest)
        if len(guess.get()) != 1:
            if guest.get() == word:
                guest.set('congrats')
                blankp.configure(text = "Congrats")
                root.title('congrats')
                counting.configure(text = word)
                a = tk.Button(root, text = "Quit", height = 4, width = 20, bg = 'red',command = lambda : quit())
                a.grid(row = 2, column = 2)
                a['font'] = myfont
            else:
                if len(guess.get()) != 0:
                    count.set(count.get()+1)
                    counting.configure(text = "wrongs: %s/6" %(count.get()))
            if count.get() >= 6:
                guest.set('loser')
                blankp.configure(text = "loser")
                root.title('loser')
                counting.configure(text = word)
                a = tk.Button(root, text = "Quit", height = 4, width = 20, bg = 'red',command = lambda : quit())
                a.grid(row = 2, column = 2)
                a['font'] = myfont
            guest.set('')
        else:
            loop = 0
            blank_2 = ""
            if guess.get() in listword:
                if guess.get() in list(blank):
                    count.set(int(count.get())+1)
                    counting.configure(text = "wrongs: %s/6" %(count.get()))
                    guest.set('')
                else:
                    for ele in listword:
                        if ele == guess.get():
                            blank = blank.split(' ')
                            blank[loop] = ele
                            for ele_2 in blank:
                                blank_2 += ele_2
                                blank_2 += " "
                            blank = blank_2
                            blank_2 = ""
                        loop += 1
                    blankp.configure(text = blank)
                    guest.set('')
            else:
                if len(guess.get()) != 0:
                    count.set(int(count.get())+1)
                    counting.configure(text = "wrongs: %s/6" %(count.get()))
                    guest.set('')
            if '_' in blank:
                if count.get() >= 6:
                    guest.set('loser')
                    blankp.configure(text = "loser")
                    root.title('loser')
                    counting.configure(text = word)
                    a = tk.Button(root, text = "Quit", height = 4, width = 20, bg = 'red',command = lambda : quit())
                    a.grid(row = 2, column = 2)
                    a['font'] = myfont
            else:
                guest.set('congrats')
                blankp.configure(text = "Congrats")
                root.title('congrats')
                counting.configure(text = word)
                a = tk.Button(root, text = "Quit", height = 4, width = 20, bg = 'red',command = lambda : quit())
                a.grid(row = 2, column = 2)
                a['font'] = myfont
            guest.set('')
    def nextlevel():
        global guess, word, guest, blankp, counting, root, listword, count, blank, words, myfont
        root = tk.Tk()
        root.title("hangman")
        root.geometry('5000x1000')
        myfont = font.Font(size = 12, font = 'algerian')
        count = tk.IntVar()
        words = ['armadillo', 'beaver', 'chimpanzee', 'dolphin', 'earthworm', 'flamingo'\
            ,'gorilla', 'hedgehog', 'iguana', 'jaguar', 'kingfisher', 'llama', 'mangoose'\
            , 'otter', 'possum', 'rhea', 'salmon', 'turkey', 'vulture', 'woodpecker'\
            , '']
        word = words[random.randrange(0, len(words))]
        blank = ""
        listword = []
        for ele in word:
            listword += ele
        blank += listword[0]
        for loop in range(0, len(word)-1):
            blank = blank + " _"
        loop += 1
        tk.Label(root, text = " ", width = 100).grid(row = 0, column = 0)
        tk.Label(root, text = " ", height = 20).grid(row = 0, column = 1)
        counting = tk.Label(root, text = "wrongs: %s/6" %(count.get()), width = 20, height = 4, bg = 'green')
        counting.grid(row = 1, column = 1)
        counting['font'] = myfont
        blankp = tk.Label(root, text = blank, width = 20, height = 4, bg = 'orange', font = 'algerian')
        blankp.grid(row = 1, column = 2)
        blankp['font'] = myfont
        guest = tk.StringVar()
        guest.set('Guess the animal')
        guess = tk.Entry(root, textvariable = guest, width = 20)
        guess.grid(row = 2, column = 1)
        d = tk.Label(root, text = " ", height = 4)
        d.grid(row = 2, column = 3)
        guess['font'] = myfont
        guess.bind('<Button>', guestsetting)
        guess.bind('<Return>', correct)
        if guess.get() == "":
            count.set(int(count.get())-1)
        root.mainloop()
    nextlevel()
def cubegame():
    global root
    root.destroy()
    root = tk.Tk()
    root.title('Cube')
    root.geometry('5000x1000')
    def entering(move, f, t, r, l, d, b):
        z = -1
        if move == "R":
            g, c, e = f[6], f[7], f[8]
            f[6], f[7], f[8] = d[2], d[1], d[0]
            d[0], d[1], d[2] = b[0], b[1], b[2]
            b[0], b[1], b[2] = t[8], t[7], t[6]
            t[6], t[7], t[8] = g, c, e
            h, i, j, k = r[0], r[7], r[8], r[1]
            r[0], r[7], r[8], r[1] = r[2], r[3], r[6], r[5]
            r[6], r[3], r[2], r[5] = h, k, j, i
            for x in range(2, 5):
                for y in range(2, 5):
                    z+=1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "R'":
            g, c, e = f[6], f[7], f[8]
            f[6], f[7], f[8] = t[6], t[7], t[8]
            t[6], t[7], t[8] = b[2], b[1], b[0]
            b[0], b[1], b[2] = d[0], d[1], d[2]
            d[0], d[1], d[2] = e, c, g
            k,h,i,j = r[6], r[5], r[2], r[3]
            r[6], r[5], r[2], r[3] = r[8], r[1], r[0], r[7]
            r[0], r[1], r[7], r[8] = k, j, h, i
            for x in range(2, 5):
                for y in range(2, 5):
                    z+=1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "L":
            g, c, e = f[0], f[1], f[2]
            f[0], f[1], f[2] = t[0], t[1], t[2]
            t[0], t[1], t[2] = b[8], b[7], b[6]
            b[6], b[7], b[8] = d[6], d[7], d[8]
            d[6], d[7], d[8] = e, c, g
            h, i, j, k = l[0], l[7], l[8], l[1]
            l[0], l[7], l[8], l[1] = l[2], l[3], l[6], l[5]
            l[6], l[3], l[2], l[5] = h, k, j, i
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "L'":
            g, c, e = f[0], f[1], f[2]
            f[0], f[1], f[2] = d[8], d[7], d[6]
            d[6], d[7], d[8] = b[8], b[7], b[6]
            b[6], b[7], b[8] = t[2], t[1], t[0]
            t[0], t[1], t[2] = g, c, e
            k,h,i,j = l[6], l[5], l[2], l[3]
            l[6], l[5], l[2], l[3] = l[8], l[1], l[0], l[7]
            l[0], l[1], l[7], l[8] = k, j, h, i
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "U":
            g, c, e = f[0], f[3], f[6]
            f[0], f[3], f[6] = r[2], r[1], r[0]
            r[0], r[1], r[2] = b[6], b[3], b[0]
            b[0], b[3], b[6] = l[6], l[7], l[8]
            l[6], l[7], l[8] = g, c, e
            h, i, j, k = t[0], t[7], t[8], t[1]
            t[0], t[7], t[8], t[1] = t[2], t[3], t[6], t[5]
            t[6], t[3], t[2], t[5] = h, k, j, i
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "U'":
            g, c, e = f[0], f[3], f[6]
            f[0], f[3], f[6] = l[6], l[7], l[8]
            l[6], l[7], l[8] = b[0], b[3], b[6]
            b[0], b[3], b[6] = r[2], r[1], r[0]
            r[0], r[1], r[2] = e, c, g
            k,h,i,j = t[6], t[5], t[2], t[3]
            t[6], t[5], t[2], t[3] = t[8], t[1], t[0], t[7]
            t[0], t[1], t[7], t[8] = k, j, h, i
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "D":
            g, c, e = f[2], f[5], f[8]
            f[2], f[5], f[8] = l[0], l[1], l[2]
            l[0], l[1], l[2] = b[8], b[5], b[2]
            b[2], b[5], b[8] = r[6], r[7], r[8]
            r[6], r[7], r[8] = g, c, e
            k,h,i,j = d[6], d[5], d[2], d[3]
            d[6], d[5], d[2], d[3] = d[8], d[1], d[0], d[7]
            d[0], d[1], d[7], d[8] = k, j, h, i
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "D'":
            g, c, e = f[2], f[5], f[8]
            f[2], f[5], f[8] = r[8], r[7], r[6]
            r[6], r[7], r[8] = b[8], b[5], b[2]
            b[2], b[5], b[8] = l[0], l[1], l[2]
            l[0], l[1], l[2] = g, c, e
            h, i, j, k = d[0], d[7], d[8], d[1]
            d[0], d[7], d[8], d[1] = d[2], d[3], d[6], d[5]
            d[6], d[3], d[2], d[5] = h, k, j, i
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "F":
            g, c, e = r[2], r[5], r[8]
            r[2], r[5], r[8] = t[2], t[5], t[8]
            t[2], t[5], t[8] = l[2], l[5], l[8]
            l[2], l[5], l[8] = d[2], d[5], d[8]
            d[2], d[5], d[8] = g, c, e
            h, i, j, k = f[0], f[7], f[8], f[1]
            f[0], f[7], f[8], f[1] = f[2], f[3], f[6], f[5]
            f[6], f[3], f[2], f[5] = h, k, j, i
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "F'":
            g, c, e = r[2], r[5], r[8]
            r[2], r[5], r[8] = d[2], d[5], d[8]
            d[2], d[5], d[8] = l[2], l[5], l[8]
            l[2], l[5], l[8] = t[2], t[5], t[8]
            t[2], t[5], t[8] = g, c, e 
            k,h,i,j = f[6], f[5], f[2], f[3]
            f[6], f[5], f[2], f[3] = f[8], f[1], f[0], f[7]
            f[0], f[1], f[7], f[8] = k, j, h, i
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "B":
            g, c, e = r[0], r[3], r[6]
            r[0], r[3], r[6] = t[0], t[3], t[6]
            t[0], t[3], t[6] = l[0], l[3], l[6]
            l[0], l[3], l[6] = d[0], d[3], d[6]
            d[0], d[3], d[6] = g, c, e
            h, i, j, k = b[0], b[7], b[8], b[1]
            b[0], b[7], b[8], b[1] = b[2], b[3], b[6], b[5]
            b[6], b[3], b[2], b[5] = h, k, j, i
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "B'":
            g, c, e = r[0], r[3], r[6]
            r[0], r[3], r[6] = d[0], d[3], d[6]
            d[0], d[3], d[6] = l[0], l[3], l[6]
            l[0], l[3], l[6] = t[0], t[3], t[6]
            t[0], t[3], t[6] = g, c, e
            k,h,i,j = b[6], b[5], b[2], b[3]
            b[6], b[5], b[2], b[3] = b[8], b[1], b[0], b[7]
            b[0], b[1], b[7], b[8] = k, j, h, i
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "M":
            g, c, e = f[3], f[4], f[5]
            f[3], f[4], f[5] = t[3], t[4], t[5]
            t[3], t[4], t[5] = b[5], b[4], b[3]
            b[5], b[4], b[3] = d[5], d[4], d[3]
            d[5], d[4], d[3] = g, c, e
            a.configure(text = "facing-{}".format(f[4]), fg = f[4], bg = t[4])
            s.configure(text = "on top-{}".format(t[4]), fg = t[4], bg = f[4])
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "M'":
            g, c, e = f[3], f[4], f[5]
            f[3], f[4], f[5] = d[5], d[4], d[3]
            d[5], d[4], d[3] = b[5], b[4], b[3]
            b[5], b[4], b[3] = t[3], t[4], t[5]
            t[3], t[4], t[5] = g, c, e
            a.configure(text = "facing-{}".format(f[4]), fg = f[4], bg = t[4])
            s.configure(text = "on top-{}".format(t[4]), fg = t[4], bg = f[4])
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "S":
            g, c, e = r[1], r[4], r[7]
            r[1], r[4], r[7] = t[1], t[4], t[7]
            t[1], t[4], t[7] = l[1], l[4], l[7]
            l[1], l[4], l[7] = d[1], d[4], d[7]
            d[1], d[4], d[7] = g, c, e
            a.configure(bg = t[4])
            s.configure(text = "on top-{}".format(t[4]), fg = t[4], bg = f[4])
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "S'":
            g, c, e = r[1], r[4], r[7]
            r[1], r[4], r[7] = d[1], d[4], d[7]
            d[1], d[4], d[7] = l[1], l[4], l[7]
            l[1], l[4], l[7] = t[1], t[4], t[7]
            t[1], t[4], t[7] = g, c, e
            a.configure(bg = t[4])
            s.configure(text = "on top-{}".format(t[4]), fg = t[4], bg = f[4])
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "E":
            g, c, e = f[1], f[4], f[7]
            f[1], f[4], f[7] = l[5], l[4], l[3]
            l[5], l[4], l[3] = b[1], b[4], b[7]
            b[1], b[4], b[7] = r[5], r[4], r[3]
            r[5], r[4], r[3] = e, c, g
            a.configure(text = "facing-{}".format(f[4]), fg = f[4], bg = t[4])
            s.configure(bg = f[4])
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "E'":
            g, c, e = f[1], f[4], f[7]
            f[1], f[4], f[7] = r[5], r[4], r[3]
            r[5], r[4], r[3] = b[1], b[4], b[7]
            b[1], b[4], b[7] = l[3], l[4], l[5]
            l[3], l[4], l[5] = e, c, g
            a.configure(text = "facing-{}".format(f[4]), fg = f[4], bg = t[4])
            s.configure(bg = f[4])
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "X":
            g, c, e = f[3], f[4], f[5]
            f[3], f[4], f[5] = d[5], d[4], d[3]
            d[5], d[4], d[3] = b[5], b[4], b[3]
            b[5], b[4], b[3] = t[3], t[4], t[5]
            t[3], t[4], t[5] = g, c, e
            g, c, e = f[6], f[7], f[8]
            f[6], f[7], f[8] = d[2], d[1], d[0]
            d[0], d[1], d[2] = b[0], b[1], b[2]
            b[0], b[1], b[2] = t[8], t[7], t[6]
            t[6], t[7], t[8] = g, c, e
            h, i, j, k = r[0], r[7], r[8], r[1]
            r[0], r[7], r[8], r[1] = r[2], r[3], r[6], r[5]
            r[6], r[3], r[2], r[5] = h, k, j, i
            g, c, e = f[0], f[1], f[2]
            f[0], f[1], f[2] = d[8], d[7], d[6]
            d[6], d[7], d[8] = b[8], b[7], b[6]
            b[6], b[7], b[8] = t[2], t[1], t[0]
            t[0], t[1], t[2] = g, c, e
            k,h,i,j = l[6], l[5], l[2], l[3]
            l[6], l[5], l[2], l[3] = l[8], l[1], l[0], l[7]
            l[0], l[1], l[7], l[8] = k, j, h, i
            a.configure(text = "facing-{}".format(f[4]), fg = f[4], bg = t[4])
            s.configure(text = "on top-{}".format(t[4]), fg = t[4], bg = f[4])
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "X'":
            g, c, e = f[6], f[7], f[8]
            f[6], f[7], f[8] = t[6], t[7], t[8]
            t[6], t[7], t[8] = b[2], b[1], b[0]
            b[0], b[1], b[2] = d[0], d[1], d[2]
            d[0], d[1], d[2] = e, c, g
            k,h,i,j = r[6], r[5], r[2], r[3]
            r[6], r[5], r[2], r[3] = r[8], r[1], r[0], r[7]
            r[0], r[1], r[7], r[8] = k, j, h, i
            g, c, e = f[0], f[1], f[2]
            f[0], f[1], f[2] = t[0], t[1], t[2]
            t[0], t[1], t[2] = b[8], b[7], b[6]
            b[6], b[7], b[8] = d[6], d[7], d[8]
            d[6], d[7], d[8] = e, c, g
            h, i, j, k = l[0], l[7], l[8], l[1]
            l[0], l[7], l[8], l[1] = l[2], l[3], l[6], l[5]
            l[6], l[3], l[2], l[5] = h, k, j, i
            g, c, e = f[3], f[4], f[5]
            f[3], f[4], f[5] = t[3], t[4], t[5]
            t[3], t[4], t[5] = b[5], b[4], b[3]
            b[5], b[4], b[3] = d[5], d[4], d[3]
            d[5], d[4], d[3] = g, c, e
            a.configure(text = "facing-{}".format(f[4]), fg = f[4], bg = t[4])
            s.configure(text = "on top-{}".format(t[4]), fg = t[4], bg = f[4])
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "Y":
            g, c, e = f[1], f[4], f[7]
            f[1], f[4], f[7] = r[5], r[4], r[3]
            r[5], r[4], r[3] = b[1], b[4], b[7]
            b[1], b[4], b[7] = l[3], l[4], l[5]
            l[3], l[4], l[5] = e, c, g
            g, c, e = f[2], f[5], f[8]
            f[2], f[5], f[8] = r[8], r[7], r[6]
            r[6], r[7], r[8] = b[8], b[5], b[2]
            b[2], b[5], b[8] = l[0], l[1], l[2]
            l[0], l[1], l[2] = g, c, e
            h, i, j, k = d[0], d[7], d[8], d[1]
            d[0], d[7], d[8], d[1] = d[2], d[3], d[6], d[5]
            d[6], d[3], d[2], d[5] = h, k, j, i
            g, c, e = f[0], f[3], f[6]
            f[0], f[3], f[6] = r[2], r[1], r[0]
            r[0], r[1], r[2] = b[6], b[3], b[0]
            b[0], b[3], b[6] = l[6], l[7], l[8]
            l[6], l[7], l[8] = g, c, e
            h, i, j, k = t[0], t[7], t[8], t[1]
            t[0], t[7], t[8], t[1] = t[2], t[3], t[6], t[5]
            t[6], t[3], t[2], t[5] = h, k, j, i
            a.configure(text = "facing-{}".format(f[4]), fg = f[4], bg = t[4])
            s.configure(text = "on top-{}".format(t[4]), fg = t[4], bg = f[4])
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "Y'":
            g, c, e = f[2], f[5], f[8]
            f[2], f[5], f[8] = l[0], l[1], l[2]
            l[0], l[1], l[2] = b[8], b[5], b[2]
            b[2], b[5], b[8] = r[6], r[7], r[8]
            r[6], r[7], r[8] = g, c, e
            k,h,i,j = d[6], d[5], d[2], d[3]
            d[6], d[5], d[2], d[3] = d[8], d[1], d[0], d[7]
            d[0], d[1], d[7], d[8] = k, j, h, i
            g, c, e = f[0], f[3], f[6]
            f[0], f[3], f[6] = l[6], l[7], l[8]
            l[6], l[7], l[8] = b[0], b[3], b[6]
            b[0], b[3], b[6] = r[2], r[1], r[0]
            r[0], r[1], r[2] = e, c, g
            k,h,i,j = t[6], t[5], t[2], t[3]
            t[6], t[5], t[2], t[3] = t[8], t[1], t[0], t[7]
            t[0], t[1], t[7], t[8] = k, j, h, i
            g, c, e = f[1], f[4], f[7]
            f[1], f[4], f[7] = l[5], l[4], l[3]
            l[5], l[4], l[3] = b[1], b[4], b[7]
            b[1], b[4], b[7] = r[5], r[4], r[3]
            r[5], r[4], r[3] = e, c, g
            a.configure(text = "facing-{}".format(f[4]), fg = f[4], bg = t[4])
            s.configure(text = "on top-{}".format(t[4]), fg = t[4], bg = f[4])
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "Z":
            g, c, e = r[0], r[3], r[6]
            r[0], r[3], r[6] = d[0], d[3], d[6]
            d[0], d[3], d[6] = l[0], l[3], l[6]
            l[0], l[3], l[6] = t[0], t[3], t[6]
            t[0], t[3], t[6] = g, c, e
            k,h,i,j = b[6], b[5], b[2], b[3]
            b[6], b[5], b[2], b[3] = b[8], b[1], b[0], b[7]
            b[0], b[1], b[7], b[8] = k, j, h, i
            g, c, e = r[2], r[5], r[8]
            r[2], r[5], r[8] = t[2], t[5], t[8]
            t[2], t[5], t[8] = l[2], l[5], l[8]
            l[2], l[5], l[8] = d[2], d[5], d[8]
            d[2], d[5], d[8] = g, c, e
            h, i, j, k = f[0], f[7], f[8], f[1]
            f[0], f[7], f[8], f[1] = f[2], f[3], f[6], f[5]
            f[6], f[3], f[2], f[5] = h, k, j, i
            g, c, e = r[1], r[4], r[7]
            r[1], r[4], r[7] = t[1], t[4], t[7]
            t[1], t[4], t[7] = l[1], l[4], l[7]
            l[1], l[4], l[7] = d[1], d[4], d[7]
            d[1], d[4], d[7] = g, c, e
            a.configure(bg = t[4])
            s.configure(text = "on top-{}".format(t[4]), fg = t[4], bg = f[4])
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "Z'":
            g, c, e = r[0], r[3], r[6]
            r[0], r[3], r[6] = t[0], t[3], t[6]
            t[0], t[3], t[6] = l[0], l[3], l[6]
            l[0], l[3], l[6] = d[0], d[3], d[6]
            d[0], d[3], d[6] = g, c, e
            h, i, j, k = b[0], b[7], b[8], b[1]
            b[0], b[7], b[8], b[1] = b[2], b[3], b[6], b[5]
            b[6], b[3], b[2], b[5] = h, k, j, i
            g, c, e = r[1], r[4], r[7]
            r[1], r[4], r[7] = d[1], d[4], d[7]
            d[1], d[4], d[7] = l[1], l[4], l[7]
            l[1], l[4], l[7] = t[1], t[4], t[7]
            t[1], t[4], t[7] = g, c, e
            g, c, e = r[2], r[5], r[8]
            r[2], r[5], r[8] = d[2], d[5], d[8]
            d[2], d[5], d[8] = l[2], l[5], l[8]
            l[2], l[5], l[8] = t[2], t[5], t[8]
            t[2], t[5], t[8] = g, c, e 
            k,h,i,j = f[6], f[5], f[2], f[3]
            f[6], f[5], f[2], f[3] = f[8], f[1], f[0], f[7]
            f[0], f[1], f[7], f[8] = k, j, h, i
            a.configure(text = "facing-{}".format(f[4]), fg = f[4], bg = t[4])
            s.configure(text = "on top-{}".format(t[4]), fg = t[4], bg = f[4])
            for x in range(2, 5):
                for y in range(2, 5):
                    z += 1
                    tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
        elif move == "exit":
            exit("bye")
    def returning(event):
        entering(w.get(), f, t, r, l, d, b)
        w.set('')
    def shufling(event):
        p = ["R", "R'", "L", "L'", "U", "U'", "D", "D'", "F", "F'", "B", "B'", "M", "M'", "E", "E'", "S", "S'"]
        for loop in range(0, 15):
            n = random.randrange(0, len(p))
            entering(p[n], f, t, r, l, d, b)
        n = loop
    f = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
    d = ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']
    b = ['yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow', 'yellow']
    t = ['red', 'red', 'red', 'red', 'red', 'red', 'red', 'red', 'red']
    l = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
    r = ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']
    z = -1
    myfont = font.Font(size = 12, font = 'algerian')
    tk.Label(root, text = " ", height = 20).grid(row = 0, column = 1)
    tk.Label(root, text = " ", width = 100).grid(row = 1, column = 0)
    for x in range(2, 5):
        for y in range(2, 5):
            z += 1
            tk.Label(root, text = " n  ", fg = f[z], bg = f[z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
    moveer = tk.Label(root, text = "move = ", width = 12)
    moveer.grid(row = 1, column = 1)
    moveer['font'] = myfont
    w = tk.StringVar()
    ac = tk.Entry(root, text = w)
    ac.grid(row = 2, column = 1)
    a = tk.Label(root, text = "facing-black", fg = 'black', bg = 'red', width = 12)
    a.grid(row = 5, column = 1)
    a['font'] = myfont
    s = tk.Label(root, text = "on top-red", fg = 'red', bg = 'black', width = 12)
    s.grid(row = 6, column = 1)
    s['font'] = myfont
    ac.bind("<Return>", returning)
    q = tk.Button(root, text = "Shuffle", bg = 'sea green', width = 12)
    q.grid(row = 7, column = 1)
    q['font'] = myfont
    q.bind("<Button>", shufling)
    root.mainloop()
def bsg():
    pass
def mmg():
    pass
root = tk.Tk()
root.geometry('1600x900')
myfont = font.Font(size = 12, font = 'algerian')
tk.Label(root, text = " ", width = 100).grid(row = 1, column = 0)
tk.Label(root, text = " ", height = 20).grid(row = 0, column = 1)
tk.Button(root, text = "Click for Cube", command = cubegame, width = 20, height = 4, bg = 'red', font = myfont).grid(row = 1, column = 1)
tk.Button(root, text = "Click for Hangman", command = hangmang, width = 20, height = 4, bg = 'blue', font = myfont).grid(row = 1, column = 2)
tk.Button(root, text = "W-I-P", command = bsg, width = 20, height = 4, bg = 'green', font = myfont).grid(row = 2, column = 1)
tk.Button(root, text = "W-I-P", command = mmg, width = 20, height = 4, bg = 'yellow', font = myfont).grid(row = 2, column = 2)
root.mainloop()