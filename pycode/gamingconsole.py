"""
Gaming console has a variety of apps and games

The apps and games are -;
01) A text editor
02) Clock app
03) calculator
04) A birthday celebration
05) Hangman game
06) Virtual Cube
07) Colour game
08) Trex run 
09) X and O (Knaughts and crosses)
10) Dots and Boxes
11) Ping Pong (Table Tennis)
12) Quiz
13) Excel Spread Sheet (Google Sheets)
14) Asteroids (An arcade Game)
"""

"""
To do -;

1) Meme app
2) Click The Button
3) Monopoly
"""

# Importing modules from datetime for the clock application
from datetime import datetime, timedelta, date

# Importing all the modules needed except tkinter(and the from ... import ...)
import pytz, pyttsx3, random, math, os

# import tkitner as tk because it is easier to write tk than tkinter
import tkinter as tk
# Importing modules from tkinter needed
from tkinter import font, ttk, colorchooser, filedialog, messagebox

#  Importing modules from PIL
from PIL import Image, ImageTk



# The main function saep
def saep(app):
    """The main function saep runs the app\n\nParameters are -\n1) app (tk.Tk)"""

    # Globalizing some variables
    global clroot, colroot, broot, hroot, hgroot, calroot, ayroot, cgroot, kroot, proot, exit_now, qroot, eroot
    
    # If you hover over any button than change the color
    def colorchanger(event):
        global exit_now

        """Changes color of widgets upon focus"""
        if 'Enter' in str(event):
            event.widget['bg'] = 'gray70'
        
        elif 'Leave' in str(event):
            # Doing this cause default bg is not white it is something like gray75
            event.widget['bg'] = root_2.cget('bg')

        else:
            exit_now = 1
            

    # The clock app
    class clock:
        """Clock app it contains :\n1) Global Clock\n2) Timer\n3) Stopwatch\nParameters are :\n1) Root_2(tk.Frame)\n2) application(tk.Tk)"""
        global clroot
        
        # __init__ runs first in any class. It runs before anything else
        def __init__(self, root_2, app):
            """start function for clock\n\nParameters are -;\n1) root_2(tk.Frame)\n2) app(tk.Tk)"""
            global clroot
            # Checks if the user came here before
            if clroot != 0:
                self.torf = False
                # Regridding root
                root_2.grid_remove()
                self.root = clroot
                self.root.grid()
                app.configure(bg = self.root.cget('bg'))
                return

            # Part 0 for the initialization process
            if True:
                
                # Putting all widgets inside root
                # Removing root_2
                root_2.grid_remove()
                clroot = tk.Frame(app)
                self.root = clroot
                self.root.grid()
                app.title('CLOCK APP')
                app.bind('<Alt_L> <c>', lambda e : self.clickedb(self.f1))
                app.bind('<Alt_L> <t>', lambda e : self.clickedb(self.f2))
                app.bind('<Alt_L> <s>', lambda e : self.clickedb(self.f4))
                app.bind('<Escape>', lambda e : self.clickedb(self.f))
                self.root.configure(bg = '#fff')

                # The speaking tool in python
                self.cump = pyttsx3.init()
                self.cump.setProperty('rate', 120)
                self.cump.setProperty('volume', 1.2)

                # Setting global variables
                self.count = 0
                self.color = ''
                self.fat = 0
                self.count = 1
                self.torf = False

                # Fonts
                self.myfont = font.Font(self.root, size = 12, family = 'Algerian', weight = 'bold', underline = 1)
                self.myfont2 = font.Font(self.root, family = 'Helvecta', size = 12, weight = 'bold')
                self.myfont3 = font.Font(self.root, family = 'Times', size = 20, weight = 'bold', slant = 'italic')
                self.myfont4 = font.Font(self.root, family = 'Helvecta', size = 24, weight = 'bold')
                self.myfont5 = font.Font(self.root, family = 'Courier', size = 18, weight = 'bold')

                # Clock, Timer, Stopwatch buttons
                self.b1 = tk.Button(self.root, text = "C l o c k", width = 47, height = 6, bg = 'red2', relief = 'flat', command = lambda : self.clickedb(self.f1), font = self.myfont)
                self.b1.grid(row = 0, column = 0, sticky = 'w')

                self.b2 = tk.Button(self.root, text = "T i m e r", width = 47, height = 6, bg = 'cyan', relief = 'flat', command = lambda : self.clickedb(self.f2), font = self.myfont)
                self.b2.grid(row = 0, column = 0, sticky = 'w', padx = 525)

                self.b4 = tk.Button(self.root, text = "S t o p w a t c h", width = 46, height = 6, bg = 'green2', relief = 'flat', command = lambda : self.clickedb(self.f4), font = self.myfont)
                self.b4.grid(row = 0, column = 0, padx = 1050, sticky = 'w')

                # Binding for changing color of these widgets
                self.b1.bind('<Enter>', self.come_leave)
                self.b2.bind('<Enter>', self.come_leave)
                self.b4.bind('<Enter>', self.come_leave)

                self.b1.bind('<Leave>', self.come_leave)
                self.b2.bind('<Leave>', self.come_leave)
                self.b4.bind('<Leave>', self.come_leave)

                # Openeing clock picture
                self.im = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\tick_toclock.png")
                self.im = self.im.subsample(3, 3)

                self.idk = "Shortcuts are :\n1) Control + W - Quit/Exit\n"\
                        + "2) Escape - come to App Screen\n3) Alt + C - go to Clock"\
                        + "\n4) Alt + T - go to Timer\n5) Alt + S - go to Stopwatch"
                self.f = tk.Label(self.root, image = self.im, text = self.idk, compound = "top", font = self.myfont5, bg = 'white', justify = 'left')
                self.f.grid(row = 1, column = 0, sticky = 'w', padx = 359)
                self.prevcatsvar = self.f

                # The frames for the subapps
                self.f1 = tk.Frame(self.root, bg = 'red2')

                self.f2 = tk.Frame(self.root, bg = 'cyan')

                self.f4 = tk.Frame(self.root, height = 700, width = 1530, bg = 'green2')

            # Part 1 for the frame 1 (clock)
            if True:
                # First doing the clock subapp
                self.lv = []
                self.fv = []

                # Places how the computer understands
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
                
                # Places how humans understand 
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
                
                self.fl = [
                    'Egypt', 'Argentina', 'Chicago', 'Indiana', 'Los Angeles', 'New York', 'Panama', \
                    'New Zealand', 'India', 'Iraq/Iran', 'UAE/Dubai', 'Hong Kong', 'Saudi Arabia', 'Singapore',\
                    'Japan', 'Ireland', 'Australia', 'Central Europe', 'Greenwich', 'England/Britain', \
                    'Italy', 'Alaska', 'Ethopia', 'Zimbawe', 'Afghanistan', 'Albania', 'Algeria', 'Andorra'\
                    , 'Angola', 'Antigua and Barbados', 'Armenia', 'Azerbaijan', 'The Bahamas', 'Bahrain',\
                    'Barbados', 'Bangladesh', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Cambodia'\
                    , 'Canada', 'Central Africa', 'Chile', 'North/South Korea', 'Russia(West)', 'Russia(West-Central)', 'Russia(East-Central)', \
                    'Russia(East)', 'France', 'Germany', 'Indonesia(West)', 'Indonesia(East)'
                    ]

                # Sorting all the lists in alphabetical order
                self.fl.sort()
                for ele in self.fl:
                    changeinto = self.fl2.index(ele)
                    self.lv.append(self.rv[changeinto])
                    self.fv.append(ele)
                self.fl2 = self.fv
                self.rv = self.lv
                self.lsel = []

                # Placing the widgets in root
                self.searcher = tk.Entry(self.f1, width = 20, font = self.myfont2, bg = 'brown2')
                self.searcher.insert(0, 'Search for places')
                self.searcher.bind('<Key>', lambda e : self.root.after(10, self.sken, e))
                self.searcher.bind('<Button>', lambda e : self.presed(0))
                self.b4.bind('<Tab>', lambda e: self.presed(0))
                self.searcher.grid(row = 0, column = 0, sticky = 'ew')

                # Listbox helps the user view a list in a vertical direction
                self.lbfrl = tk.Listbox(self.f1, font = self.myfont2, height = 15, selectbackground = 'gray80', selectforeground = 'black', activestyle = 'dotbox', bg = 'brown3')
                self.lbfrl.bind('<Button>', lambda e : self.root.after(10, self.ctz))
                self.lbfrl.bind('<space>', lambda e: self.root.after(10, self.ctz))
                self.lbfrl.bind('<Shift_L> <Tab>', lambda e: self.presed(0))
                self.lbfrl.grid(row = 1, column = 0, sticky = 'ew')

                # Putting places names in the listbox
                for x in range(0, len(self.fl)):
                    ele = self.fl[x]
                    self.lbfrl.insert(x, ele)

                # Scroll bar for the list
                self.sb = tk.Scrollbar(self.f1, command = self.lbfrl.yview, orient = 'vertical')
                self.lbfrl.configure(yscrollcommand = self.sb.set)
                self.sb.grid(row = 1, column = 1, sticky = 'ns')

                # Other global variables
                self.sev2 = tk.StringVar(self.f1, '')
                self.counter = 0

                # The #2 listbox for places after user searches
                self.l2 = tk.Listbox(self.f1, font = self.myfont2, height = 15, selectbackground = 'gray80', selectforeground = 'black', activestyle = 'dotbox', bg = 'brown3')
                self.l2.bind('<Button>', lambda e : self.root.after(10, self.ctz, 0, 1))
                self.l2.bind('<space>', lambda e : self.root.after(10, self.ctz, 0, 1))

                # This shows the time, date, timezone
                self.ltz = tk.Label(self.f1, text = "IT IS NOT FAST\nMost Countries are there on the list\n(Warning not every country\nVERY FEW cities are there)", bg = 'red2', font = self.myfont3, justify = 'left')
                self.ltz.grid(row = 1, column = 3, sticky = 's')

                # Binding tab
                self.searcher.bind('<Tab>', self.checking)
                
                # For a barier
                tk.Label(self.f1, width = 60, bg = 'red2').grid(row = 2, column = 2)

                # Buttons for returning / quiting
                tk.Button(self.f1, text = "Return to Home Screen", command = self.switch, font = myfont).grid(row = 2, column = 0, sticky = 'nsew')
                tk.Button(self.f1, text = "Return to App Screen - Escape", command = lambda : self.clickedb(self.f), font = myfont).grid(row = 3, column = 0, sticky = 'nsew')
                tk.Button(self.f1, text = "Quit                 - Ctrl+W", command = lambda : rating(app, self.root), font = myfont).grid(row = 4, column = 0, sticky = 'nsew')

            # Part 2 for the frame 2 (Timer)
            if True:
                # global variables for timer sub app
                self.secondstext = self.hourstext = self.minutestext = self.colcount = 0
                self.lotimers = []
                self.lt = []
                self.count2 = 1
                self.colors = ['dark turquoise', 'turquoise', 'aquamarine', 'medium turquoise', 'medium aquamarine']
                self.lt2 = {}
                self.prevwid = 0

                # Frame for adding timers and showing timers
                self.fat = tk.Frame(self.f2, bg = 'cyan')
                self.listtimers = tk.Frame(self.f2, bg = 'cyan')

                # Hours, minutes, seconds labels and a barrier label
                self.hours = tk.Label(self.fat, text = "0 : ", font = self.myfont4, bg = 'cadet blue')
                self.minutes = tk.Label(self.fat, text = "0 : ", font = self.myfont4, bg = 'steel blue')
                self.seconds = tk.Label(self.fat, text = 0, font = self.myfont4, bg = 'light blue')
                tk.Label(self.f2, width = 60, height = 5, bg= 'cyan').grid(row = 1, column = 1)
                self.hours.grid(row = 2, column = 1)
                self.minutes.grid(row = 2, column = 2)
                self.seconds.grid(row = 2, column = 3, ipadx = 10)

                # The dust bin(db) to discard timers
                self.db = tk.Button(self.listtimers, bitmap = 'error', bg = 'red', fg = 'blue', text = 'Discard', compound = 'top')
                
                # Buttons for increasing and decreasing
                tk.Button(self.fat, text = "⬆", command = lambda : self.movevert(0), bg = 'cadet blue', font = self.myfont2).grid(row = 1, column = 1, sticky = 'ew')
                tk.Button(self.fat, text = "⬆", command = lambda : self.movevert(2), bg = 'steel blue', font = self.myfont2).grid(row = 1, column = 2, sticky = 'ew')
                tk.Button(self.fat, text = "⬆", command = lambda : self.movevert(4), bg = 'light blue', font = self.myfont2).grid(row = 1, column = 3, sticky = 'ew')
                tk.Button(self.fat, text = "⬇", command = lambda : self.movevert(1), bg = 'cadet blue', font = self.myfont2).grid(row = 3, column = 1, sticky = 'ew')
                tk.Button(self.fat, text = "⬇", command = lambda : self.movevert(3), bg = 'steel blue', font = self.myfont2).grid(row = 3, column = 2, sticky = 'ew')
                tk.Button(self.fat, text = "⬇", command = lambda : self.movevert(5), bg = 'light blue', font = self.myfont2).grid(row = 3, column = 3, sticky = 'ew')

                # Asks the name of the timer
                self.nametimer = tk.Entry(self.fat, bg = 'LightSkyBlue2', font = self.myfont3, width = 15)
                self.nametimer.grid(row = 3, column = 4, sticky = 'nsew')
                self.nametimer.insert(0, "Name of the timer")
                self.nametimer.bind('<Return>', self.settimer)

                # The submit button
                self.submitb = tk.Button(self.fat, text = "Submit", command = self.settimer, bg = 'dodger blue', font = self.myfont4, activebackground = 'dodger blue')
                self.submitb.grid(row = 4, column = 4, sticky = 'ew')

                # The button for popping up fat frame to add a timer
                self.addtimer = tk.Button(self.f2, text = "Add a timer", font = self.myfont4, command = lambda : self.clickedb(self.fat, 1), bg = 'cyan2')
                self.addtimer.grid(row = 0, column = 0, sticky = 'ew')

                # The button for showing timers
                self.showtimers = tk.Button(self.f2, text = "Show timers", font = self.myfont4, command = lambda : self.clickedb(self.fat, 3), bg = 'pale turquoise')
                self.showtimers.grid(row = 1, column = 0, sticky = 'ew')

                # The buttons for returning / quitting
                tk.Button(self.f2, text = "Return to Home Screen", command = self.switch, font = myfont).grid(row = 4, column = 0, sticky = 'nsew')
                tk.Button(self.f2, text = "Return to App Screen", command = lambda : self.clickedb(self.f), font = myfont).grid(row = 5, column = 0, sticky = 'nsew')
                tk.Button(self.f2, text = "Quit", command = lambda : rating(app, self.root), font = myfont).grid(row = 6, column = 0, sticky = 'nsew')

            # Part 3 for the frame 3 (Stopwatch)
            if True:
                # The stopwatch subapp
                tk.Label(self.f4, width = 90, bg = 'green2').grid(row = 0, column = 0)
                self.sw = tk.Label(self.f4, text = 'welcome', bg = 'OliveDrab1', font = ('Comic sans', 50, 'bold'))
                self.sw.grid(row = 0, column = 1)

                # Global variables
                self.starttime = self.counting = self.loovar = 1
                self.lof = []
                self.rocount = 2

                # Starting, pausing, Flag buttons are here
                self.start = tk.Button(self.f4, text = "▶", command = lambda : self.stopwatch(0), font = self.myfont5, bg = 'DarkOliveGreen3')
                self.start.grid(row = 1, column = 1, sticky = 'w')
                self.stop = tk.Button(self.f4, text = "||", state = 'disabled', command = lambda : self.stopwatch(1), font = self.myfont5, bg = 'PaleGreen3')
                self.stop.grid(row = 1, column = 1, sticky = 'e')

                # Returning / quitting
                tk.Button(self.f4, text = "Return to Home Screen", command = self.switch, font = myfont).grid(sticky = 'ew', row = 2, column = 2)
                tk.Button(self.f4, text = "Return to App Screen", command = lambda : self.clickedb(self.f), font = myfont).grid(sticky = 'ew', row = 3, column = 2)
                tk.Button(self.f4, text = "Quit", command = lambda : checking(1), font = myfont).grid(sticky = 'ew', row = 4, column = 2)

        # Changes frame to root_2 to go to homescreen
        def switch(self, update = False):
            """It switches between appscreen and homescreen\n\nParameters are\n1) update (bool) = False"""
            global clroot
            
            self.torf = True

            # Unbinds all the bindings
            app.unbind('<Alt_L> <c>')
            app.unbind('<Alt_L> <s>')
            app.unbind('<Alt_L> <t>')
            app.unbind('<Escape>')
            
            # Saves the frame and removes grid and grids root_2
            # changes background too
            clroot = self.root
            root_2.grid()
            app.title('Home Screen')
            app.configure(bg = root_2.cget('bg'))
            self.root.grid_remove()

        # just like the colorchanger function
        def come_leave(self, event):
            """Changes colour of the event widget\n\nParameters are -;\n1) event(tk.Event)"""
            
            # Checks if mouse cam in or out
            if 'Enter' in str(event):
                self.color = event.widget.cget('bg')
                
                # checks which colour to keep
                if self.color == 'cyan':
                    event.widget.configure(bg = 'cyan3')
                elif self.color == 'red2':
                    event.widget.configure(bg = 'red3')
                else:
                    event.widget.configure(bg = 'green3')
            else:
                event.widget.configure(bg = self.color)

        # Changes frames in the app.
        def clickedb(self, catsvar, fatc = 0):
            """Changes to and from frames and labels\n\nParameters are -;\n1) catsvar(tk.Frame)\n2) fatc(int)"""
            
            # Checks which frame is it
            if fatc == 1:
                # the frame is fat
                self.count = 1

                # Checks if listimers is mapped
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
                # the frame fat needs to be removed
                self.count = 0

                self.fat.grid_remove()
                
                self.addtimer['text'] = "Add a timer"
                self.addtimer['command'] = lambda : self.clickedb(self.fat, fatc = 1)
                return
            elif fatc == 3:
                # the frame is listtimers
                
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
                # Listimers should be removed

                self.listtimers.grid_remove()
                
                self.showtimers['text'] = "Show timers"
                self.showtimers['command'] = lambda : self.clickedb(self.fat, fatc = 3)
                
                return 
            
            if fatc < 5 and fatc > 0:
                return
            
            # Fat is not a proper frame so change the previous frame to f2
            if self.prevcatsvar == self.fat:
                self.prevcatsvar = self.f2
            
            # Ungridding prev and gridding current
            self.prevcatsvar.grid_remove()
            
            catsvar.grid(row = 1, column = 0, sticky = 'w')
            
            self.root.configure(bg = catsvar.cget('bg'))
            app.configure(bg = catsvar.cget('bg'))
            
            self.prevcatsvar = catsvar

        # Sets focus to l2 or lbfrl or quits
        def checking(self, event):
            """Sets focus to whichever is mapped or quits\n\nParameters -;\n1)Event(tk.Event)"""
            
            if event == 1:
                self.torf = True
                root.quit()

            # Checks which is mapped
            if self.lbfrl.winfo_ismapped() == True:
                self.lbfrl.focus_set()
            elif self.l2.winfo_ismapped() == True:
                self.l2.focus_set()

        # Does the searching thing
        # Moves to l2 or lbfrl if you press down from seacher
        def sken(self, event):
            """Does two things-;\n1) moves to lbfrl or l2 depending on which is gridded\n2) Searches for what the user is looking for\nParameters -;\n1) Event(tk.Event)"""
            
            # If user pressed down move to the gridded Listbox
            if event.keysym == 'Down':
                # Sets selection to 0 and sets focus
                if self.lbfrl.winfo_ismapped() == True:
                    
                    self.lbfrl.focus_set()
                    self.lbfrl.selection_set(0)
                
                else:
                    
                    self.l2.focus_set()
                    self.l2.selection_set(0)
                
                return
            
            # reseting values of lv and fl2
            self.lv = []
            self.fl2 = []
            self.l2.delete(0, 'end')
            
            # cunducting a loop to get all items user is looking for inside the list of places
            for ele in self.fl:
                
                # checks if what the user types is in the elements
                if self.searcher.get().lower() in ele.lower():
                
                    # If True append it to l2
                    self.l2.insert('end', ele)
                
                    self.lv.append(self.rv[self.fl.index(ele)])
                    self.fl2.append(ele)
            
            # it is stored in l2 so ungridding lbfrl and gridding l2
            self.lbfrl.grid_remove()
            self.sb.configure(command = self.l2.yview, orient = 'vertical')
            self.l2.configure(yscrollcommand = self.sb.set)
            self.l2.grid(row = 1, column = 0, sticky = 'ew')

        # This is the clock.
        # This changes time every second and it changes if you change timezone
        def ctz(self, sel = 0, a = 0):
            """It updates every once per second.\n\nIt runs the clock for showing the time."""
            
            # If you stop the clock
            if self.torf:
                return

            # Format for how the user should see it as
            fmt = "Date - %d/%m/%y\nTime - %I:%M:%S %p\nTime Zone - %Z %z\nDay - %a/%B"
            
            # Checks if timezone is same or not
            # Timezone has changed
            if sel == 0:

                # Checks which should be changed l2 or lbfrl
                # This is lbfrl
                if a == 0:
                    # The place which got selected
                    selected = self.lbfrl.curselection()
                    
                    # Adding it to a string var
                    self.sev2.set(self.lv[selected[0]])
                    # Changing it's color
                    self.lbfrl.itemconfigure(selected[0], bg = 'gray50')
                    
                    # if the list is not empty the previous selected item should be it's original colour
                    if self.lsel != []:
                        self.lbfrl.itemconfigure(self.lsel[0], bg = 'brown3')
                    
                    # countinue
                    self.lsel = [selected[0]]

                # same thing for l2
                elif a == 1:
                    selected = self.l2.curselection()
                    
                    self.sev2.set(self.lv[selected[0]])
                    self.l2.itemconfigure(selected[0], bg = 'gray50')
                    
                    if self.lsel != []:
                        # Checks if previous selection was not in lbfrl
                        if len(self.fl2) >= self.lsel[0]:
                            self.l2.itemconfigure(self.lsel[0], bg = 'brown3')
                    
                    self.lsel = [selected[0]]
                
                # if counter is 0 make it 1 and start the loop
                if self.counter == 0:
                    self.counter = 1
                    # self.ctz(1)
                else:
                    return
            
            # It is the clock
            else:
                # If it has no timezone return
                if self.sev2.get() == '':
                    return
                
                # gets current time of time zone
                now_time = self.sev2.get()
                now_time = datetime.now(pytz.timezone(now_time))
                
                # gets computer lang
                s3 = self.fv[self.rv.index(self.sev2.get())]
                self.ltz.configure(text = s3+"\n"+str(now_time.strftime(fmt)))
            
            if self.torf:
                return

            if not exit_now: self.root.after(1000, self.ctz, 1)

        # if you press the sercher
        def presed(self, event):
            """If you pressed the searcher or if you presed an item of l2 or lbfrl.\n\nParameters are -;\n 1) Event(tk.Event / integer)"""
            
            # If you pressed the searcher
            if event == 0:
                self.searcher.delete(0, 'end')
                self.searcher.unbind('<Button>')
                self.searcher.bind('<Button>', self.presed)
            
            # It selects every character
            elif event == 1:
                self.searcher.focus_set()
                self.searcher.select_range(0, 'end')
                self.searcher.icursor('end')
            
            # If you pressed an item in the listboxes
            else:
                # if it is not empty
                if self.searcher.get() != '' and not exit_now:
                    
                    # Calls the function once more because it takes time to update
                    self.root.after(10, self.presed, 1)
        
        # If user wants to discard timer
        def dust_bin(self, wid, col):
            """Discards the timers\n\nParameters are -;\n 1) wid (tk.Event)\n 2) col (integer)"""
            
            # if you discard
            if col == 10:
                # list of values
                vl = list(self.lt2.values())
                # finding the value of the widget
                keyinval = vl.index(self.lt2[wid])
                # Removing timer
                wid.grid_remove()
                # Removing timer from lt2, lotimers
                self.lt2.update({wid : ""})
                self.lotimers[self.lotimers[keyinval]] = ""
                # removing db
                self.db.grid_remove()
            
            # If you press the timer
            else:
                # If it is not same widget before also
                if self.prevwid != wid.widget:
                    # Assigning prevwid to this widget
                    self.prevwid = wid.widget
                    self.db.grid(row = col, column = 1, sticky = 'ns')
                    self.db['command'] = lambda : self.dust_bin(wid.widget, 10)
                # If it is same widget before also
                else:
                    # Assigning 0 and removing db
                    self.prevwid = 0
                    self.db.grid_remove()

        def looper(self):
            """Loops through checking if timer rang\n\nParameters are None"""
            # If there are no timers return
            if len(self.lt2.values()) == 0:
                return
            # Else conduct for loop for checking if timer is over
            for vals in self.lt2.values():

                if vals <= datetime.now():
                    # If the time is over
                    # Key, values of lt2 lists
                    kl, vl = list(self.lt2.keys()), list(self.lt2.values())
                    
                    # The computer stores("Your timer, ____ Rang" while ____ is replaced by the timer) in queue
                    self.cump.say("Your timer, {} rang".format(self.lotimers[vl.index(vals)]))
                    # Runs it(Talks everything in queue)
                    self.cump.runAndWait()
                    
                    # The key for the place of item vals in the valuelist (vl)
                    keyinval = kl[vl.index(vals)]
                    # Removes the grid of that timer
                    keyinval.grid_remove()
                    
                    # removes it from lt2, L and lotimers
                    self.lt2.pop(keyinval)
                    self.lotimers.remove(self.lotimers[vl.index(vals)])
                    
                    # Runs looper again
                    self.looper()
                    return
            
            # If no timers are over wait for another second and run looper
            if not exit_now: self.root.after(1000, self.looper)

        def settimer(self):
            """Asks the user for timer name and value and makes a new timer\n\nParameters - None"""
            
            # If you have maximum no. of timers(5 here)
            if len(self.lotimers) == 5:
                # store "Maximum number of timers set" in pyttsx3(Module for text to speech) queue
                self.cump.say("Maximum number of timers set")
                # Runs everything in queue
                self.cump.runAndWait()
                # Returns because does not want to make a new timer
                return
            # If timer is set for 0 sec
            if self.secondstext == 0 and self.hourstext == 0 and self.minutestext == 0:
                self.cump.say("Put a timer for more than 0 seconds")
                self.cump.runAndWait()
                return
            # If the name is not already there in the list of timers(lotimers)
            if self.nametimer.get() not in self.lotimers:
                # Appends The name of timer in list L
                self.fat.grid_remove()
                
                # changes the name of addtimer from Cancel the timer to Add a timer
                self.addtimer['text'] = "Add a timer"
                
                # Prevcatsvar = f2
                self.prevcatsvar = self.f2
                
                # Command of addtimer changes
                self.addtimer['command'] = lambda : self.clickedb(self.fat, fatc = 1)
                
                # Increaments colcount
                self.colcount = len(self.lt2)
                
                # Time the timer was set for
                setfor = datetime.now()+timedelta(hours = self.hourstext, minutes = self.minutestext, seconds = self.secondstext)
                # Appends it in lt
                self.lt.append(setfor)
                
                # tells the user how long it is set for
                ntg = "Timer '{}' is set for\n{}".format(self.nametimer.get(), setfor.strftime("%x, %X"))
                ele = tk.Label(self.listtimers, text = ntg, bg =  self.colors[len(self.lotimers)], font = self.myfont2)
                ele.grid(row = self.colcount, column = 0, sticky = 'ew')
                lcc = self.colcount
                ele.bind('<Button>', lambda e: self.dust_bin(e, lcc))
                
                # adds this to dictionary
                self.lt2[ele] = setfor
                self.lotimers.append(self.nametimer.get())
                
                if len(self.lotimers) == 1:
                    # If length is 1 do looper
                    self.looper()
            # If it is there in the list of timers (lotimers)
            else:
                self.cump.say("Name the timer something different")
                self.cump.runAndWait()
                return

        def movevert(self, wb):
            """Increases / decreases the time of the timer\n\nParameters are -;\n1) wb (int)"""
            
            if wb == 1 or wb == 0:
                # If it is hours + / -

                if wb == 1:
                    # If it is decrease hours

                    if self.hourstext == 0:
                        # If it is 0 change to 23 instead of -1

                        self.hourstext = 23
                        self.hours['text'] = "23 : "
                    
                    else: 
                        # if it is not 0 decrement it by 1
                        
                        self.hourstext -= 1
                        self.hours['text'] = str(self.hourstext)+" : "
                else:
                    # If it is increase it by 1

                    if self.hourstext == 23:
                        # If it is 23 make it 0 instead of 24
                        
                        self.hourstext == "0 : "
                        self.hours['text'] = "0 : "
                    else:
                        # if it is not 23 increment it by 1 
                        self.hourstext += 1
                        self.hours['text'] = str(self.hourstext)+" : "
            elif wb == 2 or wb == 3:
                # If it is minutes + / -

                if wb == 3:
                    # If it is -

                    if self.minutestext == 0:
                        # If it is 0 make it 59
                        
                        self.minutestext = 59
                        self.minutes['text'] = "59 : "
                    else:
                        # If it is not 59 decrement it by 1

                        self.minutestext -= 1
                        self.minutes['text'] = str(self.minutestext)+" : "
                else:
                    # If it is +

                    if self.minutestext == 59:
                        # If it is 59 make it 0

                        self.minutestext = 0
                        self.minutes['text'] = "0 : "
                    else:
                        # If it is not 59 increase it by 1

                        self.minutestext += 1
                        self.minutes['text'] = str(self.minutestext)+" : "
            elif wb == 4 or wb == 5:
                # If it is seconds + / -
                
                if wb == 5:
                    # If it is -
                    
                    if self.secondstext == 0:
                        # If seconds is 0 make it 59

                        self.secondstext = 59
                        self.seconds['text'] = 59
                    else:
                        # If seconds is not 0 decrement it by 1

                        self.secondstext -= 1
                        self.seconds['text'] = self.secondstext
                else:
                    # If it is +

                    if self.secondstext == 59:
                        # If seconds is 59 make it 0

                        self.secondstext = 0
                        self.seconds['text'] = 0
                    else:
                        # If seconds is not 0 increment it by 1
                        
                        self.secondstext += 1
                        self.seconds['text'] = self.secondstext
            if self.count2 == 0 or wb == 10:
                # For updating the submit button

                # when the timer needs to be set
                sf = datetime.now()+timedelta(self.hourstext, self.minutestext, self.secondstext)

                # Changing the submit button text
                self.submitb['text'] = sf.strftime("Submit - \n%x\n%X")

                if self.count == 1 and not exit_now:
                    
                    self.root.after(1000, self.movevert, 10)
                    self.count2 = 1
                
                else:
                    self.count2 = 0
            
        def looping(self, rco):
            """Updates Stopwatch every second\n\nParameters are -;\n1) rco (int)"""
            
            if rco == 1 and self.loovar == 0:
                # This loops through every second

                # Adds one second to it
                self.starttime = datetime.strptime(self.starttime, "%X") + timedelta(seconds=1)
                self.starttime = self.starttime.strftime("%X")
            
                # Changes text after updating
                self.sw['text'] = self.starttime
            
                # Loops through itself
                if not exit_now: self.root.after(1000, self.looping, 1)
            elif rco == 2:
                # Resets everything

                # it sets time to 0:00
                self.sw['text'] = self.starttime
            
                # Loop variable
                self.loovar = 0
            
                # Changes text and command of start and stop
                self.start['text'] = "⚐"
                self.start['command'] = lambda : self.stopwatch(2)
            
                self.stop['text'] = '||'
                self.stop['command'] = lambda : self.stopwatch(1)
            
                # Sends it to looping(1)
                if not exit_now: self.root.after(1000, self.looping, 1)

        def stopwatch(self, choice):
            """Changes text, command and states of the buttons when you click them\n\nParameters are -;\n1) choice (int)"""
            

            if choice == 0:
                # If you click start button

                # Loop var = 0
                self.loovar = 0
                
                # dn = time now
                dn = datetime.now()
                
                # sets starttime to 0 : 00
                self.starttime = datetime.now()-timedelta(hours=dn.hour, minutes=dn.minute, seconds=dn.second)
                self.starttime = self.starttime.strftime("%X")
                
                self.fst = datetime.now()
                
                # Changes text, commands, states
                self.sw['text'] = self.starttime
                
                self.start['text'] = "⚐"
                self.start['command'] = lambda : self.stopwatch(2)
                
                self.stop['state'] = 'normal'
                
                if not exit_now: self.root.after(1000, self.looping, 1)
            
            elif choice == 1:
                # If you press pause button
                
                self.counting = 0
                
                # Changes text, commands
                self.start['text'] = "▶"
                self.start['command'] = lambda : self.looping(2)
                
                self.stop['command'] = lambda : self.stopwatch(3)
                self.stop['text'] = "⬛"
                
                # Sets looping var to 0
                self.loovar = 1
            
            elif choice == 2:
                # If you pressed flag

                # time when you pressed flag
                texoll = datetime.now()-timedelta(hours = self.fst.hour, minutes = self.fst.minute, seconds = self.fst.second, microseconds = self.fst.microsecond)
                
                # lilof is the local variable for the label of the time when you pressed flag
                lilof = tk.Label(self.f4, text = texoll.strftime("%X.%f"), bg = 'yellow green', font = self.myfont3)
                lilof.grid(row = self.rocount, column = 1)
                
                self.rocount += 1
                self.lof.append(lilof)
                self.fst = datetime.now()
            
            else:
                # If you pressed stop

                # Goes through all flags and deletes them
                for ele in self.lof:
                    ele.destroy()
                
                # changing texts, states and commands
                self.sw['text'] = "START"
                
                self.start['text'] = "▶"
                self.start['command'] = lambda : self.stopwatch(0)
                
                self.stop['text'] = '||'
                self.stop['state'] = 'disabled'
                self.stop['command'] = lambda : self.stopwatch(1)
                
                # Looping 0 for resetting
                self.looping(0)

    # For my mom's b'day
    class happybirthday:
        """Bday app\n\nParameters are -;\n1) Root_2\n2) application"""
        
        global hroot
        
        def __init__(self, root_2, app):
            """Kicks off everytime you call this class\n\nParameters are -;\n1) Root_2\n2) application"""
            
            global hroot
            if hroot != 0:
                root_2.grid_remove()
                self.root = hroot
                self.root.grid()
                app.config(bg = self.root.cget('bg'))
                return
            
            # ungrids root_2 and makes a new root
            root_2.grid_remove()
            hroot = tk.Frame(app)
            self.root = hroot

            # Bg colors
            self.root.configure(bg = 'gold')
            app.configure(bg = 'gold')
            
            # Frames mast means master
            self.mast1 = tk.Frame(self.root, bg = 'gold')
            self.mast2 = tk.Frame(self.root, bg = 'white', width = 10, height= 10)
            self.mast3 = tk.Frame(self.root, bg = 'white')
            
            self.steper = 0
            self.root.grid()

            # Global variables
            self.loframes = [self.mast1, self.mast2, self.mast3]
            
            tk.Label(self.root, width = 100, height = 18, bg = 'gold').grid(row = 1, column = 0, sticky = 'w')
            
            self.myfont = font.Font(root = self.root, family = 'castellar', size = 20, weight = 'bold', slant = 'italic')
            
            tk.Label(self.mast1, text = "Happy\nBirthday\nAmma", font = self.myfont, fg = 'white', bg = 'sienna').grid(row = 1, column = 1, sticky = 'n', ipady = 2, ipadx = 38)
            tk.Label(self.root, height = 7, bg = 'gold', width = 81).grid(row = 1, column = 2, sticky = 'ne')
            
            self.nextbutton = tk.Button(self.root, text = "Next", font = self.myfont, bg = 'orangered', height = 2, command = lambda : self.turner(True))
            self.nextbutton.grid(row = 0, column = 2, sticky = 'e')
            self.prevbutton = tk.Button(self.root, text = "Previous", font = self.myfont, bg = 'orangered', height = 2, command = lambda : self.turner(False))
            
            self.mast1.grid(row = 2, column = 1)
            
            tk.Button(self.root, text = "Return to Home Screen", command = self.switch, font = myfont).grid(sticky = 'nw', row = 0, column = 1)
            tk.Button(self.root, text = "Quit", command = lambda : rating(app, self.root), font = myfont).grid(sticky = 'nw', row = 0, column = 1, pady = 33)
            
            # Draws a cake
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

            # Ending of the card
            tk.Label(self.mast3, text = "A - Amazing\nM - MasterChef\nM - Marvellous\nA - Astounding", fg = 'goldenrod4', bg = 'gold', font = self.myfont, justify = 'left').grid(row = 0, column = 0, ipady = 66, ipadx = 40)
            tk.Label(self.mast3, text = "G - Gorgeous\nA - Adventurous\nY - Youthful\nA - Astonishing\nT - Truthful\nH - Happy\nR - Right\nI - Impressive", fg = 'goldenrod4', bg = 'gold', font = self.myfont, justify = 'left').grid(row = 0, column = 1)

        def switch(self):
            """Switches between root and root_2\n\nParameters are - None"""
            global hroot
            
            # makes a global variable the root and ungrids it. Grids the home screen
            hroot = self.root
            root_2.grid()
            
            app.title('Home screen')
            app.configure(bg = root_2.cget('bg'))
            
            self.root.grid_remove()

        def turner(self, tsf):
            """Turns between pages\n\nParameters are -;\n1) tsf (Bool)"""

            if tsf and self.steper < 2:
                # If next button is pressed and If it is less than 2

                # Increases stepperby 1
                self.steper += 1
                
                # Changes frames
                self.loframes[self.steper-1].grid_remove()
                self.loframes[self.steper].grid(row = 2, column = 1)
            
            elif not tsf and self.steper > 0:
                # If previous button was pressed and If it was less than 2

                # Decreases steper by 1
                self.steper -= 1
                
                # Changes frames
                self.loframes[self.steper+1].grid_remove()
                self.loframes[self.steper].grid(row = 2, column = 1)
            
            if self.loframes[self.steper] == self.mast1:
                # If it is mast1 then no point of prevbutton
                self.prevbutton.grid_remove()
            
            elif self.loframes[self.steper] == self.mast3:
                # If it is mast1 then no point of nextbutton
                self.nextbutton.grid_remove()
            
            else:
                # Grids both of them
                self.nextbutton.grid(row = 0, column = 2, sticky = 'e')
                self.prevbutton.grid(row = 0, column = 0, sticky = 'w')

    # Hangman game
    class hangmang:
        """Hangman Game\n\nParameters are -;\n1) Root_2\n2) application"""

        global hgroot
        
        def __init__(self, root_2, app):
            """Kicks off whenever you call this class\n\nParameters are -;\n1) Root_2\n2) application"""
            
            global hgroot
            
            if hgroot != 0:
                root_2.grid_remove()
                self.root = hgroot
                self.root.grid()
                return
            
            # Makes the Frame for the game (Rhymes Frame, Game)

            hgroot = tk.Frame(app)
            root_2.grid_remove()
            
            self.root = hgroot
            
            app.title("hangman")
            
            self.myfont = font.Font(size = 12, family = 'algerian')
            self.count = tk.IntVar()
            
            # Animal names the computer can choose from
            self.words = ['armadillo', 'beaver', 'chimpanzee', 'dolphin', 'earthworm', 'flamingo'\
                ,'gorilla', 'hedgehog', 'iguana', 'jaguar', 'kingfisher', 'llama', 'mangoose'\
                , 'otter', 'possum', 'rhea', 'salmon', 'turkey', 'vulture', 'woodpecker'\
                , '']
            
            # Randomly selects a word and other global variables
            self.word = self.words[random.randrange(0, len(self.words))]
            self.blank = ""
            self.listword = list(self.word)
            self.guesses = []
            
            # Appends the first(0 in python) element to blank
            self.blank += self.listword[0]
            
            # Appends blanks to self.blank
            for loop in range(0, len(self.word)-1):
                self.blank = self.blank + " _"
            
            loop += 1
            self.prevguess = []
            
            if self.word[0] not in self.word[1:]:
                self.prevguess.append(self.word[0])
            
            tk.Label(self.root, text = " ", width = 100).grid(row = 0, column = 0)
            tk.Label(self.root, text = " ", height = 20).grid(row = 0, column = 1)
            
            self.counting = tk.Label(self.root, text = "wrongs: %s/6\nit is %s long" %(self.count.get(), len(self.word)), width = 25, height = 5, bg = 'green')
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
            tk.Button(self.root, text = "Quit", command = lambda : rating(app, self.root), font = myfont, justify = 'center', width = 19).grid(sticky = 'nw', row = 0, column = 0, pady = 33, ipadx = 4)
            tk.Button(self.root, text = "Replay", command = lambda : self.switch(2), font = myfont, justify = 'center', width = 19).grid(sticky = 'nw', row = 0, column = 0, pady = 66, ipadx = 4)
            
            if self.guess.get() == "":
                self.count.set(int(self.count.get())-1)
            
            self.root.grid()
        
        def switch(self, count = 1):
            """Switches between root, root2\n\nParameters are -;\n1) Count = 1 (Int)"""
            global hgroot
            
            if count == 1:
                # If user chose to go to home screen
                hgroot = self.root
                root_2.grid()
                app.title('Home screen')
                app.configure(bg = root_2.cget('bg'))
                self.root.grid_remove()
            
            else: 
                # If user chose to replay
                hgroot = 0
                root_2.grid()
                self.root.destroy()
                # Self.__init__ means run the class again
                self.__init__(root_2, app)                
        
        def correct(self, event):
            """'Corrects' the user's input\n\nParameters are -;\n1) event(tk.Event)"""

            # guest's value becomes lower value of guest
            self.guest.set(self.guest.get().lower())
            self.guess['textvariable'] = self.guest
            self.lb.insert('end', self.guess.get())

            if len(self.guess.get()) != 1:
                # If user tried to guess the word

                if self.guest.get() == self.word:
                    # If user got it correct

                    # Say congrats and appreciate him / her
                    self.guest.set('congrats')
                    
                    self.lb.delete(0, 'end')
                    self.lb.insert(0, 'Winner  ^_^')
                    self.lb.insert(0, 'Congrats :)')
                    
                    self.blankp.configure(text = "Congrats")
                    self.counting.configure(text = self.word)
                else:
                    # If it is not the word
                    
                    if len(self.guess.get()) != 0:
                        # increment the errors and show it to the user

                        self.count.set(self.count.get()+1)
                        self.counting.configure(text = "wrongs: %s/6\nit is %s long" %(self.count.get(), len(self.word)))
                
                if self.count.get() >= 6:
                    # If user had 6 or more wrongs

                    # Say loser, sucker and boo him / her
                    self.lb.delete(0, 'end')
                    self.lb.insert(0, 'loser  =C')
                    self.lb.insert(0, 'sucker :(')
                    
                    self.guest.set('loser')
                    self.blankp.configure(text = "loser")
                    
                    self.counting.configure(text = self.word)
                self.guesses.append(self.guess.get())
                self.guest.set('')
            
            else:
                # If user is guessing the letters

                # Appends it to prevguess and makes loop, blank_2 None
                self.prevguess.append(self.guess.get().lower())
                loop = 0
                blank_2 = ""

                if self.guess.get() in self.listword[1:]:
                    # If it is there in the word

                    if self.guess.get() in self.prevguess[0:-1]:
                        # If user guessed it before

                        self.count.set(int(self.count.get())+1)
                        self.counting.configure(text = "wrongs: %s/6\nit is %s long" %(self.count.get(), len(self.word)))
                        
                        self.guest.set('You guessed it before')
                    else:
                        # If user did not guess it before

                        # Runs for loop
                        for ele in self.listword:

                            if ele == self.guess.get():
                                # If the letter the user guessed is ele
                                
                                self.blank = self.blank.split(' ')
                                self.blank[loop] = ele
                                
                                # Runs a loop and adds the elements of blank into blank_2
                                for ele_2 in self.blank:
                                    blank_2 += ele_2
                                    blank_2 += " "
                                
                                self.blank = blank_2
                                blank_2 = ""
                            
                            loop += 1
                        
                        self.blankp.configure(text = self.blank)
                        self.guest.set('')
                
                else:
                    # If it is wrong

                    if len(self.guess.get()) != 0:
                        # If user did not enter nothing

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
            
            # Selecting all the characters
            self.guess.icursor('end')
            self.guess.select_range(0, 'end')

    # Virtual cube
    class cubegame:
        """Cube app\n\nParameters are -;\n1) Root_2\n2) application"""
        
        global cgroot
        
        def __init__(self, root_2, app):
            """Starts whenever cubegame is called\n\nParameters are -;\n1) Root_2\n2) application"""
            
            global cgroot
            if cgroot != 0:
                root_2.grid_remove()
                self.root = cgroot
                self.root.grid()
                return
            
            # Making a Frame for a game(rhymes)
            cgroot = tk.Frame(app)
            self.root = cgroot
            
            app.title('Cube Game')
            
            root_2.grid_remove()
            
            # Lists for faces
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

            # Making a cube
            for x in range(2, 5):
                for y in range(2, 5):
                    self.z += 1
                    tk.Label(self.root, text = " n  ", fg = self.f[self.z], bg = self.f[self.z], relief = "ridge", height = 3, width = 6).grid(row = y, column = x)
            
            self.w = tk.StringVar(self.root, "Move")
            
            self.ac = tk.Entry(self.root, text = self.w, font = myfont)
            self.ac.grid(row = 2, column = 1)
            self.ac.select_range(0, 'end')
            self.ac.focus_set()
            self.ac.icursor('end')

            self.a = tk.Label(self.root, text = "facing-black", fg = 'black', bg = 'red', width = 12)
            self.a.grid(row = 5, column = 1)
            self.a['font'] = self.myfont
            
            self.s = tk.Label(self.root, text = "on top-red", fg = 'red', bg = 'black', width = 12)
            self.s.grid(row = 6, column = 1)
            self.s['font'] = self.myfont
            
            self.ac.bind("<Return>", self.entering)
            
            tk.Button(self.root, text = "Return to Home Screen", command = self.switch, font = myfont).grid(sticky = 'nw', row = 0, column = 0)
            tk.Button(self.root, text = "Quit", command = lambda : rating(app, self.root), font = myfont).grid(sticky = 'nw', row = 0, column = 0, pady = 33)
            
            self.root.grid()
        
        def switch(self):
            """Switches between root, root_2\n\nParameters are - None"""
            
            cgroot = self.root
            root_2.grid()
            app.title('Home Screen')
            app.configure(bg = root_2.cget('bg'))
            self.root.grid_remove()
        
        def entering(self, e):
            """Brain of the class Does all the moves\n\nParameters are -;\n1) e (tk.Event)"""

            # Makes variables
            self.z = -1
            move = self.w.get()
            move = move.upper()
            self.w.set('')

            # I am commanting only R because they are too many

            if move == "R":
                # If move is 'R'
                
                # Changes the color
                g, c, e = self.f[6], self.f[7], self.f[8]
                self.f[6], self.f[7], self.f[8] = self.d[2], self.d[1], self.d[0]
                self.d[0], self.d[1], self.d[2] = self.b[0], self.b[1], self.b[2]
                self.b[0], self.b[1], self.b[2] = self.t[8], self.t[7], self.t[6]
                self.t[6], self.t[7], self.t[8] = g, c, e

                h, i, j, k = self.r[0], self.r[7], self.r[8], self.r[1]
                self.r[0], self.r[7], self.r[8], self.r[1] = self.r[2], self.r[3], self.r[6], self.r[5]
                self.r[6], self.r[3], self.r[2], self.r[5] = h, k, j, i
                
                # Runs for loop to update
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
                rating(app, self.root)
        
    # Color game
    class cg:
        """Color Game\n\nParameters are -;\n1) Root_2\n2) application"""

        global colroot
        def __init__(self, root_2, app):
            """Initializes colour game\n\nParameters are -;\n1) Root_2\n2) application"""
            
            self.qui = 0
            
            # If user is playing again
            if colroot != 0:
                root_2.grid_remove()
            
                self.root = colroot
                self.counting = count.get()
            
                self.root.grid()
            
                self.qui = 0
            
                self.lesgo()
                return
            
            root_2.grid_remove()
            
            # Global variables
            self.counting = 60
            self.colours = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
            self.counter = 0
            self.words = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
            
            # Frame for the game (rhymes)
            self.root = tk.Frame(app)
            
            app.title("Colour Game")
            
            self.iv1 = tk.IntVar(self.root, 0)
            self.iv2 = tk.IntVar(self.root, 0)
            
            self.myfont = font.Font(size = 15, family = 'Algerian', weight = "bold")
            self.myfont_2 = font.Font(size = 18, family = 'Algerian', weight = "bold")
            self.myfont_4 = font.Font(size = 40)
            
            tk.Label(self.root, text = " ", width = 75).grid(row = 0, column = 0)
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
            
            tk.Button(self.root, text = "Return to Home Screen", command = self.switch, font = myfont).grid(sticky = 'nw', row = 3, column = 0)
            tk.Button(self.root, text = "Quit", command = lambda : rating(app, self.root), font = myfont).grid(sticky = 'nw', row = 3, column = 0, pady = 33)
            
            self.root.grid()
        
        def switch(self):
            """Switches between root, root_2.\n\nParameters are - None"""

            global colroot
            
            self.qui = 1
            
            colroot = self.root
            root_2.grid()
            count.set(self.counting)
            
            app.title('Home screen')
            app.configure(bg = root_2.cget('bg'))
            
            self.root.grid_remove()
        
        def lestart(self, event):
            """When You press Enter\n\nParameters are -;\n1) Event (tk.Event)"""

            if self.counting == 0: self.ges['state'] = 'disabled' # If time is up lock the state

            a = self.ges.get()
            if a.lower() == self.colours[self.iv1.get()]:
                # If it is the colour

                # Updates the score
                self.counter += 1
                self.score.configure(text = "Your score : {}".format(self.counter))
            
            # makes lists for colours and words and empties geser
            self.geser.set('')
            self.colours = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
            self.words = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
            
            a = True

            # Text of iv1, iv2
            iv1 = self.iv1.get()
            iv2 = self.iv2.get()
            
            while a:
                # Looping so it is different colours than previous one

                self.iv1.set(random.randint(0, len(self.colours)-1))
                
                if self.iv1.get() != iv1:
                
                    break

            while a:
                # Looping so it is different colours than previous one

                self.iv2.set(random.randint(0, len(self.words)-1))
                
                if self.iv2.get() != self.iv1.get() and self.iv2.get() != iv2:
                
                    break
            
            self.code.configure(text = self.words[self.iv2.get()], fg = self.colours[self.iv1.get()])
        
        def lesgo(self):
            """Loops through to update time\n\nParameters are - None"""
            
            if self.qui:
                # If user exited
                return
            
            if self.counting == 60:
                # for kicking it off

                self.ges['state'] = 'normal'
                self.geser.set('')
                
                self.colours = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
                self.words = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
                
                self.iv1.set(random.randint(0, 8))
                self.iv2.set(random.randint(0, 8))
                
                # Changes text and color of the label
                self.code.configure(text = self.words[self.iv1.get()], fg = self.colours[self.iv2.get()])
            
            self.ges.bind('<Return>', self.lestart)
            
            self.timer['text'] = "Game ends in : {}".format(self.counting)
            
            if self.counting > 0:
                # If time is up

                self.counting -= 1
                
                if not exit_now: self.root.after(1000, self.lesgo)
            
            if self.counting == 0:
                self.switch()

    # Trex run
    class trr:
        """Trex run game\n\nParameters are -;\n1) root_2(tk.Frame)\n2) app(tk.Tk)"""

        def __init__(self, root_2, app):
            """Starts of trr\n\nParameters are -;\n1) root_2(tk.Frame)\n2) app(tk.Tk)"""
            
            root_2.grid_remove()
            
            self.root = tk.Frame(app)
            self.root.grid()
            
            self.poloc = tk.IntVar(self.root, 1)
            self.plco2 = tk.IntVar(self.root, 0)
            self.plco3 = tk.IntVar(self.root, 0)
            
            # Cactus, trex images
            self.img = Image.open("D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\dinotrex.png")
            self.img2 = Image.open("D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\cactustrex.png")
            
            self.img = self.img.resize((160, 80))
            self.img2 = self.img2.resize((160, 80))
            
            # Turning the images into photoimages
            self.pi =  ImageTk.PhotoImage(self.img)
            self.pi2 = ImageTk.PhotoImage(self.img2)
            
            y = 4
            
            self.myfont = font.Font(root = self.root, family = 'Algerian', weight = 'bold', size = 12)

            for gsfidky in range(1, 3):
                tk.Label(self.root, text = "      ", height = 5, width = 20).grid(row = 3, column = gsfidky)
            
            tk.Label(self.root, text = "      ", height = 5, width = 20).grid(row = 0, column = 7)
            tk.Label(self.root, text = "      ", height = 5, width = 20).grid(row = 2, column = 7)
            tk.Label(self.root, text = "      ", height = 5, width = 20).grid(row = 1, column = 7)
            
            self.loc = tk.Label(self.root, image = self.pi)
            self.loc.grid(row = 1, column = 0)
            
            app.bind('<space>', self.ctlidky)
            app.bind('<Down>', self.ctlidky)
            app.bind('<Up>', self.ctlidky)
            
            tk.Button(self.root, text = "Return to Home Screen", command = self.switch, font = myfont).grid(sticky = 'nw', row = 3, column = 0)
            tk.Button(self.root, text = "Quit", command = lambda : rating(app, self.root), font = myfont).grid(sticky = 'nw', row = 4, column = 0)
            
            app.after(750, self.cfbc, y)
        
        def switch(self):
            """Switches between root, root_2.\n\nParameters are - None"""

            root_2.grid()
            
            app.title('Home screen')
            
            app.unbind('<Up>')
            app.unbind('<Down>')
            app.unbind('<space>')
            
            app.configure(bg = root_2.cget('bg'))
            
            self.root.grid_remove()
        
        def cfbc(self, y):
            """Runs a clock for regridding the cacti\n\nParameters are-;\n1) y (Int)"""

            if y == 0:
                # If the cactus is at x = 0

                if self.poloc.get() == self.plco2.get() or self.plco3.get() == self.poloc.get():
                    # If it crashed

                    self.switch()
                    
                    return
                else:
                    # If it didn't crash
                    
                    self.io.destroy()
                    self.io2.destroy()
                    
                    y = 4
            
            if y == 4:
                # For starting of the game

                # Making cactuses
                self.io = tk.Label(self.root, image = self.pi2)
                self.io2 = tk.Label(self.root,image = self.pi2)
                
                # Random number
                self.rrnof = random.randrange(0, 3)
                a = True

                while a:
                    # Runs a loop to prevent chosing the same number

                    rnof2 = random.randrange(0, 3)

                    if rnof2 != self.rrnof:
                        a = False

                # Grids it
                self.io.grid(row = self.rrnof, column = y)
                self.io2.grid(row = rnof2, column = y)
                
                self.plco2.set(self.rrnof)
                self.plco3.set(rnof2)
            
            self.io.grid(column = y)
            self.io2.grid(column = y)
            
            # After some time it loops again
            if not exit_now: self.root.after(250, self.cfbc, y-1)
        
        def ctlidky(self, event):
            """Regrids the dino\n\nParameters are -;\n1) Event(tk.Event)"""

            if self.poloc.get() != 2 and event.keysym == 'Down':
                # If user pressed down

                self.poloc.set(self.poloc.get()+1)
                self.loc.grid(row = self.poloc.get(), column = 0)
            
            elif self.poloc.get() != 0:
                # If user pressed space or up

                self.poloc.set(self.poloc.get()-1)
                self.loc.grid(row = self.poloc.get(), column = 0)
            
    # Knaughts And Crosses Game (KACG) (x and o)
    class kacg:
        """Knaughts and crosses game(x and o)\n\nParameter are-;\n1) Root_2(tk.Frame)\n2) app(tk.Tk)"""
        
        global kroot

        def __init__(self, root_2, app):
            """Starts when kacg is called\n\nParameter are-;\n1) Root_2(tk.Frame)\n2) app(tk.Tk)"""

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
            tk.Button(self.root, text = "Quit", command = lambda : rating(app, self.root), font = myfont).grid(sticky = 'w', row = 6, column = 0)
            
            self.root.grid()
        
        def switch(self, count = True):
            """Switches between root, root2\n\nParameters are -;\n1) Count = 1 (Int)"""
            global kroot
            
            if count:
                # If user chose to go to home screen
                
                kroot = self.root
                root_2.grid()
                
                app.title('Home screen')
                app.configure(bg = root_2.cget('bg'))
                
                self.root.grid_remove()
            
            else:
                # If user wants to replay

                # making text of all the buttons " "
                for ele in self.ln:
                    ele['text'] = " "
                
                # Changing all variables values to 0
                self.xo = self.ro1 = self.ro2 = self.ro3 = self.co1 = self.co2 = \
                self.co3 = self.di1 = self.di2 = 0
                
        def xoxo(self, value):
            """Changes text to X or O and checks wether tie, o won or x won\n\nParameters are-;\n1) Value(tk.Button)"""

            if value['text'] != " ":
                # If text is O or X do not change it
                return

            if self.xo:
                # changes text from " " to "o"
                value.config(text = "o", command = None)
                self.xo = 0

            else:
                # Changes Value from " " to "x"
                value.config(text = "x", command = None)
                self.xo = 1
            
            # changes the row, column, diagnal row of the button+1

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
            
            # Runs a loop to check if it is a tie
            for ele in self.ln:
                if ele['text'] != " ":
                    a += 1
            
            if a == 9:
                # TIE!!!
                for ele in self.ln:
                    ele['text'] = "Tie"
            
            elif 3 in lb:
                # X WON!!!
                for ele in self.ln:
                    ele['text'] = "X won"
            
            elif -3 in lb:
                # O WON!!!
                for ele in self.ln:
                    ele['text'] = "O won"

    # Boxes game
    class boxes:
        """Boxes game\n\nParameters are-;\n1) root_2(tk.Frame)\n2) app(tk.Tk)"""

        global broot
        
        def __init__(self, root_2, app):
            """Starts out Boxes game whenever boxes is called\n\nParameters are-;\n1) root_2(tk.Frame)\n2) app(tk.Tk)"""
            
            global broot
            
            if broot != 0:
                # If user is entering this app again

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
            
            # Making all the dots in the canvas
            for j in range(5):
            
                for i in range(5):
            
                    self.head.create_oval((40*i)+10, (40*j)+10, (40*i)+14, (40*j)+14, fill = 'green', tag = 'anoval')

            self.head.bind('<Button>', self.heady)
            
            tk.Button(self.root, text = "Return to Home Screen", command = self.switch, font = myfont).grid(sticky = 'nw', row = 2, column = 0)
            tk.Button(self.root, text = "Quit", command = lambda : rating(app, self.root), font = myfont).grid(sticky = 'nw', row = 3, column = 0)
            
            self.root.grid()

        def switch(self):
            """Switches between root, root_2\n\nParameters are - None"""
            
            global broot
            
            broot = self.root
            
            root_2.grid()
            
            app.title('Home screen')
            app.configure(bg = root_2.cget('bg'))
            
            self.root.grid_remove()

        def nbm(self, coords, vorh, step):
            """Returns Whose turn it is and if box is created"""
            
            # Coords of the line
            x1, y1, x2, y2 = coords
            a = []
            b = []

            if vorh == 'vertical':
                # If line is vertical

                xm = (x1+x2)/2
                ym = (y1+y2)/2
                bm = [xm - 20, ym]
                am = [xm + 20, ym]
            
            elif vorh == 'horizontal':
                # If line is horizontal

                xm = (x1+x2)/2
                ym = (y1+y2)/2
                bm = [xm, ym - 20]
                am = [xm, ym + 20]
            
            # Checking if a box is made up/right side
            for loop1 in self.head.find_enclosed(bm[0]-40, bm[1]-40, bm[0]+40, bm[1]+40):
                if loop1 > 25:
                    a.append(loop1)
            
            # Checking if a box is made left/down side
            for loop2 in self.head.find_enclosed(am[0]-40, am[1]-40, am[0]+40, am[1]+40):
                if loop2 > 25:
                    b.append(loop2)
            
            if len(a) == 4:
                # If box is made
                if step == 0:
                    self.head.create_text(bm[0], bm[1], text = "Player1", fill = 'red')
            
                    self.p1v += 1
                    self.p1.configure(text = "Player1 - {}".format(self.p1v))
            
                else:
                    self.p2v += 1
                    self.p2.configure(text = "Player2 - {}".format(self.p2v))
            
                    self.head.create_text(bm[0], bm[1], text = "Player2", fill = 'blue')
            
            if len(b) == 4:
                # If box is made

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
            """\n\nParameters are -;\n1) event (tk.Event)"""
            
            # x, y axis of the nearest dot to the cursor
            x = (event.x-10)%40
            y = (event.y-10)%40
            
            # Where we should draw the line
            exx = event.x-x
            eyy = event.y-y
            
            # Finding all lines
            tagid = self.head.find_withtag('line')
            # Finding closest item to x, y axis
            ftc = self.head.find_closest(event.x, event.y)
            
            # if out of bounds
            if event.x < 10 or event.y < 10 or event.x > 180 or event.y > 180: return
            
            # If closest item not a line
            elif ftc[0] not in tagid:

                if x <= 8:
                    # If user wanted vertical line
                    
                    if y <= 8: return
                    
                    vh = 'vertical'
                    
                    # if it is blue's turn
                    if self.counter == 1: li = self.head.create_line(exx, eyy, exx, eyy+40, fill = 'blue', tags = 'line')
                    
                    # If it is red's turn
                    else: li = self.head.create_line(exx, eyy, exx, eyy+40, fill = 'red', tags = 'line')
                    
                    self.counter = self.nbm(self.head.coords(li), vh, self.counter)
                
                elif y <= 8:
                    # If user wants a horizontal line
                    vh = 'horizontal'
                    
                    # Creates the line
                    if self.counter == 1: li = self.head.create_line(exx, eyy, exx+40, eyy, fill = 'blue', tags = 'line')
                    else: li = self.head.create_line(exx, eyy, exx+40, eyy, fill = 'red', tags = 'line')
                    
                    self.counter = self.nbm(self.head.coords(li), vh, self.counter)

    # Calculator game
    class calculator:
        """Calculator App\n\nParameters are -;\n1) root_2, app"""

        global calroot
        
        def __init__(self, app, root_2):
            """Starts the calculator\n\nParameters are -;\n1) root_2, app"""

            global calroot
            
            if calroot != 0:
                # If user is opening not 1 time
                
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
            self.keys = {'clear' : None, 'del' : None, 'equal' : None, 'asterisk' : '×', 'slash' : '÷', 'percent' : '%', 'aiicircum' : '^'}
            self.key = {'*' : '×', '/' : '÷', '/100' : '%', '**' : '^'}
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
            tk.Button(self.root, text = " × ", bg = '#00ffff', font = myfont, command = lambda : self.number('*'), borderwidth = 5).grid(row = 2, column = 3, sticky = 'nsew')
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
            tk.Button(self.root, text = "Quit", command = lambda : rating(app, self.root), font = myfont, bg = '#000fff000', borderwidth = 5).grid(row = 4, column = 6, sticky = 'nsew')
            
            self.root.grid()
        
        def number(self, no, event = None):
            """Calculates the answer\n\nParameters are -;\n1) no(str or int)\n2) event(None or tk.Event) = None"""

            if self.answer.get() == "": self.ans = 1
            
            if self.ans == 0:
                # If user wants it to reset
                
                self.cal.set("")
                self.answer.delete(0, 'end')
                
                self.ans = 1
                
                self.number(no, event)
                return

            if no == 'equal':
                # If user wants answer

                a = self.cal.get()
                self.answer.delete(0, 'end')
                
                # Tries finding the answer
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
                    # If there is an error

                    self.answer.insert(0, 'Error')
                    self.cal.set("")
                    self.ans = 0
                
                return
            
            elif no == 'clear':
                # If user wants it cleared

                if self.sc == 1:
                    self.sc = 0
                
                self.cal.set("")
                self.answer.delete(0, 'end')
                
                return
            
            elif no == 'del':
                # If user wants the last char to be removed

                la = len(self.answer.get())
                
                self.answer.delete(la-1)
                
                c = list(self.cal.get())
                c = c[0:-1]
                b = ""
                
                for ele in c:
                    b += ele
                
                self.cal.set(b)
                
                d = list(self.answer.get())
                
                if '√' not in d:
                    self.sc = 0
                
                return
            
            elif no == 'pi':
                # If user wants pi

                self.answer.insert('end', 'π')
                self.cal.set(self.cal.get()+str(math.pi))
                
                return
            
            elif no == 'sqrt':
                # If user wants square root

                self.answer.insert('end', '√')
                self.sc = 1
                
                return
            
            elif no == 'fact':
                # if user wants factorial

                self.answer.delete(0, 'end')
                self.answer.insert('end', math.factorial(eval(self.cal.get())))
                self.cal.set(math.factorial(eval(self.cal.get())))
                
                return
            
            elif no == 'expo':
                # If user wants exponent

                self.cal.set(self.cal.get()+'e')
                self.answer.insert('end', 'E')
                
                return
            
            elif no == 'e':
                # If user wants e

                self.answer.insert('end', 'e')
                self.cal.set(self.cal.get()+str(math.e))
                
                return
            
            elif event:
                # If user typed something

                if event.self.keysym == 'BackSpace' and self.ans2 == 1:
                    # If user pressed backspace
                    self.answer.delete(0, 'end')
                    self.ans2 = 0
                    self.cal.set("")
                    return
                
                elif event.self.keysym == 'Return':
                    # If user pressed return/enter
                    self.number('equal')
                
                if event.self.keysym in self.keys.keys():
                    # If user pressed /, *, -, +, etc.
                    
                    if self.keys[event.self.keysym] == None:
                        # If it is a special key

                        self.answ3 = list(self.keys.keys())
                
                        if self.answ3.index(event.self.keysym) == 2:
                
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
                
                        if event.self.keysym == 'asterisk': ek = '*'
                        elif event.self.keysym == 'slash': ek = '/'
                        elif event.self.keysym == 'percent': ek = '/100'
                        elif event.self.keysym == 'aself.sciicircum': ek = '**'
                
                        self.cal.set(self.cal.get()+ek)
                
                        try: a = list(self.answer.get()).index(ek)
                        except: return
                
                        self.answer.delete(a)
                        vallist, self.keylist = list(self.keys.values()), list(self.keys.keys())
                        self.answer.insert('end', vallist[self.keylist.index(event.self.keysym)])
                
                if self.answer.get() != "":
                    
                    b = list(self.answer.get())
                    b = b[len(b)-1]
                    
                    if b == '!':
                        self.answer.delete(0, 'end')
                        self.answer.insert('end', math.factorial(eval(self.cal.get())))
                        self.cal.set(math.factorial(eval(self.cal.get())))
                    elif b in self.keys3.keys(): self.cal.set(self.cal.get()+self.keys3[b]) 
                    elif b == event.self.keysym or event.self.keysym in self.key2: self.cal.set(self.cal.get()+b)
                
                return
            
            elif no in self.keys:
                pass
            
            self.cal.set(self.cal.get()+no)
            
            if no in self.key.keys(): self.answer.insert('end', self.key[no])
            else: self.answer.insert('end', no)
        
        def switch(self):
            """Switches between root_2, root\n\nParameters are - None"""
            
            global calroot
            
            calroot = self.root
            
            root_2.grid()
            app.title('Home screen')
            app.configure(bg = root_2.cget('bg'))
            
            self.root.grid_remove()

    # The text editor
    class aytexteditor:
        """AYTE(Advaith Yellai's Text Editor)\n\nParamters are-;\n1) App(tk.Tk)\n2) Root_2(tk.Frame)"""
        
        global ayroot

        def __init__(self, app, root_2):
            """Starts out AYTE\n\nParamters are-;\n1) App(tk.Tk)\n2) Root_2(tk.Frame)"""
            
            global ayroot
            
            app.title('Default.txt - AY text editor(AYTE)')
            
            app.bind('<Control Key>', self.binding)
            app.bind('<Control Shift Key>', self.bind2)
            
            root_2.grid_forget()
            
            if ayroot != 0:
                self.root = ayroot
                self.root.grid()
                root_2.grid_remove()
                return
            
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
            self.men.add_command(label = 'Exit ', command = lambda : rating(app, self.root), accelerator = "(Ctrl + W)")
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
            """Switches between root, root_2\n\nParameters are - None"""

            global ayroot
            
            ayroot = self.root
            
            root_2.grid()
            
            app.title('Home screen')
            
            app.configure(bg = root_2.cget('bg'))
            
            app.unbind('<Control Key>')
            app.unbind('<Control Shift Key>')
            
            self.root.grid_remove()

        def select_all(self):
            """Selects all\n\nParameters are - None"""
            
            self.editor.tag_add('sel', "1.0", 'end')
            self.editor.mark_set('insert', "1.0")
            self.editor.see('insert')

        def copy(self, e = None):
            """Copys selected text\n\nParameters are -;\n1) e(None or tk.Event) = None"""
            
            if e:
                # If user did Control C
                self.selected = app.clipboard_get()
            
            elif self.editor.selection_get():
                # If user went to menu and did it
                app.clipboard_clear()
                self.selected = self.editor.get("sel.first", "sel.last")
                app.clipboard_append(self.selected)
        def cut(self, e = None):
            """Cuts selected text\n\nParameters are -;\n1) e(None or tk.Event) = None"""
            
            if e:
                # If user did control + x
                self.selected = app.clipboard_get()
            
            elif self.editor.selection_get():
                # If user went to Menu and did it

                app.clipboard_clear()
                self.selected = self.editor.get("sel.first", "sel.last")
                app.clipboard_append(self.selected)
                self.editor.delete("sel.first", "sel.last")
        def paste(self, e = None):
            """Pastes whatever is on clipboard\n\nParameters are-;\n1) e(None or tk.Event) = None"""
            
            if e is None and self.selected:
                # if user went to menu and did it (Control + V is unnecesery because windows already pastes it)
                
                text = self.editor.index('insert')
                self.editor.insert(text, app.clipboard_get())

        def new_file(self):
            """Opens New file\n\nParameters are - None"""

            app.title("New file - AY text self.editor(AYTE) ")
            self.editor.delete(1.0, 'end')
        def open_file(self):
            """Opens file\n\nParameters are - None"""

            self.editor.delete(1.0, 'end')
            
            # Asks user for the file name for opening
            # Initialdir is which folder should be default folder
            # Title is what title should be given
            # File types are for helping the user filter out the files
            opened = filedialog.askopenfile(initialdir = "D:\\Advaith\\Code\\class\\pycode", title = 'Open File', filetypes = (("All Files", "*.*"), ("HTML Files", "*.html"), ("Python Files", "*.py"), ("Arduino Files", "*.ino"), ("Text files", "*.txt")))
            
            if opened is None: return # If user did not open

            self.name = opened
            app.title("{} - AY text self.editor(AYTE)".format(self.name.name))
            
            # Opens file and reads all the lines and writes them in AYTE
            fil = open(self.name.self.name, "r")
            self.editor.insert(1.0, fil.read())
            fil.close()

        def save_file(self):
            """Saves the file\n\nParameters are - None"""

            if not self.name:
                # If user did not open a file or asked for a new file

                self.save_as_file()
                return
            
            # Opens file and reads everything in AYTE and writes it to the file
            fil2 = open(self.name.self.name, "w")
            fil2.writelines(self.editor.get(1.0, 'end'))
            fil2.close()
        def save_as_file(self):
            """Asks The name of the file\n\nParameters are - None"""

            # Asks user name for the file name
            opened = filedialog.asksaveasfile(defaultextension = "*.*", filetypes = (("All Files", "*.*"), ("Python Files", "*.py"), ("Text Files", "*.txt"), ("Arduino Files", "*.ino"), ("HTML Files", "*.html")))
            
            if opened is None: return # If user did not open any file
            
            self.name = opened
            app.title("{} - AY text self.editor(AYTE)".format(self.name))
            
            # Saves the file
            self.save_file()

        def fonter(self, ty, ty2):
            """Changes the font to Algerian, Underline, Times, etc.\n\nParameters are -;\n1) ty (Algerian, Times, etc.)\n2) ty2 (family, underline, etc.)"""

            try:
                # Tries doing this

                if self.editor.selection_get():
                    # If user selected any text

                    # Gets font of the editor
                    myfont = font.Font(self.editor, self.editor.cget('font'))
                
                    if myfont: myfont[ty2] = ty
                    else: myfont = font.Font(self.editor, ty2 = ty)
                
                    # Makes a tag of myfont's font
                    self.editor.tag_configure(ty, font = myfont)
                    # Gets all the tag names of the first selectied item
                    bold = self.editor.tag_names("sel.first")
                
                    if ty not in bold: self.editor.tag_add(ty, "sel.first", "sel.last")
                    # add tag if the tag is not already there
                    else: self.editor.tag_remove(ty, "sel.first", "sel.last")
                    # remove tag if the tag is already there

            except: pass # If it has an error pass
        def colchange(self, e):
            """Changes fg, bg, etc.\n\nParameters are -;\n1) e (tk.Event)"""

            color = colorchooser.askcolor()[1]
            
            # If user didn't choose any colour
            if color == None: return
            
            if e == 1:
            
                try:
                    # Checks if anything is selected
                    if self.editor.selection_get(): pass
                
                except: return
                
                # Does the samething as fonter but for fg color
                myfont = font.Font(self.editor, self.editor.cget('font'))
                self.editor.tag_configure("colour", font = myfont, foreground = color)
                bold = self.editor.tag_names("sel.first")
                
                if "colour" not in bold: self.editor.tag_add("colour", "sel.first", "sel.last")
                else: self.editor.tag_remove("colour", "sel.first", "sel.last")
            
            elif e == 2: self.editor.configure(fg = color)
            # Changes fg of editor

            elif e == 3: self.editor.configure(bg = color)
            # Changes bg of editor

            elif e == 4: self.editor.configure(selectforeground = color)
            # Changes select(not selected) color

            elif e == 6:
                # Changes selected bg(highlight color)

                # Same thing but for bg instead of fg

                try: self.editor.selection_get()
                except: return
                
                myfont = font.Font(self.editor, self.editor.cget('font'))
                self.editor.tag_configure("colour", font = myfont, background = color)
                bold = self.editor.tag_names("sel.first")
                
                if "colour" not in bold: self.editor.tag_add("colour", "sel.first", "sel.last")
                else: self.editor.tag_remove("colour", "sel.first", "sel.last")

            # Changes select(not selected) bg
            else: self.editor.configure(selectbackground = color)

        def terminal(self):
            """Opens terminal\n\nParameters are - None"""
            
            if self.name != 0: os.system('cmd')
            
            else: os.system('cmd')

        def binding(self, e):
            """Binds and goes to the function\n\nParameters are -;\n1) e(tk.Event)"""
            e = e.keysym
            
            # Checks which key is pressed (ex. Ctrl - |"n"|)

            if e == 'n': self.new_file()
            elif e == 's': self.save_file()
            elif e == 'o': self.open_file()
            elif e == 'w': rating(app, self.root)
            elif e == 'z': self.editor.edit_undo()
            elif e == 'y': self.editor.edit_redo()
            elif e == 'c': self.editor.edit_redo()
            elif e == 'x': self.editor.edit_redo()
            elif e == 'v': self.editor.edit_redo()
            elif e == 'b': self.editor.edit_redo()
            elif e == 'u': self.editor.edit_redo()
            elif e == 'h': self.editor.edit_redo()
            elif e == 't': self.editor.edit_redo()
            elif e == 'quoteleft': self.editor.edit_redo()
        def bind2(self, e):
            """Does the samething as binding but has Shift involved also\n\nParameters are -;\n1) e (tk.Event)"""
            
            # Does samething as binding but with Shift also

            e = e.keysym
            
            if e == 'S': self.save_as_file()
            elif e == 'I': self.fonter('italic', "slant")
            elif e == 'O': self.fonter(True, "overstrike")
            elif e == 'A': self.fonter('Algerian', "family")
            elif e == 'C': self.fonter('Comic Sans', "family")
            elif e == 'W': self.switch()

        def change_font(self, e):
            """Changes font siZE\n\nParameters are -;\n\n1) e (tk.Event)"""
            

            try:
                if self.editor.selection_get(): pass
            except: return
            
            myfont = font.Font(self.editor, self.editor.cget('font'))
            myfont['size'] = self.fs.get()
            
            self.editor.tag_configure('mf', font = myfont)
            self.editor.tag_add('mf', "sel.first", "sel.last")

        def allign(self, pos):
            """Alligns either Left, Right or Center\n\nParameters are -;\n1) pos (String)"""
            
            position = int(float(self.editor.index('insert')))
            
            self.editor.tag_configure('just', justify = pos)
            self.editor.tag_add('just', float(position))

    # The Ping Pong Game
    class pingpong:
        """Ping Pong (Table Tennis) Game \n\nParameters are-;\n1)root_2 (tk.Frame)\n app (tk.Tk)"""

        global proot

        def __init__(self, root_2, app):
            """__init__ for Ping Pong game\n\nParameters are-;\n1)root_2 (tk.Frame)\n app (tk.Tk)"""

            global proot

            root_2.grid_remove()

            # Changes Geometry
            app.geometry('575x575+550+100')

            if proot:
                # If player is entering once more
                self.f = proot[1]
                self.f.grid()
                return

            self.root = tk.Canvas(app, bg = '#000fff000')

            self.f = tk.Frame(app)
            self.f.grid()

            # Makes a Label saying Ping Pong and asks user if user wants singleplayer or multiplayer
            tk.Label(self.f, text = "Ping Pong", font = ('Arial black', 30, 'bold'), bg = "gold", relief = 'solid').grid(row = 0, column = 0, sticky = 'ew')
            tk.Button(self.f, text = "Single Player with CPU", font = ('Elephant', 15, 'bold'), bg = "red", fg = "#d3d3d3", command = lambda : self.game_start(False)).grid(row = 1, column = 0)
            tk.Button(self.f, text = "Multiplayer", font = ('Elephant', 15, 'bold'), bg = "blue", fg = '#d3d3d3', command = lambda : self.game_start(True)).grid(row = 2, column = 0, sticky = 'ew')

            app.mainloop()

        def game_start(self, cop):
            """Starts out the game\n\nParameters are -;\n1) cop (bool)"""
            global proot
            
            # Sets focus to root because without it there is a glitch
            self.root.focus_set()

            if proot:
                # If user played before
                
                self.root = proot[0]
                
                # Binds everything
                app.bind('<Up>', self.move_up)
                app.bind('<w>', self.move_up)
                app.bind('<Control-w>', self.move_up)
                app.bind('<s>', self.move_down)
                app.bind('<Down>', self.move_down)
                app.bind('<space>', self.move_up)
                
                return

            # Makes cop global
            self.cop = cop

            # Changes height, width of root
            self.root.configure(width = 575, height = 575)

            self.f.grid_remove()
            self.root.grid()

            # Some Global Variables
            self.stop = False

            # Making the Ping Pong Bats
            self.blue = self.root.create_rectangle(0, 155, 10, 245, fill = 'blue')
            self.red = self.root.create_rectangle(390, 155, 400, 245, fill = 'red')

            # After 1 second(1000 milliseconds) move the ball
            if not exit_now: self.root.after(1000, self.motion, 'red')
            
            # If it is singleplayer 
            if not cop and not exit_now: self.root.after(100, self.checker)

            # Creates the center line and circle
            self.root.create_oval(150, 150, 250, 250)
            self.root.create_line(200, 0, 200, 400)

            # Creates the ping pong ball
            self.pong = self.root.create_oval(190, 190, 210, 210, fill = 'white')

            # Binds for red
            app.bind('<Up>', self.move_up)
            app.bind('<Down>', self.move_down)

            # Creating rectangles because there is no bg :C
            self.root.create_rectangle(0, 400, 400, 450, fill = 'red')
            self.root.create_rectangle(0, 450, 400, 500, fill = 'blue')

            # Score [0] is red, [1] is blue
            self.score = [0, 0]

            # Creating scoreboard
            self.rscore = self.root.create_text(200, 423, text = "Player 1 - 0", font = ('Palatino', 15, 'bold'))

            if cop:
                # If it is Multiplayer

                # Player 2 (blue)
                self.bscore = self.root.create_text(200, 473, text = "Player 2 - 0", font = ('Palatino', 15, 'bold'))
                # Binding only
                app.bind('<w>', self.move_up)
                app.bind('<s>', self.move_down)
            
            # If it is singleplayer
            else: self.bscore = self.root.create_text(200, 473, text = "CPU - 0", font = ('Palatino', 15, 'bold'))

            # Telling user the shortcuts
            self.root.create_text(200, 538, text = "Space - Pause / Play\nUp / Down - Moving Player 1\nW / S - Moving Player 2", fill = 'black', font = ("Arial", 15))

            # Making a font
            myfont = font.Font(self.root, family = "Algerian", slant = 'italic', size = 15)

            # Creating rectangles because no bg again :C
            self.root.create_rectangle(400, 0, 575, 575, fill = '#e0ba87')
            self.root.create_rectangle(400, 0, 575, 100, fill = 'saddle brown')
            self.root.create_rectangle(400, 100, 575, 200, fill = 'silver')
            self.root.create_rectangle(400, 200, 575, 300, fill = 'gold')
            self.root.create_rectangle(400, 300, 575, 400, fill = 'white')

            # Making Buttons
            self.root.create_text(483, 50, text = "Quit", font = myfont)
            self.root.create_text(483, 150, text = "Return to \nHome Screen", font = myfont, justify = 'center')
            self.root.create_text(483, 250, text = "Return to \nApp Screen", font = myfont, justify = 'center')
            self.root.create_text(483, 350, text = "Replay", font = myfont, justify = 'center')
            
            # Creating lines
            self.root.create_line(400, 100, 575, 100, dash = (4, 2))
            self.root.create_line(400, 200, 575, 200, dash = (4, 2))
            self.root.create_line(400, 300, 575, 300, dash = (4, 2))
            self.root.create_line(400, 400, 575, 400, dash = (4, 2))

            # Binds for B1 (Button 1 - Left click)
            self.root.bind('<Button-1>', self.click)
            
            # More bindings
            app.bind('<Control_L> <w>', lambda e : rating(app, self.root))
            app.bind('<space>', self.move_up)

        def move_up(self, event):
            """Moves blue/red UP\n\nParameters are -;\n1) event (tk.Event)"""
            
            # If user paused it and is not unpausing it
            if self.stop and (not (event.keysym == 'space')): return
            
            # If user presed 'up' key
            if event == 'up':
                # moving blue up if it is CPU
                coords = self.root.coords(self.blue)
                
                # If it is @ 0
                if coords[1] == 0: return
                
                self.root.coords(self.blue, coords[0], coords[1]-20, coords[2], coords[3]-20)
                
                return

            # If user is pausing it
            elif event.keysym == 'space':
                # If user is (un)pausing it
                
                if self.stop:
                    # If user is unpausing it
                    self.stop = False

                    if not self.cop: self.checker()
                    
                    self.motion(starter, inc)
                    
                    return
                
                self.stop = True
                return
            
            
            elif event.keysym == 'Up':
                # Moving red up if user pressed up key

                coords = self.root.coords(self.red)
                
                if coords[1] == 0: return
                
                self.root.coords(self.red, coords[0], coords[1]-20, coords[2], coords[3]-20)
            
            else:
                # If user pressed W moving blue up

                coords = self.root.coords(self.blue)
                
                if coords[1] == 0: return
                
                self.root.coords(self.blue, coords[0], coords[1]-20, coords[2], coords[3]-20)
        def move_down(self, event):
            """Moves blue/red DOWN\n\nParameters are -;\n1) event (tk.Event)"""

            # Does the same thing as move_up but instead of up it does down
            if event is None:
                self.f.grid_remove()
                self.root.grid()
                return

            if self.stop:
                return
            
            if event == 'down':
                coords = self.root.coords(self.blue)
                if coords[1] == 400: return
                self.root.coords(self.blue, coords[0], coords[1]+20, coords[2], coords[3]+20)
                return


            if event.keysym == 'Down':
                coords = self.root.coords(self.red)
                if coords[3] == 400: return
                self.root.coords(self.red, coords[0], coords[1]+20, coords[2], coords[3]+20)
            
            else:
                coords = self.root.coords(self.blue)
                if coords[1] == 400: return
                self.root.coords(self.blue, coords[0], coords[1]+20, coords[2], coords[3]+20)

        def motion(self, start, increase = 0):
            """Moves The Ping Pong Ball\n\nParameters are -;\n1) start (string)\n2) increase (integer) = 0"""

            if exit_now: return

            if self.stop:
                # If it has to stop
                global inc, starter
                
                inc = increase
                starter = start
                
                return

            coords = self.root.coords(self.pong)
            
            if coords[2] >= 400 or coords[0] <= 0:
                self.update()
                return
            
            elif coords[3] >= 400 or coords[1] <= 0: increase = 0-increase

            if start == 'red':
                # If it needs to move towards red

                # Takes coords of red
                self.redcoords = self.root.coords(self.red)
            
                if coords[2] == 390:
                    # if it is on the same y coordinate as red

                    if coords[1] > self.redcoords[1] and coords[1] < self.redcoords[3]:
                        # If it collided with red

                        raverage = (self.redcoords[1]+self.redcoords[3])/2
                        caverage = (coords[1]+coords[3])/2
            
                        if caverage != raverage:
                            # If it did not hit at the center of red
                            self.root.after(100, self.motion, 'self.blue', (caverage-raverage)/8)
                            return
            
                        self.root.after(100, self.motion, 'self.blue')
                        return
            
                # move it
                self.root.coords(self.pong, coords[0]+20, coords[1]+increase, coords[2]+20, coords[3]+increase)
                self.root.after(55, self.motion, 'red', increase)
            
            else:
                # If it needs to move the ball towards blue
                # Does the same thing but with blue

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
            """Keeps checking if computer can be able to win/loose in singleplayer\n\nParameters are-;\n1) torf (bool) = False"""

            # If it needs to stop
            if self.stop: return

            # Gets coords of Ping Pong Ball and The blue racket
            redcoords = self.root.coords(self.blue)
            coords = self.root.coords(self.pong)
            
            opposite = False

            # Taking True/False of playing better or not
            updown = random.randrange(0, 2)
            
            if coords[0] == 50 and not torf:
                # 1 in 5 for loosing
                choice = random.randrange(0, 5)
                choices = [True, False, True, True, True, True]
                choice = choices[choice]

                opposite = not choice

            # Causing computer not to do one thing twice
            elif coords[0] == 30: torf = True

            if redcoords[1] < coords[1] and redcoords[3] > coords[1]: 
                # If computer is in correct allignment as the ball

                if not opposite:
                    # If computer should not do opposite

                    if (coords[1] + coords[3])/2 == (redcoords[1] + redcoords[3])/2 and coords[0] == 50:
                        # If it is right @ center move up or down so it is harder for user

                        if updown: self.move_up('up')
                        else: self.move_down('down')

                else:
                    if exit_now: return
                    self.move_down('down')
                    self.move_down('down')
                    self.move_down('down')
                    self.move_down('down')
            
            elif redcoords[1] > coords[1]:
                # If the ball is above the racket

                if not opposite:
                    # If user should do correct

                    self.move_up('up')
                    
                    if updown:
                        # For intelligence

                        self.move_up('up')
                        self.move_up('up')
                
                else:
                    # If user needs to loose
                    
                    # Computer goes down so computer can't hit

                    self.move_down('down')
                    self.move_down('down')
                    self.move_down('down')
                    self.move_down('down')

            elif redcoords[3] < coords[3]:
                # If the Ball is below the racket
                
                if not opposite:
                    # If it should do correctly

                    self.move_down('down')

                    if updown:
                        # For intelligence

                        self.move_down('down')
                        self.move_down('down')
                
                else:
                    # If it should do opposite

                    self.move_up('up')
                    
                    self.move_up('up')
                    self.move_up('up')
                    self.move_up('up')

            # If it should hit it
            if not opposite and not exit_now: self.root.after(55, self.checker, torf)
            
            # If it needs to miss
            elif not exit_now: self.root.after(750, self.checker, torf)

        def update(self):
            """Updates the Scoreboard\n\nParameters are - None"""

            # Gets the coords of the ball
            coords = self.root.coords(self.pong)
            
            if coords[0] <= 0:
                # If it is red's point

                # Adding one to red
                self.score[0] = self.score[0] + 1
            
                # Restarting everything
                self.root.coords(self.pong, 190, 190, 210, 210)
                self.root.coords(self.red, 390, 155, 400, 245)
                self.root.coords(self.blue, 0, 155, 10, 245)

                # Restart motion allso
                if not exit_now: self.root.after(1000, self.motion, 'red')
            
                # Updating score
                self.root.itemconfigure(self.rscore, text = "Player 1 - "+str(self.score[0]))
            
            else:
                # If it is Blue's point
                # Does the same thing but for blue

                self.score[1] = self.score[1] + 1
            
                self.root.coords(self.pong, 190, 190, 210, 210)
                self.root.coords(self.red, 390, 155, 400, 245)
                self.root.coords(self.blue, 0, 155, 10, 245)

                if not exit_now: self.root.after(1000, self.motion, 'blue')
                
                if self.cop: self.root.itemconfigure(self.bscore, text = "Player 2 - "+str(self.score[1]))
                else: self.root.itemconfigure(self.bscore, text = "CPU - "+str(self.score[1]))
            
        def switch(self, torf = 0):
            """Switches between root, root_2\n\nParameters are-;\n1) torf (integer) = 0"""

            global proot
            
            self.stop = True
            self.root.grid_remove()
            
            # If it is return to appscreen
            if torf: self.f.grid()
            
            # If it is return to home screen
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
            """Handles all the clicks Because it is a canvas\n\nParameters are -;\n1) event (tk.Event)"""

            # Gets x, y coordinates of the click
            x, y = event.x, event.y
            
            # If it is out of bounds do nothing
            if not (x > 400 and x < 500): return
            
            # If it is Quit
            elif y > 0 and y < 100: rating(app, self.root)
            
            # If it is Return to home screem
            elif y > 100 and y < 200: self.switch()

            # If it is return to app screen
            elif y > 200 and y < 300:
                tk.Button(self.f, text = "Continue Playing", font = ('Elephant', 15, 'bold'), bg = 'green', fg = "#d3d3d3", command = lambda : self.move_down(None)).grid(row = 3, column = 0, sticky = 'ew')
                self.switch(1)

            # If it is restart scores
            elif y > 300 and y < 400:
                self.score = [0, 0]
                
                self.root.itemconfigure(self.rscore, text = "Player 1 - 0")

                if self.cop: self.root.itemconfigure(self.bscore, text = "Player 2 - 0")
                else: self.root.itemconfigure(self.bscore, text = "CPU - 0")

    # !1 Quiz !!
    class quiz:
            """This app helps you in GK\n\nParameters are-;\n1) root_2\n2) app"""

            global qroot

            def __init__(self, root_2, app):
                """__init__ for Quiz app\n\nParameters are-;\n1) root_2\n2) app"""

                global qroot

                self.torf = False

                self.root = tk.Frame()
                root_2.grid_remove()

                self.st = datetime.now()
                self.root.after(840000, self.move, 5)

                app.geometry("300x450+650+200")
                app.title("!! Quiz !!")
                app.configure(bg = '#e0ba87')

                self.count = -1
                
                col = ['black', 'white', 'red', 'green', 'yellow', 'blue', 'brown', 'orange', 'pink', 'purple', 'grey']
                
                # Questions&answers for quiz
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
                            "Which district is\nPV Narasimha Rao From\nWrite full form" : "Karim nagar", \
                            "What is the most grown\ncrop by area" : "rice", \
                            "Which State has most\nsugar mills" : "Uttar Pradesh", \
                            "Where are the currency\nnotes printed in" : "Nasik", \
                            "Who invented 0\nClue :No space in\nhis name" : "Aryabhatta", \
                            "How many edges\ndoes a cube have" : "12", \
                            "How many milliseconds\nare there in an day" : "86400000", \
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
                    # Picks random 10 q&a

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
                self.bnex = tk.Button(self.root, text = "Start\nQuiz", bg = "gold", font = self.myfont, command = lambda : self.move("self.prev"))

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
                """Brain Of the Quiz\n\nParameters are -;\n1) wid(int, str, Nonetype) = None"""

                if (wid == 1 or wid == 10) and not self.torf:
                    # If quiz time is up or user submited

                    if "" in self.usersansw and not self.undo:
                        # If user left some answers

                        self.undo = True

                        self.eans.delete(0, 'end')
                        self.eans.insert(0, "You left some qs")
                        return

                    # Cancels the timers
                    self.root.after_cancel(540000)
                    self.root.after_cancel(60000)

                    self.usersansw[-1] = self.eans.get()
                    
                    self.replay['state'] = "normal"

                    score = 0

                    print("Wrongs -;\n")

                    for no in range(0, len(self.usersansw)):
                        # Runs a loop for checking answers

                        # If user left it
                        if self.usersansw[no] is None: print(self.questions[no], "\n"+self.actualans[no], "\n")
                        
                        # If it is correct
                        elif self.usersansw[no].lower() == self.actualans[no].lower(): score += 1
                        
                        # If it is wrong
                        else: print(self.questions[no], "\n"+self.actualans[no], "\n")
                    
                    # If it is all correct
                    if round((score/(no+1))*100, 2) == 100: print(None)

                    self.torf = True
                    self.eans.delete(0, 'end')
                    if wid == 10: self.eans.insert(0, "Time is up")
                    
                    self.eans['state'] = 'disabled'
                    self.ques['text'] = "{}/{}, {}%\n{}".format(score, no+1, round((score/(no+1))*100, 2), datetime.now()-self.st)

                elif wid == 5:
                    # If one minute is left for the quiz to end

                    self.bnex['text'] = self.bnex['text'] + "\nLess than 1 min left"

                    self.root.after(60000, self.move, 10)

                elif not wid:
                    # If it needs to move to the previous question
                    
                    # If it is in the begining
                    if self.count <= 0: return

                    elif self.count == len(self.questions)-1:
                        # If it came from the end

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
                    # If it needs to move to the next question

                    # If it is in the end
                    if self.count >= len(self.questions)-1: return
                    
                    elif self.count+1 == len(self.questions)-1:
                        # If it is in the end

                        self.bnex['text'] = "Submit\nAnswers"
                        self.bnex['command'] = lambda : self.move(1)
                        
                        self.eans.unbind('<Return>')
                        self.eans.bind('<Return>', lambda e : self.move(1))
                    
                    # If it came from the start
                    elif self.count == -1: self.bnex['text'] = "Next\nQuestion"

                    self.count += 1
                    
                    # If it did not come from the start
                    if self.count != 0: self.usersansw[self.count-1] = self.eans.get()

                    self.ques['text'] = self.questions[self.count]
                    self.eans.delete(0, 'end')
                    
                    # If it has been used before put up the word
                    if self.usersansw[self.count]: self.eans.insert(0, self.usersansw[self.count])

            def switch(self, re = False):
                """It switches between appscreen and homescreen\n\nParameters are\n1) re (bool) = False"""
                global qroot
                
                if re:
                    self.__init__(self.root, app)
                    return

                # Saves the frame and removes grid and grids root_2
                # changes background too
                
                qroot = self.root
                
                root_2.grid()
                
                app.title('Home Screen')
                app.configure(bg = root_2.cget('bg'))
                
                self.root.grid_remove()

    # Excel Spreadsheet
    class excel:
        """Excel spreadsheet\n\nParameters are-;\n1) root_2 (tk.Frame)\n2) app (tk.Tk)"""

        global eroot

        def __init__(self, root_2, app):
            """Opens default spreadsheet, __init__ for excel\n\nParameters are-;\n1) root_2 (tk.Frame)\n2) app (tk.Tk)"""
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
            """Moves the data up/down\n\nParameters are-;\n1) updown ("up" or "down")"""
            
            if updown == 'up':
                # If it should move it up

                selected = self.tree.selection()

                for ele in selected:
                    self.tree.move(ele, "", self.tree.index(ele)-1)
            
            else:
                # If it should move it down

                selected = self.tree.selection()

                for ele in reversed(selected):
                    self.tree.move(ele, "", self.tree.index(ele)+1)

        def addata(self):
            """Adds data from name, dob, etc. to TreeVeiw\n\nParameters are - None"""

            entry = (self.name.get(), self.dob.get(), self.rating.get(), self.work.get())

            self.name.delete(0, 'end')
            self.dob.delete(0, 'end')
            self.rating.delete(0, 'end')
            self.work.delete(0, 'end')

            if entry in self.data: 
                # If it is already there the say Already there

                self.name.insert('end', "Already")
                self.dob.insert('end', "There")
                self.root.after(2000, self.name.delete, 0, 'end')
                self.root.after(2000, self.dob.delete, 0, 'end')
                
                return
            
            if self.count%2 == 0: self.tree.insert("", 'end', self.count, values = entry, tags = ('evenrow', ))
            else: self.tree.insert("", 'end', self.count, values = entry, tags = ('oddrow', ))
            # If it should put gold or silver as bg

            self.count += 1

            self.consdata.append(entry)
            self.data.append(entry)

        def clear(self, torf = False):
            """If it should clear n number of things\n\nParameters are -;\n1) torf (Bool) = False"""
            
            if torf:
                # If it is "clear selected"
                a = self.tree.selection()
                
                for ele in a:
                    # Runs a loop through selected items

                    self.tree.delete(ele)
                    self.data.remove(self.consdata[int(ele)])
                
                return

            self.data = []

            for child in self.tree.get_children():
                # Runs a loopthrough all items

                self.tree.delete(child)

        def get_selected(self):
            """Gets selected items to the entries\n\nParameters are - None"""

            selected = self.tree.focus()

            self.name.delete(0, 'end')
            self.dob.delete(0, 'end')
            self.work.delete(0, 'end')
            self.rating.delete(0, 'end')

            value = self.tree.item(selected, 'value')
            # Gets selected['value']
            
            self.name.insert('end', value[0])
            self.dob.insert('end', value[1])
            self.work.insert('end', value[3])
            self.rating.insert('end', value[2])

        def modify(self):
            """Modifies selected item\n\nParameters are - None"""
            
            selected = self.tree.focus()

            self.tree.item(selected, text = "", values = (self.name.get(), self.dob.get(), self.rating.get(), self.work.get()))

            self.name.delete(0, 'end')
            self.dob.delete(0, 'end')
            self.work.delete(0, 'end')
            self.rating.delete(0, 'end')

        def switch(self):
                """Switches between self.root and root_2\n\nParameters are - None"""
                global eroot
                
                # makes a global variable the self.root and ungrids it. Grids the home screen
                eroot = self.root
                root_2.grid()
                
                app.title('Home screen')
                app.configure(bg = root_2.cget('bg'))
                
                self.root.grid_remove()

    # Asteroids (an arcade game)
    class Asteroids:
        """Asteroids(An arcade Game) this game use to played in 1950s, I guess...\n\nParameters are -;\n1) Root_2 (tk.Frame)\n2) app (tk.Tk)"""
        global astroot
            
        def __init__(self, root_2, app):
            """This is the __init__ of Asteroids(an arcade game)\n\nParameters are -;\n1) Root_2 (tk.Frame)\n2) app (tk.Tk)"""

            global astroot

            app.bind('<f>', self.switch)
            app.bind('<Key>', self.pushed)
            app.bind('<1>', lambda e : self.pushed("space"))
            app.bind("<Motion>", self.move)
            app.bind("<Control_L> <w>", lambda e : app.destroy())

            self.no0 = app.after(15000, self.move, "Random")
            self.no1 = app.after(3000, self.attack, True, 3000)
            
            app.title('Asteroids (An arcade game)')
            app.state('zoomed')

            root_2.grid_remove()

            self.root = tk.Canvas(app, bg = 'black', width = 1550, height = 860, cursor = 'none')

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
            self.stop = False
            self.once = False

            self.gwords = ["OOOOO00000ooooofffff", "NOICE SHOT", "KEEP IT UP", "sUpeR", "LET'S GOOOO", "PRO", "AMAZING", "HIT", "BROKEN!!!", "=D"]
            self.bwords = ["OOOOO00000ooooofffff", "JUST MISS!!!", "HARD LUCK!!!", "DON'T KEEP IT UP", "noT sUpER", "LET'S NOT GOOOO", "NOOB!!!", "UMMMM....", "D=", "LOST MY HOPE"]

            self.img = Image.open("images_for_gcpy\\rocket.png")
            self.img = self.img.resize((100, 100), Image.ANTIALIAS)
            self.image = ImageTk.PhotoImage(self.img.rotate(0))

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

            self.attr = False

            self.dtn = datetime.now()

            self.root.create_rectangle(0, 800, 1550, 860, fill = "#e0ba47")
            self.gbw = self.root.create_text(775, 830, font=("Algerian", 15, 'bold', 'italic'))

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
                        self.no4 = self.root.after(3000, self.root.delete, h1)
                        if self.hearts == 2: self.root.itemconfigure(self.heart3, fill = 'black')
                        elif self.hearts == 1: self.root.itemconfigure(self.heart2, fill = 'black')
                        elif self.hearts == 0: exit("Game Over")
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

            if e != 'space' and e != 10: e = e.keysym
            
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
                    self.root.tag_bind(self.besc, "<Button>", lambda e : app.quit())

            elif e == "Escape":
                self.root['cursor'] = 'none'
                
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
                self.no9 = self.root.after(900, self.pushed, 10, 900)

        def move(self, event):
            if self.stop: return

            if event == "Random":
                ran = random.randrange(0, 10)
                if ran == 0:
                    if self.hearts == 1: self.root.itemconfigure(self.heart2, fill = 'red')
                    elif self.hearts == 2: self.root.itemconfigure(self.heart3, fill = 'red')
                    self.hearts += 1
                    h1 = self.root.create_text(775, 100, text = "+1 Heart", fill = '#000fff000', font = ("Algerian", 15, 'bold'))
                    self.no10 = self.root.after(3000, self.root.delete, h1)
                self.no11 = self.root.after(15000, self.move, "Random")
                return
            app.unbind("<Motion>")
            x, y = event.x-775, event.y-400
            self.angle -= (y+x)/3
            self.angle %= 360
            if self.stop: return
            self.image = ImageTk.PhotoImage(self.img.rotate(self.angle))

            self.root.itemconfig(self.ball, image = self.image)
            app.event_generate('<Motion>', warp = True, x = 775, y = 400)
            app.bind("<Motion>", self.move)

        def switch(self, event = None):
            """Switches between root and root_2\n\nParameters are - None"""
            global astroot

            if event == 10:
                self.stopper = False
                return
            
            elif event:
                self.attr = not self.attr
                app.attributes('-fullscreen', self.attr)
                return
            
            # makes a global variable the self.root and ungrids it. Grids the home screen
            astroot = self.root
            root_2.grid()
            
            app.title('Home screen')
            app.configure(bg = root_2.cget('bg'))
            
            self.root.grid_remove()


    # If Control + W exit
    app.bind('<Control_L> <w>', lambda e : rating(app, root_2))
    app.geometry('1600x900+1+1')
    app.state('zoomed')

    # Root_2 the frame for all the apps faces
    root_2 = tk.Frame()
    root_2.grid()
    
    # Main font - Algerian, 12, 'bold
    myfont = font.Font(family="algerian", size=12, root = root_2, weight = "bold")

    # getting and resizing the images
    
    # Rubik's cube image
    p1 = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\rubikube.png") 
    # Resizing it
    p1 = p1.subsample(3, 3)
    
    # Hangman image
    p2 = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\hangman.png")
    p2 = p2.subsample(2, 2)
    
    # colors image
    p3 = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\coloursg.png")
    p3 = p3.subsample(5, 5)
    
    # Dinosaur image
    p4 = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\dinotrex.png")
    p4 = p4.subsample(3, 3)
    
    # Tic tac toe image
    p5 = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\x_and_o.png")
    p5 = p5.subsample(2, 2)
    
    # Dots and boxes image
    p6 = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\dot_box.png")
    p6 = p6.subsample(2, 2)
    
    # Clock image
    p7 = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\tick_toclock.png")
    p7 = p7.subsample(10, 10)
    
    # Calculator image
    p8 = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\calculator.png")
    p8 = p8.subsample(2, 2)
    
    # Book image
    p9 = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\AYtexteditor.png")
    p9 = p9.subsample(2, 2)

    # Table tennis image
    p10 = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\table_tennis.png")
    p10 = p10.subsample(2, 2)

    # Thinking emoji
    p11 = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\think_emoji.png")
    p11 = p11.subsample(2, 2)

    # Excel Logo
    p12 = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\xcelsheet.png")
    p12 = p12.subsample(2, 2)

    # Spaceship
    p13 = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\rocket.png")
    p13 = p13.subsample(10, 10)

    # Defining variables for reusing the same app frame
    cgroot = clroot = calroot = hroot = hgroot = colroot = broot = ayroot = kroot = exit_now = proot = qroot = eroot = astroot = 0
    count = tk.IntVar(app, 0)

    # The buttons, putting images, binding for changing color
    # Active background means when you click the button what color bg shoould be there

    # Cubegame button
    bc = tk.Button(root_2, image = p1, compound = 'top', text = "Cube", command = lambda : cubegame(root_2, app), font = myfont, relief = 'flat', activebackground = 'red')
    bc.image = p1
    bc.grid(row = 1, column = 1)
    bc.bind('<Enter>', colorchanger)
    bc.bind('<Leave>', colorchanger)
    
    # Hangman game button
    bh = tk.Button(root_2, image = p2, compound = 'top', text = "Hangman", command = lambda : hangmang(root_2, app), font = myfont, relief = 'flat', activebackground = 'blue')
    bh.image = p2
    bh.grid(row = 1, column = 2, sticky = 'nsew')
    bh.bind('<Enter>', colorchanger)
    bh.bind('<Leave>', colorchanger)

    # Excel Sheet button
    be = tk.Button(root_2, image = p12, compound = 'top', text = "Excel", command = lambda : excel(root_2, app), font = myfont, relief = 'flat', activebackground = '#1CE96B', bg = root_2['bg'])
    be.image = p12
    be.grid(row = 1, column = 4, sticky = 'nsw')
    be.bind('<Enter>', colorchanger)
    be.bind('<Leave>', colorchanger)
    
    # Colour game button
    bcg = tk.Button(root_2, image = p3, compound = 'top', text = "Color Game", command = lambda : cg(root_2, app), font = myfont, relief = 'flat', activebackground = 'yellow')
    bcg.image = p3
    bcg.grid(row = 2, column = 1, sticky = 'nsew')
    bcg.bind('<Enter>', colorchanger)
    bcg.bind('<Leave>', colorchanger)

    # Trex run game
    bt = tk.Button(root_2, image = p4, compound = 'top', text = "Trex Run", command = lambda : trr(root_2, app), font = myfont, relief = 'flat', activebackground = 'orange')
    bt.image = p4
    bt.grid(row = 2, column = 2, sticky = 'nsew')
    bt.bind('<Enter>', colorchanger)
    bt.bind('<Leave>', colorchanger)
    
    # Clock app
    bcl = tk.Button(root_2, image = p7, compound = 'top', text = "Clock App", command = lambda : clock(root_2, app), font = myfont, relief = 'flat', activebackground = 'brown')
    bcl.image = p7
    bcl.grid(row = 2, column = 3, sticky = 'nsew')
    bcl.bind('<Enter>', colorchanger)
    bcl.bind('<Leave>', colorchanger)

    # Asteroids(An arcade game)
    bast = tk.Button(root_2, image = p13, compound = 'top', text = "Asteroids", command = lambda : Asteroids(root_2, app), font = myfont, relief = 'flat', activebackground = "#0E131C")
    bast.image = p13
    bast.grid(row = 2, column = 4, sticky = 'nsw', ipadx = 30)
    bast.bind('<Enter>', colorchanger)
    bast.bind('<Leave>', colorchanger)

    # Dots and Boxes
    bb = tk.Button(root_2, image = p6, compound = 'top', text = "dots and boxes", command = lambda : boxes(root_2, app), font = myfont, relief = 'flat', activebackground = 'deep pink')
    bb.image = p6
    bb.grid(row = 3, column = 1, sticky = 'nsew')
    bb.bind('<Enter>', colorchanger)
    bb.bind('<Leave>', colorchanger)

    # X and O game
    bxo = tk.Button(root_2, image = p5, compound = 'top', text = "X and O", command = lambda : kacg(root_2, app), font = myfont, relief = 'flat', activebackground = 'green')
    bxo.image = p5
    bxo.grid(row = 3, column = 2, sticky = 'nsew')   
    bxo.bind('<Enter>', colorchanger)
    bxo.bind('<Leave>', colorchanger)
    
    # Calculator app
    bcal = tk.Button(root_2, image = p8, compound = 'top', text = "Calculator app", command = lambda : calculator(app, root_2), font = myfont, relief = 'flat', activebackground = 'magenta2')
    bcal.image = p8
    bcal.grid(row = 3, column = 3, sticky = 'nsew')
    bcal.bind('<Enter>', colorchanger)
    bcal.bind('<Leave>', colorchanger)

    # Text Editor
    bayte = tk.Button(root_2, image = p9, compound = 'top', text = "Text Editor", command = lambda : aytexteditor(app, root_2), font = myfont, relief = 'flat', activebackground = '#00ffff')
    bayte.image = p9
    bayte.grid(row = 4, column = 1, sticky = 'nsew')
    bayte.bind('<Enter>', colorchanger)
    bayte.bind('<Leave>', colorchanger)

    # Ping Png
    bpp = tk.Button(root_2, image = p10, compound = 'top', text = "Ping Pong", command = lambda : pingpong(root_2, app), font = myfont, relief = 'flat', activebackground = '#e0ba87')
    bpp.image = p10
    bpp.grid(row = 4, column = 2, sticky = 'nsew')
    bpp.bind('<Enter>', colorchanger)
    bpp.bind('<Leave>', colorchanger)
    
    bq = tk.Button(root_2, image = p11, compound = 'top', text = "Quiz!!!", command = lambda : quiz(root_2, app), font = myfont, relief = 'flat', activebackground = '#FFFF00')
    bq.image = p11
    bq.grid(row = 4, column = 3, sticky = 'nsew')
    bq.bind('<Enter>', colorchanger)
    bq.bind('<Leave>', colorchanger)

    # Opens the class happybirthday
    def opclass(e, a = 0):
        """Opens the class happybirthday"""
        if str(e) == "1":
            happybirthday(root_2, app)
            return
        chb.config(bg = 'black')
        opclass(1, a)
    
    # Drawing a cake for the image
    chb = tk.Canvas(root_2, width = 240, height = 180)
    chb.bind('<Button>', opclass)
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
    chb.grid(row = 1, column = 3, sticky = 'nsew')
    chb.bind('<Enter>', colorchanger)
    chb.bind('<Leave>', colorchanger)

    # Copyrighting and otherstuff
    tk.Label(root_2, text = "© 2020 Copyright", font = (11)).grid(row = 5, column = 4, pady = 70, sticky = 'n')
    tk.Label(root_2, text = "D:\\Advaith\\Code\\class\\pycode\\gamingconsole.py\nAll rights reserved\n version 1.3.2 full release 30-06-20", font = myfont).grid(row = 5, column = 4, sticky = 'n', pady = 100)

    # If user closed it
    app.bind('<Destroy>', colorchanger)



