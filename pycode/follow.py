# import tkinter as tk
# import random
# def callthiswhatevs(event):
#     if 'Motion' in str(event):
#         x, y = event.x, event.y
#         c.coords(rect, x, y)
#     else:
#         c.coords(rect, -10, -10)
# self.root = tk.Tk()
# self.root.geometry('500x500')
# c = tk.Canvas(self.root, width = 1600, height = 850, cursor = 'none')
# rr = ["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
# bit = rr[random.randrange(0, len(rr))]
# print(bit)
# rect = c.create_bitmap(-10, -10, bitmap = bit)
# c.bind('<Motion>', callthiswhatevs)
# c.bind('<Leave>', callthiswhatevs)
# c.grid()
# self.root.mainloop()

# import pyttsx3
# cump = pyttsx3.init()
# cump.setProperty('rate', 120)
# cump.setProperty('volume', 1)
# cump.runAndWait()

# from datetime import datetime
# a = datetime.self.now()
# b = "%z%Z\n%a = %A = %w\n%Y = %y / %b = %B = %m / %self.d\n%H = %I(24hrs) %p : %M : %S.%f\n%U(week no. first day of week is Sunday) = %W(Monday)\n%c | %x | %X | %%"
# print(a.strftime(b))


# DO NOT keep a = b = []
# you can keep a = b = 0 or a = b= "hi" but no a = b = []

# tk.Tk size  = 1600x900
# Canvas size = 795x1530

# import tkinter as tk
# self.root = tk.Tk()
# canvas = tk.Canvas(self.root)
# scrollbar = tk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
# scrollable_frame = tk.Frame(canvas)
# scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
# canvas.create_window((0, 0), window=scrollable_frame, anchor = 'nw')
# canvas.configure(yscrollcommand=scrollbar.set)
# for i in range(50):
#     tk.Label(scrollable_frame, width = 20, text = "Label").grid()
# canvas.grid(row = 0, column = 0)
# scrollbar.grid(row = 0, column = 1, sticky = 'ns')
# self.root.mainloop()

