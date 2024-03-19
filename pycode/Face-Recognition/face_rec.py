import face_recognition
import cv2

vid = cv2.VideoCapture(0)
counter = -1
check2 = 0

try: f = open("faceData.txt", "r")
except:
    f2 = open("faceData.txt", "w")
    f2.close()
    f = open("faceData.txt", "r")
fr = f.read()
knownfaces = {}
for line in fr.split("\n"):
    if not line: continue
    knownface = eval(line)
    knownfaces[knownface[-1]] = knownface[:-1]

while True:
    counter += 1
    if counter%5 != 0:
        cv2.imshow('Face Recognition', img)
        if cv2.waitKey(1) & 0xFF == ord('q'): break
        continue
    
    ret, img = vid.read()
    bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    facelocs = face_recognition.face_locations(bw_img)
    faceencs = face_recognition.face_encodings(bw_img)

    for i in range(len(facelocs)):
        faceenc, faceloc = faceencs[i], facelocs[i]
        check = face_recognition.face_distance(list(knownfaces.values()), faceenc)
        print(check)
        if True not in (check<=0.5):
            if check2 == 5:
                f.close()
                vid.release()
                cv2.destroyAllWindows()
                
                newname = input("Person not found. Input name: ")
                f3 = open("faceData.txt", "a")
                f3.write(str(list(faceenc)+[newname])+"\n")
                f3.close()
                exit()
            check2 += 1
            continue

        name = list(knownfaces.keys())[list(check).index(min(check))]
        cv2.putText(img, name, (faceloc[3], faceloc[0]-20), 5, 1, (255, 255, 0))
        cv2.rectangle(img, (faceloc[3], faceloc[0]), (faceloc[1], faceloc[2]), (0, 0, 0), 2)

f.close()
vid.release()
cv2.destroyAllWindows()