class rating:
    """Asks user to self.rate\n\nParameters are -;\n1) self.rate\n2) root(tk.Frame)"""

    global ex

    def __init__(self, rate, root):
        """Rating apps __init__\n\nParameters are -;\n1) self.rate(tk.Tk)\n2) root(tk.Frame)"""

        global ex

        self.rate = rate

        if root: root.grid_forget()
        else: self.rate = tk.Tk()

        # Rate is the application

        self.rate.geometry("230x140+650+300")

        # Opening the file cluedo.txt for reading purpose only
        c = open("cluedo.txt", 'r')
        
        # Makes a list for the ratings of the previous users
        words = []

        # Puts the ratings in the list words
        for word in c.read():
            
            # Checks if the word is a digit
            if word.isdigit():
                # Checks if the rating is 10
                if word == '0':
                    if prevword == 1:
                        words.pop(-1)
                        words.append(10)
                        continue
                # Finally puts the integer form of the word
                prevword = int(word)
                words.append(int(word))

        # Do not exit
        ex = 1

        # Gets the average value of all the previous users ratings
        # sum(list_name) gives the sum of all the objecs in the list
        # len(list_name) gives the length of the list

        # If there is something in cluedo.txt tell the user the average
        if words != []: 
            # Telling user average value
            average = sum(words)/len(words)
            tk.Label(self.rate, text = 'Average - %s%%' %(round(average*10)), font = ('Algerian', 12, 'bold'), bg = '#00ffff').grid(row = 3, column = 0, sticky = 'ew')
        # If there is nothing tell 'You are first to self.rate'
        else: tk.Label(self.rate, text = 'You are first to self.rate' , font = ('Algerian', 12, 'bold'), bg = '#00ffff').grid(row = 3, column = 0, sticky = 'ew')

        # closing cluedo.txt because we don't need it
        c.close()

        # This is the rating bar
        self.rater = tk.Scale(self.rate, from_ = 1, to = 10, orient = 'horizontal')

        # This asks the name of the user
        self.idk = tk.Entry(self.rate, font = ('comic sans', 15, 'bold'))
        # Sets focus
        self.idk.focus_set()
        self.idk.insert('end', "Your Name")
        self.idk.select_range(0, 'end')
        self.idk.grid(row = 0, column = 0)

        # sticky means where should it go?
        # e = east, w = west, n = north, s = south, ns = from north to south, ew = from east to west, nsew = all the space
        self.rater.grid(row = 1, column = 0, sticky = 'ew')

        # font = (family, size, weight, etc.)
        self.submitb = tk.Button(self.rate, text = "RATE", font = ('Comic Sans', 15, 'bold'), command = self.submit)
        self.submitb.grid(row = 2, column = 0, sticky = 'ew')

        if not root: self.rate.mainloop()

    def submit(self, sure = False):
        # opens clue for reading purpose
        clue = open("cluedo.txt", 'r')
        # reads all the lines and stores lines as elements in a list
        clued = clue.readlines()

        if sure:
            clue2 = open("cluedo.txt", 'w')
            clued2 = ""
            for ele in clued:
                if self.idk.get() in ele:
                    continue
                clued2 += ele
            clue2.write(clued2)
            clue2.close()

        intstr = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        # checks if there are numbers in the name
        # if yes: a = True
        a = False
        for letters in self.idk.get():
            if letters in intstr:
                a = True

        # Checks if user has already rated
        # If yes: b = True
        b = False
        for ele in clued:
            if self.idk.get() in ele:
                b = True

        # if name is not a correct name do this
        if self.idk.get().lower() == 'your name' or a:
            # delete deletes from index1 - index2
            self.idk.delete(0, 'end')
            self.idk.insert(0, 'Wrong name')
            clue.close()
            return

        # if the user rated before and does not know that then do that
        elif b and not sure:
            self.rate.geometry("290x210")
            self.submitb['command'] = lambda : self.submit(True)
            self.submitb['text'] = "You already reveiwed.\n Do you want to overwrite it?\nEnd the program if no,\nelse click me"
            clue.close()
            return

        clue.close()

        # Appends the new user's details
        cluedo = open("cluedo.txt", 'a')
        cluedo.write(self.idk.get()+" - "+str(self.rater.get())+"\n")
        cluedo.close()
        
        # Stroing the user's name
        text = self.idk.get()

        # Going through all the children of self.rate
        for ele in self.rate.winfo_children():

            # If ele is not nothing
            if ele:
                # Destroy it
                ele.destroy()
        
        # Says thanks to user
        self.rate.geometry("500x50")
        tk.Label(self.rate, text = "Thanks for rating, %s" %(text), fg = "white", bg = 'black', font = ('System', 20)).grid()
        
        # After 2000 seconds destroys the application
        self.rate.after(2000, self.rate.destroy)


