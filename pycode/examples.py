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

# # This is just like a string Variable(sv = "Menu") but better
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
# root.configure(bg= "blue")
# c = tk.Canvas(root, width = 100, height = 100, cursor = 'none')
# rr = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
# bit = rr[random.randrange(0, len(rr))]
# print(bit)
# for bits in rr:
#     tk.Label(root, bitmap= bits, text= bits).grid(row= 1, column= rr.index(bits))
# rect = c.create_bitmap(-10, -10, bitmap = bit)
# c.bind('<Motion>', callthiswhatevs)
# c.bind('<Leave>', callthiswhatevs)
# c.grid(row= 0, column= 0)
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

# import tkinter as tk

# root = tk.Tk()
# root.geometry('650x450')

# frame = tk.Frame(root, bg = 'blue')

# button = tk.Button(frame, text= "CLICK ME!!!")
# button.grid()

# frame.grid(row= 0, column= 0, sticky= "NSEW")

# root.rowconfigure(0, weight= 1)
# root.columnconfigure(0, weight= 1)

# frame.rowconfigure(0, weight= 1)
# frame.columnconfigure(0, weight= 1)

# root.mainloop()

# #Import the required libraries
# from tkinter import *

# #Create an instance of Tkinter Frame
# win = Tk()

# #Set the geometry
# win.geometry("700x250")

# #Adding transparent background property
# win.wm_attributes('-transparentcolor', '#ab23ff')

# #Create a Label
# Label(win, text= "This is a New line Text", font= ('Helvetica 18'), bg= '#ab23ff').pack(ipadx= 50, ipady=50, padx= 20)

# win.mainloop()

# import tkinter as tk
# from PIL import ImageTk, Image
# import os

# def func(e):
#     new_img = img.resize((canvas.winfo_width(), canvas.winfo_height()))
#     new_photo_img = ImageTk.PhotoImage(new_img)
    
#     canvas.img = new_photo_img
#     canvas.coords(item, canvas.winfo_width()/2, canvas.winfo_height()/2)
#     canvas.itemconfig(item, image= new_photo_img)

# root = tk.Tk()

# img = Image.open("Main\\images_for_gcpy\\gcpy_background.jpg")
# photo_img = ImageTk.PhotoImage(img)

# canvas = tk.Canvas(root, bg= 'blue')
# item = canvas.create_image(100, 100, image= photo_img)

# canvas.grid(sticky= 'nsew')
# canvas.bind('<Configure>', func)

# root.rowconfigure(0, weight= 1)
# root.columnconfigure(0, weight= 1)

# root.mainloop()

# import pandas as pd
# import numpy as np

# def impute(item):
#     pclass, sex, title = item.Pclass, item.Sex, item.Title
#     return round(grp[(grp.Pclass==pclass)&(grp.Sex==sex)&(grp.Title==title)]["Age"].values[0], 2)

# mapping = {"Capt": "Officer","Col": "Officer","Major": "Officer","Jonkheer": "Royalty", \
#            "Don": "Royalty", "Dona":"Royalty", "Sir" : "Royalty","Dr": "Royalty","Rev": "Royalty", \
#            "Countess":"Royalty", "Mme": "Mrs", "Mlle": "Miss", "Ms": "Mrs","Mr" : "Mr", \
#            "Mrs" : "Mrs","Miss" : "Miss","Master" : "Master","Lady" : "Royalty"}

# train_data = pd.read_csv("titanic_data/train.csv")
# test_data = pd.read_csv("titanic_data/test.csv")

# train_data["Title"] = train_data.Name.str.extract(" ([A-Za-z]+)\.", expand=False)
# train_data["Title"] = train_data.Title.map(mapping)
# test_data["Title"] = test_data.Name.str.extract(" ([A-Za-z]+)\.", expand=False)
# test_data["Title"] = test_data.Title.map(mapping)
# test_data.index = range(len(train_data), len(train_data)+len(test_data))

# combined = train_data.append(test_data)

# print(round(combined.isnull().sum().sort_values(ascending=False)*100/len(combined), 1))
# print(round(combined.groupby(["Title", "Pclass"])["Age"].agg(["mean", "count"]), 2))

# grp = combined.groupby(['Pclass','Sex','Title'])['Age'].mean().reset_index()[['Pclass', 'Sex', 'Title', "Age"]]
# print(combined.loc[combined["Age"].isnull()][["PassengerId", "Pclass", "Sex", "Title"]])
# combined["Age"] = combined.apply(lambda x: impute(x) if np.isnan(x["Age"]) else x["Age"], axis=1)
# train_data["Age"] = train_data.apply(lambda x: impute(x) if np.isnan(x["Age"]) else x["Age"], axis=1)
# test_data["Age"] = test_data.apply(lambda x: impute(x) if np.isnan(x["Age"]) else x["Age"], axis=1)
# print(combined["Embarked"].value_counts(ascending=True).keys().to_list())

# import os
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# import pandas as pd
# from sklearn import preprocessing
# from tensorflow import keras
# from datetime import datetime

