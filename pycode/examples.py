# # Importing ttk(GUI secondary) and messagebox(GUI treshary)
# from tkinter import ttk, messagebox

# # Importing tkinter(GUI Primary)
# # Changing the name from tkinter to tk
# import tkinter as tk

# # root is Tk
# root_2 = tk.Tk()

# # Putting a title to this
# root_2.title("All the widgets in tkiner and in ttk")

# # Frame
# root = ttk.Notebook(root_2)
# # Gridding means placing it on the root
# root.grid(row = 0, column = 2)

# # This updates progress bar(Downloading bar)
# def change():
#     # Increasing value by 10
#     nb['value'] = nb.cget('value')+10
    
#     # Checking if it is 100% done
#     if nb['value'] != 100:
#         # If it is not 100% then countinue
#         root.after(250, change)
#     else:
#         # if it is 100% then update user
#         msg = messagebox.askyesno("Done", "Hello, You're program is done.\nDo you want to run it?")
        
#         # If user says quit then quit
#         if msg == True: quit()

# # Just like integer variable(rbv = 0) but better
# rbv = tk.IntVar(root, 0)

# # Radiobutton - Means Button but can select only one at a time
# ttk.Radiobutton(root, variable = rbv, text = "Food", value = 1, command = lambda : print("Food")).grid(row = 3, column = 2)
# ttk.Radiobutton(root, variable = rbv, text = "Water", value = 0, command = lambda : print("Water")).grid(row = 3, column = 2)

# # Separates two or more widgets
# ttk.Separator(root).grid(row = 4, column = 2, sticky = 'ew')
# ttk.Separator(root, orient = 'vertical').grid(sticky = 'ns', row = 6, column = 2)

# # style makes the widget look better
# style = ttk.Style()

# # Like microsoft excel but can not edit
# tree = ttk.Treeview(root, columns = ("1", "2", "3", "4"))
# tree.grid(row = 6, column = 2)

# # It makes the columns
# tree.column("1", anchor = 'c', width = 125)
# tree.column("2", anchor = 'c', width = 125)
# tree.column("3", anchor = 'c', width = 125)
# tree.column("4", anchor = 'c', width = 125)
# tree.heading("1", text = "Me")
# tree.heading("2", text = "Amma")
# tree.heading("3", text = "Akka")
# tree.heading("4", text = "Envolope")

# # This makes the rows
# # the start is parent(None = ""), next is position and then text and last is values for the columns
# tree.insert("", 'end', text = "", values = ("", "", "", ""))
# tree.insert("", 'end', text = "Mustard", values = ("x", "✓", "x", "x"))
# tree.insert("", 'end', text = "White", values = ("x", "x", "x", "✓"))

# # This lets user resize the root
# ttk.Sizegrip(root).grid(row = 5, column = 2)

# # This is the Entry which can only have values from 0 - 10
# spinner = ttk.Spinbox(root, from_ = 0, to = 10)
# spinner.grid(row = 7, column = 2)

# # If you change the value it prints it
# spinner['command'] = lambda : print(spinner.get())

# # This s just like a string Variable(sv = "Menu") but better
# sv = tk.StringVar(root, "Drop")

# # This is the dropdown Menu
# # First is master then is variable then default value then n number of values then you can do whatever you want
# ttk.OptionMenu(root, sv, "Drop", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", command = print).grid()

# # It is like a dropdown Menu but with an Entry
# cbb = ttk.Combobox(root, values = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))

# # This is the scrollbar but it does not scroll anything
# # This unlike Scale shows the value of it's position
# lbs = ttk.LabeledScale(root, from_ = 0, to = 10)

# # Another Style
# s = ttk.Style()
# # Idk what the next 2 lines are
# s.theme_use('clam')
# s.configure("red.Horizontal.TProgressbar", foreground='red', background='black')

# # This is just like LabledScale but does not shaw it's value
# ttk.Scale(root, from_ = 0, orient = 'vertical', to = 10).grid(row = 0, column = 2)

# # A normal text showing widget
# ttk.Label(root, text = "Hello").grid()

# # Accepts string data from the user
# e = ttk.Entry(root)
# e.grid()
# # This does not have text option so we have to insert the text
# e.insert(0, "hello")

# # A button
# ttk.Button(root, text = "Hello", command = lambda : print("click")).grid()

# # A button but looks different and has more options
# ttk.Checkbutton(root, text = "Food", command = lambda : print("check food")).grid()
# ttk.Checkbutton(root, text = "Water", command = lambda : print("check water")).grid()

# # The downloading bar
# nb = ttk.Progressbar(root, value = 0, style = "red.Horizontal.TProgressbar", length = 300)
# # Calling a function to Update it
# root.after(250, change)
# nb.grid(row = 2, column = 2)
# lbs.grid(row = 0, column = 2)
# cbb.insert(0, 'Select')
# cbb.grid(row = 1, column = 2)

# # Done with the ttk part moving on to the tkinter part

# # The container of other widgets
# root = tk.Frame(root_2, bg = 'red')

# # Tkinter Button just like ttk button but simpler
# tk.Button(root, text = "Click me!!!", command = lambda : print("Clicked")).grid()

# # Canvas for painting
# c = tk.Canvas(root, bg = 'blue', width = 30, height = 30)
# c.create_polygon(10, 10, 20, 10, 20, 20, 10, 20, 10, 10, fill = '#000fff000')
# c.grid()

