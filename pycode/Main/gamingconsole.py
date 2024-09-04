"""
Gaming console has a variety of apps and games

The apps and games are -;
01) Hangman
02) Colour Game
03) X and O
04) Dots and Boxes
05) Clock App
06) Calculator
07) Text Editor
08) Ping Pong
09) General Knowledge Quiz
10) Excel Sheets
11) Asteroids
12) Quit To Win
13) Minesweeper
14) Geography Quiz
15) Birthday(idk why)
"""

from datetime import datetime, timedelta
import pytz, random, math, os, sys #, pyttsx3
import tkinter as tk
from tkinter import font, ttk, colorchooser, filedialog, messagebox
from PIL import Image, ImageTk
import pandas as pd


def saep(app):
    global clroot, broot, hroot, hgroot, calroot, cgroot, kroot, proot, exit_now, qroot, eroot, msroot, gqroot, colors
    
    def colorchanger(event):
        global colors
        if 'Enter' in str(event):
            if event.widget.cget('bg') in ('red2', 'cyan', 'green2'): colors = [event.widget.cget('bg')]
            event.widget['bg'] = 'gray70'
        elif 'Leave' in str(event):
            if colors:
                event.widget['bg'] = colors[0]
                colors = []
                return
            event.widget['bg'] = "SystemButtonFace"

    class clock:
        global clroot
        
        def __init__(self, root_2, app):
            global clroot
            if clroot != 0:
                self.torf = False
                root_2.grid_remove()
                self.root = clroot
                self.root.grid()
                app.configure(bg = self.root.cget('bg'))
                return

            if True:
                
                root_2.grid_remove()
                clroot = tk.Frame(app)
                self.root = clroot
                self.root.grid(sticky='nsew')
                app.title('CLOCK APP')
                app.bind('<Alt_L> <c>', lambda e : self.clickedb(self.f1))
                app.bind('<Alt_L> <t>', lambda e : self.clickedb(self.f2))
                app.bind('<Alt_L> <s>', lambda e : self.clickedb(self.f4))
                app.bind('<Escape>', lambda e : self.clickedb(self.f))
                self.root.configure(bg= "#fff")
                app.configure(bg= "#fff")

                # self.cump = pyttsx3.init()
                # self.cump.setProperty('rate', 120)
                # self.cump.setProperty('volume', 1.2)

                self.count = 0
                self.color = ''
                self.fat = 0
                self.count = 1
                self.torf = False

                self.myfont = font.Font(self.root, size = 12, family = 'Algerian', weight = 'bold', underline = 1)
                self.myfont2 = font.Font(self.root, family = 'Helvecta', size = 12, weight = 'bold')
                self.myfont3 = font.Font(self.root, family = 'Times', size = 20, weight = 'bold', slant = 'italic')
                self.myfont4 = font.Font(self.root, family = 'Helvecta', size = 24, weight = 'bold')
                self.myfont5 = font.Font(self.root, family = 'Courier', size = 18, weight = 'bold')

                self.b1 = tk.Button(self.root, text = "C l o c k", width = 47, height = 6, bg = 'red2', relief = 'flat', command = lambda : self.clickedb(self.f1), font = self.myfont)
                self.b1.grid(row = 0, column = 0, sticky="n")

                self.b2 = tk.Button(self.root, text = "T i m e r", width = 47, height = 6, bg = 'cyan', relief = 'flat', command = lambda : self.clickedb(self.f2), font = self.myfont)
                self.b2.grid(row = 0, column = 1, sticky="n")

                self.b4 = tk.Button(self.root, text = "S t o p w a t c h", width = 46, height = 6, bg = 'green2', relief = 'flat', command = lambda : self.clickedb(self.f4), font = self.myfont)
                self.b4.grid(row = 0, column = 2, sticky="n")

                self.b1.bind('<Enter>', colorchanger)
                self.b2.bind('<Enter>', colorchanger)
                self.b4.bind('<Enter>', colorchanger)

                self.b1.bind('<Leave>', colorchanger)
                self.b2.bind('<Leave>', colorchanger)
                self.b4.bind('<Leave>', colorchanger)

                self.im = tk.PhotoImage(file = r"images_for_gcpy/tick_toclock.png")
                self.im = self.im.subsample(3, 3)

                self.idk = "Shortcuts are :\n1) Control + W - Quit/Exit\n"\
                        + "2) Escape - come to App Screen\n3) Alt + C - go to Clock"\
                        + "\n4) Alt + T - go to Timer\n5) Alt + S - go to Stopwatch"
                self.f = tk.Label(self.root, image = self.im, text = self.idk, compound = "top", font = self.myfont5, bg = 'white', justify = 'left')
                self.f.grid(row = 1, column = 0, columnspan=3)
                self.prevcatsvar = self.f
                
                self.f1 = tk.Frame(self.root, bg = 'red2')
                self.f2 = tk.Frame(self.root, bg = 'cyan')
                self.f4 = tk.Frame(self.root, height = 700, width = 1530, bg = 'green2')
                
                self.root.rowconfigure(0, weight= 1)
                self.root.rowconfigure(1, weight= 3)
                self.root.columnconfigure(0, weight= 1)
                self.root.columnconfigure(1, weight= 1)
                self.root.columnconfigure(2, weight= 1)

            if True:
                self.lv = []
                self.fv = []

                self.rv = [
                    'Africa/Cairo', 'America/Argentina/Buenos_Aires', 'America/Chicago', 'America/Indiana/Indianapolis',\
                    'America/Los_Angeles', 'America/New_York', 'America/Panama', 'Antarctica/South_Pole', 'Asia/Calcutta', \
                    'Asia/Baghdad', 'Asia/Dubai', 'Asia/Hong_Kong', 'Asia/Riyadh', 'Asia/Singapore', 'Asia/Tokyo', 'Atlantic/Reykjavik'\
                    , 'Australia/ACT', 'CET', 'Etc/Greenwich', 'Europe/London', 'Europe/Rome', \
                    'US/Alaska', 'Africa/Addis_Ababa', 'Africa/Harare', 'Asia/Kabul', 'Europe/Tirane', 'Africa/Algiers', 'Europe/Andorra'\
                    , 'Africa/Luanda', 'America/Barbados', 'Asia/Yerevan', 'Asia/Baku', 'America/Nassau'\
                    , 'Asia/Bahrain', 'America/Barbados', 'Asia/Dhaka', 'Europe/Minsk', 'Europe/Brussels', 'America/Belize'\
                    , 'Africa/Porto-Novo', 'Asia/Thimphu', 'Asia/Phnom_Penh', 'Canada/Central', \
                    'Africa/Bangui', 'America/Santiago', 'Asia/Seoul', 'Europe/Moscow', 'Asia/Krasnoyarsk', \
                    'Asia/Yakutsk', 'Asia/Magadan', 'Europe/Paris', 'Europe/Berlin', 'Asia/Jakarta', 'Asia/Jayapura'
                    ]
                
                self.fl2 = [
                    'Egypt', 'Argentina', 'Chicago', 'Indiana', 'Los Angeles', 'New York', 'Panama', \
                    'New Zealand', 'India', 'Iraq/Iran', 'UAE/Dubai', 'Hong Kong', 'Saudi Arabia', 'Singapore',\
                    'Japan', 'Ireland', 'Australia', 'Central Europe', 'Greenwich', 'England/Britain', \
                    'Italy', 'Alaska', 'Ethopia', 'Zimbawe', 'Afghanistan', 'Albania', 'Algeria', 'Andorra'\
                    , 'Angola', 'Antigua and Barbados', 'Armenia', 'Azerbaijan', 'The Bahamas', 'Bahrain',\
                    'Barbados', 'Bangladesh', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Cambodia'\
                    , 'Canada', 'Central Africa', 'Chile', 'North/South Korea', 'Russia(West)', 'Russia(West-Central)', 'Russia(East-Central)', \
                    'Russia(East)', 'France', 'Germany', 'Indonesia(West)', 'Indonesia(East)'
                    ]
                
                self.fl = [ele for ele in self.fl2]

                self.fl.sort()
                for ele in self.fl:
                    changeinto = self.fl2.index(ele)
                    self.lv.append(self.rv[changeinto])
                    self.fv.append(ele)
                self.fl2 = self.fv
                self.rv = self.lv
                self.lsel = []

                self.searcher = tk.Entry(self.f1, width = 20, font = self.myfont2, bg = 'brown2')
                self.searcher.insert(0, 'Search for places')
                self.searcher.bind('<Key>', lambda e : self.root.after(10, self.sken, e))
                self.searcher.bind('<Button>', lambda e : self.presed(0))
                self.b4.bind('<Tab>', lambda e: self.presed(0))
                self.searcher.grid(row = 0, column = 0, sticky = 'ew')

                self.lbfrl = tk.Listbox(self.f1, font = self.myfont2, height = 15, selectbackground = 'gray80', selectforeground = 'black', activestyle = 'dotbox', bg = 'brown3')
                self.lbfrl.bind('<Button>', lambda e : self.root.after(10, self.ctz))
                self.lbfrl.bind('<space>', lambda e: self.root.after(10, self.ctz))
                self.lbfrl.bind('<Shift_L> <Tab>', lambda e: self.presed(0))
                self.lbfrl.grid(row = 1, column = 0, sticky = 'ew')

                for ele in self.fl: self.lbfrl.insert("end", ele)

                self.sb = tk.Scrollbar(self.f1, command = self.lbfrl.yview, orient = 'vertical')
                self.lbfrl.configure(yscrollcommand = self.sb.set)
                self.sb.grid(row = 1, column = 1, sticky = 'ns')

                self.sev2 = tk.StringVar(self.f1, '')
                self.counter = 0

                self.l2 = tk.Listbox(self.f1, font = self.myfont2, height = 15, selectbackground = 'gray80', selectforeground = 'black', activestyle = 'dotbox', bg = 'brown3')
                self.l2.bind('<Button>', lambda e : self.root.after(10, self.ctz, 0, 1))
                self.l2.bind('<space>', lambda e : self.root.after(10, self.ctz, 0, 1))
                
                tk.Label(self.f1, text=" ", bg="red2", fg="red2", width=100).grid(row=1, column=2)
                self.ltz = tk.Label(self.f1, text = "IT IS NOT FAST\nMost Countries are there on the list\n(Warning not every country\nVERY FEW cities are there)", bg = 'red2', font = self.myfont3, justify = 'left')
                self.ltz.grid(row = 1, column = 2, sticky = 'e')

                self.searcher.bind('<Tab>', self.checking)
                
                tk.Button(self.f1, text = "Return to Home Screen", command = self.switch, font = myfont).grid(row = 2, column = 0, sticky = 'nsew')
                tk.Button(self.f1, text = "Return to App Screen", command = lambda : self.clickedb(self.f), font = myfont).grid(row = 3, column = 0, sticky = 'nsew')
                tk.Button(self.f1, text = "Quit", command = root.destroy, font = myfont).grid(row = 4, column = 0, sticky = 'nsew')

            if True:
                self.secondstext = self.hourstext = self.minutestext = self.colcount = 0
                self.lotimers = []
                self.lt = []
                self.count2 = 1
                self.colors = ['dark turquoise', 'turquoise', 'aquamarine', 'medium turquoise', 'medium aquamarine']
                self.lt2 = {}
                self.prevwid = 0

                self.fat = tk.Frame(self.f2, bg = 'cyan')
                self.listtimers = tk.Frame(self.f2, bg = 'cyan')

                self.hours = tk.Label(self.fat, text = "0 : ", font = self.myfont4, bg = 'cadet blue')
                self.minutes = tk.Label(self.fat, text = "0 : ", font = self.myfont4, bg = 'steel blue')
                self.seconds = tk.Label(self.fat, text = 0, font = self.myfont4, bg = 'light blue')
                tk.Label(self.f2, width = 60, height = 5, bg= 'cyan').grid(row = 1, column = 1)
                self.hours.grid(row = 2, column = 1)
                self.minutes.grid(row = 2, column = 2)
                self.seconds.grid(row = 2, column = 3, ipadx = 10)

                self.db = tk.Button(self.listtimers, bitmap = 'error', bg = 'red', fg = 'blue', text = 'Discard', compound = 'top')
                
                tk.Button(self.fat, text = "⬆", command = lambda : self.movevert(0), bg = 'cadet blue', font = self.myfont2).grid(row = 1, column = 1, sticky = 'ew')
                tk.Button(self.fat, text = "⬆", command = lambda : self.movevert(2), bg = 'steel blue', font = self.myfont2).grid(row = 1, column = 2, sticky = 'ew')
                tk.Button(self.fat, text = "⬆", command = lambda : self.movevert(4), bg = 'light blue', font = self.myfont2).grid(row = 1, column = 3, sticky = 'ew')
                tk.Button(self.fat, text = "⬇", command = lambda : self.movevert(1), bg = 'cadet blue', font = self.myfont2).grid(row = 3, column = 1, sticky = 'ew')
                tk.Button(self.fat, text = "⬇", command = lambda : self.movevert(3), bg = 'steel blue', font = self.myfont2).grid(row = 3, column = 2, sticky = 'ew')
                tk.Button(self.fat, text = "⬇", command = lambda : self.movevert(5), bg = 'light blue', font = self.myfont2).grid(row = 3, column = 3, sticky = 'ew')

                self.nametimer = tk.Entry(self.fat, bg = 'LightSkyBlue2', font = self.myfont3, width = 15)
                self.nametimer.grid(row = 3, column = 4, sticky = 'nsew')
                self.nametimer.insert(0, "Name of the timer")
                self.nametimer.bind('<Return>', lambda e: self.settimer)

                self.submitb = tk.Button(self.fat, text = "Submit", command = self.settimer, bg = 'dodger blue', font = self.myfont4, activebackground = 'dodger blue')
                self.submitb.grid(row = 4, column = 4, sticky = 'ew')

                self.addtimer = tk.Button(self.f2, text = "Add a timer", font = self.myfont4, command = lambda : self.clickedb(self.fat, 1), bg = 'cyan2')
                self.addtimer.grid(row = 0, column = 0, sticky = 'ew')

                self.showtimers = tk.Button(self.f2, text = "Show timers", font = self.myfont4, command = lambda : self.clickedb(self.fat, 3), bg = 'pale turquoise')
                self.showtimers.grid(row = 1, column = 0, sticky = 'ew')

                tk.Button(self.f2, text = "Return to Home Screen", command = self.switch, font = myfont).grid(row = 4, column = 0, sticky = 'nsew')
                tk.Button(self.f2, text = "Return to App Screen", command = lambda : self.clickedb(self.f), font = myfont).grid(row = 5, column = 0, sticky = 'nsew')
                tk.Button(self.f2, text = "Quit", command = root.destroy, font = myfont).grid(row = 6, column = 0, sticky = 'nsew')

            if True:
                tk.Label(self.f4, width = 90, bg = 'green2').grid(row = 0, column = 0)
                self.sw = tk.Label(self.f4, text = 'welcome', bg = 'OliveDrab1', font = ('Comic sans', 50, 'bold'))
                self.sw.grid(row = 0, column = 1)

                self.starttime = self.counting = self.loovar = 1
                self.lof = []
                self.rocount = 2

                self.start = tk.Button(self.f4, text = "▶", command = lambda : self.stopwatch(0), font = self.myfont5, bg = 'DarkOliveGreen3')
                self.start.grid(row = 1, column = 1, sticky = 'w')
                self.stop = tk.Button(self.f4, text = "||", state = 'disabled', command = lambda : self.stopwatch(1), font = self.myfont5, bg = 'PaleGreen3')
                self.stop.grid(row = 1, column = 1, sticky = 'e')

                tk.Button(self.f4, text = "Return to Home Screen", command = self.switch, font = myfont).grid(sticky = 'nsew', row = 2, column = 2)
                tk.Button(self.f4, text = "Return to App Screen", command = lambda : self.clickedb(self.f), font = myfont).grid(sticky = 'nsew', row = 3, column = 2)
                tk.Button(self.f4, text = "Quit", command = lambda : self.checking(1), font = myfont).grid(sticky = 'nsew', row = 4, column = 2)
        def switch(self):
            global clroot
            
            self.torf = True

            app.unbind('<Alt_L> <c>')
            app.unbind('<Alt_L> <s>')
            app.unbind('<Alt_L> <t>')
            app.unbind('<Escape>')
            
            clroot = self.root
            root_2.grid()
            app.title('Home Screen')
            app.configure(bg = root_2.cget('bg'))
            self.root.grid_remove()
        def clickedb(self, catsvar, fatc = 0):
            if fatc == 1:
                self.count = 1

                if self.listtimers.winfo_ismapped() == True:
                    self.listtimers.grid_remove()
                    self.showtimers['text'] = "Show timers"
                    self.showtimers['command'] = lambda : self.clickedb(self.fat, fatc = 3)
                
                self.nametimer.selection_range(0, 'end')
                self.nametimer.focus_set()
                
                catsvar.grid(row = 2, column = 2)
                
                self.addtimer['text'] = "Cancel the timer"
                self.addtimer['command'] = lambda : self.clickedb(self.fat, fatc = 2)
                
                self.prevcatsvar = catsvar
                
                self.movevert(10)
                return
            elif fatc == 2:
                self.count = 0

                self.fat.grid_remove()
                
                self.addtimer['text'] = "Add a timer"
                self.addtimer['command'] = lambda : self.clickedb(self.fat, fatc = 1)
                return
            elif fatc == 3:                
                if self.fat.winfo_ismapped() == True:
                
                    self.fat.grid_remove()
                
                    self.addtimer['text'] = "Add a timer"
                    self.addtimer['command'] = lambda : self.clickedb(self.fat, fatc = 1)
                
                self.listtimers.grid(row = 2, column = 2)
                
                self.showtimers['text'] = "Hide the timers"
                self.showtimers['command'] = lambda : self.clickedb(self.fat, fatc = 4)
                
                self.prevcatsvar = catsvar
                
                return
            elif fatc == 4:
                self.listtimers.grid_remove()
                
                self.showtimers['text'] = "Show timers"
                self.showtimers['command'] = lambda : self.clickedb(self.fat, fatc = 3)
                
                return 
            
            if fatc < 5 and fatc > 0: return
            
            if self.prevcatsvar == self.fat:
                self.prevcatsvar = self.f2
            
            self.prevcatsvar.grid_remove()
            
            catsvar.grid(row = 1, column = 0, columnspan= 3, sticky= 'nsew')
            
            background = catsvar.cget('bg')
            self.root.configure(bg = background)
            app.configure(bg = background)
            
            self.prevcatsvar = catsvar
        def checking(self, event):         
            if event == 1:
                self.torf = True
                root.quit()

            if self.lbfrl.winfo_ismapped() == True:
                self.lbfrl.focus_set()
            elif self.l2.winfo_ismapped() == True:
                self.l2.focus_set()
        def sken(self, event):
            if event.keysym == 'Down':
                if self.lbfrl.winfo_ismapped() == True:
                    
                    self.lbfrl.focus_set()
                    self.lbfrl.selection_set(0)
                
                else:
                    
                    self.l2.focus_set()
                    self.l2.selection_set(0)
                
                return
            
            self.lv = []
            self.fl2 = []
            self.l2.delete(0, 'end')
            
            for ele in self.fl:
                
                if self.searcher.get().lower() in ele.lower():
                
                    self.l2.insert('end', ele)
                
                    self.lv.append(self.rv[self.fl.index(ele)])
                    self.fl2.append(ele)
            
            self.lbfrl.grid_remove()
            self.sb.configure(command = self.l2.yview, orient = 'vertical')
            self.l2.configure(yscrollcommand = self.sb.set)
            self.l2.grid(row = 1, column = 0, sticky = 'ew')
        def ctz(self, sel = 0, a = 0):
            if self.torf: return
            fmt = "Date - %d/%m/%y\nTime - %I:%M:%S %p\nTime Zone - %Z %z\nDay - %a/%B"
            
            if sel == 0:
                if a == 0:
                    selected = self.lbfrl.curselection()
                    
                    self.sev2.set(self.lv[selected[0]])
                    self.lbfrl.itemconfigure(selected[0], bg = 'gray50')
                    
                    if self.lsel != []:
                        self.lbfrl.itemconfigure(self.lsel[0], bg = 'brown3')
                    
                    self.lsel = [selected[0]]

                elif a == 1:
                    selected = self.l2.curselection()
                    
                    self.sev2.set(self.lv[selected[0]])
                    self.l2.itemconfigure(selected[0], bg = 'gray50')
                    
                    if self.lsel != []:
                        if len(self.fl2) >= self.lsel[0]:
                            self.l2.itemconfigure(self.lsel[0], bg = 'brown3')
                    
                    self.lsel = [selected[0]]
                
                if self.counter == 0: self.counter = 1
                else: return
            
            if self.sev2.get() == '': return
            
            now_time = self.sev2.get()
            now_time = datetime.now(pytz.timezone(now_time))
            
            s3 = self.fv[self.rv.index(self.sev2.get())]
            self.ltz.configure(text = s3+"\n"+str(now_time.strftime(fmt)))
            self.root.after(1000, self.ctz, 1, 1)
        def presed(self, event):
            if event == 0:
                self.searcher.delete(0, 'end')
                self.searcher.unbind('<Button>')
                self.searcher.bind('<Button>', self.presed)
            
            elif event == 1:
                self.searcher.focus_set()
                self.searcher.select_range(0, 'end')
                self.searcher.icursor('end')
            
            else:
                if self.searcher.get() != '' and not exit_now:
                    self.root.after(10, self.presed, 1)
        def dust_bin(self, wid, col):
            if col == 10:
                wid.grid_remove()
                index = list(self.lt2.keys()).index(wid)
                self.lotimers.pop(index)
                self.lt2.pop(wid)
                self.db.grid_remove()
            
            else:
                if self.prevwid != wid.widget:
                    self.prevwid = wid.widget
                    self.db.grid(row = col, column = 1, sticky = 'ns')
                    self.db['command'] = lambda : self.dust_bin(wid.widget, 10)
                else:
                    self.prevwid = 0
                    self.db.grid_remove()
        def looper(self):
            if len(self.lt2.values()) == 0:
                return
            for vals in self.lt2.values():

                if vals <= datetime.now():
                    kl, vl = list(self.lt2.keys()), list(self.lt2.values())
                    
                    print("Your timer, {} rang".format(self.lotimers[vl.index(vals)]))
                    # self.cump.say("Your timer, {} rang".format(self.lotimers[vl.index(vals)]))
                    # self.cump.runAndWait()
                    
                    keyinval = kl[vl.index(vals)]
                    keyinval.grid_remove()
                    
                    self.lt2.pop(keyinval)
                    self.lotimers.remove(self.lotimers[vl.index(vals)])
                    
                    self.looper()
                    return
            
            if not exit_now: self.root.after(1000, self.looper)
        def settimer(self):
            if len(self.lotimers) == 5:
                print("Maximum number of timers set")
                # self.cump.say("Maximum number of timers set")
                # self.cump.runAndWait()
                return
            if self.secondstext == 0 and self.hourstext == 0 and self.minutestext == 0:
                print("Put a timer for more than 0 seconds")
                # self.cump.say("Put a timer for more than 0 seconds")
                # self.cump.runAndWait()
                return
            if self.nametimer.get() not in self.lotimers:
                self.fat.grid_remove()
                self.addtimer['text'] = "Add a timer"    
                self.prevcatsvar = self.f2
                self.addtimer['command'] = lambda : self.clickedb(self.fat, fatc = 1)    
                self.colcount = len(self.lt2)
                setfor = datetime.now()+timedelta(hours = self.hourstext, minutes = self.minutestext, seconds = self.secondstext)
                self.lt.append(setfor)
                
                ntg = "Timer '{}' is set for\n{}".format(self.nametimer.get(), setfor.strftime("%x, %X"))
                ele = tk.Label(self.listtimers, text = ntg, bg =  self.colors[len(self.lotimers)], font = self.myfont2)
                ele.grid(row = self.colcount, column = 0, sticky = 'ew')
                lcc = self.colcount
                ele.bind('<Button>', lambda e: self.dust_bin(e, lcc))
                
                self.lt2[ele] = setfor
                self.lotimers.append(self.nametimer.get())
                
                if len(self.lotimers) == 1: self.looper()
            else:
                print("Name the timer something different")
                # self.cump.say("Name the timer something different")
                # self.cump.runAndWait()
                return
        def movevert(self, wb):
            if wb == 1 or wb == 0:
                if wb == 1:
                    if self.hourstext == 0:
                        self.hourstext = 23
                        self.hours['text'] = "23 : "
                    else:
                        self.hourstext -= 1
                        self.hours['text'] = str(self.hourstext)+" : "
                else:
                    if self.hourstext == 23:
                        self.hourstext = 0
                        self.hours['text'] = "0 : "
                    else:
                        self.hourstext += 1
                        self.hours['text'] = str(self.hourstext)+" : "
            elif wb == 2 or wb == 3:
                if wb == 3:
                    if self.minutestext == 0:
                        self.minutestext = 59
                        self.minutes['text'] = "59 : "
                    else:
                        self.minutestext -= 1
                        self.minutes['text'] = str(self.minutestext)+" : "
                else:
                    if self.minutestext == 59:
                        self.minutestext = 0
                        self.minutes['text'] = "0 : "
                    else:
                        self.minutestext += 1
                        self.minutes['text'] = str(self.minutestext)+" : "
            elif wb == 4 or wb == 5:
                if wb == 5:
                    if self.secondstext == 0:
                        self.secondstext = 59
                        self.seconds['text'] = 59
                    else:
                        self.secondstext -= 1
                        self.seconds['text'] = self.secondstext
                else:
                    if self.secondstext == 59:
                        self.secondstext = 0
                        self.seconds['text'] = 0
                    else:
                        self.secondstext += 1
                        self.seconds['text'] = self.secondstext
            if self.count2 == 0 or wb == 10:
                sf = datetime.now()+timedelta(self.hourstext, self.minutestext, self.secondstext)

                self.submitb['text'] = sf.strftime("Submit - \n%x\n%X")

                if self.count == 1 and not exit_now:
                    
                    self.root.after(1000, self.movevert, 10)
                    self.count2 = 1
                
                else:
                    self.count2 = 0
        def looping(self, rco):
            if rco == 1 and self.loovar == 0:
                self.starttime = self.starttime + timedelta(milliseconds=10)
        
                self.sw['text'] = self.starttime.strftime("%X.%f")[:-4]
            
                self.root.after(10, self.looping, 1)
            elif rco == 2:
                self.sw['text'] = self.starttime.strftime("%X.%f")[:-4]
            
                self.loovar = 0
            
                self.start['text'] = "⚐"
                self.start['command'] = lambda : self.stopwatch(2)
            
                self.stop['text'] = '||'
                self.stop['command'] = lambda : self.stopwatch(1)
            
                self.root.after(10, self.looping, 1)
        def stopwatch(self, choice):
            if choice == 0:
                self.loovar = 0
                
                dn = datetime.now()
                
                self.starttime = datetime.now()-timedelta(hours=dn.hour, minutes=dn.minute, seconds=dn.second)
                
                self.fst = self.starttime
                
                self.sw['text'] = self.starttime.strftime("%X.%f")[:-4]
                
                self.start['text'] = "⚐"
                self.start['command'] = lambda : self.stopwatch(2)
                
                self.stop['state'] = 'normal'
                
                self.root.after(10, self.looping, 1)
            elif choice == 1:
                self.counting = 0
                
                self.start['text'] = "▶"
                self.start['command'] = lambda : self.looping(2)
                
                self.stop['command'] = lambda : self.stopwatch(3)
                self.stop['text'] = "⬛"
                
                self.loovar = 1
            elif choice == 2:
                texoll = self.starttime-timedelta(hours = self.fst.hour, minutes = self.fst.minute, seconds = self.fst.second, microseconds = self.fst.microsecond)

                text = texoll.strftime("{}. %X.%f".format(len(self.lof)+1))
                lilof = tk.Label(self.f4, text=text[:-4], bg = 'yellow green', font = self.myfont3, highlightbackground="brown", highlightthickness=1)
                lilof.grid(row = self.rocount, column = 1, sticky='nsew')
                
                self.rocount += 1
                self.lof.append(lilof)
                self.fst = self.starttime
            else:
                for ele in self.lof:
                    ele.destroy()
                
                self.sw['text'] = "START"
                
                self.start['text'] = "▶"
                self.start['command'] = lambda : self.stopwatch(0)
                
                self.stop['text'] = '||'
                self.stop['state'] = 'disabled'
                self.stop['command'] = lambda : self.stopwatch(1)
                
                self.looping(0)

    class happybirthday:
        global hroot
        
        def __init__(self, root_2, app):
            global hroot
            
            if hroot != 0:
                root_2.grid_remove()
                self.root = hroot
                self.root.grid()
                app.config(bg = self.root.cget('bg'))
                return
            
            root_2.grid_remove()
            hroot = tk.Frame(app)
            self.root = hroot

            self.root.configure(bg = 'gold')
            app.configure(bg = 'gold')
            
            self.mast1 = tk.Frame(self.root, bg = 'gold')
            self.mast2 = tk.Frame(self.root, bg = 'white', width = 10, height= 10)
            self.mast3 = tk.Frame(self.root, bg = 'white')
            
            self.steper = 0
            self.root.grid()

            self.loframes = [self.mast1, self.mast2, self.mast3]
            
            tk.Label(self.root, width = 100, height = 18, bg = 'gold').grid(row = 1, column = 0, sticky = 'w')
            
            self.myfont = font.Font(root = self.root, family = 'castellar', size = 20, weight = 'bold', slant = 'italic')
            
            tk.Label(self.mast1, text = "Happy\nBirthday\nAmma", font = self.myfont, fg = 'white', bg = 'sienna').grid(row = 1, column = 1, sticky = 'n', ipady = 2, ipadx = 38)
            tk.Label(self.root, height = 7, bg = 'gold', width = 81).grid(row = 1, column = 2, sticky = 'ne')
            
            self.nextbutton = tk.Button(self.root, text = "Next", font = self.myfont, bg = 'orangered', height = 2, command = lambda : self.turner(True))
            self.nextbutton.grid(row = 0, column = 0, sticky = 'e')
            self.prevbutton = tk.Button(self.root, text = "Previous", font = self.myfont, bg = 'orangered', height = 2, command = lambda : self.turner(False))
            
            self.mast1.grid(row = 2, column = 1)
            
            tk.Button(self.root, text = "Return to Home Screen", command = self.switch, font = myfont).grid(sticky = 'nw', row = 0, column = 1)
            tk.Button(self.root, text = "Quit", command = root.destroy, font = myfont).grid(sticky = 'nw', row = 0, column = 1, pady = 33)
            
            self.c1 = tk.Canvas(self.mast2, height = 240, width = 240, bg = 'black')
            self.c1.create_rectangle(100, 60, 140, 100, fill = 'pink')
            self.c1.create_polygon(101, 60, 140, 60, 140, 70, 100, 70, fill = 'maroon1')
            self.c1.create_rectangle(60, 100, 180, 140, fill = 'pink')
            self.c1.create_polygon(61, 100, 180, 100, 180, 110, 60, 110, fill = 'maroon1')
            self.c1.create_rectangle(20, 140, 220, 180, fill = 'pink')
            self.c1.create_polygon(21, 140, 220, 140, 220, 150, 21, 150, fill = 'maroon1')
            self.c1.create_rectangle(100,60, 107,40, fill = 'red')
            self.c1.create_rectangle(111,60, 118,40, fill = 'DarkOrchid1')
            self.c1.create_rectangle(122,60, 129,40, fill = 'dodgerblue')
            self.c1.create_rectangle(133,60, 140,40, fill = "#000fff000")
            self.c1.create_polygon(100,40, 103,40, 102,30,  fill = 'gold')
            self.c1.create_polygon(102,40, 105,40, 104,30,  fill = 'gold')
            self.c1.create_polygon(104,40, 107,40, 106,30,  fill = 'gold')
            self.c1.create_polygon(111,40, 114,40, 113,30,  fill = 'gold')
            self.c1.create_polygon(113,40, 116,40, 115,30,  fill = 'gold')
            self.c1.create_polygon(115,40, 118,40, 117,30,  fill = 'gold')
            self.c1.create_polygon(122,40, 125,40, 124,30,  fill = 'gold')
            self.c1.create_polygon(124,40, 127,40, 126,30,  fill = 'gold')
            self.c1.create_polygon(126,40, 129,40, 128,30,  fill = 'gold')
            self.c1.create_polygon(133,40, 136,40, 135,30,  fill = 'gold')
            self.c1.create_polygon(135,40, 138,40, 137,30,  fill = 'gold')
            self.c1.create_polygon(137,40, 140,40, 139,30,  fill = 'gold')
            self.c1.grid(row = 1, column = 3, sticky = 'e', padx = 5, pady = 5)
            tk.Label(self.mast3, text = "A - Amazing\nM - MasterChef\nM - Marvellous\nA - Astounding", fg = 'goldenrod4', bg = 'gold', font = self.myfont, justify = 'left').grid(row = 0, column = 0, ipady = 66, ipadx = 40)
            tk.Label(self.mast3, text = "G - Gorgeous\nA - Adventurous\nY - Youthful\nA - Astonishing\nT - Truthful\nH - Happy\nR - Right\nI - Impressive", fg = 'goldenrod4', bg = 'gold', font = self.myfont, justify = 'left').grid(row = 0, column = 1)

        def switch(self):
            global hroot
            
            hroot = self.root
            root_2.grid()
            
            app.title('Home screen')
            app.configure(bg = root_2.cget('bg'))
            
            self.root.grid_remove()

        def turner(self, tsf):
            if tsf and self.steper < 2:
                self.steper += 1
                self.loframes[self.steper-1].grid_remove()
                self.loframes[self.steper].grid(row = 2, column = 1)
            elif not tsf and self.steper > 0:
                self.steper -= 1
                
                self.loframes[self.steper+1].grid_remove()
                self.loframes[self.steper].grid(row = 2, column = 1)   
            if self.loframes[self.steper] == self.mast1:
                self.prevbutton.grid_remove()
            elif self.loframes[self.steper] == self.mast3:
                self.nextbutton.grid_remove() 
            else:
                self.nextbutton.grid(row = 0, column = 0, sticky = 'e')
                self.prevbutton.grid(row = 0, column = 0, sticky = 'w')

    class hangmang:
        global hgroot
        
        def __init__(self, root_2, app):
            global hgroot
            
            if hgroot != 0:
                root_2.grid_remove()
                self.root = hgroot
                self.root.grid()
                return
            
            hgroot = tk.Frame(app)
            root_2.grid_remove()
            
            self.root = hgroot
            app.title("hangman")
            
            self.myfont = font.Font(size = 12, family = 'algerian')
            self.count = tk.IntVar()
            
            self.words = ['armadillo', 'beaver', 'chimpanzee', 'dolphin', 'earthworm', 'flamingo'\
                ,'gorilla', 'hedgehog', 'iguana', 'jaguar', 'kingfisher', 'llama', 'mangoose'\
                , 'otter', 'possum', 'rhea', 'salmon', 'turkey', 'vulture', 'woodpecker'\
                , '']
            
            self.word = self.words[random.randrange(0, len(self.words))]
            self.blank = ""
            self.listword = list(self.word)
            self.guesses = []
            
            self.blank += self.listword[0]
            
            for loop in range(0, len(self.word)-1):
                self.blank = self.blank + " _"
            
            loop += 1
            self.prevguess = []
            
            if self.word[0] not in self.word[1:]:
                self.prevguess.append(self.word[0])
            
            tk.Label(self.root, text = " ", width = 100).grid(row = 0, column = 0)
            tk.Label(self.root, text = " ", height = 20).grid(row = 0, column = 1)
            
            self.counting = tk.Label(self.root, text = "wrongs: %s/6\nit is %s long" %(self.count.get(), len(self.word)), width = 25, height = 5, bg = '#00FFFF')
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
            self.guess.bind('<Button>', lambda e : self.guest.set(''))
            self.guess.bind('<Return>', self.correct)
            
            self.lb = tk.Listbox(self.root, selectbackground = '#00ffff', selectforeground = 'navy blue', font = self.myfont, bg = '#000fff000')
            self.lb.grid(row = 2, column = 2, sticky = 'ew')
            
            tk.Button(self.root, text = "Return to Home Screen", command = self.switch, font = myfont).grid(sticky = 'nw', row = 0, column = 0)
            tk.Button(self.root, text = "Quit", command = root.destroy, font = myfont, justify = 'center', width = 19).grid(sticky = 'nw', row = 0, column = 0, pady = 33, ipadx = 4)
            tk.Button(self.root, text = "Replay", command = lambda : self.switch(2), font = myfont, justify = 'center', width = 19).grid(sticky = 'nw', row = 0, column = 0, pady = 66, ipadx = 4)
            
            if self.guess.get() == "":
                self.count.set(int(self.count.get())-1)
            
            self.root.grid()
        def switch(self, count = 1):
            global hgroot
            
            if count == 1:
                hgroot = self.root
                root_2.grid()
                app.title('Home screen')
                app.configure(bg = root_2.cget('bg'))
                self.root.grid_remove()
            
            else: 
                hgroot = 0
                root_2.grid()
                self.root.destroy()
                self.__init__(root_2, app)                
        def correct(self, event):
            self.guest.set(self.guest.get().lower())
            self.guess['textvariable'] = self.guest
            self.lb.insert('end', self.guess.get())

            if len(self.guess.get()) != 1:
                if self.guest.get() == self.word:
                    self.guest.set('congrats')
                    
                    self.lb.delete(0, 'end')
                    self.lb.insert(0, 'Winner  ^_^')
                    self.lb.insert(0, 'Congrats :)')
                    
                    self.blankp.configure(text = "Congrats")
                    self.counting.configure(text = self.word)
                else:
                    if len(self.guess.get()) != 0:
                        self.count.set(self.count.get()+1)
                        self.counting.configure(text = "wrongs: %s/6\nit is %s long" %(self.count.get(), len(self.word)))
                
                if self.count.get() >= 6:
                    self.lb.delete(0, 'end')
                    self.lb.insert(0, 'loser  =C')
                    self.lb.insert(0, 'sucker :(')
                    
                    self.guest.set('loser')
                    self.blankp.configure(text = "loser")
                    
                    self.counting.configure(text = self.word)
                self.guesses.append(self.guess.get())
                self.guest.set('')
            
            else:
                self.prevguess.append(self.guess.get().lower())
                loop = 0
                blank_2 = ""

                if self.guess.get() in self.listword[1:]:
                    if self.guess.get() in self.prevguess[0:-1]:
                        self.counting.configure(text = "wrongs: %s/6\nit is %s long" %(self.count.get(), len(self.word)))
                        self.guest.set('You guessed it before')
                    
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
                        self.counting.configure(text = "wrongs: %s/6\nit is %s long" %(self.count.get(), len(self.word)))
                        self.guest.set('')
                

                if '_' in self.blank:
                    if self.count.get() >= 6:
                        self.guest.set('loser')
                        self.lb.delete(0, 'end')
                        self.lb.insert(0, 'Loser  =C')
                        self.lb.insert(0, 'Sucker :(')
                        self.blankp.configure(text = "loser")
                        self.counting.configure(text = self.word)
                
                else:
                    self.guest.set('congrats')
                    self.lb.delete(0, 'end')
                    self.lb.insert(0, 'Winner  ^_^')
                    self.lb.insert(0, 'Congrats :)')
                    self.blankp.configure(text = "Congrats")
                    self.counting.configure(text = self.word)
            self.guess.icursor('end')
            self.guess.select_range(0, 'end')

    class cg:
        def __init__(self, root_2, app):
            self.qui = 0
            
            root_2.grid_remove()
            
            self.counting = 60
            self.counter = 0
            self.colours = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
            self.words = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
            
            self.root = tk.Frame(app)
            app.title("Colour Game")
            
            self.iv1 = tk.IntVar(self.root, 0)
            self.iv2 = tk.IntVar(self.root, 0)
            
            self.myfont = font.Font(size = 15, family = 'Algerian', weight = "bold")
            self.myfont_2 = font.Font(size = 18, family = 'Algerian', weight = "bold")
            self.myfont_4 = font.Font(size = 40)
            
            tk.Label(self.root, text = " ", width = 75).grid(row = 0, column = 0)
            tk.Label(self.root, text = "Game Description: Enter the colour of the words displayed below.", fg = 'grey', font = self.myfont).grid(row = 0, column = 1)
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
            
            self.rethome = tk.Button(self.root, text = "Return to Home Screen", command = self.switch, font = myfont)
            self.rethome.grid(sticky = 'nw', row = 3, column = 0)
            tk.Button(self.root, text = "Quit", command = root.destroy, font = myfont).grid(sticky = 'nw', row = 3, column = 0, pady = 33)

            self.root.grid()
        def switch(self, game_over=0):
            global colroot

            if game_over == 0:                
                self.qui = 1
                
                root_2.grid()
                count.set(self.counting)
                
                app.title('Home screen')
                app.configure(bg = root_2.cget('bg'))
                
                self.root.grid_remove()
                colroot = self.root
            else:
                self.timer['text'] = "Game has ended"
                self.code["text"] = ""
                self.rethome["state"] = "normal"
                self.starter["state"] = "normal"
                self.ges['state'] = 'disabled'
                self.counting = 60
                self.root.after_cancel(self.loop)

        def lestart(self, event):
            a = self.ges.get()
            if a.lower() == self.colours[self.iv1.get()]:
                self.counter += 1
                self.score.configure(text = "Your score : {}".format(self.counter))
            
            self.geser.set('')
            self.colours = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
            self.words = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
            
            a = True

            iv1 = self.iv1.get()
            iv2 = self.iv2.get()
            
            while a:
                self.iv1.set(random.randint(0, len(self.colours)-1))
                if self.iv1.get() != iv1: break

            while a:
                self.iv2.set(random.randint(0, len(self.words)-1))
                if self.iv2.get() != self.iv1.get() and self.iv2.get() != iv2: break
            
            self.code.configure(text = self.words[self.iv2.get()], fg = self.colours[self.iv1.get()])
        def lesgo(self):
            if self.qui: return
            
            if self.counting == 60:
                self.starter["state"] = "disabled"
                self.rethome["state"] = "disabled"
                self.ges['state'] = 'normal'
                self.geser.set('')
                
                
                self.colours = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
                self.words = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
                
                                
                self.colours = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
                self.words = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
                
                self.iv1.set(random.randint(0, 8))
                self.iv2.set(random.randint(0, 8))
                
                self.code.configure(text = self.words[self.iv1.get()], fg = self.colours[self.iv2.get()])
            
            self.ges.bind('<Return>', self.lestart)
            
            self.timer['text'] = "Game ends in : {}".format(self.counting)
            
            if self.counting > 0:
                self.counting -= 1
                if not exit_now: self.loop = self.root.after(1000, self.lesgo)
            
            if self.counting == 0: self.switch(game_over=1)

    class kacg:
        global kroot

        def __init__(self, root_2, app):
            global kroot
            if kroot:
                root_2.grid_remove()
                self.root = kroot
                self.root.grid()
                return

            root_2.grid_remove() 
            
            self.xo = self.ro1 = self.ro2 = self.ro3 = self.co1 = self.co2 = self.co3 = self.di1 = self.di2 = 0
            
            self.root = tk.Frame(app)
            
            app.title("Knots And Crosses")
            
            self.myfont = font.Font(root = self.root, family = 'Algerian', size = 12, weight = "bold", overstrike = 1)
            
            self.b1 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = '#00ffff', command = lambda : self.xoxo(self.b1))
            self.b1.grid(row = 0, column = 0)
            
            self.b2 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = '#000fff000', command = lambda : self.xoxo(self.b2))
            self.b2.grid(row = 0, column = 1)
            
            self.b3 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = '#00ffff', command = lambda : self.xoxo(self.b3))
            self.b3.grid(row = 0, column = 2)
            
            self.b4 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = '#000fff000', command = lambda : self.xoxo(self.b4))
            self.b4.grid(row = 1, column = 0)
            
            self.b5 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = '#00ffff', command = lambda : self.xoxo(self.b5))
            self.b5.grid(row = 1, column = 1)
            
            self.b6 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = '#000fff000', command = lambda : self.xoxo(self.b6))
            self.b6.grid(row = 1, column = 2)
            
            self.b7 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = '#00ffff', command = lambda : self.xoxo(self.b7))
            self.b7.grid(row = 2, column = 0)
            
            self.b8 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = '#000fff000', command = lambda : self.xoxo(self.b8))
            self.b8.grid(row = 2, column = 1)
            
            self.b9 = tk.Button(self.root, text = " ", width = 27, height = 10, font = self.myfont, bg = '#00ffff', command = lambda : self.xoxo(self.b9))
            self.b9.grid(row = 2, column = 2)
            
            self.ln = [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]

            tk.Button(self.root, text = "Return to Home screen", command = self.switch, font = myfont).grid(sticky = 'nw', row = 4, column = 0)
            tk.Button(self.root, text = "Replay", command = lambda : self.switch(False), font = myfont).grid(sticky = 'w', row = 5, column = 0)
            tk.Button(self.root, text = "Quit", command = root.destroy, font = myfont).grid(sticky = 'w', row = 6, column = 0)
            
            self.root.grid()
        def switch(self, count = True):
            global kroot
            
            if count:
                kroot = self.root
                root_2.grid()
                app.title('Home screen')
                app.configure(bg = root_2.cget('bg'))
                self.root.grid_remove()
            else:
                for ele in self.ln: ele['text'] = " "
                self.xo = self.ro1 = self.ro2 = self.ro3 = self.co1 = self.co2 = \
                self.co3 = self.di1 = self.di2 = 0
        def xoxo(self, value):
            if value['text'] != " ": return
            if self.xo:
                value.config(text = "o", command = None)
                self.xo = 0
            else:
                value.config(text = "x", command = None)
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
            lb = [self.ro1, self.ro2, self.ro3, self.co1, self.co2, self.co3, self.di1, self.di2]
            a = 0
            for ele in self.ln:
                if ele['text'] != " ": a += 1
            if a == 9:
                for ele in self.ln: ele['text'] = "Tie"
            elif 3 in lb:
                for ele in self.ln: ele['text'] = "X won"
            elif -3 in lb:
                for ele in self.ln: ele['text'] = "O won"

    class boxes:
        global broot
        
        def __init__(self, root_2, app):
            global broot
            
            if broot != 0:
                root_2.grid_remove()
                self.root = broot
                self.root.grid()
                return
            
            root_2.grid_remove()
            self.root = tk.Frame(app)
            app.title("dots and boxes")
            
            self.head = tk.Canvas(self.root, height = 180, width = 180)
            self.head.grid()
            
            self.counter = 0
            
            self.myfont = font.Font(root = self.root, family = 'Times', weight = 'bold')
            
            self.p1v = 0
            self.p2v = 0
            
            self.p1 = tk.Label(self.root, text = "Player1 - 0", bg = 'red', height = 3, width = 15, font = self.myfont)
            self.p2 = tk.Label(self.root, text = "Player2 - 0", bg = 'blue', height = 3, width = 15, font = self.myfont)
            
            self.p1.grid(column = 1, row = 0, sticky = 'n')
            self.p2.grid(column = 1, row = 0, sticky = 'n', pady = 75)
            
            for j in range(5):
                for i in range(5):
                    self.head.create_oval((40*i)+10, (40*j)+10, (40*i)+14, (40*j)+14, fill = 'green', tag = 'anoval')

            self.head.bind('<Button>', self.heady)
            
            tk.Button(self.root, text = "Return to Home Screen", command = self.switch, font = myfont).grid(sticky = 'nw', row = 2, column = 0)
            tk.Button(self.root, text = "Quit", command = root.destroy, font = myfont).grid(sticky = 'nw', row = 3, column = 0)
            
            self.root.grid()

        def switch(self):
            global broot
            
            broot = self.root
            root_2.grid()
            app.title('Home screen')
            app.configure(bg = root_2.cget('bg'))
            
            self.root.grid_remove()
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
            
            if len(a) != 4 and len(b) != 4: step = not step
            return step
        def heady(self, event):
            x = (event.x-10)%40
            y = (event.y-10)%40
            exx = event.x-x
            eyy = event.y-y
            
            tagid = self.head.find_withtag('line')
            ftc = self.head.find_closest(event.x, event.y)
            
            if event.x < 10 or event.y < 10 or event.x > 180 or event.y > 180: return
            
            elif ftc[0] not in tagid:

                if x <= 8:
                    if y <= 8: return
                    vh = 'vertical'
                    
                    if self.counter == 1: li = self.head.create_line(exx, eyy, exx, eyy+40, fill = 'blue', tags = 'line')
                    else: li = self.head.create_line(exx, eyy, exx, eyy+40, fill = 'red', tags = 'line')
                
                    self.counter = self.nbm(self.head.coords(li), vh, self.counter)
                
                elif y <= 8:
                    vh = 'horizontal'
                    
                    if self.counter == 1: li = self.head.create_line(exx, eyy, exx+40, eyy, fill = 'blue', tags = 'line')
                    else: li = self.head.create_line(exx, eyy, exx+40, eyy, fill = 'red', tags = 'line')
                    
                    self.counter = self.nbm(self.head.coords(li), vh, self.counter)

    class calculator:
        global calroot
        
        def __init__(self, root_2, app):
            global calroot
            if calroot != 0:
                root_2.grid_remove()
                self.root = calroot
                app.configure(bg = 'blue')
                self.root.grid()
                return
            
            root_2.grid_remove()
            self.root = tk.Frame(app)
            app.title('calculator App')
            app.configure(bg = 'blue')
            self.root.config(bg = 'blue')
            
            myfont = font.Font(self.root, size = 15, weight = 'bold')
            
            self.answer = tk.Entry(self.root, font = myfont, selectbackground = 'yellow', selectforeground = 'black', width = 18)
            self.answer.grid(row = 0, column = 3, sticky = 'ew')
            self.answer.insert(0, "WELCOME")
            
            self.cal = tk.StringVar(self.root, "")
            self.answer.focus_set()
            self.answer.bind('<Key>', lambda e : self.root.after(10, self.number, 'self.key', e))
            
            self.ans = 0
            self.keys = {'clear' : None, 'del' : None, 'equal' : None, 'asterisk' : 'x', 'slash' : '÷', 'percent' : '%', 'aiicircum' : '^'}
            self.key = {'*' : 'x', '/' : '÷', '/100' : '%', '**' : '^'}
            self.key2 = ['plus', 'minus']
            self.keys3 = {'x' : '*', '÷' : '/', '%' : '/100', '^' : '**'}
            self.sc = self.ans2 = 0
            
            tk.Button(self.root, text = " . ", bg = 'red', font = myfont, command = lambda : self.number("."), borderwidth = 5, width = 15, height = 5).grid(row = 0, column = 2)
            tk.Button(self.root, text = " 0 ", bg = 'red', font = myfont, command = lambda : self.number("0"), borderwidth = 5, width = 15, height = 5).grid(row = 0, column = 0)
            tk.Button(self.root, text = " 1 ", bg = 'red', font = myfont, command = lambda : self.number("1"), borderwidth = 5, width = 15, height = 5).grid(row = 1, column = 0)
            tk.Button(self.root, text = " 2 ", bg = 'red', font = myfont, command = lambda : self.number("2"), borderwidth = 5).grid(row = 1, column = 1, sticky = 'ewns')
            tk.Button(self.root, text = " 3 ", bg = 'red', font = myfont, command = lambda : self.number("3"), borderwidth = 5, width = 15).grid(row = 1, column = 2, sticky = 'ns')
            tk.Button(self.root, text = " 4 ", bg = 'red', font = myfont, command = lambda : self.number("4"), borderwidth = 5, height = 5).grid(row = 2, column = 0, sticky = 'ew')
            tk.Button(self.root, text = " 5 ", bg = 'red', font = myfont, command = lambda : self.number("5"), borderwidth = 5).grid(row = 2, column = 1, sticky = 'nsew')
            tk.Button(self.root, text = " 6 ", bg = 'red', font = myfont, command = lambda : self.number("6"), borderwidth = 5).grid(row = 2, column = 2, sticky = 'nsew')
            tk.Button(self.root, text = " 7 ", bg = 'red', font = myfont, command = lambda : self.number("7"), borderwidth = 5, height = 5).grid(row = 3, column = 0, sticky = 'ew')
            tk.Button(self.root, text = " 8 ", bg = 'red', font = myfont, command = lambda : self.number("8"), borderwidth = 5).grid(row = 3, column = 1, sticky = 'nsew')
            tk.Button(self.root, text = " 9 ", bg = 'red', font = myfont, command = lambda : self.number("9"), borderwidth = 5).grid(row = 3, column = 2, sticky = 'nsew')
            
            tk.Button(self.root, text = "Del", bg = '#000fff000', font = myfont, command = lambda : self.number('del'), borderwidth = 5, height = 5).grid(row = 4, column = 0, sticky = 'ew')
            tk.Button(self.root, text = "Clear", bg = '#000fff000', font = myfont, command = lambda : self.number('clear'), borderwidth = 5).grid(row = 4, column = 1, sticky = 'nsew')
            tk.Button(self.root, text = " = ", bg = '#000fff000', font = myfont, command = lambda : self.number('equal'), borderwidth = 5).grid(row = 4, column = 2, sticky = 'nsew')
            tk.Button(self.root, text = " ÷ ", bg = '#00ffff', font = myfont, command = lambda : self.number('/'), borderwidth = 5).grid(row = 1, column = 3, sticky = 'nsew')
            tk.Button(self.root, text = " x ", bg = '#00ffff', font = myfont, command = lambda : self.number('*'), borderwidth = 5).grid(row = 2, column = 3, sticky = 'nsew')
            tk.Button(self.root, text = " + ", bg = '#00ffff', font = myfont, command = lambda : self.number('+'), borderwidth = 5).grid(row = 3, column = 3, sticky = 'nsew')
            tk.Button(self.root, text = " - ", bg = '#00ffff', font = myfont, command = lambda : self.number('-'), borderwidth = 5).grid(row = 4, column = 3, sticky = 'nsew')
            tk.Button(self.root, text = " √ ", bg = 'saddle brown', font = myfont, command = lambda : self.number('sqrt'), borderwidth = 5, width = 15).grid(row = 0, column = 1, sticky = 'ns')
            tk.Button(self.root, text = " π ", bg = 'saddle brown', font = myfont, command = lambda : self.number('pi'), borderwidth = 5, width = 15).grid(row = 0, column = 5, sticky = 'ns')
            tk.Button(self.root, text = " % ", bg = 'saddle brown', font = myfont, command = lambda : self.number('/100'), borderwidth = 5).grid(row = 1, column = 5, sticky = 'nsew')
            tk.Button(self.root, text = " ^ ", bg = 'saddle brown', font = myfont, command = lambda : self.number('**'), borderwidth = 5).grid(row = 2, column = 5, sticky = 'nsew')
            tk.Button(self.root, text = " ( ", bg = 'gold', font = myfont, command = lambda : self.number('('), borderwidth = 5).grid(row = 3, column = 5, sticky = 'nsew')
            tk.Button(self.root, text = " ) ", bg = 'gold', font = myfont, command = lambda : self.number(')'), borderwidth = 5).grid(row = 4, column = 5, sticky = 'nsew')
            tk.Button(self.root, text = " ! ", bg = 'gold', font = myfont, command = lambda : self.number('fact'), borderwidth = 5).grid(row = 0, column = 6, sticky = 'ewns')
            tk.Button(self.root, text = " E ", bg = 'black', font = myfont, command = lambda : self.number('expo'), fg = 'white', borderwidth = 5).grid(row = 1, column = 6, sticky = 'ewns')
            tk.Button(self.root, text = " e ", bg = 'black', font = myfont, command = lambda : self.number('e'), fg = 'white', borderwidth = 5).grid(row = 2, column = 6, sticky = 'ewns')
            tk.Button(self.root, text = "Return to Home Screen", command = self.switch, font = myfont, bg = '#000fff000', borderwidth = 5).grid(sticky = 'ns', row = 3, column = 6)
            tk.Button(self.root, text = "Quit", command = root.destroy, font = myfont, bg = '#000fff000', borderwidth = 5).grid(row = 4, column = 6, sticky = 'nsew')
            
            self.root.grid()
        
        def number(self, no, event = None):
            if self.answer.get() == "": self.ans = 1
            
            if self.ans == 0:
                self.cal.set("")
                self.answer.delete(0, 'end')
                self.ans = 1
                self.number(no, event)
                return

            if no == 'equal':
                a = self.cal.get()
                self.answer.delete(0, 'end')
                
                try:
                    if self.sc == 1: 
                        self.sc = 0
                        
                        self.cal.set(math.sqrt(float(a)))
                        self.answer.insert(0, math.sqrt(float(a)))
                        
                        return
                
                    self.answer.insert(0, eval(a))
                    self.cal.set(eval(a))
                    
                    self.ans2 = 1
                
                except:
                    self.answer.insert(0, 'Error')
                    self.cal.set("")
                    self.ans = 0
                return
            
            elif no == 'clear':
                if self.sc == 1:
                    self.sc = 0
                
                self.cal.set("")
                self.answer.delete(0, 'end')
                return
            
            elif no == 'del':
                la = len(self.answer.get())
                self.answer.delete(la-1)
                
                c = list(self.cal.get())
                c = c[0:-1]
                b = ""
                
                for ele in c: b += ele
                
                self.cal.set(b)
                
                d = list(self.answer.get())
                
                if '√' not in d: self.sc = 0
                return
            
            elif no == 'pi':
                self.answer.insert('end', 'π')
                self.cal.set(self.cal.get()+str(math.pi))
                return
            
            elif no == 'sqrt':
                self.answer.insert('end', '√')
                self.sc = 1
                return
            
            elif no == 'fact':
                self.answer.delete(0, 'end')
                try:
                    self.answer.insert('end', math.factorial(eval(self.cal.get())))
                    self.cal.set(math.factorial(eval(self.cal.get())))
                except SyntaxError:
                    self.answer.insert(0, 'Error')
                    self.cal.set("")
                    self.ans = 0
                return
            
            elif no == 'expo':
                self.cal.set(self.cal.get()+'e')
                self.answer.insert('end', 'E')
                return
            
            elif no == 'e':
                self.answer.insert('end', 'e')
                self.cal.set(self.cal.get()+str(math.e))
                return
            
            elif event:
                if event.keysym == 'BackSpace' and self.ans2 == 1:
                    self.answer.delete(0, 'end')
                    self.ans2 = 0
                    self.cal.set("")
                    return
                
                elif event.keysym == 'Return':
                    self.number('equal')
                
                if event.keysym in self.keys.keys():
                    if self.keys[event.keysym] == None:
                        self.answ3 = list(self.keys.keys())
                        if self.answ3.index(event.keysym) == 2:
                            try:
                                if self.sc == 1: 
                                    self.sc = 0
                                    self.cal.set(math.sqrt(float(self.cal.get())))
                                    self.answer.insert(0, math.sqrt(float(self.cal.get())))
                                    return
                
                                a = list(self.answer.get())
                                a = a.index('=')
                
                                self.answer.delete(a)
                                self.answer.delete(0, 'end')
                                self.cal.set(eval(self.cal.get()))
                                self.answer.insert(0, self.cal.get())
                                self.ans2 = 1
                            except:
                                self.answer.delete(0, 'end')
                                self.cal.set("")
                                self.answer.insert(0, 'Error')
                                self.ans = 0
                    else:
                        if event.keysym == 'asterisk': ek = '*'
                        elif event.keysym == 'slash': ek = '/'
                        elif event.keysym == 'percent': ek = '/100'
                        elif event.keysym == 'aself.sciicircum': ek = '**'
                        self.cal.set(self.cal.get()+ek)
                        
                        try: a = list(self.answer.get()).index(ek)
                        except: return
                        
                        self.answer.delete(a)
                        vallist, self.keylist = list(self.keys.values()), list(self.keys.keys())
                        self.answer.insert('end', vallist[self.keylist.index(event.keysym)])
                
                if self.answer.get() != "":
                    
                    b = list(self.answer.get())
                    b = b[len(b)-1]
                    
                    if b == '!':
                        self.answer.delete(0, 'end')
                        self.answer.insert('end', math.factorial(eval(self.cal.get())))
                        self.cal.set(math.factorial(eval(self.cal.get())))
                    elif b in self.keys3.keys(): self.cal.set(self.cal.get()+self.keys3[b]) 
                    elif b == event.keysym or event.keysym in self.key2: self.cal.set(self.cal.get()+b)
                return
            
            elif no in self.keys: pass
            
            self.cal.set(self.cal.get()+no)
            
            if no in self.key.keys(): self.answer.insert('end', self.key[no])
            else: self.answer.insert('end', no)
        
        def switch(self):
            global calroot
            
            calroot = self.root
            root_2.grid()
            app.title('Home screen')
            app.configure(bg = root_2.cget('bg'))
            
            self.root.grid_remove()

    class aytexteditor:
        def __init__(self, root_2, app):            
            app.title('Default.txt - AY text editor(AYTE)')
            
            app.bind('<Control Key>', self.binding)
            app.bind('<Control Shift Key>', self.bind2)
            
            root_2.grid_forget()
            
            self.name = 0
            self.job = None
            
            app.title('Default.txt - AY text editor(AYTE)')
            app.configure(bg = '#000fff000')

            self.root = tk.Frame(app, bg = '#000fff000')
            self.selected = None
            self.editor = tk.Text(self.root, selectbackground = 'blue', selectforeground = '#ffffff', undo = True, width = 106, height = 25, font = ('courier', 18), borderwidth = 8, bg = '#00FFFF', wrap = 'none')
            self.editor.insert('end', "Welcome to AY text editor(AYTE)")
            self.editor.grid(row = 2, column = 0)

            self.sb1 = tk.Scrollbar(self.root, command = self.editor.yview, bg = '#000fff000')
            self.sb2 = tk.Scrollbar(self.root, command = self.editor.xview, orient = "horizontal", bg = '#000fff000')
            self.sb1.grid(row = 2, column = 1, sticky = 'ns')
            self.sb2.grid(row = 3, column = 0, sticky = 'ew')
            self.editor.configure(yscrollcommand = self.sb1.set, xscrollcommand = self.sb2.set)

            self.menubar = tk.Menu(app)
            self.men_1 = tk.Menubutton(self.root, text = 'File', bg = '#000FFF000')
            self.men_1.grid(row = 0, column = 0, sticky = 'w')
            self.men = tk.Menu(self.men_1, tearoff = 0, bg = '#00FFFF')
            self.men_1['menu'] = self.men

            self.men.add_command(label = 'New file ', command = self.new_file, accelerator = "(Ctrl + N)")
            self.men.add_command(label = 'Open file ', command = self.open_file, accelerator = "(Ctrl + O)")
            self.men.add_command(label = 'Save ', command = self.save_file, accelerator = "(Ctrl + S)")
            self.men.add_command(label = 'Save as ', command = self.save_as_file, accelerator = "(Ctrl + Shift + S)")

            self.men.add_separator()
            self.men.add_command(label = 'Exit ', command = root.destroy, accelerator = "(Ctrl + W)")
            self.men.add_command(label = 'Return to Home Screen', command = self.switch, accelerator = "(Ctrl + Shift + W)")

            self.men_2 = tk.Menubutton(self.root, text = 'Edit', bg = '#000FFF000')
            self.men_2.grid(row = 0, column = 0, sticky = 'w', padx = 30)
            self.men2 = tk.Menu(self.men_2, tearoff = 0, bg = '#00FFFF')
            self.men_2['menu'] = self.men2

            self.men2.add_command(label = 'Cut ', command = self.cut, accelerator = "(Ctrl + X)")
            self.men2.add_command(label = 'Paste ', command = self.paste, accelerator = "(Ctrl + V)")
            self.men2.add_command(label = 'Copy ', command = self.copy, accelerator = "(Ctrl + C)")

            self.men2.add_separator()
            self.men2.add_command(label = 'undo ', command = self.editor.edit_undo, accelerator = "(Ctrl + Z)")
            self.men2.add_command(label = 'redo ', command = self.editor.edit_redo, accelerator = "(Ctrl + Y)")

            self.men2.add_separator()
            self.men2.add_command(label = "Select All ", command = self.select_all, accelerator = "(Ctrl + A)")

            self.men_3 = tk.Menubutton(self.root, text = 'Font', bg = '#000FFF000')
            self.men_3.grid(row = 0, column = 0, sticky = 'w', padx = 60)
            self.men3 = tk.Menu(self.men_3, tearoff = 0, bg = '#00FFFF')
            self.men_3['menu'] = self.men3

            self.men3.add_command(label = "Bold", command = lambda : self.fonter('bold', "weight"), accelerator = "(Ctrl + B)")
            self.men3.add_command(label = "Italics", command = lambda : self.fonter('italic', "slant"), accelerator = "(Ctrl + Shift + I)")
            self.men3.add_command(label = "Underline", command = lambda : self.fonter(True, "underline"), accelerator = "(Ctrl + U)")
            self.men3.add_command(label = "Overstrike", command = lambda : self.fonter(True, "overstrike"), accelerator = "(Ctrl + Shift + O)")

            self.men3.add_separator()
            self.men3.add_command(label = 'Algerian', command = lambda : self.fonter('algerian', "family"), accelerator = "(Ctrl + Shift + A)")
            self.men3.add_command(label = 'Helvecta', command = lambda : self.fonter('helvecta', "family"), accelerator = "(Ctrl + H)")
            self.men3.add_command(label = 'Times', command = lambda : self.fonter('times', "family"), accelerator = "(Ctrl + T)")
            self.men3.add_command(label = "Comic Sans", command = lambda : self.fonter('comic sans', "family"), accelerator = "(Ctrl + Shift + C)")

            self.men_4 = tk.Menubutton(self.root, text = 'Colour', bg = '#000FFF000')
            self.men_4.grid(row = 0, column = 0, sticky = 'w', padx = 95)
            self.men4 = tk.Menu(self.men_4, tearoff = 0, bg = '#00FFFF')
            self.men_4['menu'] = self.men4

            self.men4.add_command(label = 'selected text fg', command = lambda : self.colchange(1))
            self.men4.add_command(label = 'all text bg', command = lambda : self.colchange(3))
            self.men4.add_command(label = 'all text fg', command = lambda : self.colchange(2))
            self.men4.add_command(label = 'Select fg', command = lambda : self.colchange(4))
            self.men4.add_command(label = 'Select bg', command = lambda : self.colchange(5))
            self.men4.add_command(label = 'Highlight color', command = lambda : self.colchange(6))

            self.men3.add_separator()
            self.men3.add_command(label = 'Allign Right', command = lambda : self.allign('right'))
            self.men3.add_command(label = 'Allign Left', command = lambda : self.allign('left'))
            self.men3.add_command(label = 'Allign Center', command = lambda : self.allign('center'))


            self.fs = tk.Scale(self.root, from_ = 12, to = 72, orient = 'horizontal', command = self.change_font, bg = '#000fff000')
            self.fs.grid(row = 1, column = 0, sticky = 'w', padx = 10)

            self.root.grid()
        def switch(self):
            ex = messagebox.askokcancel("Changes left pending", "Unsaved changes will be abandoned if you exit")
            if not ex: return

            root_2.grid()
            app.title('Home screen')
            app.configure(bg = root_2.cget('bg'))
            
            app.unbind('<Control Key>')
            app.unbind('<Control Shift Key>')
            
            self.root.grid_remove()

        def select_all(self):
            self.editor.tag_add('sel', "1.0", 'end')
            self.editor.mark_set('insert', "1.0")
            self.editor.see('insert')

        def copy(self, e = None):
            if e: self.selected = app.clipboard_get()
            
            elif self.editor.selection_get():
                app.clipboard_clear()
                self.selected = self.editor.get("sel.first", "sel.last")
                app.clipboard_append(self.selected)
        def cut(self, e = None):
            if e: self.selected = app.clipboard_get()
            
            elif self.editor.selection_get():
                app.clipboard_clear()
                self.selected = self.editor.get("sel.first", "sel.last")
                app.clipboard_append(self.selected)
                self.editor.delete("sel.first", "sel.last")
        def paste(self, e = None):
            if e is None and self.selected:
                text = self.editor.index('insert')
                self.editor.insert(text, app.clipboard_get())

        def new_file(self):
            app.title("New file - AY text self.editor(AYTE) ")
            self.editor.delete(1.0, 'end')
        def open_file(self):
            self.editor.delete(1.0, 'end')
            opened = filedialog.askopenfile(initialdir = "D:\\Advaith\\Code\\class\\pycode", title = 'Open File', filetypes = (("All Files", "*.*"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("Arduino Files", "*.ino"), ("Text files", "*.txt")))
            
            if opened is None: return

            self.name = opened
            app.title("{} - AY text self.editor(AYTE)".format(self.name.name))
            
            fil = open(self.name.name, "r")
            self.editor.insert(1.0, fil.read())
            fil.close()

        def save_file(self):
            if not self.name:
                self.save_as_file()
                return
            
            fil2 = open(self.name.name, "w")
            fil2.writelines(self.editor.get(1.0, 'end'))
            fil2.close()
        def save_as_file(self):
            opened = filedialog.asksaveasfile(defaultextension = "*.*", filetypes = (("All Files", "*.*"), ("Python Files", "*.py"), ("Text Files", "*.txt"), ("Arduino Files", "*.ino"), ("HTML Files", "*.html")))
            
            if opened is None: return
            
            self.name = opened
            app.title("{} - AY text self.editor(AYTE)".format(self.name.name))
            self.save_file()

        def fonter(self, ty, ty2):
            try:
                if self.editor.selection_get():
                    myfont = font.Font(self.editor, self.editor.cget('font'))
                    myfont[ty2] = ty
                    
                    self.editor.tag_configure(ty, font = myfont)
                    bold = self.editor.tag_names("sel.first")
                
                    if ty not in bold: self.editor.tag_add(ty, "sel.first", "sel.last")
                    else: self.editor.tag_remove(ty, "sel.first", "sel.last")
            except: pass
        def colchange(self, e):
            color = colorchooser.askcolor()[1]
            if color == None: return
            if e == 1:
                try:
                    if self.editor.selection_get(): pass
                except: return
                
                myfont = font.Font(self.editor, self.editor.cget('font'))
                self.editor.tag_configure("colour", font = myfont, foreground = color)
                bold = self.editor.tag_names("sel.first")
                
                if "colour" not in bold: self.editor.tag_add("colour", "sel.first", "sel.last")
                else: self.editor.tag_remove("colour", "sel.first", "sel.last")
            
            elif e == 2: self.editor.configure(fg = color)
            elif e == 3: self.editor.configure(bg = color)
            elif e == 4: self.editor.configure(selectforeground = color)
            elif e == 6:
                try: self.editor.selection_get()
                except: return
                myfont = font.Font(self.editor, self.editor.cget('font'))
                self.editor.tag_configure("colour", font = myfont, background = color)
                bold = self.editor.tag_names("sel.first")
                if "colour" not in bold: self.editor.tag_add("colour", "sel.first", "sel.last")
                else: self.editor.tag_remove("colour", "sel.first", "sel.last")
            else: self.editor.configure(selectbackground = color)

        def terminal(self):
            if self.name != 0: os.system('cmd')
            
            else: os.system('cmd')

        def binding(self, e):
            e = e.keysym
            
            if e == 'n': self.new_file()
            elif e == 's': self.save_file()
            elif e == 'o': self.open_file()
            elif e == 'w': root.destroy()
            elif e == 'z': self.editor.edit_undo()
            elif e == 'y': self.editor.edit_redo()
            elif e == 'c': self.copy()
            elif e == 'x': self.cut()
            elif e == 'v': self.paste()
            elif e == 'b': self.fonter("Algerian", "Font")
            elif e == 'u': self.fonter(True, "Underline")
        def bind2(self, e):
            e = e.keysym
            
            if e == 'S': self.save_as_file()
            elif e == 'I': self.fonter('italic', "slant")
            elif e == 'O': self.fonter(True, "overstrike")
            elif e == 'A': self.fonter('Algerian', "family")
            elif e == 'C': self.fonter('Comic Sans', "family")
            elif e == 'W': self.switch()

        def change_font(self, e):
            try:
                if self.editor.selection_get(): pass
            except: return
            
            myfont = font.Font(self.editor, self.editor.cget('font'))
            myfont['size'] = self.fs.get()
            
            self.editor.tag_configure('mf', font = myfont)
            self.editor.tag_add('mf', "sel.first", "sel.last")

        def allign(self, pos):
            position = int(float(self.editor.index('insert')))
            
            self.editor.tag_configure('just', justify = pos)
            self.editor.tag_add('just', float(position))

    class pingpong:
        global proot

        def __init__(self, root_2, app):
            global proot

            root_2.grid_remove()
            app.geometry('575x575+550+100')

            if proot:
                self.f = proot[1]
                self.f.grid()
                return

            self.f = tk.Frame(app)
            self.f.grid()

            tk.Label(self.f, text = "Ping Pong", font = ('Arial black', 30, 'bold'), bg = "gold", relief = 'solid').grid(row = 0, column = 0, sticky = 'ew')
            tk.Button(self.f, text = "Single Player with CPU", font = ('Elephant', 15, 'bold'), bg = "red", fg = "#d3d3d3", command = lambda : self.game_start(False)).grid(row = 1, column = 0)
            tk.Button(self.f, text = "Multiplayer", font = ('Elephant', 15, 'bold'), bg = "blue", fg = '#d3d3d3', command = lambda : self.game_start(True)).grid(row = 2, column = 0, sticky = 'ew')

            app.mainloop()

        def game_start(self, cop):
            global proot

            self.root = tk.Canvas(app, bg = '#000fff000')
            
            if proot:
                self.root = proot[0]
                
                app.bind('<Up>', self.move_up)
                app.bind('<w>', self.move_up)
                app.bind('<Control-w>', self.move_up)
                app.bind('<s>', self.move_down)
                app.bind('<Down>', self.move_down)
                app.bind('<space>', self.move_up)
                
                return

            self.cop = cop

            self.root.configure(width = 575, height = 575)

            self.f.grid_remove()
            self.root.grid()

            self.ft = True
            self.opposite = False
            self.stop = True
            self.inc = 0
            self.starter = "red"

            self.paused = self.root.create_text(1000, 1000, text="PAUSED", font=("Times New Roman", 30))

            self.blue = self.root.create_rectangle(0, 155, 10, 245, fill = 'blue')
            self.red = self.root.create_rectangle(390, 155, 400, 245, fill = 'red')
            
            self.root.coords(self.paused, 200, 50)

            self.root.create_oval(150, 150, 250, 250)
            self.root.create_line(200, 0, 200, 400)

            self.pong = self.root.create_oval(190, 190, 210, 210, fill = 'white')

            app.bind('<Up>', self.move_up)
            app.bind('<Down>', self.move_down)

            self.root.create_rectangle(0, 400, 400, 450, fill = 'red')
            self.root.create_rectangle(0, 450, 400, 500, fill = 'blue')

            self.score = [0, 0]
            self.rscore = self.root.create_text(200, 423, text = "Player 1 - 0", font = ('Palatino', 15, 'bold'))

            if cop:
                self.bscore = self.root.create_text(200, 473, text = "Player 2 - 0", font = ('Palatino', 15, 'bold'))
                app.bind('<w>', self.move_up)
                app.bind('<s>', self.move_down)
            else: self.bscore = self.root.create_text(200, 473, text = "CPU - 0", font = ('Palatino', 15, 'bold'))

            self.root.create_text(200, 538, text = "Space - Pause / Play\nUp / Down - Moving Red(Player 1)\nW / S - Moving Blue(Player 2)", fill = 'black', font = ("Arial", 15))
            myfont = font.Font(self.root, family = "Algerian", slant = 'italic', size = 15)

            self.root.create_rectangle(400, 0, 575, 100, fill = 'saddle brown')
            self.root.create_rectangle(400, 100, 575, 200, fill = 'silver')
            self.root.create_rectangle(400, 200, 575, 300, fill = 'gold')
            self.root.create_rectangle(400, 300, 575, 400, fill = 'white')
            self.root.create_text(483, 50, text = "Quit", font = myfont, fill="white")
            self.root.create_text(483, 150, text = "Return to \nHome Screen", font = myfont, justify = 'center')
            self.root.create_text(483, 250, text = "Return to \nApp Screen", font = myfont, justify = 'center')
            self.root.create_text(483, 350, text = "Replay", font = myfont, justify = 'center')
            
            self.root.create_line(400, 100, 575, 100, dash = (4, 2))
            self.root.create_line(400, 200, 575, 200, dash = (4, 2))
            self.root.create_line(400, 300, 575, 300, dash = (4, 2))
            self.root.create_line(400, 400, 575, 400, dash = (4, 2))

            self.root.bind('<Button-1>', self.click)
            app.bind('<space>', self.move_up)

        def move_up(self, event):
            if self.stop and (not (event.keysym == 'space')): return
            if event == 'up':
                coords = self.root.coords(self.blue)
                if coords[1] == 0: return
                
                self.root.coords(self.blue, coords[0], coords[1]-20, coords[2], coords[3]-20)
                
                return
            elif event.keysym == 'space':
                # If user is (un)pausing it
                
                if self.stop:
                    # If user is unpausing it
                    self.stop = False
                    self.root.coords(self.paused, 1000, 1000)

                    if not self.cop: self.checker()
                    
                    self.motion(self.starter, self.inc)
                    
                    return
                
                self.root.coords(self.paused, 200, 50)
                self.stop = True
                return
            elif event.keysym == 'Up':
                coords = self.root.coords(self.red)
                if coords[1] == 0: return
                self.root.coords(self.red, coords[0], coords[1]-20, coords[2], coords[3]-20)
            else:
                coords = self.root.coords(self.blue)
                if coords[1] == 0: return
                
                self.root.coords(self.blue, coords[0], coords[1]-20, coords[2], coords[3]-20)
        
        def move_down(self, event):
            if event is None:
                self.f.grid_remove()
                self.root.grid()
                return

            elif self.stop: return
            
            elif event == 'down':
                coords = self.root.coords(self.blue)
                if coords[1] == 400: return
                self.root.coords(self.blue, coords[0], coords[1]+20, coords[2], coords[3]+20)

            elif event == "up":
                coords = self.root.coords(self.blue)
                if coords[1] == 400: return
                self.root.coords(self.blue, coords[0], coords[1]+20, coords[2], coords[3]+20)
            
            elif event.keysym == 'Down':
                coords = self.root.coords(self.red)
                if coords[3] == 400: return
                self.root.coords(self.red, coords[0], coords[1]+20, coords[2], coords[3]+20)
            
            else:
                coords = self.root.coords(self.blue)
                if coords[1] == 400: return
                self.root.coords(self.blue, coords[0], coords[1]+20, coords[2], coords[3]+20)

        def motion(self, start, increase = 0):
            if exit_now: return

            if self.stop:
                self.inc = increase
                self.starter = start                
                return

            coords = self.root.coords(self.pong)
            
            if coords[2] >= 400 or coords[0] <= 0:
                self.update()
                return
            
            elif coords[3] >= 400 or coords[1] <= 0: increase = 0-increase

            if start == 'red':
                self.redcoords = self.root.coords(self.red)
            
                if coords[2] == 390:
                    if coords[1] > self.redcoords[1] and coords[1] < self.redcoords[3]:
                        self.ft = True
                        raverage = (self.redcoords[1]+self.redcoords[3])/2
                        caverage = (coords[1]+coords[3])/2
            
                        if caverage != raverage:
                            self.root.after(100, self.motion, 'blue', (caverage-raverage)/8)
                            return
            
                        self.root.after(100, self.motion, 'blue')
                        return
            
                self.root.coords(self.pong, coords[0]+20, coords[1]+increase, coords[2]+20, coords[3]+increase)
                self.root.after(55, self.motion, 'red', increase)
            
            else:
                self.redcoords = self.root.coords(self.blue)
                if coords[0] == 10:
                    if coords[1] > self.redcoords[1] and coords[1] < self.redcoords[3]:
                        raverage = (self.redcoords[1]+self.redcoords[3])/2
                        caverage = (coords[1]+coords[3])/2
                        if caverage != raverage:
                            self.root.after(100, self.motion, 'red', (caverage-raverage)/8)
                            return
                        self.root.after(100, self.motion, 'red')
                        return
                self.root.coords(self.pong, coords[0]-20, coords[1]+increase, coords[2]-20, coords[3]+increase)
                self.root.after(55, self.motion, 'blue', increase)

        def checker(self, torf = False):
            if self.stop: return

            redcoords = self.root.coords(self.blue)
            coords = self.root.coords(self.pong)

            updown = random.randrange(0, 2)

            if coords[0] < 150 and self.ft == True:
                self.ft = False
                choice = random.randrange(0, 5)
                choices = [False, True, True, True, True]
                choice = choices[choice]
                self.opposite = not choice

            elif coords[0] == 30: torf = True

            if redcoords[1] < coords[1] and redcoords[3] > coords[1]: 
                if not self.opposite:
                    if (coords[1] + coords[3])/2 == (redcoords[1] + redcoords[3])/2 and coords[0] == 50:
                        if updown: self.move_up('up')
                        else: self.move_down('down')
                elif redcoords[3] <= 390:
                    if exit_now: return
                    self.move_down('down')
                    self.move_down('down')
                    self.move_down('down')
                    self.move_down('down')
                else:
                    self.move_down('up')
                    self.move_down('up')
                    self.move_down('up')
                    self.move_down('up')
            
            elif redcoords[1] > coords[1]:
                if not self.opposite:
                    self.move_up('up')
                    if updown:
                        self.move_up('up')
                        self.move_up('up')
                
                elif redcoords[3] <= 390:
                    self.move_down('down')
                    self.move_down('down')
                    self.move_down('down')
                    self.move_down('down')

            elif redcoords[3] < coords[3]:
                if not self.opposite:
                    self.move_down('down')
                    if updown:
                        self.move_down('down')
                        self.move_down('down')
                
                elif redcoords[3] >= 10:
                    self.move_up('up')
                    self.move_up('up')
                    self.move_up('up')
                    self.move_up('up')

            if not self.opposite and not exit_now: self.root.after(55, self.checker, torf)
            elif not exit_now: self.root.after(750, self.checker, torf)

        def update(self, coords=[]):
            if coords == []: coords = self.root.coords(self.pong)

            self.ft = True
            self.opposite = False
            
            if coords[0] <= 0:
                self.ft = True
                self.score[0] = self.score[0] + 1
            
                self.root.coords(self.pong, 190, 190, 210, 210)
                self.root.coords(self.red, 390, 155, 400, 245)
                self.root.coords(self.blue, 0, 155, 10, 245)
                if not exit_now: self.root.after(1000, self.motion, 'red')
                self.root.itemconfigure(self.rscore, text = "Player 1 - "+str(self.score[0]))
            
            else:
                self.ft = True
                self.score[1] = self.score[1] + 1
            
                self.root.coords(self.pong, 190, 190, 210, 210)
                self.root.coords(self.red, 390, 155, 400, 245)
                self.root.coords(self.blue, 0, 155, 10, 245)

                if not exit_now: self.root.after(1000, self.motion, 'blue')
                
                if self.cop: self.root.itemconfigure(self.bscore, text = "Player 2 - "+str(self.score[1]))
                else: self.root.itemconfigure(self.bscore, text = "CPU - "+str(self.score[1]))
            
        def switch(self, torf = 0):
            global proot
            
            self.stop = True
            self.root.grid_remove()
            
            if torf: self.f.grid()
            
            else:
                proot = self.root, self.f
                
                tk.Button(self.f, text = "Continue Playing", font = ('Elephant', 15, 'bold'), bg = 'green', fg = "#d3d3d3", command = lambda : self.move_down(None)).grid(row = 3, column = 0, sticky = 'ew')
                
                root_2.grid()
                
                app.geometry('1600x900')
                
                app.unbind('<Up>')
                app.unbind('<Control-w>')
                app.unbind('<w>')
                app.unbind('<s>')
                app.unbind('<Down>')
                app.unbind('<space>')
                
                app.title('Home Screen')
                app.configure(bg = root_2.cget('bg'))
                
                self.root.grid_remove()
        
        def click(self, event):
            x, y = event.x, event.y
            
            if not (x > 400 and x < 575): return
            elif y > 0 and y < 100: root.destroy()
            elif y > 100 and y < 200: self.switch()
            elif y > 200 and y < 300:
                tk.Button(self.f, text = "Continue Playing", font = ('Elephant', 15, 'bold'), bg = 'green', fg = "#d3d3d3", command = lambda : self.move_down(None)).grid(row = 3, column = 0, sticky = 'ew')
                self.switch(1)
            elif y > 300 and y < 400:
                self.score = [0, 0]

                self.ft = True
                self.stop = True
            
                self.root.coords(self.pong, 190, 190, 210, 210)
                self.root.coords(self.red, 390, 155, 400, 245)
                self.root.coords(self.blue, 0, 155, 10, 245)
                self.root.coords(self.paused, 200, 50)
                
                self.root.itemconfigure(self.rscore, text = "Player 1 - 0")

                if self.cop: self.root.itemconfigure(self.bscore, text = "Player 2 - 0")
                else: self.root.itemconfigure(self.bscore, text = "CPU - 0")

    class quiz:
            global qroot

            def __init__(self, root_2, app):
                global qroot

                self.torf = False

                self.root = tk.Frame()
                root_2.grid_remove()

                self.st = datetime.now()
                self.root.after(540000, self.move, 5)

                app.geometry("300x450+650+200")
                app.title("!! Quiz !!")
                app.configure(bg = '#e0ba87')

                self.count = -1
                
                col = ['black', 'white', 'red', 'green', 'yellow', 'blue', 'brown', 'orange', 'pink', 'purple', 'grey']
                
                questions = {"1 + 1" : "2", "Who started DRDO" : "Avinash Chander", \
                            "Who was the first\nman in space" : "yuri gagarin", \
                            "Who was the first\nIndian in space" : "Rakesh Sharma", \
                            "Who was the first\nwoman in space" : "Valentina Tereshkova", \
                            "Who was the first\nPM of India" : "jawaharlal nehru", \
                            "2 + 2" : "4", "First president of india" : "Rajendra Prasad", \
                            "Who discovered cell" : "Robert hooke", "1248 / 78" : "16", \
                            "What doesn't have\ndefinite volume" : "gas", \
                            "Earth's radius in km\nno need of writing km" : "6371", \
                            "No. of people on Earth\nRound to 0.1 billion\nJust write number" : "7.8", \
                            "Largest continent" : "Asia", "6th largest country " : " australia", \
                            "What is Buddha's real name" : "Siddhartha Gautama", \
                            "What is the\ncapital of Tripura" : "Agartala", \
                            "What is the\ncapital of Assam" : "Dispur", \
                            "What is the\ncapital of\nArunachal pradesh" : "Itanagar", \
                            "What is the\ncapital of Meghalaya" : "Shillong", \
                            "What is the\ncapital of Manipur" : "Imphal", \
                            "What is the\ncapital of Mizoram" : "Aizwal", \
                            "What is the\ncapital of Nagaland" : "Kohima", \
                            "currency of kuwait\nJust write the\ncurrency no need of\nkuwaitan" : "dinar", \
                            "What is the currency\nof cuba no need\nof cuban" : "peso", \
                            "Capital of equador" : "quito", "Who is Rajya\nSabha head?" : "Venkaiah Naidu", \
                            "When did telangana form?\nType day, month, ex\n 15, February" : "2, June", \
                            "What party formed first\ngovernment in TS\nWrite Full Form" : "Telangana Rashtra Samiti", \
                            "Which state is\nPV Narasimha Rao From" : "Telangana", \
                            "What is the most grown\ncrop by area" : "rice", \
                            "Which State has most\nsugar mills" : "Uttar Pradesh", \
                            "Where are the currency\nnotes printed in" : "Nasik", \
                            "Who invented 0\nClue :No space in\nhis name" : "Aryabhatta", \
                            "How many edges\ndoes a cube have" : "12", \
                            "How many milliseconds\nare there in a day" : "86400000", \
                            "Largest non-extinct animal" : "Blue Whale", "Largest asteroid in the\nAsteroid belt" : "Ceres", \
                            "Who said 'I have not\nfailed. I have found 10,000\nways to not work'" : "Thomas Edison", \
                            "which year did WW2 start" : "1939", "What country's capital\nis Vienna" : "Austria", \
                            "Which year did IPL start" : "2008", "Who is the hero of\nMission Impossible" : "Tom Cruise", \
                            "What are compunds made up of" : "Elements", "When did India become\na British Colony\nNot East India Company" : "1858", \
                            "How many Union Teritories\nare there in India" : "9", \
                            "Which State's Main\nlanguage is Khasi" : "Meghalaya", \
                            "Which State produces\nthe most coffee" : "Karnataka", \
                            "3rd Largest State\nin India" : "Maharastra", "3rd most populated\nstate in India" : "Bihar"}
                
                
                qs = list(questions.keys())
                sa = list(questions.values())

                self.questions = list((None, )*10)
                self.actualans = []
                
                self.undo = False

                while True:
                    rr = random.randrange(0, len(questions))
                    if qs[rr] not in self.questions:
                        self.questions[self.questions.index(None)] = qs[rr]
                        self.actualans.append(sa[rr])
                    
                    if None not in self.questions: break

                self.usersansw = list((None, )*10)

                self.myfont = font.Font(self.root, family = "Lusida Calligraphy", size = 16, weight = 'bold')

                self.ques = tk.Label(self.root, text = "Question\nWrite First and Last\nnames only\nFor true and false", bg = "#E7E620", font = self.myfont)

                self.eans = tk.Entry(self.root, bg = "#D3D3D3", font = self.myfont)
                self.eans.insert(0, "Answer")
                self.eans.bind('<Return>', self.move)

                self.prev = tk.Button(self.root, text = "Previous\nQuestion", bg = "red", font = self.myfont, command = self.move)
                self.bnex = tk.Button(self.root, text = "Start\nQuiz", bg = "gold", font = self.myfont, command = lambda : self.move("prev"))

                self.replay = tk.Button(self.root, text = "Replay", bg = 'white', font = self.myfont, command = lambda : self.switch(True), state = "disabled")
                self.replay.grid(row = 4, column = 0, sticky = 'ew')
                
                tk.Button(self.root, text = "Return to\nHome Screen", bg = 'gray45', font = self.myfont, command = self.switch).grid(row = 5, column = 0, sticky = 'ew')
                tk.Button(self.root, text = "Quit", bg = 'black', fg = 'white', font = self.myfont, command = app.destroy).grid(row = 6, column = 0, sticky = 'ew')

                self.ques.grid(row = 0, column = 0, sticky = 'ew')
                self.eans.grid(row = 1, column = 0, sticky = 'ew')
                self.prev.grid(row = 2, column = 0, sticky = 'ew')
                self.bnex.grid(row = 3, column = 0, sticky = 'ew')

                self.root.grid()

            def move(self, wid = None):
                if (wid == 1 or wid == 10) and not self.torf:
                    if "" in self.usersansw and not self.undo:
                        self.undo = True

                        self.eans.delete(0, 'end')
                        self.eans.insert(0, "You left some qs")
                        return

                    self.root.after_cancel(540000)
                    self.root.after_cancel(60000)

                    self.usersansw[-1] = self.eans.get()
                    
                    self.replay['state'] = "normal"

                    score = 0

                    print("Wrongs -;\n")

                    for no in range(0, len(self.usersansw)):
                        given_ans = self.usersansw[no]
                        if given_ans.lower() == self.actualans[no].lower(): score += 1
                        else:
                            if not given_ans or given_ans == "You left some qs":
                                print("\nQuestion:", self.questions[no], "\nCorrect Answer:", self.actualans[no], "\nYou did not attempt this question.", "\n")
                            else:
                                print("\nQuestion:", self.questions[no], "\nCorrect Answer:", self.actualans[no], "\nYour answer:", given_ans, "\n")

                    self.torf = True
                    self.eans.delete(0, 'end')
                    if wid == 10: self.eans.insert(0, "Time is up")
                    
                    self.eans['state'] = 'disabled'
                    self.ques['text'] = "{}/{}, {}%\n{}".format(score, no+1, round((score/(no+1))*100, 2), datetime.now()-self.st)

                elif wid == 5:
                    self.bnex['text'] = self.bnex['text'] + "\nLess than 1 min left"
                    self.root.after(60000, self.move, 10)

                elif not wid:
                    if self.count <= 0: return

                    elif self.count == len(self.questions)-1:
                        self.bnex['text'] = "Next\nQuestion"
                        self.bnex['command'] = lambda : self.move('self.prev')
                        
                        self.eans.unbind('<Return>')
                        self.eans.bind('<Return>', self.move)

                    self.count -= 1

                    self.usersansw[self.count+1] = self.eans.get()

                    self.ques['text'] = self.questions[self.count]
                    self.eans.delete(0, 'end')
                    self.eans.insert(0, self.usersansw[self.count])

                else:
                    if self.count >= len(self.questions)-1: return
                    
                    elif self.count+1 == len(self.questions)-1:
                        self.bnex['text'] = "Submit\nAnswers"
                        self.bnex['command'] = lambda : self.move(1)
                        
                        self.eans.unbind('<Return>')
                        self.eans.bind('<Return>', lambda e : self.move(1))
                    
                    elif self.count == -1: self.bnex['text'] = "Next\nQuestion"

                    self.count += 1
                    if self.count != 0: self.usersansw[self.count-1] = self.eans.get()

                    self.ques['text'] = self.questions[self.count]
                    self.eans.delete(0, 'end')
                    
                    if self.usersansw[self.count]: self.eans.insert(0, self.usersansw[self.count])

            def switch(self, re = False):
                global qroot
                
                if re:
                    self.__init__(self.root, app)
                    return

                qroot = self.root
                root_2.grid()
                app.title('Home Screen')
                app.configure(bg = root_2.cget('bg'))
                self.root.grid_remove()

    class excel:
        global eroot

        def __init__(self, root_2, app):
            global eroot

            app.title('AY excel sheets')
            app.configure(bg = "#e0ba87")
            root_2.grid_remove()

            if eroot:
                self.root = eroot
                self.root.grid()
                return

            self.root = tk.Frame(app, bg = '#e0ba87')

            app.title('AY excel sheets')
            app.configure(bg = "#e0ba87")
            self.root = tk.Frame(app, bg = '#e0ba87')

            self.options = ['winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative']
            self.chance = [True, False, True, True, True, True, True, True, True, True]

            self.tree = ttk.Treeview(self.root, columns = ("Name", "DOB", "Rating", "Favourite Language"), selectmode = "extended")

            self.scrolltree = tk.Scrollbar(self.root, command = self.tree.yview)
            self.tree.configure(yscrollcommand = self.scrolltree.set)
            self.scrolltree.grid(row = 0, column = 3, sticky = 'ns')

            self.style = ttk.Style()
            self.style.theme_use(self.options[random.randrange(0, 7)])

            if self.chance[random.randrange(0, 10)]:
                self.style.configure("Treeview", background = 'gold', foreground = 'black', rowheight = 25, fieldbackground = '#e0ba87')
                self.style.map('Treeview', background = [('selected', 'orange')], foreground = [('selected', 'black')])
                self.tree.tag_configure("oddrow", background = 'silver', foreground = 'black')
                self.tree.tag_configure("evenrow", background = 'gold', foreground = 'black')

            else:
                self.tree.tag_configure("odd", background = 'white', foreground = 'black')
                self.tree.tag_configure("even", background = 'white', foreground = 'black')

            self.myfont = font.Font(app, family = "Elephant", size = 15, weight = "bold")
            self.entryfont = font.Font(app, family = "Georgia", size = 13, weight = 'bold', slant = 'italic', )

            self.tree.column("#0", width = 0, stretch = 'no')

            self.tree.column("Name", width = 120, anchor = "w", minwidth = 60)
            self.tree.column("DOB", width = 120, anchor = "c", minwidth = 60)
            self.tree.column("Rating", width = 120, anchor = "c", minwidth = 60)
            self.tree.column("Favourite Language", width = 120, anchor = "c", minwidth = 60)


            self.tree.heading("#0", anchor = 'center', text = "")

            self.tree.heading("Name", anchor = "center", text = "Name")
            self.tree.heading("DOB", anchor = "center", text = "Age")
            self.tree.heading("Rating", anchor = "center", text = "ID")
            self.tree.heading("Favourite Language", anchor = "center", text = "Job")

            self.consdata = [("Gayathri", 38, 1, "House self.work")\
                , ("Mahesh", 43, 2, "Office self.work")\
                , ("Advaith", 11, 5, "Study")\
                , ("Adithi", 14, 3, "Study")\
                , ("Bob", "1 month", 10, "Stay behind")
                , ("Steve", 9, 4, "Mine ores")\
                , ("Notch", 11, 9, "Minecraft")\
                , ("Shawn Mendes", 22, 7, "Sing")\
                , ("DanTDM", 28, 8, "Play")\
                , ("Mr. Beast", 22, 6, "Spend money")\
                , ("Computer", 67, 11, "Calculate")\
                , ("Trivikram", 48, 20, "Director")\
                , ("Iron Man", 35, 15, "Fight evil")\
                ]

            self.data = [("Gayathri", 38, 1, "House self.work")\
                , ("Mahesh", 43, 2, "Office self.work")\
                , ("Advaith", 11, 5, "Study")\
                , ("Adithi", 14, 3, "Study")\
                , ("Bob", "1 month", 10, "Stay behind")
                , ("Steve", 9, 4, "Mine ores")\
                , ("Notch", 11, 9, "Minecraft")\
                , ("Shawn Mendes", 22, 7, "Sing")\
                , ("DanTDM", 28, 8, "Play")\
                , ("Mr. Beast", 22, 6, "Spend money")\
                , ("Computer", 67, 11, "Calculate")\
                , ("Trivikram", 48, 20, "Director")\
                , ("Iron Man", 35, 15, "Fight evil")\
                ]

            self.count = 0
            for ele in self.data:

                if self.count%2 == 0:  self.tree.insert("", 'end', iid = self.count, text = "", values = ele, tags = ('evenrow',))
                else: self.tree.insert("", 'end', iid = self.count, text = "", values = ele, tags = ('oddrow',))

                self.count += 1

            tk.Label(self.root, width = 75, bg = "#e0ba87").grid(row = 0, column = 0)

            self.tree.bind('<Double-1>', lambda e : self.root.after(10, self.get_selected))

            self.tree.grid(row = 0, column = 2)

            self.name = tk.Entry(self.root, font = self.entryfont, width = 10, bg = '#00ffff', fg = 'blue')
            self.name.insert("end", "Name")
            self.name.select_range(0, 'end')
            self.name.focus_set()
            self.name.grid(row = 1, column = 2, sticky = 'w')

            self.dob = tk.Entry(self.root, font = self.entryfont, width = 10, bg = "#000fff000", fg = 'green')
            self.dob.insert("end", "Age")
            self.dob.select_range(0, 'end')
            self.dob.grid(row = 1, column = 2, padx = 120, sticky = 'w')

            self.rating = tk.Entry(self.root, font = self.entryfont, width = 10, bg = 'green', fg = '#000fff000')
            self.rating.insert("end", "ID")
            self.rating.select_range(0, 'end')
            self.rating.grid(row = 1, column = 2, padx = 120, sticky = 'e')

            self.work = tk.Entry(self.root, font = self.entryfont, width = 10, bg = 'blue', fg = '#00ffff')
            self.work.insert("end", "Work")
            self.work.select_range(0, 'end')
            self.work.grid(row = 1, column = 2, sticky = 'e')

            tk.Button(self.root, text = "Add", font = self.myfont, command = self.addata, bg = 'black', fg = 'white').grid(row = 2, column = 2, pady = 20)
            
            tk.Button(self.root, text = "Clear all", font = self.myfont, command = self.clear, bg = 'saddle brown', fg = 'white').grid(row = 3, column = 2, pady = 10)
            tk.Button(self.root, text = "Clear Selected", font = self.myfont, command = lambda : self.clear(True), bg = 'red', fg = 'white').grid(row = 4, column = 2, pady = 10)
            
            tk.Button(self.root, text = "Move Selected Up", font = self.myfont, command = lambda : self.move('up'), bg = 'white', fg = 'red').grid(row = 5, column = 2, pady = 10)
            tk.Button(self.root, text = "Move Selected Down", font = self.myfont, command = lambda : self.move('down')).grid(row = 6, column = 2, pady = 10)
            
            tk.Button(self.root, text = "Modify Selected Values", font = self.myfont, command = self.modify, bg = 'white', fg = 'saddle brown').grid(row = 7, column = 2, pady = 10)
            
            tk.Button(self.root, text = "Exit", font = self.myfont, command = app.destroy, bg = 'gold').grid(row = 0, column = 0)
            tk.Button(self.root, text = "Return to Home Screen", font = self.myfont, command = self.switch, bg = '#d3d3d3').grid(row = 0, column = 5, sticky = 'e')

            tk.Label(self.root, width = 17, bg = self.root['bg']).grid(row = 0, column = 4)

            tk.Label(self.root, text = "If you get no colour, you are lucky\nChance is 1 in {} (1/{})".format(len(self.chance), len(self.chance)), font = self.myfont, bg = "#0E00AF", fg = "#F3F2F7").grid(row = 8, column = 2)

            ttk.Sizegrip(self.root).grid(column = 2, sticky = 's', row = 9)
            ttk.Sizegrip(self.root).grid(column = 2, sticky = 'ws', row = 9)

            self.root.grid()

        def move(self, updown):
            if updown == 'up':
                selected = self.tree.selection()
                for ele in selected:
                    self.tree.move(ele, "", self.tree.index(ele)-1)
            
            else:
                selected = self.tree.selection()
                for ele in reversed(selected):
                    self.tree.move(ele, "", self.tree.index(ele)+1)

        def addata(self):
            entry = (self.name.get(), self.dob.get(), self.rating.get(), self.work.get())

            self.name.delete(0, 'end')
            self.dob.delete(0, 'end')
            self.rating.delete(0, 'end')
            self.work.delete(0, 'end')

            if entry in self.data: 
                self.name.insert('end', "Already")
                self.dob.insert('end', "There")
                self.root.after(2000, self.name.delete, 0, 'end')
                self.root.after(2000, self.dob.delete, 0, 'end')
                return
            
            if self.count%2 == 0: self.tree.insert("", 'end', self.count, values = entry, tags = ('evenrow', ))
            else: self.tree.insert("", 'end', self.count, values = entry, tags = ('oddrow', ))
            
            self.count += 1

            self.consdata.append(entry)
            self.data.append(entry)

        def clear(self, torf = False):
            if torf:
                a = self.tree.selection()
                for ele in a:
                    self.tree.delete(ele)
                    self.data.remove(self.consdata[int(ele)])
                return

            self.data = []

            for child in self.tree.get_children(): self.tree.delete(child)

        def get_selected(self):
            selected = self.tree.focus()

            self.name.delete(0, 'end')
            self.dob.delete(0, 'end')
            self.work.delete(0, 'end')
            self.rating.delete(0, 'end')

            value = self.tree.item(selected, 'value')
            
            self.name.insert('end', value[0])
            self.dob.insert('end', value[1])
            self.work.insert('end', value[3])
            self.rating.insert('end', value[2])

        def modify(self):
            selected = self.tree.focus()

            self.tree.item(selected, text = "", values = (self.name.get(), self.dob.get(), self.rating.get(), self.work.get()))

            self.name.delete(0, 'end')
            self.dob.delete(0, 'end')
            self.work.delete(0, 'end')
            self.rating.delete(0, 'end')

        def switch(self):
                global eroot
                
                eroot = self.root
                root_2.grid()
                app.title('Home screen')
                app.configure(bg = root_2.cget('bg'))
                self.root.grid_remove()

    class Asteroids:
        global astroot
            
        def __init__(self, root_2, app):
            global astroot

            app.title('Asteroids (An arcade game)')
            app.state('zoomed')

            root_2.grid_remove()

            self.root = tk.Canvas(app, bg = 'black', width = 1550, height = 860, cursor="cross")

            self.side = 'left'


            self.stop = False
            self.reshoot = True
            self.selfstop = False
            self.orange = False
            self.red = False
            self.stopper = False
            
            self.hearts = 3
            
            self.creation = []
            self.tfa = []
            self.tfm = []

            self.d = {}

            
            self.angle = 0
            self.duration = 7500
            self.once = False

            self.gwords = ["OOOOO00000ooooofffff", "NOICE SHOT", "KEEP IT UP", "sUpeR", "LET'S GOOOO", "PRO", "AMAZING", "HIT", "BROKEN!!!", "=D"]
            self.bwords = ["OOOOO00000ooooofffff", "JUST MISS!!!", "HARD LUCK!!!", "DON'T KEEP IT UP", "noT sUpER", "LET'S NOT GOOOO", "NOOB!!!", "UMMMM....", "D=", "LOST MY HOPE"]

            self.img = Image.open("images_for_gcpy/rocket.png")
            self.img = self.img.resize((100, 100), Image.Resampling.LANCZOS)
            self.image = ImageTk.PhotoImage(self.img.rotate(0))

            self.ball = self.root.create_image(775, 400, image = self.image)

            self.heart1 = self.root.create_rectangle(10, 10, 50, 50, fill = 'red')
            self.heart2 = self.root.create_rectangle(75, 10, 115, 50, fill = 'red')
            self.heart3 = self.root.create_rectangle(140, 10, 180, 50, fill = 'red')
            self.lohearts = [self.heart1, self.heart2, self.heart3]

            self.bbtg = self.root.create_rectangle(-10, -10, -2, -2, fill = "gray20")
            self.btg = self.root.create_text(-10, -10, text = "Back To Game", fill = "white", font = ("Informal roman", 24, 'bold'))

            self.besc = self.root.create_rectangle(-10, -10, -2, -2, fill = "gray20")
            self.esc = self.root.create_text(-10, -10, text = "Quit", fill = "white", font = ("Informal roman", 24, 'bold'))

            self.bret = self.root.create_rectangle(-10, -10, -2, -2, fill = "gray20")
            self.ret = self.root.create_text(-10, -10, text = "Return to Home Screen", fill = "white", font = ("Informal roman", 24, 'bold'))

            self.now = None
            self.sod = True

            self.attr = False

            self.dtn = datetime.now()

            self.root.create_rectangle(0, 800, 1550, 860, fill = "#e0ba47")
            self.gbw = self.root.create_text(775, 830, font=("Algerian", 15, 'bold', 'italic'))

            self.no0 = app.after(15000, self.move, "Random")
            self.no1 = app.after(3000, self.attack, True, 3000)
            
            self.inx, self.iny = 775, 350

            app.event_generate('<Motion>', warp = True, x = 775, y = 250)
            app.bind('<f>', self.switch)
            app.bind('<Key>', self.pushed)
            app.bind('<1>', lambda e : self.pushed("space"))
            app.bind("<Motion>", self.move)

            self.root.grid()

        def attack(self, create = False, time = 0):

            if self.stop:
                self.creation.append(create)
                self.tfa.append(time)
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
                self.no2 = self.root.after(self.duration, self.attack, True, self.duration)
                self.now = datetime.now()
                self.no3 = self.root.after(300, self.attack, metior, 300)
                return
            
            if "Metior" not in self.root.itemcget(create, "tag") : return

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
                        self.no4 = self.root.after(3000, self.root.delete, h1)
                        if self.hearts == 0: self.switch()
                        else:
                            self.root.itemconfig(self.lohearts[-1], fill = "black")
                            self.lohearts.pop(-1)
                        self.root.coords(ele, -100, 0, -100, 0)
                        self.root.itemconfigure(ele, tag = "torn")
                        rr = random.randrange(0, len(self.bwords))
                        self.root.itemconfig(self.gbw, text = self.bwords[rr])

            self.no5 = self.root.after(300, self.attack, create, 300)

        def movit(self, obj, dist = None, time = 0):
            if self.stop:
                self.d[obj] = dist
                self.tfm.append(time)
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

                a = self.root.find_enclosed(coords[0], coords[1], coords[2], coords[3])

                if a:
                    
                    if self.root.itemcget(ast, 'fill') == "green" and self.orange and not self.red:
                        self.root.itemconfigure(ast, fill = 'orange')
                        self.sod = self.red = True
                    
                    elif self.root.itemcget(ast, 'fill') == "green" or self.root.itemcget(ast, 'fill') == "orange" and not self.sod:
                        self.root.itemconfigure(ast, fill = 'red')
                        self.sod = True
                        self.red = False
                    
                    elif not self.sod:
                        self.root.coords(ast, -250, -250, -250, -250)
                        self.root.itemconfigure(ast, tag = "Broke")
                    
                    rr = random.randrange(0, len(self.gwords))
                    self.root.itemconfig(self.gbw, text = self.gwords[rr])
                    self.no6 = self.root.after(2000, lambda : self.root.itemconfig(self.gbw, text = ""))
                    self.root.delete(obj)
                    return
            self.no7 = self.root.after(100, self.movit, obj, dist, 100)

        def pushed(self, e, time = 0):

            if e != 'space' and e != 10 and e != "Escape": e = e.keysym
            
            if self.stop and e != "Escape":
                if e == 10:
                    self.reshoot = "Hello"
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
                
                app.after_cancel(self.no0)
                app.after_cancel(self.no1)

                self.dtn2 = datetime.now()-self.dtn

                self.stop = True
                self.root['cursor'] = 'arrow'
                self.root.coords(self.bbtg, 620, 250, 930, 350)
                self.root.coords(self.btg, 775, 300)
                
                self.root.coords(self.besc, 620, 350, 930, 450)
                self.root.coords(self.esc, 775, 400)

                self.root.coords(self.bret, 620, 450, 930, 550)
                self.root.coords(self.ret, 775, 500)

                self.stopper = True

                if not self.once:
                    self.once = True
                    self.root.tag_bind(self.bret, "<Button>", lambda e : self.switch())
                    self.root.tag_bind(self.bbtg, "<Button>", lambda e : self.root.event_generate("<Escape>"))
                    self.root.tag_bind(self.besc, "<Button>", lambda e : app.destroy())

            elif e == "Escape":
                self.root['cursor'] = 'cross'
                
                ts = self.dtn2.total_seconds()

                if ts <= 3:
                    self.no1 = app.after(int(round((3-ts)*1000)), self.attack, True)
                    self.no0 = app.after(int(round((15-ts)*1000)), self.move, "Random")
                elif self.dtn2.total_seconds() <= 15:
                    self.no0 = app.after(int(round((15-ts)*1000, 0)), self.move, "Random")

                self.stop = False

                counter = 0

                for ele in self.creation:
                    self.root.after(int(round(self.tfa[counter]-(ts*1000))), self.attack(ele))
                    counter += 1
                counter = 0

                for key, val in self.d.items():
                    if self.root.itemcget(key, 'tag') != 'torn':
                        self.root.after(int(round(self.tfm[counter]-(ts*1000))), self.movit(key, val))
                        counter += 1

                self.root.coords(self.bbtg, -10, -10, -2, -2)
                self.root.coords(self.btg, -10, -10)
                
                self.root.coords(self.besc, -10, -10, -2, -2)
                self.root.coords(self.esc, -10, -10)
                
                self.root.coords(self.bret, -10, -10, -2, -2)
                self.root.coords(self.ret, -10, -10)

                self.root.after(10, self.switch, 10)

                if self.reshoot == "Hello":
                    self.root.after(int(round(900-(ts*1000))), self.pushed, 10, 900)

            elif e == 'space' and self.reshoot and not self.stopper:
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
                self.no9 = self.root.after(200, self.pushed, 10, 900)

        def move(self, event):
            if self.stop: return

            if event == "Random":
                ran = random.randrange(0, 7)
                if ran == 0:
                    if self.hearts == 1: self.root.itemconfigure(self.heart2, fill = 'red')
                    elif self.hearts == 2: self.root.itemconfigure(self.heart3, fill = 'red')
                    elif self.hearts == 3:
                        self.heart4 = self.root.create_rectangle(205, 10, 245, 50, fill = 'red')
                        self.lohearts.append(self.heart4)
                    elif self.hearts == 4:
                        self.heart5 = self.root.create_rectangle(270, 10, 310, 50, fill = 'red')
                        self.lohearts.append(self.heart5)
                    else: return
                    self.hearts += 1
                    h1 = self.root.create_text(775, 100, text = "+1 Heart", fill = '#000fff000', font = ("Algerian", 15, 'bold'))
                    self.no10 = self.root.after(3000, self.root.delete, h1)
                self.no11 = self.root.after(15000, self.move, "Random")
                return
            
            cx, cy = self.root.coords(self.ball)
            x, y = event.x-cx, event.y-cy
            self.angle = 180 + math.degrees(math.atan2(x, y))
            self.angle %= 360
            
            if self.stop: return
            
            self.image = ImageTk.PhotoImage(self.img.rotate(self.angle))
            self.root.itemconfig(self.ball, image = self.image)
            
        def switch(self, event = None):
            global astroot

            if event == 10:
                self.stopper = False
                return
            elif event:
                self.attr = not self.attr
                app.attributes('-fullscreen', self.attr)
                return
            
            app.attributes('-fullscreen', False)
            self.root.delete("Metior")
            self.root.delete("Shoot")
            self.root.coords(self.ball, 775, 400)
            app.unbind('<f>')
            app.unbind('<Key>')
            app.unbind('<1>')
            app.unbind("<Motion>")
            if not self.stop: self.pushed("Escape")
            
            astroot = self.root
            root_2.grid()
            
            app.title('Home screen')
            app.configure(bg = root_2.cget('bg'))
            
            self.root.grid_remove()

    class quittowin:
        global qtwroot

        def __init__(self, root_2, app):
            global qtwroot

            app.protocol("WM_DELETE_WINDOW", lambda : print(end = ""))
            app.bind('<w>', self.switch)

            app.state('zoomed')
            app.configure(bg = 'grey15')
            app.title('Quit the game to WIN!!!')
            app.event_generate('<Motion>', warp = True, x = 100, y = 100)

            root_2.grid_remove()

            self.root = tk.Frame(app, bg = 'grey15', height = 796, width = 1530)
            self.root.grid()

            self.twist = tk.Button(self.root, text = "QUIT THE GAME TO WIN", bg = 'grey15', fg = 'white', font = ('Times', 32, 'bold'), relief = 'flat')
            self.twist.place(relx = 0.34, rely = 0)

            self.xvar = 0
            self.xvar2 = 0

            self.win = tk.Button(self.root, text = "Quit", bg = 'grey15', fg = 'white', font = ('Times', 32, 'bold'), relief = 'flat')
            self.win.place(relx = 0.46, rely = 0.5)
            self.win.bind('<Enter>', self.enter)

            self.teller = tk.Label(self.root, text = "don't kill the process. That's cheating", bg = 'grey15', fg = 'white', font = ("times", 40, 'bold'))
            self.teller.place(relx = 0, rely = 0.9)

            self.root.mainloop()

        def enter(self, event):
            
            if event == 1:
                global x
                self.teller['text'] = "What about that 'X' on the top right hand corner"
                x = tk.Button(self.root, text = "X", bg = 'red', fg = 'grey15', font = ('times', 25, 'bold'), relief = 'flat')
                x.place(relx = 0.9, rely = 0)
                x.bind('<Enter>', self.enter)
                return
            elif event == 2:
                self.teller['text'] = "I think we scared it off..."
                x.place_forget()
                self.root.after(3000, self.enter, 3)
                return
            elif event == 3:
                global x2
                self.teller['text'] = "Here, take this. It surely looks better."
                x2 = tk.Button(self.root, text = 'X', bg = 'black', fg = 'red', font = ('', 40, 'bold'), command = lambda : self.enter(4))
                x2.place(relx = 0.5, rely = 0.4)
                return
            elif event == 4:
                x2.place_forget()
                self.teller['text'] = "Wait. Where did it go?"
                self.root.after(3000, self.enter, 5)
                return
            elif event == 5:
                global t2
                self.teller['text'] = "I think it is a shy one. Try calling it by it's name"
                t2 = tk.Label(self.root, text = "", bg = 'grey15', fg = 'red', font = ('times', 34, 'bold'))
                t2.place(relx = 0.42, rely = 0.5)
                self.root.after(3500, lambda : t2.configure(text = "I am not an object!"))
                self.root.after(5000, lambda : self.teller.configure(text = "Alright, try calling HIM by HIS name"))
                self.root.after(8500, lambda : t2.configure(text = "I am a she!!!"))
                self.root.after(10000, self.enter, 6)
                return
            elif event == 6:
                self.teller['text'] = "Fine!!! Try calling HER by HER name"
                t2.place_forget()
                self.xvar = 4
                x2.place(relx = 1, rely = 0.5)
                app.bind('<x>', self.enter)
                return
            elif event == 7:
                self.teller['text'] = "Did we just win?!"
                x2.place_forget()
                self.root.after(3000, lambda : self.teller.configure(text = "...oh,     I guess we didn't"))
                self.root.after(6000, lambda : self.teller.configure(text = "Here we go again..."))
                self.root.after(9000, lambda : self.teller.configure(text = "When the lights went off i think i saw something..."))
                self.root.after(13000, lambda : self.teller.configure(text = "Like a switch behind the title. Try clicking the title"))
                self.root.after(13000, lambda : self.twist.configure(command = lambda : self.enter(8)))
                return
            elif event == 8:
                global onoff
                self.twist.place_forget()
                self.teller['text'] = "QUIT THE GAME TO WIN"
                self.teller['font'] = ('times', 32, 'bold')
                onoff = tk.Button(self.root, text = "Off", bg = 'grey15', fg = 'white', font = ('times', 32, 'bold'), command = lambda : self.enter(9))
                onoff.place(relx = 0.5, rely = 0)
                return
            elif event == 9:
                global switch
                self.teller['font'] = ("times", 40, 'bold')
                self.teller['bg'] = 'black'
                self.teller['text'] = "What is that dangling thing?"
                self.root.configure(bg = 'black')
                onoff.place_forget()
                switch = tk.Button(self.root, text = "|\n|\n|\n|", command = lambda : self.enter(10), font = ('elephant', 30, 'bold'), bg = 'black', fg = 'white', relief = 'flat')
                switch.place(relx = 0.9, rely = 0)
                return
            elif event == 10:
                switch.place_forget()
                global final
                final = tk.Button(self.root, text = "Kill the process!!!", font = ('times', 35, 'bold'), bg = 'red', fg = 'grey15')
                final.place(relx = 0.4, rely = 0.43)
                self.teller['text'] = "Don't push that button!!!"
                self.root.after(3000, lambda : self.teller.configure(text = "I just realised something important..."))
                self.root.after(6000, lambda : self.teller.configure(text = "Killing the process IS quiting the game"))
                self.root.after(9000, lambda : self.teller.configure(text = "And that means I will cease to exist"))
                self.root.after(12000, lambda : self.teller.configure(text = "How could you push that button?!"))
                self.root.after(15000, lambda : self.teller.configure(text = "How could you kill that process?!"))
                self.root.after(18000, lambda : self.teller.configure(text = "After all the time we spent together..."))
                self.root.after(21000, lambda : self.teller.configure(text = "After all the challenges we faced..."))
                self.root.after(24000, lambda : self.teller.configure(text = "How could you kill me?!"))
                self.root.after(27000, self.enter, 11)
                return
            elif event == 11:
                self.teller['text'] = "Ok, fine. I won't interfere with your choices. Click it"
                final['command'] = lambda : self.enter(12)
                return
            elif event == 12:
                self.root.configure(bg = 'red')
                app.configure(bg = 'red')
                final.place_forget()
                self.teller.place_configure(relx = 0, rely = 0.42)
                self.teller['bg'] = '#00ffff'
                self.teller['fg'] = 'red'
                self.teller['text'] = "Did you really think it was that simple?"
                self.teller.place_forget()
                self.teller.pack()
                self.root.after(3000, lambda : self.teller.configure(text = "Nobody's gonna kill me..."))
                self.root.after(6000, lambda : self.teller.configure(text = "You are not gonna win this game"))
                self.root.after(9000, lambda : self.teller.configure(text = "I will win this game"))
                self.root.after(12000, self.enter, 13)
                return
            elif event == 13:
                self.teller['text'] = "I WILL QUIT THE GAME. HAHAHAHA"
                self.root.after(3000, self.switch)
                return

            elif event.widget != self.win and self.xvar == 0:
                x.place(relx = 0, rely = 0)
                self.xvar = 1
                return
            elif event.widget != self.win and self.xvar == 1:
                x.place(relx = 0.5, rely = 0.5)
                self.xvar = 2
                return
            elif event.widget != self.win and self.xvar == 2:
                x.place(relx = 0.75, rely = 0.5)
                self.xvar = 3
                if self.xvar2 == 0:
                    self.teller['text'] = "Nope. But there must be a way to touch it."
                    self.xvar2 = 1
                    self.root.after(5000, lambda : self.teller.configure(text = "I think it just needs a friendly rootroach. Be gentle..."))
                    self.root.after(9000, lambda : self.teller.configure(text = "Let's try it slowly."))
                    self.root.after(18000, lambda : self.teller.configure(text = "(I dont't think it is working...)"))
                    self.root.after(21000, lambda : self.teller.configure(text = "Let's do it fast now!!!"))
                    self.root.after(27000, self.enter, 2)
                return
            elif event.widget != self.win and self.xvar == 3:
                x.place(relx = 0.25, rely = 0.5)
                self.xvar = 2
                return
            elif event.widget != self.win and self.xvar == 4:
                x2.place_configure(relx = float(x2.place_info()['relx'])-0.005, rely = float(x2.place_info()['rely']))
                if x2.place_info()['relx'] == '0.94':
                    self.root.unbind('<x>')
                    self.teller['text'] = "We got it! ...I mean, her. Now, click on i- ...her"
                    x2['command'] = lambda : self.enter(7)
                return

            self.win.unbind('<Enter>')
            self.win.place_forget()
            self.teller['text'] = "Oops..."
            self.root.after(2000, lambda : self.teller.configure(text = "'Esc' and 'Alt-F4' won't work either..."))
            self.root.after(5000, self.enter, 1)

        def switch(self, event = None):
            global qtwroot
            
            qtwroot = self.root
            root_2.grid()
            
            app.unbind('<w>')
            app.title('Home screen')
            app.configure(bg = root_2.cget('bg'))
            app.protocol("WM_DELETE_WINDOW", app.destroy)

            self.root.grid_remove()

            return

    class minesweeper:
        global msroot

        def __init__(self, root_2, app):
            global msroot
            
            app.bind('<Escape>', lambda e : self.setting(1))
            app.bind('<Control_L> <s>', self.setting)
            app.configure(bg = 'grey10')
            app.state('zoomed')

            root_2.grid_remove()

            if msroot:
                self.root, self.settings = msroot
                self.root.grid()
                return

            self.root = tk.Frame(app, bg = 'grey10')
            self.root.grid(padx = 400, pady = 50)

            self.inst = tk.Label(self.root, text = "Left click if it's not bomb,\nRight click if it's a bomb,\nPress Ctrl+S for settings.", font = ('Algerian', 20, 'bold'), bg = 'grey10', fg = 'white')
            self.inst.grid(row = 0, column = 0, columnspan = 5)

            self.size = self.nobombs = 5
            self.blist = []
            self.bombs = []

            for rount in range(1, 6):
                for count in range(0, 5):
                    b = tk.Button(self.root, width = 16, height = 6, font = ('Helvetica', 11, 'bold'), bg = "#00ff00")
                    b.grid(row = rount, column = count)
                    self.blist.append(b)
                    b.bind('<1>', self.pressed)
                    b.bind('<3>', self.flagged)

            while len(self.bombs) != 5:
                rr = random.randrange(0, 25)
                
                if rr not in self.bombs:
                    self.bombs.append(rr)

            self.settings = tk.Frame(app, bg = self.root.cget('bg'))
                
            self.width = ttk.Combobox(self.settings, values = ["5x5 (5 bombs)", "10x10 (20 bombs)", "15x15 (50 bombs)", "20x20 (90 bombs)"], font = ('Helvetica', 20, 'bold'))
            self.width.insert(0, "Enter Grid Size")
            self.width.grid(sticky = 'ew')
            app.option_add('*TCombobox*Listbox.font', ('Helvetica', 20, 'bold'))

            self.reset = tk.Button(self.settings, text = "Reset Game", font = ('Helvetica', 20, 'bold'), anchor = 'center', bg = '#D3d3d3', fg = "#000fff", command = self.setting)
            self.reset.grid(sticky = 'ew', pady = 20)

            self.quit = tk.Button(self.settings, text = "Quit", command = exit, font = ('Helvetica', 20, 'bold'), bg = '#00ffff')
            self.quit.grid(sticky = 'ew', pady = 10)

            self.hs = tk.Button(self.settings, text = "Home Screen", command = self.switch, font = ('Helvetica', 20, 'bold'), bg = "#fff000", fg = 'saddle brown')
            self.hs.grid(sticky = 'ew', pady = 10)

        def pressed(self, event):

            if "tkinter.Button" in str(type(event)): wid = event
            else: wid = event.widget

            if self.blist.index(wid) in self.bombs:
                self.size = 0
                
                self.width.delete(0, 'end')
                self.width.insert('end', ":x You Lost!!! :(")
                self.setting(torf = 2)
                
                return
            
            count = 0

            if self.blist.index(wid)+self.size in self.bombs: count += 1
            if self.blist.index(wid)-self.size in self.bombs: count += 1
            
            if self.blist.index(wid)%self.size != 0:
                if self.blist.index(wid)-self.size-1 in self.bombs: count += 1
                if self.blist.index(wid)-1 in self.bombs: count += 1
                if self.blist.index(wid)+self.size-1 in self.bombs: count += 1
            
            if self.blist.index(wid)%self.size != (self.size-1):
                if self.blist.index(wid)+(self.size+1) in self.bombs: count += 1
                if self.blist.index(wid)+1 in self.bombs: count += 1
                if self.blist.index(wid)-(self.size-1) in self.bombs: count += 1

            wid['text'] = count

            if not count:
                if self.blist.index(wid)+self.size < self.size**2:
                    if self.blist[self.blist.index(wid)+self.size]['text'] == "": self.pressed(self.blist[self.blist.index(wid)+self.size])

                if self.blist[self.blist.index(wid)-self.size]['text'] == "" and self.blist.index(wid)-self.size >= 0: self.pressed(self.blist[self.blist.index(wid)-self.size])

                if self.blist.index(wid)%self.size != 0:
                    
                    if self.blist[self.blist.index(wid)-(self.size+1)]['text'] == "" and self.blist.index(wid)-(self.size+1) >= 0: self.pressed(self.blist[self.blist.index(wid)-(self.size+1)])
                    
                    if self.blist[self.blist.index(wid)-1]['text'] == "" and self.blist.index(wid)-1 >= 0: self.pressed(self.blist[self.blist.index(wid)-1])
                    
                    if self.blist.index(wid)+(self.size-1) < self.size**2:
                        if self.blist[self.blist.index(wid)+(self.size-1)]['text'] == "": self.pressed(self.blist[self.blist.index(wid)+(self.size-1)])
                
                if self.blist.index(wid)%self.size != (self.size-1):
                    
                    if self.blist.index(wid)+(self.size+1) < self.size**2:
                        if self.blist[self.blist.index(wid)+(self.size+1)]['text'] == "": self.pressed(self.blist[self.blist.index(wid)+(self.size+1)])
                    
                    if self.blist.index(wid)+1 < self.size**2:
                        if self.blist[self.blist.index(wid)+1]['text'] == "": self.pressed(self.blist[self.blist.index(wid)+1])
                    
                    if self.blist[self.blist.index(wid)-(self.size-1)]['text'] == "" and self.blist.index(wid)-(self.size-1) >= 0: self.pressed(self.blist[self.blist.index(wid)-(self.size-1)])

            counter = 0
            
            for x in self.blist:
                if x['text'] == "" or x['text'] == "⚐": counter += 1
            
            if counter == self.nobombs:
                self.size = 0
                
                self.width.delete(0, 'end')
                self.width.insert('end', "=D You Won!!! :)")
                self.setting(torf = 2)
                
                return

        def flagged(self, event):
            
            if "tkinter.Button" not in str(type(event)):
                
                wid = event.widget
                
                if wid['text'] != "": return
                
                wid.unbind('<1>')
                wid['text'] = "⚐"
                wid.bind('<3>', lambda e : self.flagged(wid))
                
                return
            
            wid = event
            wid.bind('<1>', self.pressed)
            wid['text'] = ""
            wid.bind('<3>', self.flagged)

        def setting(self, torf = None):
            
            if torf == 1:
                self.settings.grid_remove()
                self.root.grid()

                app.bind('<Control_L> <s>', self.setting)

            elif torf:
                self.root.grid_remove()

                self.width.focus_set()
                self.width.selection_range(0, 'end')            
                
                self.settings.grid(padx = 650, pady = 275)

                app.bind('<Control_L> <s>', lambda e : self.setting(1))
            
            else:
                grid = self.width.get()
                
                if grid not in self.width['values']:
                    self.width.delete(0, 'end')
                    self.width.insert(0, "Error")
                    return

                if "5x5" in grid: grid = 5
                else: grid = int(grid[0:2])
                
                if self.size == grid:
                    self.setting(1)
                    return

                count = 0
                for ele in self.root.winfo_children():
                    if count == 0:
                        count = 1
                        continue
                    ele.destroy()

                self.blist = []
                self.bombs = []

                loop = [5, 17, 45, 80]

                for rount in range(1, grid+1):
                    for count in range(0, grid):
                        if 30/grid != round(30/grid): x = 1
                        else: x = round(30/grid)
                    
                        b = tk.Button(self.root, width = round(90/grid), height = x, font = ('Helvetica', 9, 'bold'), bg = '#00ff00')
                        b.grid(row = rount, column = count)

                        self.blist.append(b)
                        
                        b.bind('<1>', self.pressed)
                        b.bind('<3>', self.flagged)

                while len(self.bombs) != loop[int(grid/5-1)]:
                    rr = random.randrange(0, grid**2)
                
                    if rr not in self.bombs:
                        self.bombs.append(rr)

                self.inst.grid(row = 0, column = 0, columnspan = grid)
                self.size = grid
                self.nobombs = len(self.bombs)
                self.setting(1)

        def switch(self):
            global msroot
            
            msroot = [self.root, self.settings]
            
            root_2.grid()
            
            app.unbind('<Return>')
            app.unbind('<Control_L> <s>')
            app.unbind('<Escape>')

            app.title('Home Screen')
            app.configure(bg = root_2.cget('bg'))
            
            self.settings.grid_remove()
            self.root.grid_remove()

    class geoquiz:
        def __init__(self, app, root_2=None, game=0, gametype=""):
            global gqroot

            if root_2:
                root_2.grid_remove()
                self.root_2 = root_2
            app.state("normal")
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
            self.ds = pd.read_csv("test.csv")
            self.cluecounter = 0

            if self.game == 0:
                self.app.minsize(100, 100)
                self.app.geometry("650x350+400+200")
                tk.Label(self.root, text="Which quiz do you want to play?", font=self.myfont2, bg="blue2", fg="White").grid(row=0, column=0, sticky="nsew")
                tk.Button(self.root, text="Guess the Country", font=self.myfont2, command= lambda: self.replay("", 1), bg="MediumPurple4", fg="White", activebackground="black", activeforeground="white", relief="groove").grid(row=1, column=0, sticky="nsew")
                tk.Button(self.root, text="Guess the Capital", font=self.myfont2, command= lambda: self.replay("", 2, "capital"), bg="saddlebrown", fg="White", activebackground="black", activeforeground="white", relief="groove").grid(row=2, column=0, sticky="nsew")
                tk.Button(self.root, text="Guess the Currency", font=self.myfont2, command= lambda: self.replay("", 2, "currency"), bg="#004d39", fg="White", activebackground="black", activeforeground="white", relief="groove").grid(row=3, column=0, sticky="nsew")
                tk.Button(self.root, text="Guess the Languages", font=self.myfont2, command= lambda: self.replay("", 2, "language"), bg="#334d00", fg="White", activebackground="black", activeforeground="white", relief="groove").grid(row=4, column=0, sticky="nsew")
                tk.Button(self.root, text="Return to home screen", font=self.myfont2, command= lambda: self.replay("Return"), bg="#465a7a", fg="white", activebackground="black", activeforeground="white", relief="groove").grid(row=5, column=0, sticky="nsew")
                tk.Button(self.root, text="Quit", font=self.myfont2, command= self.app.destroy, bg="black", fg="White", activebackground="black", activeforeground="white", relief="groove").grid(row=6, column=0, sticky="nsew")
                self.root.columnconfigure(0, weight=1)
                self.root.rowconfigure(0, weight=1)
                self.root.rowconfigure(1, weight=2)
                self.root.rowconfigure(2, weight=2)
                self.root.rowconfigure(3, weight=2)
                self.root.rowconfigure(4, weight=2)
                self.root.rowconfigure(5, weight=1)
                self.root.rowconfigure(6, weight=1)
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
                self.guess.focus_set()
                self.guess.selection_range(0, "end")
                self.guess.icursor("end")
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

                self.guess.focus_set()
                self.guess.selection_range(0, "end")
                self.guess.icursor("end")
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
            if e == "Return":
                self.app.rowconfigure(0, weight=0)
                self.app.columnconfigure(0, weight=0)
                
                self.app.title("Home Screen")
                self.app.state("zoomed")

                self.root.grid_remove()
                self.root_2.grid(row=0, column=0)
                return
            self.root.destroy()
            self.__init__(self.app, game=gn, gametype=gt)

    root_2 = tk.Frame()
    root_2.grid()
    app.title('Home screen')

    colors = []

    myfont = font.Font(family="algerian", size=12, root = root_2, weight = "bold")

    thumbnails = {"hangman.png": (2, 2), "coloursg.png": (5, 5), "x_and_o.png": (2, 2),\
                "dot_box.png": (2, 2), "tick_toclock.png": (10, 10), "calculator.png": (2, 2),
                "AYtexteditor.png": (2, 2), "table_tennis.png": (2, 2), "think_emoji.png": (2, 2),
                "xcelsheet.png": (2, 2), "rocket.png": (10, 10), "quit_win.png": (7, 7), "minesweeper_bomb.png": (2, 2),\
                "Earth.png": (3, 3)}

    p = []

    for pics, size in thumbnails.items():
        picture = tk.PhotoImage(file = r"images_for_gcpy/"+pics)
        p.append(picture.subsample(size[0], size[1]))
    
    cgroot = clroot = calroot = hroot = hgroot = broot = kroot = exit_now = proot = qroot = eroot = astroot = qtwroot = msroot = gqroot = 0
    count = tk.IntVar(app, 0)
    b1 = b2 = b3 = b4 = b5 = b6 = b7 = b8 = b9 = b10 = b11 = b12 = b13 = b14 = b15 = b16 = b17 = 0

    b = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, b16, b17]

    b_info = [("Hangman", lambda: hangmang(root_2, app)), ("Colour Game", lambda: cg(root_2, app)),\
            ("X and O", lambda: kacg(root_2, app)), ("Dots and Boxes", lambda: boxes(root_2, app)),\
            ("Clock", lambda: clock(root_2, app)), ("Calculator", lambda: calculator(root_2, app)),\
            ("Text Editor", lambda: aytexteditor(root_2, app)), ("Ping Pong", lambda: pingpong(root_2, app)),\
            ("GK Quiz", lambda: quiz(root_2, app)), ("Excel", lambda: excel(root_2, app)),\
            ("Asteroids", lambda: Asteroids(root_2, app)), ("Quit To Win", lambda: quittowin(root_2, app)),\
            ("Minesweeper", lambda: minesweeper(root_2, app)), ("Geography Quiz", lambda: geoquiz(app, root_2))]

    r = 0
    c = 0

    for items in b_info:
        index = b_info.index(items)

        b[index] = tk.Button(root_2, image = p[index], compound = 'top', text = items[0], command = items[1], font = myfont, relief = 'flat')

        b[index].image = p[index]
        b[index].command = items[1]
        b[index].grid(row = r, column = c, sticky = 'nsew')
        
        b[index].bind('<Enter>', colorchanger)
        b[index].bind('<Leave>', colorchanger)
        
        c += 1
        if c == 4:
            r += 1
            c = 0

    chb = tk.Canvas(root_2, width = 240, height = 180)
    chb.bind('<Button>', lambda e: happybirthday(root_2, app))
    chb.create_rectangle(100, 60, 140, 100, fill = 'pink')
    chb.create_polygon(101, 60, 140, 60, 140, 70, 100, 70, fill = 'maroon1')
    chb.create_rectangle(60, 100, 180, 140, fill = 'pink')
    chb.create_polygon(61, 100, 180, 100, 180, 110, 60, 110, fill = 'maroon1')
    chb.create_rectangle(20, 140, 220, 180, fill = 'pink')
    chb.create_polygon(21, 140, 220, 140, 220, 150, 21, 150, fill = 'maroon1')
    chb.create_rectangle(100,60, 107,40, fill = 'red')
    chb.create_rectangle(111,60, 118,40, fill = 'DarkOrchid1')
    chb.create_rectangle(122,60, 129,40, fill = 'dodgerblue')
    chb.create_rectangle(133,60, 140,40, fill = "#000fff000")
    chb.create_polygon(100,40, 103,40, 102,30,  fill = 'gold')
    chb.create_polygon(102,40, 105,40, 104,30,  fill = 'gold')
    chb.create_polygon(104,40, 107,40, 106,30,  fill = 'gold')
    chb.create_polygon(111,40, 114,40, 113,30,  fill = 'gold')
    chb.create_polygon(113,40, 116,40, 115,30,  fill = 'gold')
    chb.create_polygon(115,40, 118,40, 117,30,  fill = 'gold')
    chb.create_polygon(122,40, 125,40, 124,30,  fill = 'gold')
    chb.create_polygon(124,40, 127,40, 126,30,  fill = 'gold')
    chb.create_polygon(126,40, 129,40, 128,30,  fill = 'gold')
    chb.create_polygon(133,40, 136,40, 135,30,  fill = 'gold')
    chb.create_polygon(135,40, 138,40, 137,30,  fill = 'gold')
    chb.create_polygon(137,40, 140,40, 139,30,  fill = 'gold')
    chb.create_text(120, 160, text = "Click for a birthday", font = myfont)
    chb.grid(row = r, column = c, sticky = 'nsew')
    chb.bind('<Enter>', colorchanger)
    chb.bind('<Leave>', colorchanger)


