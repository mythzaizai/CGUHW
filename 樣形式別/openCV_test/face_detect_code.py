import cv2



def img_sensor():

    img = cv2.imread("S__60137489.jpg")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray, (21,21), 0)

    faceCascade = cv2.CascadeClassifier("face_detect.xml")
    faceRect = faceCascade.detectMultiScale(gray, 1.2, 2)                  #(data, 縮小倍數, 被框幾次才被偵測到)

    for(x, y, w, h) in faceRect:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)


    cv2.imshow("img", img)
    cv2.waitKey(0)


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



def camera():

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    faceCascade = cv2.CascadeClassifier("face_detect.xml")

    if not cap.isOpened():
        print("Cannot not find camera...")
        return

    while(True):

        try:

            ret, frame = cap.read()
            if not ret:
                print("No signal! Exiting..")
                break


            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faceRect = faceCascade.detectMultiScale(frame, 1.3, 10)



            face_img = frame

            for(x, y, w, h) in faceRect:
                

                face_img = frame[y-10:y+h+10, x-10:x+h+10]      #臉部畫面
                face_img = cv2.resize(face_img, (0,0), fx=2.0, fy=2.0) 

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)




            cv2.imshow("camera", frame)

            cv2.imshow("face_window", face_img)



            if cv2.waitKey(100) == ord('q'):
                cv2.imwrite('./outputData/face.jpg', face_img)
                cap.release()
                cv2.destroyAllWindows()
                break


        except:
            continue



if __name__ == '__main__':
    #img_sensor()
    video_sensor()
    #camera()

