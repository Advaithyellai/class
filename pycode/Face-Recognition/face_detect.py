import cv2
import face_recognition

video = cv2.VideoCapture(0)
faceLoc = a = 0

while True:
    a += 1

    ret, img = video.read()

    if a%5 == 0:
        bw_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        FacesLoc = face_recognition.face_locations(bw_img)
        
        for faceLoc in FacesLoc: cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 0, 0), 2)
        if not FacesLoc: faceLoc = None
    
    elif faceLoc: cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (0, 0, 0), 2)
    
    cv2.imshow("Face Detection", img)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

video.release()
cv2.destroyAllWindows()