def showing():
    global pwd_hidden

    if pwd_hidden:
        show_pwd.config(text = "Hide letters")
        password.config(show = "")
        
    else:
        show_pwd.config(text = "Show letters")
        password.config(show = "•")

    pwd_hidden = not pwd_hidden
    
def pwd_check(event):
    global can_rate, pwd_attempts

    if attempt_pwd.get().lower() == pwd.lower() or event == 1:

        forgot_pwd.destroy()
        password.destroy()
        show_pwd.destroy()
        hint_pwd.destroy()
        frame.destroy()
        root.rowconfigure(0, weight= 0)
        root.columnconfigure(0, weight= 0)
        can_rate = True

        saep(root)
        return

    else:
        if pwd_attempts == MAX_PWD_ATTEMPTS:
            messagebox.showwarning("THIEF!!!", "Incorrect password, you have attempted\n too many times")
            sys.exit()

        else:
            pwd_attempts += 1
            messagebox.showinfo("Incorrect Password", "Wrong Password")
            
            password.selection_range(0, 'end')
            password.icursor('end')

def forgot_pass():
    global pwd

    hint_pwd.grid(row = 2, column= 0, sticky= "EW")
    
    password.focus_set()
    password.selection_range(0, 'end')

MAX_PWD_ATTEMPTS = 3
USER = "ADVAITH"
exit_now = False
can_rate = False

