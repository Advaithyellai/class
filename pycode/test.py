from datetime import datetime, timedelta, date
import pytz
import tkinter.font as font
import tkinter as tk
import pyttsx3

root = tk.Tk()
root.bind('<Alt_L> <c>', lambda e : clickedb(f1))
root.bind('<Alt_L> <t>', lambda e : clickedb(f2))
root.bind('<Alt_L> <s>', lambda e : clickedb(f4))
root.bind('<Escape>', lambda e : clickedb(f))
root.configure(bg = '#fff')
root.geometry('1605x905+0+0')

cump = pyttsx3.init()
cump.setProperty('rate', 120)
cump.setProperty('volume', 1.2)

# +300+300 is center
# To do: clock(calendar, cubing timer), ultimate banking [ listboxes ], mango tree

# root_2 = tk.Tk()
# def blehbleh(event):
#     C = tk.Canvas(root_2, height = 65, width = 110, bg = 'black')
#     C.grid()
#     if a.get() == '0':
#         coords = [10, 10, 15, 15]
#         C.create_oval(coords, fill="red")
#     elif a.get() == '1':
#         coords = [10,10, 60,60]
#         C.create_oval(coords, fill="red")
#     elif a.get() == '2':
#         coords = [10, 10, 60, 60]
#         C.create_arc(coords, start=0, extent=180, fill="red")
#     elif a.get() == '3':
#         coords = [40,40, 20,20, 60,20, 40,40]
#         C.create_polygon(coords, fill = 'red')
#     elif a.get() == '4':
#         coords = [20,40, 20,10, 60,10, 60,40, 20,40]
#         C.create_polygon(coords, fill = 'red')
#     elif a.get() == '5':
#         coords = [10,30, 30,10, 50,30, 50,60, 10,60, 10,30]
#         C.create_polygon(coords, fill = 'red')
#     elif a.get() == '6':
#         coords = [20,10, 10,20, 20,30, 30,30, 40,20, 30,10, 20,10]
#         C.create_polygon(coords, fill = 'red')
#     elif a.get() == '7':
#         coords = [35,10, 20,20, 20,30, 30,40, 40,40, 50,30, 50,20, 35,10]
#         C.create_polygon(coords, fill = 'red')
#     elif a.get() == '8':
#         coords = [30,10, 20,20, 20,30, 30,40, 40,40, 50,30, 50,20, 40,10, 30,10]
#         C.create_polygon(coords, fill = 'red')
#     elif a.get() == '9':
#         coords = [25,5, 15,10, 8,20, 12,33, 20,40, 30,40, 38,33, 42,20, 35,10, 25,5]
#         C.create_polygon(coords, fill = 'red')
#     elif a.get() == '10':
#         coords = [20,5, 12,10, 8,20, 12,33, 20,40, 30,40, 38,33, 42,20, 38,10, 30,5, 20,5]
#         C.create_polygon(coords, fill = 'red')
#     else:
#         a.set('Error')
# tk.Label(root, text = "Number(0-10)=").grid(row = 0, column = 0)
# a = tk.StringVar(root)
# b = tk.Spinbox(root, text = a, from_ = 0, to = 10)
# b.grid(row = 0, column = 1)
# b.bind('<Return>', blehbleh)
# root_2.mainloop()



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

# b = 500
# a = 500
# e = 0
# print("you should enter below 1000 and above 0")
# print("if it takes me 11 tries to guess yvofejvioejou win and I will give 100 rs")
# print("else you give me 10 rs")
# c = int(input("What is your number  "))
# if c > 0 and c < 1000:
#     d = True
# else:
#     exit("You should enter below 1000 and above 0")
# while d == True:
#     e += 1
#     if e == 11:
#         exit("You beat me :(")
#     if e == 1:
#         if a > c:
#             b = 0
#         elif a < c:
#             b = 500
#             a = 1000
#         else:
#             d = False
#     else:
#         f = round((a+b)/2)
#         if f > c:
#             a = f
#         elif f < c:
#             b = f
#         else:
#             d = False
# if a == c:
#     print("It is {} I guessed in {} try / tries".format(a, e))
# elif f == c:
#     print("It is {} i guessed in {} try / tries".format(int(f), e))
# elif b == c:
#     `print`("It is {} I guessed in {} try / tries".format(b, e))
# else:
#     print("Sorry, some kind of error came")

count = 0
color = ''
fat = 0

