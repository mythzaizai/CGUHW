import cv2
import numpy as np

def img():

    img_data = cv2.imread("takagi.png")
    print(img_data)

    kernel = np.ones((3,3), np.uint8)   #np.uint8 8bit 0-255

    img_gray = cv2.cvtColor(img_data, cv2.COLOR_BGR2GRAY)       #灰階圖片
    img_blur = cv2.GaussianBlur(img_data, (3,3), 0)             #高斯模糊 (data,核(要基數),標準差)
    img_canny = cv2.Canny(img_data, 150, 200)                   #邊緣圖片 (data,最低,最高)
    img_dilate = cv2.dilate(img_canny, kernel, iterations=1)    #將邊緣圖片膨脹，把線條變粗 (canny, kernel array, 膨脹次數)
    img_erode = cv2.erode(img_dilate, kernel, iterations=1)     #圖片侵蝕，把線條變細




    #cv2.imshow("org", img_data)
    #cv2.imshow("gray", img_gray)
    #cv2.imshow("blur", img_blur)
    #cv2.imshow("canny", img_canny)
    cv2.imshow("dilate", img_dilate)
    cv2.imshow("erode", img_erode)



    cv2.waitKey(0)             #wait picture for how many


def video():

    cap = cv2.VideoCapture("噴火龍.mp4")

    while True:
        ret, frame = cap.read()

        if ret:
            frame = cv2.resize(frame, (0,0), fx=2.0, fy=2.0)    #resize video window size
            cv2.imshow("video", frame)
        else:
            break

        if cv2.waitKey(10) == ord('q'):
            break


def draw():
    img = np.zeros((600, 600, 3), np.uint8)
    cv2.line(img, (0,0), (img.shape[1], 300), (0,255,0), 2)

    cv2.imshow("draw", img)
    cv2.waitKey(0)



def empty(v):
    pass

def sensor_color():
    img_data = cv2.imread("takagi.png")
    img_data = cv2.resize(img_data, (0,0), fx=0.5, fy=0.5)

    img_hsv = cv2.cvtColor(img_data, cv2.COLOR_BGR2HSV)

    #create window
    cv2.namedWindow("TrackBar")
    cv2.resizeWindow("TrackBar", 640, 320)

    cv2.createTrackbar("Hue Min", "TrackBar", 0, 179, empty)    #色調
    cv2.createTrackbar("Hue Max", "TrackBar", 179, 179, empty)
    cv2.createTrackbar("Sat Min", "TrackBar", 0, 255, empty)    #飽和度
    cv2.createTrackbar("Sat Max", "TrackBar", 255, 255, empty)
    cv2.createTrackbar("Val Min", "TrackBar", 0, 255, empty)    #亮度
    cv2.createTrackbar("Val Max", "TrackBar", 255, 255, empty)


    while True:
        h_min = cv2.getTrackbarPos("Hue Min", "TrackBar")
        h_max = cv2.getTrackbarPos("Hue Max", "TrackBar")
        s_min = cv2.getTrackbarPos("Sat Min", "TrackBar")
        s_max = cv2.getTrackbarPos("Sat Max", "TrackBar")
        v_min = cv2.getTrackbarPos("Val Min", "TrackBar")
        v_max = cv2.getTrackbarPos("Val Max", "TrackBar")

        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])

        mask = cv2.inRange(img_hsv, lower, upper)
        result = cv2.bitwise_and(img_data,img_data,mask=mask)

        cv2.imshow("org", img_data)
        cv2.imshow("hsv", img_hsv)
        cv2.imshow("mask", mask)
        cv2.imshow("result", result)

        cv2.waitKey(1)



def img_contour():
    img_data = cv2.imread("takagi.png")
    imgContour = img_data.copy()


    img_data = cv2.cvtColor(img_data, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(img_data, 150, 200)
    contours, hierarchy = cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        cv2.drawContours(imgContour, cnt, -1, (255,255,255), 4)         #(data, cnt, 第幾個輪廓, color, 線條粗度)


    cv2.imshow("img", img_data)
    cv2.imshow("canny", canny)
    cv2.imshow("imgContour", imgContour)
    cv2.waitKey(0)


if __name__ == '__main__':
    
    #img()
    #video()
    #draw()
    #sensor_color()
    img_contour()
    


    print("success!")