exit_now = 0

# The password checker
root = tk.Tk()
# telling the position(generally size also but no size here)
root.geometry('+650+300')
# The password is here don't look
fina = "minetdm"

# Global variables(Data that can be accesed anywhere)
a = 1
b = 0

def loading(tf = False):
    """Loads the loading bar and puts everything in place\n\nParameters are -;\n1) tf(bool) = False"""

    if exit_now:
        return

    global labv, barv, passvar, password, shower, fp

    if tf:
        # If it is loading

        if barv == 1:
            # If loading is done 

            if not exit_now: loading()
            return
        
        if labv == 3: labv = 0
        # If there are 3 dots reset to 1
        # Else add one to it
        else: labv += 1
        
        # Multiplication of strings are allowed
        lab['text'] = "One sec" + ("."*labv)
        bar['value'] += 10

        if bar['value'] == 100:
            # If it is 100

            bar['value'] = 0
            barv += 1
        
        if not exit_now: root.after(250, loading, True)
        return

    root.configure(cursor = 'arrow')
    
    # Destroying the bar and the label which says "One second..."
    bar.destroy()
    lab.destroy()

    # The password
    passvar = tk.StringVar(root, 'Password please')
    # The widget for the password
    # font = 12 means the font size, show = "" means show the letters the user typed
    password = tk.Entry(root, textvariable = passvar, show = "", font = 12)

    # The hide and show button
    # Command means do this if the specific event happened(here the event is pressed the button)
    shower = tk.Button(root, text = "Hide letters", command = showing, font = 12)
    # Grid puts it on the application(root)
    shower.grid()

    password.grid()
    # Checking 72 times in a second weather the user did something. If the user did 
    # something then do a function(Here it is openinger)
    # Here if the user presses Enter button(It is called Return, Enter is different)
    # Return is called an event
    password.bind('<Return>', openinger)
    # Setting focus on this widget
    password.focus_set()
    # Selecting all the charectars in the password widget
    password.selection_range(0, 'end')
    # Positioning the cursor(default is 0)
    password.icursor('end')

    # Asking the user if he/she forgot password
    fp = tk.Button(root, text = "Forgot Password?", fg = '#00ffff', bg = 'black', font = ('Arial black', 12, 'bold'), command = forgot_pass)
    fp.grid()

