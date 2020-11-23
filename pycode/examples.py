# # Importing ttk(GUI secondary) and messagebox(GUI treshary)
# from tkinter import ttk, messagebox

# # Importing tkinter(GUI Primary)
# # Changing the self.name from tkinter to tk
# import tkinter as tk

# # self.root is Tk
# root_2 = tk.Tk()

# # Putting a title to this
# root_2.title("All the widgets in tkiner and in ttk")

# # Frame
# self.self.root = ttk.Notebook(root_2)
# # Gridding means placing it on the self.root
# self.self.root.grid(row = 0, column = 2)

# # This updates progress bar(Downloading bar)
# def change():
#     # Increasing value by 10
#     nb['value'] = nb.cget('value')+10
    
#     # Checking if it is 100% done
#     if nb['value'] != 100:
#         # If it is not 100% then countinue
#         self.self.root.after(250, change)
#     else:
#         # if it is 100% then update user
#         msg = messagebox.askyesno("Done", "Hello, You're program is done.\nDo you want to run it?")
        
#         # If user says quit then quit
#         if msg == True: quit()

# # Just like integer variable(rbv = 0) but better
# rbv = tk.IntVar(self.self.root, 0)

# # Radiobutton - Means Button but can select only one at a time
# ttk.Radiobutton(self.self.root, variable = rbv, text = "Food", value = 1, command = lambda : print("Food")).grid(row = 3, column = 2)
# ttk.Radiobutton(self.self.root, variable = rbv, text = "Water", value = 0, command = lambda : print("Water")).grid(row = 3, column = 2)

# # Separates two or more widgets
# ttk.Separator(self.self.root).grid(row = 4, column = 2, sticky = 'ew')
# ttk.Separator(self.self.root, orient = 'vertical').grid(sticky = 'ns', row = 6, column = 2)

# # self.style makes the widget look better
# self.style = ttk.Style()

# # Like microsoft excel but can not edit
# self.tree = ttk.Treeview(self.self.root, columns = ("1", "2", "3", "4"))
# self.tree.grid(row = 6, column = 2)

# # It makes the columns
# self.tree.column("1", anchor = 'c', width = 125)
# self.tree.column("2", anchor = 'c', width = 125)
# self.tree.column("3", anchor = 'c', width = 125)
# self.tree.column("4", anchor = 'c', width = 125)
# self.tree.heading("1", text = "Me")
# self.tree.heading("2", text = "Amma")
# self.tree.heading("3", text = "Akka")
# self.tree.heading("4", text = "Envolope")

# # This makes the rows
# # the start is parent(None = ""), next is position and then text and last is values for the columns
# self.tree.insert("", 'end', text = "", values = ("", "", "", ""))
# self.tree.insert("", 'end', text = "Mustard", values = ("x", "✓", "x", "x"))
# self.tree.insert("", 'end', text = "White", values = ("x", "x", "x", "✓"))

# # This lets user resize the self.root
# ttk.Sizegrip(self.self.root).grid(row = 5, column = 2)

# # This is the Entry which can only have values from 0 - 10
# spinner = ttk.Spinbox(self.self.root, from_ = 0, to = 10)
# spinner.grid(row = 7, column = 2)

# # If you change the value it prints it
# spinner['command'] = lambda : print(spinner.get())

# # This s just like a string Variable(sv = "Menu") but better
# sv = tk.StringVar(self.self.root, "Menu")

# # This is the dropdown Menu
# # First is master then is variable then default value then n number of values then you can do whatever you want
# ttk.OptionMenu(self.self.root, sv, "Menu", "Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", command = print).grid()

# # It is like a dropdown Menu but with an Entry
# cbb = ttk.Combobox(self.self.root, values = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))

# # This is the scrollbar but it does not scroll anything
# # This unlike Scale shows the value of it's position
# lbs = ttk.LabeledScale(self.self.root, from_ = 0, to = 10)

# # Another Style
# s = ttk.Style()
# # Idk what the next 2 lines are
# s.theme_use('clam')
# s.configure("red.Horizontal.TProgressbar", foreground='red', background='black')

