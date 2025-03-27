import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'Haarcascade_frontalface_default.xml')
cap =cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Cemera not found!") 
    exit()
while True:
    ret, frame= cap.read()

    if not ret:

        print("Failed to capture frame")
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y),(x+w, y+h),(0,255,0),2)
        cv2.imshow('Face Detector', frame)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()