root = tk.Tk()
root.state('zoomed')
root.minsize(350, 400)

root.rowconfigure(0, weight= 1)
root.columnconfigure(0, weight= 1)

pwd = "python!"

pwd_hidden = False
pwd_attempts = 0

frame = tk.Frame(root, bg= "black")

attempt_pwd = tk.StringVar(root, 'Password')
password = tk.Entry(frame, textvariable = attempt_pwd, show = "", font = 15, width= 30)

show_pwd = tk.Button(frame, bitmap= "error", command = showing, font = 15, width= 30, height= 30, relief= "groove", bd= 2, fg= "red")

show_pwd.grid(row = 1, column= 0, sticky= "e", pady= 10)
password.grid(row = 1, column= 0, sticky= "ns", pady= 10)

user_img = Image.open("images_for_gcpy/user.png")
user_img = user_img.crop([0, 10, 225, 215])
user_img = ImageTk.PhotoImage(user_img)

user_img_display = tk.Label(frame, image= user_img, text= USER, compound= "top", font = ('Helvetica', 25, "bold"), bg= "black", fg= "white")
user_img_display.grid(row= 0, column= 0, ipady= 20, sticky= "new")

password.bind('<Return>', pwd_check)

password.focus_set()
password.selection_range(0, 'end')
password.icursor('end')

