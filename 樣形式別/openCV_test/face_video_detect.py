import cv2


def video_sensor():
    cap = cv2.VideoCapture("test_video.mp4")
    faceCascade = cv2.CascadeClassifier("face_detect.xml")
     

    while True:
        ret, frame = cap.read()
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if ret:
            frame = cv2.resize(frame, (0,0), fx=2.0, fy=2.0)
            

            faceRect = faceCascade.detectMultiScale(frame, 1.1, 2)

            for(x, y, w, h) in faceRect:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            

            cv2.imshow("video", frame)
            
        else:
            break

        if cv2.waitKey(10) == ord('q'):
            break


if __name__ == '__main__':

    video_sensor()


