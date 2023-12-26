import tkinter as tk
import pandas as pd
import random
from tkinter import font

class geoquiz:
    def __init__(self, app, game=0, gametype=""):
        self.app = app
        self.game = game
        self.gt = gametype

        self.app.rowconfigure(0, weight=1)
        self.app.columnconfigure(0, weight=1)
        self.app.title("Geography Quiz!")

        self.root = tk.Frame(self.app)
        self.root.grid(sticky="nsew")
        self.BREAKLENGTH = 30
        
        self.myfont = font.Font(self.root, family="Helvetica", size=17)
        self.myfont2 = font.Font(self.root, family="Times", size=15)
        self.ds = pd.read_csv("test.txt")
        self.cluecounter = 0

        if self.game == 0:
            self.app.minsize(100, 100)
            self.app.geometry("650x350+400+200")
            tk.Label(self.root, text="Which quiz do you want to play?", font=self.myfont2, bg="blue2", fg="White").grid(row=0, column=0, sticky="nsew")
            tk.Button(self.root, text="Guess the Country", font=self.myfont2, command= lambda: self.replay("", 1), bg="MediumPurple4", fg="White", activebackground="black", activeforeground="white", relief="groove").grid(row=1, column=0, sticky="nsew")
            tk.Button(self.root, text="Guess the Capital", font=self.myfont2, command= lambda: self.replay("", 2, "capital"), bg="saddlebrown", fg="White", activebackground="black", activeforeground="white", relief="groove").grid(row=2, column=0, sticky="nsew")
            tk.Button(self.root, text="Guess the Currency", font=self.myfont2, command= lambda: self.replay("", 2, "currency"), bg="#004d39", fg="White", activebackground="black", activeforeground="white", relief="groove").grid(row=3, column=0, sticky="nsew")
            tk.Button(self.root, text="Guess the Languages", font=self.myfont2, command= lambda: self.replay("", 2, "language"), bg="#334d00", fg="White", activebackground="black", activeforeground="white", relief="groove").grid(row=4, column=0, sticky="nsew")
            self.root.columnconfigure(0, weight=1)
            self.root.rowconfigure(0, weight=1)
            self.root.rowconfigure(1, weight=2)
            self.root.rowconfigure(2, weight=2)
            self.root.rowconfigure(3, weight=2)
            self.root.rowconfigure(4, weight=2)
            self.submit = tk.Button(self.root, text="Submit!", justify="center", font=self.myfont2, relief="groove", activeforeground="white", bg="rosybrown1", activebackground="gray20")

        else:
            self.index = self.ds.loc[random.randint(0, 49)]
            self.frame = tk.Frame(self.root)
            self.hint = tk.Button(self.root, text="Reveal the next clue", justify="center", font=self.myfont2, relief="solid", activeforeground="brown", command=self.reveal, disabledforeground="blue", bg="lightsalmon")
            self.stringvar = tk.StringVar(self.root)
            self.guess = tk.Entry(self.frame, font=self.myfont, justify="center", textvariable=self.stringvar)
            self.lbofcont = tk.Listbox(self.frame, background="khaki1", font=self.myfont2, selectbackground = 'gray80', selectforeground = 'black', activestyle = 'dotbox')
            self.sb = tk.Scrollbar(self.frame, command = self.lbofcont.yview, orient = 'vertical')
            self.submit = tk.Button(self.root, text="Submit!", justify="center", font=self.myfont2, relief="groove", activeforeground="white", bg="rosybrown1", activebackground="gray20")
            self.lbofcont.configure(yscrollcommand = self.sb.set)
        
        if self.game == 1:
            self.app.minsize(750, 600)
            self.app.geometry("750x600+375+60")
            self.app.title("Guess the Country - A Geography Quiz.")

            self.stringvar.set("Guess the country!")

            self.specialcountrynames = {"usa":"United States", "united states of america":"United States",\
                "drc":"Democratic Republic of the Congo", "Democratic republic of congo":"Democratic Republic of the Congo",\
                "turkey":"Turkiye", "uae":"United Arab Emirates", "uk":"United Kingdom", "car":"Central African Republic",\
                "burma":"Myanmar", "swaziland":"Eswatini", "cote divoire": "Ivory Coast"}
            self.locountries = list(self.ds["country"])
            self.locountries.sort()

            self.clue1 = tk.Label(self.root, text=self.bettervisuals(self.index["clue 1"]), font=self.myfont, justify="center", bg="light green")
            self.clue2 = tk.Label(self.root, text=self.bettervisuals(self.index["clue 2"]), font=self.myfont, justify="center", bg="light blue")
            self.continent = tk.Label(self.root, text="Continent: "+self.index["continent"], font=self.myfont, justify="center", bg="light gray")
            self.capital = tk.Label(self.root, text="Capital: "+self.bettervisuals(self.index["capital"]), font=self.myfont, justify="center", bg="lavender")
            self.country = tk.Label(self.root, text="Country: "+self.index["country"], font=self.myfont, justify="center", bg="light goldenrod")

            for ele in self.locountries: self.lbofcont.insert("end", ele)

            self.guess.bind("<Key>", self.pressed_key)
            self.lbofcont.bind('<Button 1>', self.pressed_key)
            self.lbofcont.bind('<Key>', self.pressed_key)
            self.submit.bind("<Button 1>", self.pressed_key)

        elif self.game == 2:
            self.app.minsize(750, 600)
            self.app.geometry("750x600+375+60")
            self.app.title("Guess the {} - A Geography Quiz.".format(self.gt.capitalize()))

            self.stringvar.set("Guess the {}!".format(self.gt.capitalize()))

            self.specialcountrynames = {"usa":"United States", "united states of america":"United States",\
                "drc":"Democratic Republic of the Congo", "Democratic republic of congo":"Democratic Republic of the Congo",\
                "turkey":"Turkiye", "uae":"United Arab Emirates", "uk":"United Kingdom", "car":"Central African Republic",\
                "burma":"Myanmar", "swaziland":"Eswatini", "cote divoire": "Ivory Coast"}
            
            self.locaps2 = list(self.ds[self.gt])
            self.locaps = []
            for ele in self.locaps2:
                if type(ele) != type(1.2) and ele not in self.locaps: self.locaps.append(ele)
            self.locaps.sort()

            self.clue1 = tk.Label(self.root, text=self.bettervisuals("First Country Clue: "+self.index["clue 1"]), font=self.myfont, justify="center", bg="light green")
            self.clue2 = tk.Label(self.root, text=self.bettervisuals("Second Country Clue: "+self.index["clue 2"]), font=self.myfont, justify="center", bg="light blue")
            self.country = tk.Label(self.root, text="Country: "+self.index["country"], font=self.myfont, justify="center", bg="light goldenrod")
            self.capital = tk.Label(self.root, text=self.gt.capitalize()+": "+self.bettervisuals(self.index[self.gt]), font=self.myfont, justify="center", bg="lavender")

            for ele in self.locaps: self.lbofcont.insert("end", ele)

            self.guess.bind("<Key>", self.pressed_key)
            self.lbofcont.bind('<Button 1>', self.pressed_key)
            self.lbofcont.bind('<Key>', self.pressed_key)
            self.submit.bind("<Button 1>", self.pressed_key)
            self.root.bind("<Control w>", lambda e: self.root.destroy())

        if self.game !=0:
            self.submit.grid(row=7, column=0, sticky="nsew")
            self.hint.grid(row=6, column=0, sticky="nsew")
            self.clue1.grid(row=0, column=0, sticky="nsew")
            self.frame.grid(row=5, column=0, sticky="nsew")

            self.guess.selection_range(0, "end")
            self.guess.grid(row=0, column=0, sticky="nsew")
            self.lbofcont.grid(row=1, column=0, sticky="nsew")
            self.sb.grid(row=1, column=0, sticky="nse")

            self.frame.rowconfigure(0, weight=1)
            self.frame.rowconfigure(1, weight=1)
            self.frame.columnconfigure(0, weight=1)

            self.root.rowconfigure(0, weight=2)
            self.root.rowconfigure(5, weight=2)
            self.root.rowconfigure(6, weight=1)
            self.root.rowconfigure(7, weight=1)
            self.root.columnconfigure(0, weight=1)
            
            self.root.bind("<Control w>", lambda e: self.root.destroy())

    def bettervisuals(self, string):
        splitstring = string.replace("/", ", ")
        splitstring = splitstring.split(" ")

        totallen = 0
        eleind = -1
        for ele in splitstring:
            lenele = len(ele)
            eleind += 1
            totallen += lenele+1
            if totallen >= self.BREAKLENGTH:
                totallen = 0
                splitstring[eleind] = ele+"\n"

        if splitstring[-1][-1] == "\n": splitstring[-1] = splitstring[-1][:-1]
        return " ".join(splitstring)

    def reveal(self, rev_all=False):
        if rev_all:
            for i in range(4): self.reveal()
        if self.cluecounter == 0:
            self.root.rowconfigure(1, weight=2)
            self.clue2.grid(row=1, column=0, sticky="nsew")
            if self.game == 1: self.hint["text"] = "Reveal the Continent"
            else: self.hint["text"] = "Reveal the Country"
        elif self.cluecounter == 1 and self.game == 1:
            self.root.rowconfigure(2, weight=2)
            self.continent.grid(row=2, column=0, sticky="nsew")
            self.hint["text"] = "Reveal the Capital"
        elif self.cluecounter == 1 and self.game == 2:
            self.root.rowconfigure(2, weight=2)
            self.country.grid(row=2, column=0, sticky="nsew")
            self.hint["text"] = "I give up!"
        elif self.cluecounter == 2 and self.game == 1:
            self.root.rowconfigure(3, weight=2)
            self.capital.grid(row=3, column=0, sticky="nsew")
            self.hint["text"] = "I give up!"
        elif self.cluecounter == 2 and self.game == 2:
            self.root.rowconfigure(3, weight=2)
            self.capital.grid(row=3, column=0, sticky="nsew")
            
            self.guess["state"] = "disabled"
            self.guess["disabledbackground"] = "black"
            self.guess["disabledforeground"] = "white"

            self.hint["state"] = "disabled"
            self.hint["relief"] = "flat"
            self.hint["text"] = "Well played!"
            
            self.submit["text"] = "Play Again"
            self.guess.unbind("<Key>")
            self.submit.unbind("<Button 1>")
            self.submit.bind("<Button 1>", self.replay)
            self.lbofcont.delete(0, "end")

            if self.stringvar.get() == "Correct Answer!":
                self.lbofcont.insert("end", "YAY!")
            else:
                self.lbofcont.insert("end", "OH NO!")
        elif self.cluecounter == 3 and self.game == 1:
            self.root.rowconfigure(4, weight=2)
            self.country.grid(row=4, column=0, sticky="nsew")
            
            self.guess["state"] = "disabled"
            self.guess["disabledbackground"] = "black"
            self.guess["disabledforeground"] = "white"

            self.hint["state"] = "disabled"
            self.hint["relief"] = "flat"
            self.hint["text"] = "Well played!"
            
            self.submit["text"] = "Play Again"
            self.guess.unbind("<Key>")
            self.submit.unbind("<Button 1>")
            self.submit.bind("<Button 1>", self.replay)
            self.lbofcont.delete(0, "end")

            if self.stringvar.get() == "Correct Answer!":
                self.lbofcont.insert("end", "YAY!")
            else:
                self.lbofcont.insert("end", "OH NO!")
        self.cluecounter += 1

    def pressed_key(self, event, ft=0):
        if not ft:
            self.root.after(10, self.pressed_key, event, 1)
            return
        elif event.widget == self.submit or event.keysym == "Return":
            if self.game == 1:
                if self.guess.get().lower() not in [x.lower() for x in self.locountries]:
                    self.stringvar.set(self.guess.get()+" is not a country!")
                    self.guess.focus_set()
                    self.guess.selection_range(0, "end")
                    self.guess.icursor("end")
                    return
                if self.guess.get().lower() == self.index["country"].lower():
                    self.stringvar.set("Correct Answer!")
                    self.reveal(True)
                    return
                else:
                    self.reveal()
                    self.stringvar.set("Wrong Answer!")
                    self.guess.focus_set()
                    self.guess.selection_range(0, "end")
                    self.guess.icursor("end")
                    return
            else:
                if self.guess.get().lower() not in [x.lower() for x in self.locaps]:
                    self.stringvar.set(self.guess.get()+" is not a {}!".format(self.gt))
                    self.guess.focus_set()
                    self.guess.selection_range(0, "end")
                    self.guess.icursor("end")
                    return
                if self.guess.get().lower() == self.index[self.gt].lower():
                    self.stringvar.set("Correct Answer!")
                    self.reveal(True)
                    return
                else:
                    self.reveal()
                    self.stringvar.set("Wrong Answer!")
                    self.guess.focus_set()
                    self.guess.selection_range(0, "end")
                    self.guess.icursor("end")
                    return
        elif event.widget == self.lbofcont:
            selected = self.lbofcont.selection_get()
            self.stringvar.set(selected)
            return
        elif self.guess.get().lower() == "guess the country!" or self.guess.get().lower() == "guess the {}!".format(self.gt):
            self.stringvar.set("")
            return
        else:
            self.lbofcont.delete(0, "end")
            displayedcounts = []
            if self.game == 1:
                for ele in self.locountries:
                    if self.guess.get().lower() in ele.lower() or ele.lower() in self.guess.get().lower():
                        displayedcounts.append(ele)
            
                for ele2 in self.specialcountrynames.keys():
                    if (self.guess.get().lower() in ele2.lower() or ele2.lower() in self.guess.get().lower()) and (self.specialcountrynames[ele2] not in displayedcounts):
                        displayedcounts.append(self.specialcountrynames[ele2])
            else:
                for ele in self.locaps:
                    if self.guess.get().lower() in ele.lower() or ele.lower() in self.guess.get().lower():
                        displayedcounts.append(ele)
                
            displayedcounts.sort()
            for ele in displayedcounts: self.lbofcont.insert("end", ele)

    def replay(self, e, gn=0, gt=""):
        self.root.destroy()
        self.__init__(self.app, gn, gt)

app = tk.Tk()
geoquiz(app)
app.mainloop()