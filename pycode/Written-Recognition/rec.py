import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

import numpy as np
import tkinter as tk
from PIL import ImageGrab
import win32gui
import tensorflow as tf

try: model = tf.keras.models.load_model("digit_rec")
except Exception as ex:
    print("Error: There is no model")
    print("You need to create a new model\n")
    print("Go to train.py file to create a new model")
    quit()

root = tk.Tk()
root.title('Handwritten Digit Recognition')

r = 3
font = ("sans-serif", 20)

def draw(e):
    board.create_oval(e.x-r, e.y-r, e.x+r, e.y+r, fill= "black")

def clear_all():
    board.delete("all")

def predict():
    HWND = board.winfo_id()
    
    rect = win32gui.GetWindowRect(HWND)
    rect = (rect[0]+100, rect[1]+100, rect[2]+100, rect[3]+100)
    
    img = ImageGrab.grab(rect)
    img = img.resize((28,28))
    img = img.convert('L')
    
    img = np.invert(np.array(img))/255
    img = img.reshape(1, 28, 28, 1)

    predicted_results = list(model.predict([img])[0])

    predicted_number['text'] = ""
    
    for i in range(3):
    
        prob = max(predicted_results)
        pred_numb = predicted_results.index(prob)
    
        prob = round(prob*100, 2)
        predicted_results[pred_numb] = 0
        
        predicted_number['text'] += "{} ({}%)\n".format(pred_numb, prob)

board = tk.Canvas(root, width= 500, height= 400, bg="#ffffff")
board.grid(row= 0, column= 0)
board.bind("<B1-Motion>", draw)

clear_btn = tk.Button(root, text= "Clear Board", command= clear_all, bg= "red", font=font)
clear_btn.grid(row= 1, column= 0, sticky="ew")

predicted_number = tk.Label(root, bg= "cyan", font= font, text= "Draw in the center\non the white screen\nto the left", justify= 'left')
predicted_number.grid(row= 0, column= 1, sticky= "nsew")

rec_btn = tk.Button(root, text= "Recognise", command= predict, bg= "red", font= font, width= 25)
rec_btn.grid(row= 1, column= 1, sticky= "ns")

root.mainloop()