def come_leave(event):
    global color
    if 'Enter' in str(event):
        color = event.widget.cget('bg')
        if color == 'blue':
            event.widget.configure(bg = 'blue3')
        elif color == 'red2':
            event.widget.configure(bg = 'red3')
        else:
            event.widget.configure(bg = 'yellow3')
    else:
        event.widget.configure(bg = color)

def clickedb(catsvar, fatc = 0):
    global prevcatsvar, fat, nametimer, listtimers, count
    if fatc == 1:
        count = 1
        if listtimers.winfo_ismapped() == True:
            listtimers.grid_remove()
            showtimers['text'] = "Show timers"
            showtimers['command'] = lambda : clickedb(fat, fatc = 3)
        nametimer.selection_range(0, 'end')
        nametimer.focus_set()
        catsvar.grid(row = 2, column = 2)
        addtimer['text'] = "Cancel the timer"
        addtimer['command'] = lambda : clickedb(fat, fatc = 2)
        prevcatsvar = catsvar
        movevert(10)
        return
    elif fatc == 2:
        count = 0
        fat.grid_remove()
        addtimer['text'] = "Add a timer"
        addtimer['command'] = lambda : clickedb(fat, fatc = 1)
        return
    elif fatc == 3:
        if fat.winfo_ismapped() == True:
            fat.grid_remove()
            addtimer['text'] = "Add a timer"
            addtimer['command'] = lambda : clickedb(fat, fatc = 1)
        listtimers.grid(row = 2, column = 2)
        showtimers['text'] = "Hide the timers"
        showtimers['command'] = lambda : clickedb(fat, fatc = 4)
        prevcatsvar = catsvar
        return
    elif fatc == 4:
        listtimers.grid_remove()
        showtimers['text'] = "Show timers"
        showtimers['command'] = lambda : clickedb(fat, fatc = 3)
        return 
    if fatc < 5 and fatc > 0:
        return
    if prevcatsvar == fat:
        prevcatsvar = f2
    prevcatsvar.grid_remove()
    catsvar.grid(row = 1, column = 0, sticky = 'w')
    root.configure(bg = catsvar.cget('bg'))
    prevcatsvar = catsvar

count = 1
myfont = font.Font(root, size = 12, family = 'Algerian', weight = 'bold', underline = 1)
myfont2 = font.Font(root = root, family = 'Helvecta', size = 12, weight = 'bold')
myfont3 = font.Font(root = root, family = 'Times', size = 20, weight = 'bold', slant = 'italic')
myfont4 = font.Font(root = root, family = 'Helvecta', size = 24, weight = 'bold')

b1 = tk.Button(root, text = "C l o c k", width = 47, height = 6, bg = 'red2', relief = 'flat', command = lambda : clickedb(f1), font = myfont)
b1.grid(row = 0, column = 0, sticky = 'w')

b2 = tk.Button(root, text = "T i m e r", width = 47, height = 6, bg = 'blue', relief = 'flat', command = lambda : clickedb(f2), font = myfont)
b2.grid(row = 0, column = 0, sticky = 'w', padx = 525)

b4 = tk.Button(root, text = "S t o p w a t c h", width = 46, height = 6, bg = 'gold', relief = 'flat', command = lambda : clickedb(f4), font = myfont)
b4.grid(row = 0, column = 0, padx = 1050, sticky = 'w')

b1.bind('<Enter>', come_leave)
b2.bind('<Enter>', come_leave)
b4.bind('<Enter>', come_leave)

b1.bind('<Leave>', come_leave)
b2.bind('<Leave>', come_leave)
b4.bind('<Leave>', come_leave)

im = tk.PhotoImage(file = r"D:\\Advaith\\Code\\class\\pycode\\images_for_gcpy\\tick_toclock.png")
im = im.subsample(3, 3)

f = tk.Label(root, image = im, text = "Welcome to your clock app", compound = "top", font = myfont4, bg = 'white')
f.grid(row = 1, column = 0, sticky = 'w', padx = 359)
prevcatsvar = f

f1 = tk.Frame(root, bg = 'red2')

f2 = tk.Frame(root, bg = 'blue')

f4 = tk.Frame(root, height = 700, width = 1530, bg = 'gold')


lv = []
fv = []