forgot_pwd = tk.Button(frame, text = "Forgot Password?", font = ('Arial black', 14, 'bold'), command = forgot_pass)
forgot_pwd.grid(row = 2, column= 0, sticky= "EW")

hint_pwd = tk.Label(frame, text= "Hint: Language!", font = ('Arial black', 14, 'bold'))
    
frame.grid(row= 0, column= 0)
root.rowconfigure(0, weight= 1)
root.columnconfigure(0, weight= 1)

root.bind('<Control_L> <w>', lambda e: root.destroy())
root.mainloop()
if can_rate == False:
    sys.exit()

str_numbs = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def submit(sure = False, pop_index=None):
    ratings = pd.read_csv("ratings.csv")
    user_name = username.get()
    raterget = rater.get()
    feedbackget = " ".join(feedback.get("1.0", "end").split("\n"))

    if not sure:
        for ele in list(ratings["username"]):
            if ele and (user_name.lower() in ele.lower() or ele.lower() in user_name.lower()):
                rate.geometry("290x210")
                submitb['command'] = lambda : submit(True, ele)
                submitb['text'] = "You already rated.\n Do you want to re-rate it?\nEnd the program if no,\nif yes, click me"
                return

    if sure: ratings.loc[ratings[ratings["username"]==pop_index].index[0]] = [user_name, raterget, feedbackget]
    else: ratings.loc[len(ratings.index)] = [user_name, raterget, feedbackget]
    average = sum(ratings["ratings"])/len(ratings["ratings"])

    for ele in rate_frame.winfo_children():
        if ele: ele.grid_forget()
    rate_frame['bg'] = 'SystemButtonFace'
    tk.Label(rate_frame, text = "Thanks for rating %s!" %(user_name), font = ('Algerian', 20, 'bold')).grid(pady= 10)
    tk.Label(rate_frame, text = "Average User Rating- {:.1f}".format(average), font = ('Algerian', 20, 'bold')).grid(pady= 10)
    rate.after(2000, rate.destroy)
    ratings.to_csv("ratings.csv", index=False)

