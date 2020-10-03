# # Importing Library tkinter(python GUI(Graphical User Interface))
# import tkinter as tk
# import random
# from tkinter import font
# # app is the application(Window or Tk)
# app = tk.Tk()
# app.geometry('1600x900')
# # Font
# myfont = font.Font(root = app, family = 'Algerian', size = 15, weight = 'bold')
# # The place where the board is there(the Canvas)
# root = tk.Canvas(app, height = 795, width = 795)
# root_2 = tk.Frame(app)
# root_2.grid(row = 0, column = 1, sticky = 'ns')
# root.create_rectangle(10, 10, 780, 780, fill = 'light green')
# # Binding for coordinates
# # root.bind('<Button>', print)
# # Creating Top lines of properties
# # Left line
# root.create_line(129, 10, 129, 780)
# # Top line
# root.create_line(10, 129, 780, 129)
# # Right Line
# root.create_line(651, 10, 651, 780)
# # Bottom Line
# root.create_line(10, 651, 780, 651)
# # 58x130 area, corners are 130x130
# blue = root.create_rectangle(650, 765, 715, 780, fill = 'blue')
# red = root.create_rectangle(715, 765, 780, 780, fill = 'red')
# green = root.create_rectangle(715, 750, 780, 765, fill = 'green')
# yellow = root.create_rectangle(650, 750, 715, 765, fill = 'yellow')


# # Colors of properties and text which should be shown in Picadilly's line(Top line)
# colors = ['red', 'khaki1', 'red', 'red', 'black', 'yellow', 'yellow', 'white', 'yellow']
# amount = ['  $2.2 M\n\nSTRAND', 'CHANCE\n     ???', '$2.2 M\n\nFLEET\nSTREET', '   $2.4 M\n\nTRAFA-\nLGAR\nSQUARE', \
#           '  $2 M \n\nFENCHU-\nRCH ST.', '   $2.6 M\n\nLEICESTER\nSQUARE', "$2.6 M\n\nCOVE-\nNTRY\nSTREET", \
#           "$1.5 M\n\nWATER\nWORKS", "$2.8 M\n\nPICCA-\nDILLY"]
# # Creating Picadilly's line(Top line)
# for y in range(2, 11):
#     x = 58*(y+1)+13
#     if y != 10:
#         root.create_line(x, 10, x, 130)
#     root.create_text(x-29, 65, text = amount[y-2])
#     root.create_rectangle(x-58, 110, x, 130, fill = colors[y-2])

# # Repeating same thing for Mayfair line(Right line)
# colors = ['green', 'green', None, 'green', 'black', 'khaki1', 'blue', 'purple', 'blue']
# amount = ['REGENT STREET\n        $3 M', 'OXFORD STREET\n        $3 M', 'COMMUNITY\n      CHEST', 'BOND STREET\n    $3.2 M', \
#           'LIVERPOOL ST. \n      $2 M', 'CHANCE\n      ???', "PARK LANE\n     $3.5 M", \
#           "SUPER TAX\n PAY $1 M", "MAYFAIR\n    $4 M"]
# for y in range(2, 11):
#     x = 58*(y+1)+18
#     if y != 10: root.create_line(650, x, 780, x)
#     root.create_text(720, x-29, text = amount[y-2])
#     root.create_rectangle(650, x-58, 670, x, fill = colors[y-2])

# # Repeating same thing for Old Kent line(Left line)
# colors = ['deep sky blue', 'deep sky blue', 'khaki1', 'deep sky blue', 'black', 'purple', 'saddle brown', None, 'saddle brown']
# amount = ['PENTO-\nNVILLE\nROAD\n\n $1.2 M', 'EUSTON\n  ROAD\n\n $1 M', 'CHANCE\n     ???', 'ANGEL,\nISLIN-\nGTON\n\n $1 M', \
#           ' KINGS\nCROSS\n\n  $2 M', 'INCOME\n    TAX\n\nPAY $2 M', "WHITEC-\nHAPEL\nROAD\n\n $600 K", \
#           "COMMU-\n    NITY\n  CHEST", "OLD\nKENT\nROAD\n\n$600 K"]
# for y in range(2, 11):
#     x = 58*(y+1)+13
#     if y != 10:
#         root.create_line(x, 650, x, 780)
#     root.create_text(x-29, 715, text = amount[y-2])
#     root.create_rectangle(x-58, 670, x, 650, fill = colors[y-2])

# # Repeating same thing for Vine street line(Left line)
# colors = ['orange', 'orange', None, 'orange', 'black', 'deep pink', 'deep pink', 'white', 'deep pink']
# amount = ['VINE STREET\n     $2 M', 'MARLBOROUGH\n        STREET\n        $1.8 M', 'COMMUNITY\n      CHEST', 'BOW STREET\n    $1.8 M', \
#           'MARYLEBONE\n    STATION\n      $2 M', "NORTHUMB 'ND\n       AVENUE\n          $1.6", "WHITEHALL\n    $1.4 M", \
#           "  ELECTRIC\nCOMPANY\n     $1 M", "PALL MALL\n    $1.4 M"]
# root.create_text(65, 161, text = amount[0])
# root.create_rectangle(130, 131, 110, 193, fill = colors[0])
# for y in range(2, 10):
#     x = 58*(y+1)+18
#     root.create_line(130, x, 10, x)
#     if y == 2:
#         continue
#     root.create_text(60, x-29, text = amount[y-2])
#     root.create_rectangle(130, x-58, 110, x, fill = colors[y-2])
# root.create_text(60, 625, text = amount[-1])
# root.create_rectangle(130, 597, 110, 649, fill = colors[-1])