rv = [
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
fl2 = [
    'Egypt', 'Argentina', 'Chicago', 'Indiana', 'Los Angeles', 'New York', 'Panama', \
    'New Zealand', 'India', 'Iraq/Iran', 'UAE/Dubai', 'Hong Kong', 'Saudi Arabia', 'Singapore',\
    'Japan', 'Ireland', 'Australia', 'Central Europe', 'Greenwich', 'England/Britain', \
    'Italy', 'Alaska', 'Ethopia', 'Zimbawe', 'Afghanistan', 'Albania', 'Algeria', 'Andorra'\
    , 'Angola', 'Antigua and Barbados', 'Armenia', 'Azerbaijan', 'The Bahamas', 'Bahrain',\
    'Barbados', 'Bangladesh', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Cambodia'\
    , 'Canada', 'Central Africa', 'Chile', 'North/South Korea', 'Russia(West)', 'Russia(West-Central)', 'Russia(East-Central)', \
    'Russia(East)', 'France', 'Germany', 'Indonesia(West)', 'Indonesia(East)'
    ]
fl = [
    'Egypt', 'Argentina', 'Chicago', 'Indiana', 'Los Angeles', 'New York', 'Panama', \
    'New Zealand', 'India', 'Iraq/Iran', 'UAE/Dubai', 'Hong Kong', 'Saudi Arabia', 'Singapore',\
    'Japan', 'Ireland', 'Australia', 'Central Europe', 'Greenwich', 'England/Britain', \
    'Italy', 'Alaska', 'Ethopia', 'Zimbawe', 'Afghanistan', 'Albania', 'Algeria', 'Andorra'\
    , 'Angola', 'Antigua and Barbados', 'Armenia', 'Azerbaijan', 'The Bahamas', 'Bahrain',\
    'Barbados', 'Bangladesh', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Cambodia'\
    , 'Canada', 'Central Africa', 'Chile', 'North/South Korea', 'Russia(West)', 'Russia(West-Central)', 'Russia(East-Central)', \
    'Russia(East)', 'France', 'Germany', 'Indonesia(West)', 'Indonesia(East)'
    ]

fl.sort()
for ele in fl:
    changeinto = fl2.index(ele)
    lv.append(rv[changeinto])
    fv.append(ele)
fl2 = fv
rv = lv
lsel = []

searcher = tk.Entry(f1, width = 20, font = myfont2, bg = 'brown2')
searcher.insert(0, 'Search for places')
searcher.bind('<Key>', lambda e : root.after(10, sken, e))
searcher.bind('<Button>', lambda e : presed(0))
b4.bind('<Tab>', lambda e: presed(0))
searcher.grid(row = 0, column = 0)

lbfrl = tk.Listbox(f1, font = myfont2, height = 15, selectbackground = 'gray80', selectforeground = 'black', activestyle = 'dotbox', bg = 'brown3')
lbfrl.bind('<Button>', lambda e : root.after(10, ctz))
lbfrl.bind('<space>', lambda e: root.after(10, ctz))
lbfrl.bind('<Shift_L> <Tab>', lambda e: presed(0))
lbfrl.grid(row = 1, column = 0)

for x in range(0, len(fl)):
    ele = fl[x]
    lbfrl.insert(x, ele)

sb = tk.Scrollbar(f1, command = lbfrl.yview, orient = 'vertical')
lbfrl.configure(yscrollcommand = sb.set)
sb.grid(row = 1, column = 1, sticky = 'ns')

sev2 = tk.StringVar(f1, '')
counter = 0

l2 = tk.Listbox(f1, font = myfont2, height = 15, selectbackground = 'gray80', selectforeground = 'black', activestyle = 'dotbox', bg = 'brown3')
l2.bind('<Button>', lambda e : root.after(10, ctz, 0, 1))
l2.bind('<space>', lambda e : root.after(10, ctz, 0, 1))

def checking(event):
    if lbfrl.winfo_ismapped() == True:
        lbfrl.focus_set()
    elif l2.winfo_ismapped() == True:
        l2.focus_set()

def sken(event):
    global lv, fl, rv, fl2
    if event.keysym == 'Down':
        if lbfrl.winfo_ismapped() == True:
            lbfrl.focus_set()
            lbfrl.selection_set(0)
        else:
            l2.focus_set()
            l2.selection_set(0)
        return
    lv = []
    fl2 = []
    l2.delete(0, 'end')
    for ele in fl:
        if searcher.get().lower() in ele.lower():
            l2.insert('end', ele)
            lv.append(rv[fl.index(ele)])
            fl2.append(ele)
    lbfrl.grid_remove()
    sb.configure(command = l2.yview, orient = 'vertical')
    l2.configure(yscrollcommand = sb.set)
    l2.grid(row = 1, column = 0)

def ctz(sel = 0, a = 0):
    global ltz, lv, lsel, fv, counter
    fmt = "Date - %d/%m/%y\nTime - %I:%M:%S %p\nTime Zone - %Z %z\nDay - %a/%B"
    if sel == 0:
        if a == 0:
            selected = lbfrl.curselection()
            sev2.set(lv[selected[0]])
            lbfrl.itemconfigure(selected[0], bg = 'gray50')
            if lsel != []:
                lbfrl.itemconfigure(lsel[0], bg = 'brown3')
            lsel = [selected[0]]
        elif a == 1:
            selected = l2.curselection()
            sev2.set(lv[selected[0]])
            l2.itemconfigure(selected[0], bg = 'gray50')
            if lsel != []:
                if len(fl2) >= lsel[0]:
                    l2.itemconfigure(lsel[0], bg = 'brown3')
            lsel = [selected[0]]
        if counter == 0:
            counter = 1
            ctz(1)
        else:
            return
    else:
        if sev2.get() == '':
            return
        else:
            now_time = sev2.get()
            now_time = datetime.now(pytz.timezone(now_time))
        s3 = fv[rv.index(sev2.get())]
        ltz.configure(text = s3+"\n"+str(now_time.strftime(fmt)))
    root.after(1000, ctz, 1)

def presed(event):
    if event == 0:
        searcher.delete(0, 'end')
        searcher.unbind('<Button>')
        searcher.bind('<Button>', presed)
    elif event == 1:
        searcher.focus_set()
        searcher.select_range(0, 'end')
        searcher.icursor('end')
    else:
        if searcher.get() != '':
            root.after(15, presed, 1)

ltz = tk.Label(f1, text = "IT IS NOT FAST\nVersion 1.5.1 Final Release\nMost Countries are there on the list\n(Warning not every country\nVERY FEW cities are there)", bg = 'red2', font = myfont3, justify = 'left')
ltz.grid(row = 1, column = 3, sticky = 's')

searcher.bind('<Tab>', checking)

tk.Label(f1, width = 60, bg = 'red2').grid(row = 2, column = 2)


L1 = L2 = L3 = L4 = L5 = secondstext = hourstext = minutestext = colcount = 0
lotimers = []
lt = []
count2 = 1
colors = ['dark turquoise', 'turquoise', 'aquamarine', 'medium turquoise', 'medium aquamarine']
lt2 = {}

def looper():
    if 1 not in lt2.values():
        return
    vallist = []
    keylist = []
    for key, val in lt2.items():
        vallist.append(val)
        keylist.append(key)
    for vals in vallist:
        dtn = datetime.now()
        dtnr = datetime(dtn.year, dtn.month, dtn.day, dtn.hour, dtn.minute, dtn.second)
        valsl = list(lt2.values())
        vals2 = lt[valsl.index(vals)]
        valsr = datetime(vals2.year, vals2.month, vals2.day, vals2.hour, vals2.minute, vals2.second)
        if valsr <= dtnr:
            cump.say("Your timer rang")
            cump.runAndWait()
            keyinval = keylist[vallist.index(vals)]
            keyinval.grid_remove()
            lt2.pop(keyinval)
            looper()
            return
    root.after(1000, looper)

def settimer():
    global secondstext, hourstext, minutestext, prevcatsvar, lt, lt2
    if len(lotimers) == 5:
        cump.say("Maximum number of timers set")
        cump.runAndWait()
        return
    if secondstext == 0 and hourstext == 0:
        if minutestext == 0:
            cump.say("Put a timer for more than 0 seconds")
            cump.runAndWait()
            return
    if nametimer.get() not in lotimers:
        fat.grid_remove()
        addtimer['text'] = "Add a timer"
        prevcatsvar = f2
        addtimer['command'] = lambda : clickedb(fat, fatc = 1)
        colcount = len(lt2)
        setfor = datetime.now()+timedelta(hours = hourstext, minutes = minutestext, seconds = secondstext)
        lt.append(setfor)
        ntg = "Timer '{}' is set for\n{}".format(nametimer.get(), setfor.strftime("%x, %X"))
        ele = tk.Label(listtimers, text = ntg, bg =  colors[len(lotimers)], font = myfont2)
        ele.grid(row = colcount, column = 0, sticky = 'ew')
        lt2[ele] = 1
        lotimers.append(nametimer.get())
        if len(lotimers) == 1:
            looper()
    else:
        cump.say("Name the timer something different")
        cump.runAndWait()
        return

def movevert(wb):
    global secondstext, hourstext, minutestext, count2
    if wb == 1 or wb == 0:
        if wb == 1:
            if hourstext == 0:
                hourstext = 23
                hours['text'] = "23 : "
            else: 
                hourstext -= 1
                hours['text'] = str(hourstext)+" : "
        elif wb == 0:
            if hourstext == 23:
                hourstext == "0 : "
                hours['text'] = "0 : "
            else:
                hourstext += 1
                hours['text'] = str(hourstext)+" : "
    elif wb == 2 or wb == 3:
        if wb == 3:
            if minutestext == 0:
                minutestext = 59
                minutes['text'] = "59 : "
            else:
                minutestext -= 1
                minutes['text'] = str(minutestext)+" : "
        elif wb == 2:
            if minutestext == 59:
                minutestext = 0
                minutes['text'] = "0 : "
            else:
                minutestext += 1
                minutes['text'] = str(minutestext)+" : "
    elif wb == 4 or wb == 5:
        if wb == 5:
            if secondstext == 0:
                secondstext = 59
                seconds['text'] = 59
            else:
                secondstext -= 1
                seconds['text'] = secondstext
        elif wb == 4:
            if secondstext == 59:
                secondstext = 0
                seconds['text'] = 0
            else:
                secondstext += 1
                seconds['text'] = secondstext
    else:
        sf = datetime.now()+timedelta(hours = hourstext, minutes = minutestext, seconds = secondstext)
        submitb['text'] = sf.strftime("Submit - \n%x\n%X")
        if count == 1:
            root.after(1000, movevert, 10)
            count2 = 1
        else:
            count2 = 0
        return
    if count2 == 0:
        movevert(10)

fat = tk.Frame(f2, bg = 'blue')
listtimers = tk.Frame(f2, bg = 'blue')

hours = tk.Label(fat, text = "0 : ", font = myfont4, bg = 'cadet blue')
minutes = tk.Label(fat, text = "0 : ", font = myfont4, bg = 'steel blue')
seconds = tk.Label(fat, text = 0, font = myfont4, bg = 'light blue')
tk.Label(f2, width = 60, height = 5, bg= 'blue').grid(row = 1, column = 1)
hours.grid(row = 2, column = 1)
minutes.grid(row = 2, column = 2)
seconds.grid(row = 2, column = 3, ipadx = 10)

tk.Button(fat, text = "⬆", command = lambda : movevert(0), bg = 'cadet blue', font = myfont2).grid(row = 1, column = 1, sticky = 'ew')
tk.Button(fat, text = "⬆", command = lambda : movevert(2), bg = 'steel blue', font = myfont2).grid(row = 1, column = 2, sticky = 'ew')
tk.Button(fat, text = "⬆", command = lambda : movevert(4), bg = 'light blue', font = myfont2).grid(row = 1, column = 3, sticky = 'ew')
tk.Button(fat, text = "⬇", command = lambda : movevert(1), bg = 'cadet blue', font = myfont2).grid(row = 3, column = 1, sticky = 'ew')
tk.Button(fat, text = "⬇", command = lambda : movevert(3), bg = 'steel blue', font = myfont2).grid(row = 3, column = 2, sticky = 'ew')
tk.Button(fat, text = "⬇", command = lambda : movevert(5), bg = 'light blue', font = myfont2).grid(row = 3, column = 3, sticky = 'ew')

nametimer = tk.Entry(fat, bg = 'LightSkyBlue2', font = myfont3, width = 15)
nametimer.grid(row = 3, column = 4, sticky = 'nsew')
nametimer.insert(0, "Name of the timer")
nametimer.bind('<Return>', settimer)

submitb = tk.Button(fat, text = "Submit", command = settimer, bg = 'dodger blue', font = myfont4, activebackground = 'dodger blue')
submitb.grid(row = 4, column = 4, sticky = 'ew')

addtimer = tk.Button(f2, text = "Add a timer", font = myfont4, command = lambda : clickedb(fat, 1), bg = 'cyan2')
addtimer.grid(row = 0, column = 0, sticky = 'ew')

showtimers = tk.Button(f2, text = "Show timers", font = myfont4, command = lambda : clickedb(fat, 3), bg = 'pale turquoise')
showtimers.grid(row = 1, column = 0, sticky = 'ew')

root.mainloop()