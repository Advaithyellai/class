# import tkinter as tk
# root_2 = tk.Tk()
# def blehbleh(event):
#     root = tk.Tk()
#     C = tk.Canvas(root, height = 65, width = 110, bg = 'black')
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
# tk.Label(root_2, text = "Number(0-10)=").grid(row = 0, column = 0)
# a = tk.StringVar()
# b = tk.Spinbox(root_2, text = a, )
# b.grid(row = 0, column = 1)
# b.bind('<Return>', blehbleh)
# root_2.mainloop()

# import random
# colors = ['blue', 'orange', 'red', 'green', 'black', 'purple', 'white', 'yellow']
# code = []
# for loop in range(0, 4):
#     codes = random.randrange(0, 7)-loop
#     code.append(colors[codes])
#     colors.remove(colors[codes])
# a = False
# colors = ['blue', 'orange', 'red', 'green', 'black', 'purple', 'white', 'yellow']
# while(a==False):
#     print("0 - blue")
#     print("1 - orange")
#     print("2 - red")
#     print("3 - green")
#     print("4 - black")
#     print("5 - purple")
#     print("6 - white")
#     print("7 - yellow")
#     a = int(input("guess 1   "))
#     b = int(input("guess 2   "))
#     c = int(input("guess 3   "))
#     d = int(input("guess 4   "))
#     red = 0
#     try:
#         if colors[a] == code[a]:
#             print("Red")
#             red += 1
#         elif colors[a] in code:
#             print("White")
#         if colors[b] == code[b]:
#             print("Red_2")
#             red += 1
#         elif colors[b] in code:
#             print("White_2")
#         if colors[c] == code[c]:
#             print("Red_3")
#             red += 1
#         elif colors[c] in code:
#             print("White_3")
#         if colors[d] == code[d]:
#             print("Red_4")
#             red += 1
#         elif colors[d] in code:
#             print("White_4")
#         if red == 4:
#             print("Corect")
#             a = True
#     except:
#         pass

# import tkinter as tk
# root = tk.Tk()
# B = tk.Button(root, text = "Button", command = root.destroy)
# C = tk.Canvas(root, bg = 'black')
# Ch0 = tk.IntVar(root)
# Ch1 = tk.Checkbutton(root, text = "Checkbutton1", variable = Ch0)
# Ch0 = tk.IntVar(root)
# Ch2 = tk.Checkbutton(root, text = "Checkbutton2", variable = Ch0)
# E = tk.Entry(root)
# L = tk.Label(root, text = "Label")
# Li = tk.Listbox(root)
# Li.insert(1, "Python")
# Li.insert(2, "Java")
# Li.insert(3, "HTML")
# Li.insert(4, "Arduino")
# Li.insert(5, "Scratch")
# Li.insert(6, "Lego Mindstorms")
# Mb = tk.Menubutton(root, text = "Menubutton")
# Mb.menu = tk.Menu(Mb)
# Mb['menu'] = Mb.menu
# Mb.menu.add_checkbutton(label = "Idk")
# Mb.menu.add_checkbutton(label = "Idk_2")
# M = tk.Message(root, text = "Message")
# RV = tk.IntVar(root)
# Rb = tk.Radiobutton(root, text = "Value 1", variable = RV, value = 1, indicatoron = 2)
# Rb2 = tk.Radiobutton(root, text = "Value 2", variable = RV, value = 2)
# Sv = tk.IntVar(root)
# Sv.set(0.0)
# S = tk.Scale(root, variable = Sv, from_ = 0, to = 10)
# Sb = tk.Spinbox(root, from_ = 0.0, to = 10.0)
# B.grid()
# C.grid()
# Ch1.grid()
# Ch2.grid()
# E.grid()
# L.grid()
# Li.grid()
# Mb.grid()
# M.grid()
# Rb.grid()
# Rb2.grid()
# S.grid(row = 1, column = 1)
# Sb.grid(row = 0, column = 1)
# root.mainloop()

