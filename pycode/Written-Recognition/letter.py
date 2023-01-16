# Work In Progress

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import tkinter as tk
from PIL import ImageGrab, Image
import win32gui
import pytesseract as pytes

root = tk.Tk()
root.title('Letter Recognition')
root.geometry("+300+125")
root.config(bg= "#00FF00")
root.update()

r = 10
font = ("arial", 20)
pytes.pytesseract.tesseract_cmd = r"C:\Users\Gayathri\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.9_qbz5n2kfra8p0\LocalCache\local-packages\Python39\site-packages\pytesseract\pytesseract.exe"

def draw(e):
    board.create_oval(e.x-r, e.y-r, e.x+r, e.y+r, fill= "black")

def predict():
    HWND = board.winfo_id() 
    rect = win32gui.GetWindowRect(HWND)
    rect = [rect[0]+100, rect[1]+100, rect[2]+100, rect[3]+100]

    img = ImageGrab.grab(rect)
    
    words = pytes.image_to_string(img)
    predicted_number["text"] = words

board = tk.Canvas(root, width= 500, height= 400)
board.grid(row= 0, column= 0, padx= 10, pady= 10)
board.bind("<B1-Motion>", draw)

clear_btn = tk.Button(root, text= "Clear Board", command= lambda: board.delete("all"), bg= "red", font=font)
clear_btn.grid(row= 1, column= 0, sticky="ew", padx= 10, pady= 10)

predicted_number = tk.Label(root, bg= "cyan", font= font, text= "Draw in the center\non the white screen\nto the left", justify= 'left')
predicted_number.grid(row= 0, column= 1, sticky= "nsew", padx= 10, pady= 10)

rec_btn = tk.Button(root, text= "Recognise", command= predict, bg= "red", font= font, width= 25)
rec_btn.grid(row= 1, column= 1, sticky= "ns", padx= 10, pady= 10)

root.mainloop()