import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import numpy as np
import tkinter as tk
from PIL import ImageGrab, Image
import win32gui
from keras.models import load_model

try: model = load_model("digit_rec_model")
except Exception() as ex:
    print("Error: There is no model")
    print("Need to create a new model\n")
    import train
    model = load_model("digit_rec_model")

root = tk.Tk()
root.title('Handwritten Single Digit Recognition')
root.geometry("+300+125")
root.config(bg= "#00FF00")
root.update()

r = 10
font = ("arial", 20)

def draw(e):
    board.create_oval(e.x-r, e.y-r, e.x+r, e.y+r, fill= "black")

def predict():
    HWND = board.winfo_id() 
    rect = win32gui.GetWindowRect(HWND)
    rect = [rect[0]+100, rect[1]+100, rect[2]+100, rect[3]+100]

    img = ImageGrab.grab(rect)
    
    img = img.resize((28,28))
    img = img.convert('L')
    img.save('first.jpeg')

    img = np.array(img)
    img = img.reshape(1,28,28,1)
    img = img/255.0

    numbers = list(range(10))
    predicted_results = list(model.predict([img])[0])

    predicted_number['text'] = ""

    for i in range(3):
        if i != 0:
            numbers.remove(predicted_result)
            predicted_results.remove(prob)

        prob = max(predicted_results)
        predicted_result = numbers[predicted_results.index(prob)]
        predicted_number['text'] += "{}. {} ({}%)\n".format(i+1, predicted_result, round(prob*100, 2))

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