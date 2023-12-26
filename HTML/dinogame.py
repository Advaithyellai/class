import tkinter as tk
from PIL import Image, ImageTk

def space

app = tk.Tk()
app.title("Dinosaur Game!")
root = tk.Canvas(app, bg = "white")

img = Image.open("trex.png")
img = ImageTk.PhotoImage(img.resize((100, 100)))
dino = root.create_image(80, 300, image=img)

root.grid(row=0, column=0, sticky="nsew")
app.rowconfigure(0, weight=1)
app.columnconfigure(0, weight=1)
app.geometry("1020x370+250+200")
app.bind("<space>", print)
app.mainloop()