# start = datetime.now()

# def create_model():
    
#     model = keras.Sequential()
#     model.add(keras.layers.Dense(NEURONS[0], input_dim=x_train.shape[1], activation=ACTIVATION))
#     model.add(keras.layers.Dropout(DROPOUT))
    
#     for i in NEURONS[1: -1]:
#         model.add(keras.layers.Dense(i, activation=ACTIVATION))
#         model.add(keras.layers.Dropout(DROPOUT))
    
#     model.add(keras.layers.Dense(1, activation='sigmoid'))
#     model.compile(loss='binary_crossentropy', optimizer=OPTIMIZER, metrics=['accuracy'])
#     return model

# train = pd.read_csv("titanic_data/train.csv")
# NEURONS = [14, 28, 42, 28, 14, 1]
# EPOCHS = 100
# ACTIVATION = "tanh"
# DROPOUT = 0
# OPTIMIZER = "Adam"

# # relation_emb = {"C": 0, "Q": 1, "S": 2}
# # relation_tit = {'Mr': 0, 'Miss': 1, 'Mrs': 2, 'Master': 3, 'Royalty': 4, 'Officer': 5}
# # train["Embarked_n"] = train.Embarked.map(relation_emb)
# # train["Title_n"] = train.Title.map(relation_tit)

# for var in ['Embarked', 'Title']:
#     train = pd.concat([train, pd.get_dummies(train[var], prefix=var)], axis=1)

# train.drop(['Cabin', "Fare", "Family", 'Name', 'Ticket', 'Sex', "Embarked", "Title", "PassengerId"], axis=1, inplace=True)
# scaler = preprocessing.StandardScaler()
# for var in ['Age', 'Parch', 'SibSp']:
#     train[var] = train[var].astype('float64')
#     train[var] = scaler.fit_transform(train[var].values.reshape(-1, 1))

# train, test = train.loc[:791], train.loc[791:]
# x_train, y_train = train.drop(["Survived"], axis=1), train["Survived"]
# x_test, y_test = test.drop(["Survived"], axis=1), test["Survived"]

# model = create_model()
# training = model.fit(x_train, y_train, epochs=EPOCHS, batch_size=32, verbose=0, validation_split=0.2)
# score = model.evaluate(x_test, y_test, verbose=0)

# print("\nFeatures:", x_train.columns.tolist())
# print("Loss: {:.2f}%".format(score[0]*100))
# print("Accuracy: {:.2f}%".format(score[1]*100))
# print()

# hist = training.history
# for key, value in training.history.items():
#     print("{}: {:.2f}%".format(key, sum(value)*100/len(value)))

# end = datetime.now()
# time = end-start
# print("Time Taken:", round(time.total_seconds(), 2), "seconds")

# import pandas as pd
# from sklearn import preprocessing, model_selection, tree
# from datetime import datetime
# from tensorflow import keras

# start = datetime.now()

# def build_model():
#     model = keras.models.Sequential()

#     model.add(keras.layers.Dense(NEURONS[0], input_shape=(len(data.drop(["Survived", "PassengerId"], axis=1).columns.tolist()),), activation="relu"))
#     model.add(keras.layers.Dropout(DROPOUT))
    
#     for neuron in NEURONS[1:-1]:
#         model.add(keras.layers.Dense(neuron, activation="relu"))
#         model.add(keras.layers.Dropout(DROPOUT))
    
#     model.add(keras.layers.Dense(NEURONS[-1], activation="sigmoid"))

#     model.compile(loss='binary_crossentropy', optimizer="Adam", metrics=['accuracy'])
#     return model

# def preprocess(df):
#     for var in ['Embarked', 'Title']:
#         df = pd.concat([df, pd.get_dummies(df[var], prefix=var)], axis=1)

#     scaler = preprocessing.StandardScaler()
#     for var in ['Age', 'Parch', 'SibSp', "Pclass", "Family", "Fare"]:
#         df[var] = df[var].astype('float64')
#         df[var] = scaler.fit_transform(df[var].values.reshape(-1, 1))
    
#     df.drop(['Cabin', 'Name', 'Ticket', 'Sex', "Embarked", "Title"], axis=1, inplace=True)
#     return df

# NEURONS = [14, 28, 42, 28, 14, 1]
# DROPOUT = 0.12
# data = pd.read_csv("titanic_data/train.csv")
# data = preprocess(data)
# train = data[:791]
# test = data[791:]
# x_data, y_data = data.drop(["PassengerId", "Survived"], axis=1), data["Survived"]
# param_grid_nn = {"batch_size": [16, 32, 64],
#                  "epochs": [50, 100, 150]}

# model = keras.wrappers.scikit_learn.KerasClassifier(build_fn=build_model, verbose=0)
# gridsearch = model_selection.GridSearchCV(model, param_grid = param_grid_nn, n_jobs=-1, cv=3, verbose=2)
# gridsearch.fit(x_data, y_data)

