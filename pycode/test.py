# import tkinter as tk

# root = tk.Tk()
# root.geometry('1600x900')
# root.title("Dots and Boxes")
# # To do: maze, clock, calendar, google, cleaner, notes, maps, contacts, ultimate banking [ listboxes ]

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


# def change(event):
#     global coords1, cont
#     if event.x >= 15 and event.x <= 145:
#         if event.y >= 0 and event.y <= 15:
#             if cont == 0:
#                 head.create_line(coords1, fill = 'red')
#                 cont = 1
#             else:
#                 cont = 0
#                 head.create_line(coords1, fill = 'blue')
#         if event.y >= 145 and event.y <= 155:
#             if cont == 0:
#                 head.create_line(coords3, fill = 'red')
#                 cont = 1
#             else:
#                 cont = 0
#                 head.create_line(coords3, fill = 'blue')
#     elif event.x >= 0 and event.x <= 15:
#         if event.y >= 15 and event.y <= 145:
#             if cont == 0:
#                 head.create_line(coords2, fill = 'red')
#                 cont = 1
#             else:
#                 cont = 0
#                 head.create_line(coords2, fill = 'blue')
# head = tk.Canvas(root, height = 850, width = 1600)
# head.grid()
# cont = 0
# coords1 = [10, 10, 150, 10]
# coords2 = [10, 10, 10, 150]
# coords3 = [10, 150, 150, 150]
# coords4 = [150, 150, 150, 10]
# head.create_line(coords1, dash = (6, 3))
# head.create_line(coords2, dash = (6, 3))
# head.create_line(coords3, dash = (6, 3))
# head.create_line(coords4, dash = (6, 3))
# head.create_oval([5, 5, 15, 15], fill = 'green')
# head.bind('<Button>', change)

# root.mainloop()