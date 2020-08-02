# import tkinter as tk
# def callthiswhatevs(event):
#     x, y = event.x, event.y
#     c.coords(rect, x - 10, y - 10, x + 10, y + 10)
# root = tk.Tk()
# root.geometry('500x500')
# c = tk.Canvas(root, width = 1600, height = 850, bg = 'black')
# rect = c.create_rectangle(0, 0, 0, 0, fill = 'blue')
# c.bind('<Motion>', callthiswhatevs)
# c.grid()
# root.mainloop()


# import pyttsx3
# cump = pyttsx3.init()
# cump.setProperty('rate', 120)
# cump.setProperty('volume', 1)
# cump.runAndWait()

# from datetime import datetime
# a = datetime.now()
# b = "%z%Z\n%a = %A = %w\n%Y = %y / %b = %B = %m / %d\n%H = %I(24hrs) %p : %M : %S.%f\n%U(week no. first day of week is Sunday) = %W(Monday)\n%c | %x | %X | %%"
# print(a.strftime(b))


# DO NOT keep a = b = []
# you can keep a = b = 0 or a = b= "hi" but no list