# # Monopoly name
# root.create_text(400, 400, text = "MONOPOLY", font = ('Algerian', 50, 'bold'))
# root.create_text(400, 450, text = "(Electronic banking)", font = ('Algerian', 30, 'bold'))

# # Creating corners(Ignore property variable i made a mistake)
# properties = {'    |\n    |\n<--- Go ' : (700, 715), 'Free\nParking' : (63, 65), "Go To\n JAIL" : (700, 65), "Jail": (63, 715)}
# for ele, vals in properties.items():
#     root.create_text(vals, text = ele, font = myfont)
# pos = 0
# player = 1
# players = ['Player 1', 'Player 2', 'Player 3', 'Player 4']
# root.grid(row = 0, column = 0)
# a = ran = None
# b = [0, 0, 0, 0]
# b2 = [0, 0, 0, 0]
# def move(mover, added = None):
#     global player, pos, a, ran
#     root.coords(blue, 130, 650, 145, 670)
#     if mover == 0 and ran:
#         die1['text'] = 1#random.randrange(1, 7)
#         die2['text'] = 5#random.randrange(1, 7)
#         addie = int(die1.cget('text'))+int(die2.cget('text'))
#         a = (650-(addie*58))+5
#         if b2[player-1]+addie > 10:
#             move(1, (addie+b2[player-1])-10)
#             return
#         if player == 1:
#             x2 = root.coords(blue)
#             x2 = x2[2]
#             root.coords(blue, x2-(650-a)-69, 635, x2-(650-a)-40, 650)
#         elif player == 2:
#             x2 = root.coords(red)
#             x2 = x2[2]
#             root.coords(red, x2-(650-a)-105, 635, x2-(650-a)-76, 650)
#         elif player == 3:
#             x2 = root.coords(green)
#             x2 = x2[2]
#             root.coords(green, x2-(650-a)-133, 620, x2-(650-a)-105, 635)
#         else:
#             x2 = root.coords(yellow)
#             x2 = x2[2]
#             root.coords(yellow, x2-(650-a)-40, 620, x2-(650-a)-11, 635)
#         if player == 4:
#             ran = 1
#             player = 1
#             roller['text'] = "Roll {}".format(players[0])
#             return
#         roller['text'] = "Roll {}".format(players[player-1])
#         player += 1
#     elif mover == 1 and added:
#         x2 = root.coords(blue)
#         x2 = x2[2]
#         if player == 1:
#             # 598, 540
#             root.coords(blue, 130, 58*added+482, 145, 58*added+424)
#         elif player == 2:
#             root.coords(red, x2-(650-a)-63, 635, x2-(650-a)-5, 650)
#         elif player == 3:
#             root.coords(green, x2-(650-a)-63, 635, x2-(650-a)-5, 650)
#         else:
#             root.coords(yellow, x2-(650-a)-63, 635, x2-(650-a)-5, 650)
#         roller['text'] = "Roll {}".format(players[player-1])
#         player += 1 
#     elif mover == 0:
#         die1['text'] = 1#random.randrange(1, 7)
#         die2['text'] = 1#random.randrange(1, 7)
#         addie = int(die1.cget('text'))+int(die2.cget('text'))
#         a = 58*addie
#         if player == 1:
#             x1, x2 = root.coords(blue)[0], root.coords(blue)[2]
#             root.coords(blue, x1-a, 635, x2-a, 650)
#         elif player == 2:
#             x1, x2 = root.coords(red)[0], root.coords(red)[2]
#             root.coords(red, x1-a, 635, x2-a, 650)
#         elif player == 3:
#             x1, x2 = root.coords(green)[0], root.coords(green)[2]
#             root.coords(green, x1-a, 620, x2-a, 635)
#         else:
#             x1, x2 = root.coords(yellow)[0], root.coords(yellow)[2]
#             root.coords(yellow, x1-a, 620, x2-a, 635)
#         if player == 4:
#             ran = 1
#             player = 1
#             roller['text'] = "Roll {}".format(players[0])
#             return
#         roller['text'] = "Roll {}".format(players[player-1])
#         player += 1

# def roll():
#     global player
#     if b[player-1] == 0:
#         move(0)
#     elif b[player-1] == 1:
#         move(1)
#     elif b[player-1] == 2:
#         move(2)
#     else:
#         move(3)

# die1 = tk.Label(root_2, bg = 'black', width = 10, height = 5, borderwidth = 3, fg = 'white', text = "Player1's ", font = myfont)
# die2 = tk.Label(root_2, bg = 'black', width = 10, height = 5, borderwidth = 3, fg = 'white', text = "Turn, Roll", font = myfont)
# die1.grid(row = 0, column = 0, sticky = 'w')
# die2.grid(row = 0, column = 0, sticky = 'e')
# roller = tk.Button(root_2, text = "Roll {}".format(players[0]), width = 22, command = roll, font = myfont)
# roller.grid(row = 1, column = 0)
# app.mainloop()
# # pwd minecraftwarrior19@215 - Codetantra and coursera
# # vimudium@gmail.com
# # sreyasatluri@gmail.com