# import tkinter as tk
# root = tk.Tk()
# canvas = tk.Canvas(root)
# scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview)
# scrollable_frame = tk.Frame(canvas)
# scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
# canvas.create_window((0, 0), window=scrollable_frame, anchor = 'nw')
# canvas.configure(yscrollcommand=scrollbar.set)
# for i in range(50):
#     tk.Label(scrollable_frame, text="Sample scrolling label").grid()
# canvas.grid(row = 0, column = 0)
# scrollbar.grid(row = 0, column = 1, sticky = 'ns')
# root.mainloop()




# import tkinter as tk
# class Checkbar(tk.Frame):
#    def __init__(self, picks=[]):
#       tk.Frame.__init__(self)
#       self.vars = []
#       for pick in picks:
#          var = tk.IntVar()
#          chk = tk.Checkbutton(self, text=pick, variable=var)
#          chk.pack()
#          self.vars.append(var)
# root = tk.Tk()
# lng = Checkbar(['Python', 'Ruby', 'Perl', 'C++'])
# tgl = Checkbar(['English','German'])
# lng.pack(side='left',  fill='x')
# tgl.pack(side='left')
# lng.config(relief=tk.GROOVE, bd=2)
# tk.Button(root, text='Quit', command=root.quit).pack(side=tk.RIGHT)
# root.mainloop()



import tkinter as tk
import tkinter.font as font
import random
root = tk.Tk()
root.title("                                                                                                                                                                                                                             Colour Game")
root.geometry('1600x900')
def quore():
    pass
def lestart(event):
    global colours, labc, labt, words, counter, counting
    if counting == 0:
        quore()
    a = ges.get()
    if a.lower() == colours[labc]:
        counter += 1
        Score.configure(text = "Your score : {}".format(counter))
    geser.set('')
    colours = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
    words = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
    labc = random.randint(0, len(colours)-1)
    labt = random.randint(0, len(words)-1)
    code.configure(text = words[labt], fg = colours[labc])
def lesgo(counting):
    if counting == 60:
        geser.set('')
        colours = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
        words = ['black', 'blue', 'green', 'orange', 'yellow', 'red', 'brown', 'purple', 'pink']
        labc = random.randint(0, len(colours)-1)
        labt = random.randint(0, len(words)-1)
        code.configure(text = words[labt], fg = colours[labc])
    ges.bind('<Return>', lestart)
    root.after(1, starter.destroy)
    Timer['text'] = "Game ends in : {}".format(counting)
    if counting > 0:
        root.after(1000, lesgo, counting-1)
    if counting == 0:
        quore()
counter = 0
counting = 60
colours = ['rllllllllllllllssssdddddddfffffffffrrrrrrrttttttt']
labc = 0
words = ['eeeeeeeerrrrrrrrttfffffffgggggcccccccnnnnnnnnvvvvvv']
labt = 0
myfont = font.Font(size = 15)
myfont_2 = font.Font(size = 20)
myfont_4 = font.Font(size = 40)
tk.Label(root, text = " ", width = 75).grid(row = 0, column = 0)
tk.Label(root, text = "Game Description: Enter the colour of the words displayed below.", fg = 'grey', font = myfont).grid(row = 0, column = 1)
tk.Label(root, text = "And keep in mind not to enter the word text itself", fg = 'grey', font = myfont).grid(row = 1, column = 1)
Score = tk.Label(root, text = "Your score : {}".format(counter), fg = 'forest green', font = myfont_2)
Score.grid(row = 2, column = 1)
code = tk.Label(root, text = "   ",height = 4, font = myfont_4)
code.grid(row = 3, column = 1)
Timer = tk.Label(root, text = "Game ends in : __", fg = 'gold2', font = myfont_2)
Timer.grid(row = 4, column = 1)
tk.Label(root, text = "").grid(row = 5, column = 1)
geser = tk.StringVar(root, "")
ges = tk.Entry(root, textvariable = geser, width = 37)
ges.grid(row = 6, column = 1)
tk.Label(root, text = "", height = 40).grid()
starter = tk.Button(root, text = "Start", width = 20, height = 3, font = myfont, bg = 'peach puff', command = lambda : lesgo(counting))
starter.grid(row = 7, column = 1)
root.mainloop()