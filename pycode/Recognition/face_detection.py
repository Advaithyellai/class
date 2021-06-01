# import cv2

# face_cascade = cv2.CascadeClassifier('face-data//Image_face.xml')
# eye_cascade = cv2.CascadeClassifier('face-data//all_eye.xml')

# img = cv2.imread('face-data//face_1.jpg')

# faces = face_cascade.detectMultiScale(img, 1.1, 4)
# eyes = eye_cascade.detectMultiScale(img, 1.1, 4)

# for (x, y, w, h) in faces: cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# for (x, y, w, h) in eyes: cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 2)

# cv2.imshow("Faces and eyes found", img)

# print('Found {} faces'.format(len(faces)))

# ok_flag = True
# while ok_flag:
#     if cv2.waitKey(0) == ord('q'): ok_flag = False

# cv2.destroyAllWindows()


# import numpy as np
# import face_recognition
# import cv2

# path = input("Type in the selected image:   ")

# img = cv2.imread("dataImages//{}.jpg".format(path))
# bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# faceLoc = face_recognition.face_locations(bw_img)[0]
# faceenc = face_recognition.face_encodings(bw_img)
# faceEnc = list(faceenc[0])

# f = open("faceData.txt", "r")
# fr = f.read()

# for line in fr.split("\n"):
#     try:
#         if line == "":
#             sameface = False
#             break
#         line2 = eval(line)
#         line = line2[0:-1]
#         sameface = face_recognition.compare_faces([np.array(line)], faceenc[0])[0]
#         if sameface: break
#     except Exception as ex: pass

# f.close() 

# if sameface:
#     f2 = open("faceData.txt", "r")
#     cv2.putText(img, line2[-1], (faceLoc[3]-5, faceLoc[0]-20),\
#         cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0))

# else: 
#     f2 = open("faceData.txt", "a")
#     name = input("Who is in the image?   ")
#     f2.write(str(faceEnc+[name])+"\n")
#     print("saved the image successfuly")
#     cv2.putText(img, name, (faceLoc[3]-5, faceLoc[0]-20),\
#         cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 0))

# f2.close()

# cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 0, 0), 2)

# cv2.imshow("Face", img)
# cv2.waitKey(0)



import face_recognition
import cv2
import numpy as np
import tkinter as tk
import pyttsx3

def nameget(event):
    if event:
        global name
        
        name = nam.get()
        
        label["text"] = "Welcome aboard {}!!!".format(name)
        
        nameget(None)
    
    else: root.after(3500, root.destroy)

video = cv2.VideoCapture(0)

comp = pyttsx3.init()

comp.setProperty('rate', 140)
comp.setProperty('volume', 1)

counter = correct = incorrect = c = 0
text = "  "
penc = -1

f = open("faceData.txt", "r")
fr = f.read()
f2 = open("faceData.txt", "r")

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
            
            cv2.imshow("Face", img)
            if cv2.waitKey(1) & 0xFF == ord('q'): break
        
        continue
    
    torf2 = True

    ret, img = video.read()

    bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    try:
        lLoc = face_recognition.face_locations(bw_img)
        # faceLoc = lLoc[0]

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
                    root.configure(bg= "red")
                    root.geometry("+600+300")

                    label = tk.Label(root, text= "Welcome! Type in your name\n to registering for Face Recognition!",\
                                    font=("Elephant", 15), bg= "cyan", fg= "saddle brown")
                    label.pack()

                    nam = tk.Entry(root, font=("Elephant", 15), fg="Blue")
                    nam.pack(pady = 20)
                    nam.bind("<Return>", nameget)

                    root.mainloop()
                    
                    f3.write(str(faceEnc+[name])+"\n")

                    f3.close()

                    comp.say("Welcome aboard "+name)
                    comp.runAndWait()

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
                if text == "Advaith": text2 = "Hello Advaith sire u are the greatest of the great"
                else: text2 = "Hello {}, you are recognised".format(text)
                comp.say(text2)
                comp.runAndWait()

video.release()
cv2.destroyAllWindows()