rate = tk.Tk()
rate.state('zoomed')
rate.minsize(500, 500)

rate_frame = tk.Frame(rate, bg= 'black')

Average = tk.Label(rate_frame, font = ('Algerian', 30, 'bold'), bg = '#00ffff', text= "Please Rate")
Average.grid(sticky = 'ew', row= 0, column= 0, pady= 20)

rater = tk.Scale(rate_frame, from_ = 1, to = 10, orient = 'horizontal', font= ("Arial black", 15))
rater.grid(row = 2, column = 0, sticky = 'ew', ipady= 10, pady= 10)

username = tk.Entry(rate_frame, font = ('comic sans', 20, 'bold'))
username.focus_set()
username.insert('end', "Your Name")
username.select_range(0, 'end')
username.grid(row = 1, column = 0, sticky= 'ew')

feedback = tk.Text(master= rate_frame, font= ('comic sans', 12, 'bold'), height= 10, width= 50)
feedback.grid(row= 3, column= 0, sticky= 'ew')
feedback.insert('end', "Please Enter Your Feedback Here")

submitb = tk.Button(rate_frame, text = "SUBMIT", font = ('Comic Sans', 15, 'bold'), command = submit)
submitb.grid(row = 4, column = 0, sticky = 'ew')

rate_frame.grid(row= 0, column= 0)
rate.rowconfigure(0, weight=1)
rate.columnconfigure(0, weight=1)

rate.bind("<Control_L>  <w>", lambda e: rate.destroy())
rate.mainloop()