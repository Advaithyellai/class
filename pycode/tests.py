# a = (1, 2, 3, 4, 5)
# b = a
# a = (1, 2, 3)
# c = [1, 2, 3, 4, 5]
# d = c
# c = [1, 2, 3]
# print(list(b))
# print(d)

import tkinter as tk

def clicked_number(e, typing=False):
    if type: operation = e
    else: operation = e.widget['text']

    if operation == 'CE': display["text"] = display["text"][0:-1]
    elif operation == 'answer': display["text"] += prev_ans
    else: display['text'] += operation

def evaluate(e):
    global prev_ans

    try:
        answer = eval(display['text'])
        if float(answer)%1 == 0: answer = int(answer)
        
        answer = str(answer)
        prev_ans = answer

    except:
        answer = "ERROR"
        prev_ans = 0
    
    display["text"] = answer

def typed(e):
    info = e.keysym

    if info.isnumeric(): clicked_number(e.keysym, True)
    elif info in funcs.keys(): clicked_number(funcs[info], True)
    elif info in ["Return", "equal"]: evaluate(None)
    elif info == "a": clicked_number('answer', True)
    elif info == "BackSpace": clicked_number("CE", True)

app = tk.Tk()
app.title('Calculator App')
app.geometry("580x650")

prev_ans = 0
funcs = {"asterisk":"*", "slash":"/", "parenleft":"(", "parenright":")", "plus":"+", "minus":"-", "period":"."}

app.bind("<Key>", typed)

display = tk.Label(app, anchor='e', font=('Courier', 20, "bold"), borderwidth=2, relief='solid', background="aqua")
display.grid(row=0, column=0, sticky='nsew', columnspan=4)
app.rowconfigure(0, weight=1)

texts = [('(', ')', 'ex', "CE"), ('1', '2', '3', '+'), ('4', '5', '6', '-'), ('7', '8', '9', '*'),
    ('0', 'Answer', 'ex', '/')]
for r in range(1, 6):
    app.rowconfigure(r, weight=1)
    for c in range(0, 4):
        if r == 1: app.columnconfigure(c, weight=1)
        
        set_text = texts[r-1][c]
        if set_text == "ex": continue
        
        b = tk.Button(app, text=set_text, background='red', font=(20))
        b.grid(row=r, column=c, sticky='nsew')
        b.bind("<Button-1>", clicked_number)

bdot = tk.Button(app, text=".", background='red', font=("Arial", 20, "bold"))
bdot.grid(row=1, column=2, sticky='nsew')
bdot.bind("<Button-1>", clicked_number)

benter = tk.Button(app, text="=", background='red', font=(20))
benter.grid(row=5, column=2, sticky='nsew')
benter.bind("<Button-1>", evaluate)

app.mainloop()