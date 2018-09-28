import cv2

cap = cv2.VideoCapture("http://192.168.43.1:8080/videofeed")

while True:
    _,frame = cap.read()
    cv2.imshow("Video",frame)

    if cv2.waitKey(1) == 27:
        exit(0)