# param_grid2 = {"max_depth": [5, 7, 10],
#                "criterion": ["gini", "entropy"]}
# model = tree.DecisionTreeClassifier()
# gridsearch2 = model_selection.GridSearchCV(model, param_grid = param_grid2, n_jobs=-1, cv=5, verbose=2)
# gridsearch2.fit(x_data, y_data)

# print("\n\n"+"--"*30)
# print("Neural Network")
# means = gridsearch.cv_results_['mean_test_score']
# params = gridsearch.cv_results_['params']
# for mean, param in zip(means, params):
#     print("{:.2%} with: {}".format(mean, param))
# print("Best: {:.2%} using {}.".format(gridsearch2.best_score_, gridsearch2.best_params_))

# print("\n\n"+"--"*30)
# print("Decision Tree")
# means = gridsearch2.cv_results_['mean_test_score']
# params = gridsearch2.cv_results_['params']
# for mean, param in zip(means, params):
#     print("{:.2%} with: {}".format(mean, param))
# print("Best: {:.2%} using {}.".format(gridsearch2.best_score_, gridsearch2.best_params_))

# end = datetime.now()
# elapsed_time = end-start
# print("\n\n"+"--"*30)
# print("Total time:", elapsed_time.total_seconds())

# t0 = {'gradient_boosting': 84.16, 'neural_network': 81.25, 'support_vector_machine': 81.25, 'linear_discriminant_analysis': 81.25, 'logistic': 81.2, 'naive_bayes': 80.53, 'decision_tree': 80.48, 'k_nearest_neighbor': 80.48, 'random_forest': 79.7}
# t1 = {'logistic': 84.66, 'gradient_boosting': 83.84, 'support_vector_machine': 81.7, 'linear_discriminant_analysis': 81.59, 'random_forest': 80.89, 'neural_network': 79.79, 'decision_tree': 77.89, 'k_nearest_neighbor': 77.13, 'naive_bayes': 76.83}
# t2 = {'logistic': 89.51, 'support_vector_machine': 87.96, 'linear_discriminant_analysis': 85.8, 'k_nearest_neighbor': 85.67, 'gradient_boosting': 85.52, 'random_forest': 84.95, 'decision_tree': 83.07, 'neural_network': 81.76, 'naive_bayes': 80.76}
# t3 = {'random_forest': 91.02, 'support_vector_machine': 90.26, 'linear_discriminant_analysis': 89.52, 'naive_bayes': 87.37, 'logistic': 86.53, 'neural_network': 85.76, 'gradient_boosting': 85.71, 'decision_tree': 83.99, 'k_nearest_neighbor': 78.26}
# t4 = {'gradient_boosting': 88.74, 'neural_network': 84.16, 'support_vector_machine': 83.58, 'linear_discriminant_analysis': 82.86, 'logistic': 82.86, 'random_forest': 82.74, 'k_nearest_neighbor': 81.86, 'naive_bayes': 80.71, 'decision_tree': 80.6}
# t5 = {'gradient_boosting': 85.07, 'logistic': 83.72, 'support_vector_machine': 83.66, 'neural_network': 83.5, 'linear_discriminant_analysis': 81.54, 'random_forest': 81.39, 'k_nearest_neighbor': 80.06, 'naive_bayes': 78.71, 'decision_tree': 76.21}
# t6 = {'support_vector_machine': 88.2, 'linear_discriminant_analysis': 87.49, 'logistic': 86.79, 'neural_network': 86.72, 'random_forest': 86.72, 'gradient_boosting': 86.57, 'decision_tree': 85.87, 'naive_bayes': 85.38, 'k_nearest_neighbor': 82.2}
# t7 = {'logistic': 85.78, 'support_vector_machine': 85.75, 'linear_discriminant_analysis': 84.28, 'naive_bayes': 83.58, 'random_forest': 83.43, 'k_nearest_neighbor': 81.2, 'gradient_boosting': 81.15, 'decision_tree': 80.36, 'neural_network': 78.68}
# t8 = {'gradient_boosting': 81.48, 'support_vector_machine': 81.39, 'random_forest': 80.6, 'neural_network': 79.3, 'logistic': 77.9, 'linear_discriminant_analysis': 77.2, 'naive_bayes': 76.51, 'k_nearest_neighbor': 74.75, 'decision_tree': 73.0}
# t9 = {'gradient_boosting': 79.95, 'neural_network': 79.83, 'support_vector_machine': 79.15, 'random_forest': 79.15, 'linear_discriminant_analysis': 78.42, 'logistic': 78.38, 'k_nearest_neighbor': 76.93, 'decision_tree': 76.61, 'naive_bayes': 73.26}

# t = {}
# for key in t1.keys():
#     t[key] = round((t0[key]+t1[key]+t2[key]+t3[key]+t4[key]+t5[key]+t6[key]+t7[key]+t8[key]+t9[key])/10, 2)

# t = {key: val for key, val in sorted(t.items(), key = lambda ele: ele[1], reverse = True)}
# print(t)
# print("The best fscore is {} from the model {}".format(list(t.values())[0], list(t.keys())[0]))