# # This is just like LabledScale but does not shaw it's value
# ttk.Scale(self.self.root, from_ = 0, orient = 'vertical', to = 10).grid(row = 0, column = 2)

# # A normal text showing widget
# ttk.Label(self.self.root, text = "Hello").grid()

# # Accepts string self.data from the user
# e = ttk.Entry(self.self.root)
# e.grid()
# # This does not have text option so we have to insert the text
# e.insert(0, "hello")

# # A button
# ttk.Button(self.self.root, text = "Hello", command = lambda : print("click")).grid()

# # A button but looks different and has more self.options
# ttk.Checkbutton(self.self.root, text = "Food", command = lambda : print("check food")).grid()
# ttk.Checkbutton(self.self.root, text = "Water", command = lambda : print("check water")).grid()

# # The downloading bar
# nb = ttk.Progressbar(self.self.root, value = 0, self.style = "red.Horizontal.TProgressbar", length = 300)
# # Calling a function to Update it
# self.self.root.after(250, change)
# nb.grid(row = 2, column = 2)
# lbs.grid(row = 0, column = 2)
# cbb.insert(0, 'Select')
# cbb.grid(row = 1, column = 2)

# # Done with the ttk part moving on to the tkinter part

# # The container of other widgets
# self.self.root = tk.Frame(root_2, bg = 'red')

# # Tkinter Button just like ttk button but simpler
# tk.Button(self.self.root, text = "Click me!!!", command = lambda : print("Clicked")).grid()

# # Canvas for painting
# c = tk.Canvas(self.self.root, bg = 'blue', width = 30, height = 30)
# c.create_polygon(10, 10, 20, 10, 20, 20, 10, 20, 10, 10, fill = '#000fff000')
# c.grid()

# # Just like button but slightly different
# tk.Checkbutton(self.self.root, text = "Mustard", command = lambda : print("mustard")).grid(column = 2, row = 2)
# tk.Checkbutton(self.self.root, text = "Ketchup", command = lambda : print("Ketchup")).grid(column = 2, row = 2)

# # just like ttk Entry
# e = tk.Entry(self.self.root)
# e.insert('end', "Hello")
# e.grid()

# # Label + Frame
# lf = tk.LabelFrame(self.self.root, text = "hello", font = ('Algerian', 15, 'bold'), bg = 'yellow', fg = 'black')
# lf.grid()

# # Just like ttk label
# tk.Label(lf, text = "This is a label", font = ('Algerian', 15, 'bold'), fg = 'yellow', bg = 'black').grid()

# # A vertical view of a list
# l = tk.Listbox(self.self.root)

# # Scroll bar
# sb = tk.Scrollbar(self.self.root, command = l.yview)
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
# menubar = tk.Menu(self.self.root)

# # assigning menubar as the menu
# root_2.configure(menu = menubar)

# # Menu men inside menubar
# men = tk.Menu(menubar, tearoff = 0)

# # Adding buttons
# intvar = tk.IntVar(self.self.root, 0)
# intvar2 = tk.IntVar(self.self.root, 0)
# intvar3 = tk.IntVar(self.self.root, 0)
# men.add_command(label = "Hello", command = lambda : print("hello"))
# men.add_separator()
# men.add_radiobutton(label = ":)", variable = intvar, value = 1)
# men.add_radiobutton(label = ":(", variable = intvar, value = 2)
# men.add_separator()
# men.add_checkbutton(label = "LOL", variable = intvar2)
# men.add_checkbutton(label = "LOL2", variable = intvar3)

# # Adding this men to the menubar and labeling it "Menu"
# menubar.add_cascade(menu = men, label = "Menu")

# mb = tk.Menubutton(self.self.root, text = "Hello", relief = 'groove')
# mb.grid()
# mb_menu = tk.Menu(mb, tearoff = 0)
# mb['menu'] = mb_menu
# mb_menu.add_command(label = "Print", command = lambda : print("Print"))
# mb_menu.add_command(label = "Quit", command = quit)

# self.self.root.grid(row = 0, column = 2)
# # Running the whole code