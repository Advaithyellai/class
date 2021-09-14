import face_recognition
import cv2
import numpy as np
import tkinter as tk

def nameget(event):
    if event:
        global name
        
        name = nam.get()
        nam.grid_forget()
        
        label["text"] = "Run the app again for recognition."
        
        nameget(None)
    
    else: root.after(3500, root.destroy)

video = cv2.VideoCapture(0)

counter = correct = incorrect = c = 0
text = "  "
penc = -1

try: f = open("faceData.txt", "r")
except:
    f2 = open("faceData.txt", "w")
    f2.close()
    f = open("faceData.txt", "r")
fr = f.read()

lenc = []

for line in fr.split("\n"):
    if not line: continue

    line2 = eval(line)
    
    lenc.append(line2)

torf2 = False
LLoc = None
ltext = []
ppl = []

while True:

    counter += 1
    if not (counter%5 == 0):
        
        if torf2:
            
            cv2.imshow("Face Recognition", img)
            if cv2.waitKey(1) & 0xFF == ord('q'): break
        
        continue
    
    torf2 = True

    ret, img = video.read()

    bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    try:
        lLoc = face_recognition.face_locations(bw_img)

    except Exception as ex:
        if not lLoc: continue
    
    faceenc = face_recognition.face_encodings(bw_img)
    faceenc2 = faceenc

    if counter >= 25:
        
        for faceLoc in lLoc:
        
            faceEnc = list(faceenc2[lLoc.index(faceLoc)])

            if True:
                counter = 1
                torf = False

                penc2 = {}

                for encs in lenc:
                    
                    sameface = face_recognition.compare_faces([np.array(encs[0:-1])], faceenc[0])[0]
                    
                    if sameface:
                        sameface2 = face_recognition.face_distance([np.array(encs[0:-1])], faceenc[0])[0]
                        penc2[sameface2] = lenc.index(encs)
                        torf = True
                
                nothing = False

                if len(penc2) > 1:
                    l = 100
                    
                    for key in penc2.keys():
                        if key < l: l = key
                    
                    c2 = list(penc2.keys()).index(l)
                
                elif len(penc2) == 1: c2 = 0

                else: nothing = True
                
                if not nothing: text = lenc[list(penc2.values())[c2]][-1]

            if torf:
                
                penc = lenc.index(encs)

                if correct and incorrect >= 5: correct = incorrect = 0
                elif correct and not incorrect: incorrect += 1

            else:
                
                correct += 1

                if correct >= 2:

                    video.release()
                    cv2.destroyAllWindows()
                    
                    f3 = open("faceData.txt", "a")

                    name = None
                    
                    root = tk.Tk()
                    
                    root.title("Register for Face Recognition")
                    root.geometry("+600+300")

                    label = tk.Label(root, text= "Enter your name now\nfor further recognition",\
                                    font=("Algerian", 15))
                    label.pack()

                    nam = tk.Entry(root, font=("Algerian", 15))
                    nam.pack(pady = 20)
                    nam.bind("<Return>", nameget)

                    root.mainloop()

                    if not name: name = "unknown"
                    
                    f3.write(str(faceEnc+[name])+"\n")

                    f3.close()

                    exit()
                        
            cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 0, 0), 2)
            cv2.putText(img, text, (faceLoc[3]+30, faceLoc[0]-20),\
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 0))

            ltext.append(text)
        
        LLoc = lLoc

    elif LLoc:
        
        for faceLoc in LLoc:
            
            text = ltext[LLoc.index(faceLoc)]
            
            cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 0, 0), 2)
            cv2.putText(img, text, (faceLoc[3]+30, faceLoc[0]-20),\
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 255, 0))
            
            if text not in ppl:
                ppl.append(text)

video.release()
cv2.destroyAllWindows()
f.close()