# Shows and hides the password
def showing():
    """Shows and hides the password\n\nParameters are - None"""
    # Global means changing a variable outside this functiono to a new value
    # Here the variable we are changig are 'a'
    global a

    # Shows and hides letters in the password
    if a:
        shower.config(text = "Show letters")
        password.config(show = "•")

        a = 0
    else:
        shower.config(text = "Hide letters")
        
        a = 1

        password.config(show = "")

# Checks if the password is correct or wrong
def openinger(event):
    """Checks if the password is correct or wrong\n\nParameters are -;\n1) event(tk.Event)"""
    # Globalizing root, a, b
    global root, a, b

    # If password is correct
    if passvar.get().lower() == fina:

        # Destroying the widgets
        fp.destroy()
        password.destroy()
        shower.destroy()

        # Allowing acces to the apps
        saep(root)
        return

    else:
        shower.config(text = "Hide letters")
        password.config(show = "")
        
        a = 0
        b += 1
        
        # setting it to no
        passvar.set("no")
        
        # If wrong 6 times
        if b == 6:
            a = messagebox.showinfo("THIEF!!!", "You have tried to many times\nIf you have any doubts contact\n1234567890")
            root.destroy()

# If user forgot the password do this
def forgot_pass(e = 0):
    """If user forgot the password\n\nParameters are-;\n1) e (int) = 0"""
    global fina
    
    if e == 0:
        # If user forgot password

        a = "Type Gmail adress"
        b = 'Hint: subed YTer\nRemember password?'
        c = lambda : forgot_pass(1)
    
        fina = "idk"
    
    else:
        # Resets 

        a = "Password please"
        b = 'Forgot Password?'
        c = forgot_pass
    
        fina = 'minetdm'
    
    # Delets 0 to -1 of password
    password.delete(0, 'end')
    # Inserts string a into pasition 0
    password.insert(0, a)
    # Sets focus to password
    password.focus_set()
    password.selection_range(0, 'end')
    # Postions corsor at the end
    password.icursor('end')
    
    # Changes texts, commands of fp to b, c
    fp['text'] = b
    fp['command'] = c

# Making variables to count the dots in lab and no. of times bar completed
# Ex is if user exited
labv = barv = ex = 0

# Making a loading bar and a label whch says "One sec..."
bar = ttk.Progressbar(root, mode = 'determinate', length = 400)
lab = tk.Label(root, text = "One sec", font = ('Algerian', 15, 'bold'))
# Gridding them
lab.grid()
bar.grid()

root.configure(cursor = 'watch')

# After 100 secs it updates bar
if not exit_now: root.after(250, loading, True)

# Running this line until it is closed(Both by the user and by itself)
# This means the lines after this don't execute until it is closed
root.mainloop()

exit_now = 1

if not ex:
    rating(None, None)