# # Just like button but slightly different
# tk.Checkbutton(root, text = "Mustard", command = lambda : print("mustard")).grid(column = 2, row = 2)
# tk.Checkbutton(root, text = "Ketchup", command = lambda : print("Ketchup")).grid(column = 2, row = 2)

# # just like ttk Entry
# e = tk.Entry(root)
# e.insert('end', "Hello")
# e.grid()

# # Label + Frame
# lf = tk.LabelFrame(root, text = "hello", font = ('Algerian', 15, 'bold'), bg = 'yellow', fg = 'black')
# lf.grid()

# # Just like ttk label
# tk.Label(lf, text = "This is a label", font = ('Algerian', 15, 'bold'), fg = 'yellow', bg = 'black').grid()

# # A vertical view of a list
# l = tk.Listbox(root)

# # Scroll bar
# sb = tk.Scrollbar(root, command = l.yview)
# sb.grid(row = 5, column = 2, sticky = 'nsw')

# # Assigning the widget to the scroll bar
# l.configure(yscrollcommand = sb.set)

# # Making a list of items
# y = ["Menu", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# # Looping through the list
# for x in y:
#     # Inserting it in it's position
#     l.insert('end', x)
# l.grid(row = 5, column = 2, sticky = 'ew')

# # The menubar
# menubar = tk.Menu(root)

# # assigning menubar as the menu
# root_2.configure(menu = menubar)

# # Menu men inside menubar
# men = tk.Menu(menubar, tearoff = 0)

# # Adding buttons
# intvar = tk.IntVar(root, 0)
# intvar2 = tk.IntVar(root, 0)
# intvar3 = tk.IntVar(root, 0)
# men.add_command(label = "Hello", command = lambda : print("hello"))
# men.add_separator()
# men.add_radiobutton(label = ":)", variable = intvar, value = 1)
# men.add_radiobutton(label = ":(", variable = intvar, value = 2)
# men.add_separator()
# men.add_checkbutton(label = "LOL", variable = intvar2)
# men.add_checkbutton(label = "LOL2", variable = intvar3)

# # Adding this men to the menubar and labeling it "Menu"
# menubar.add_cascade(menu = men, label = "Menu")

# mb = tk.Menubutton(root, text = "Hello", relief = 'groove')
# mb.grid()
# mb_menu = tk.Menu(mb, tearoff = 0)
# mb['menu'] = mb_menu
# mb_menu.add_command(label = "Print", command = lambda : print("Print"))
# mb_menu.add_command(label = "Quit", command = quit)

# root.grid(row = 0, column = 2)
# # Running the whole code
# root_2.mainloop()



# import tkinter as tk
# import tkinter.ttk as ttk

# import random
# import string


# def insert_something_to_combobox(box):
#     box['values'] = [gen_key() for _ in range(10)]


# def gen_key(size=6, chars=string.ascii_uppercase + string.digits):
#     # just to generate some random stuff
#     return ''.join(random.choice(chars) for _ in range(size))


# root = tk.Tk()
# text_font = ('Courier New', '30')
# main_frame = tk.Frame(root, bg='gray')                  # main frame
# combo_box = ttk.Combobox(main_frame, font=text_font)    # apply font to combobox
# entry_box = ttk.Entry(main_frame, font=text_font)       # apply font to entry
# root.option_add('*TCombobox*Listbox.font', text_font)   # apply font to combobox list
# combo_box.pack()
# entry_box.pack()
# main_frame.pack()

# insert_something_to_combobox(combo_box)

# root.mainloop()

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
# a = datetime.self.now()
# b = "%z%Z\n%a = %A = %w\n%Y = %y / %b = %B = %m / %self.d\n%H = %I(24hrs) %p : %M : %S.%f\n%U(week no. first day of week is Sunday) = %W(Monday)\n%c | %x | %X | %%"
# print(a.strftime(b))

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



# import sqlite3
# con = sqlite3.connect("face_rec.db")

# c = con.cursor()

# class Employees():
#     def __init__(self, first="", last="", pay=0, updated_pay=0):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.upay = updated_pay
#         if not last: self.ret = True
#         else: self.ret = False

#     def getEmpByName(self):
#         if self.ret: return "Incorrect Employee"

#         c.execute("SELECT * FROM employees WHERE last=:last", {"last": self.last})
        
#         empl = ""
#         for emps in c.fetchall():
#             empl += str(emps)+"\n"
        
#         return empl

#     def addEmp(self):
#         if not self.first or not self.pay or self.ret: return "The emplyee is incorrect"

#         c.execute("INSERT INTO employees VALUES (:first, :last, :pay)", {"first": self.first, "last": self.last, "pay": pay})
        
#         return "Successfuly added {}".format(self.first)

#     def updatePay(self):
#         if not self.first or (not self.upay or self.ret): return "Something went wrong. Please try again"

#         c.execute("UPDATE employees SET pay=:pay WHERE first=:first AND last=:last", {"first": self.first, "last": self.last, "pay": self.upay})

#         return "Successfuly updated {}'s pay".format(self.first)
    
#     def deleteEmp(self):
#         if not self.first or self.ret: return "The emplyee is incorrect"

#         c.execute("DELETE FROM employees WHERE first=:first AND last=:last", {"first": self.first, "last": self.last})
        
#         return "Successfuly deleted {}".format(self.first)

# emp3 = Employees("Adithi", "Yellai", updated_pay=1000).updatePay()
# print(emp3)

# emp2 = Employees(last="Yellai").getEmpByName()
# print(emp2)

# con.commit()

# con.close()
