import cv2
import numpy as np
import matplotlib.pyplot as plt

#cam resolution 1280x720
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

points = []
#green
glower = np.array([35,50,20])
gupper = np.array([90,220,255])
#blue
blower = np.array([91,50,20])
bupper = np.array([135,220,255])
#red
rlower1 = np.array([165,50,20])
rupper1 = np.array([180,220,255])
rlower2 = np.array([0,50,20])
rupper2 = np.array([15,220,255])
while True:

    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA)
    hf = frame.shape[0]
    wf = frame.shape[1]
    hdiv3 = hf//3
    wdiv3 = wf//3

    #divide the frame in 9 parts
    #top left
    tl = frame[hdiv3*2:hf, 0:wdiv3]
    #top middle
    tm = frame[hdiv3*2:hf, wdiv3:wdiv3*2]
    #top right
    tr = frame[hdiv3*2:hf, wdiv3*2:wf]
    #middle left
    ml = frame[hdiv3:hdiv3*2, 0:wdiv3]
    #middle middle
    mm = frame[hdiv3:hdiv3*2, wdiv3:wdiv3*2]
    #middle right
    mr = frame[hdiv3:hdiv3*2, wdiv3*2:wf]
    #bottom left
    bl = frame[0:hdiv3, 0:wdiv3]
    #bottom middle
    bm = frame[0:hdiv3, wdiv3:wdiv3*2]
    #bottom right
    br = frame[0:hdiv3, wdiv3*2:wf]

    parts = [tl, tm, tr, ml, mm, mr, bl, bm, br]
    i = 0
    for img in parts:
        #filter one color
        hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

        maskG = cv2.inRange(hsv, glower, gupper)
        maskB = cv2.inRange(hsv, blower, bupper)
        maskR1= cv2.inRange(hsv, rlower1, rupper1)
        maskR2= cv2.inRange(hsv, rlower2, rupper2)
        #if red
        maskR = cv2.bitwise_or(maskR1, maskR2)
        res = cv2.bitwise_and(img, img, mask= maskG)

        #convert to gray
        imgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)

        #convert to binary
        thresh = cv2.adaptiveThreshold(imgray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,15)

        blur = cv2.blur(thresh,(30,30))

        #find contours
        contours, hierarchy = cv2.findContours(blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        if len(contours) > 0:

            #sort contours
            contours = sorted(contours, key=cv2.contourArea, reverse=True)

            #get largest contour
            c = contours[0]

            #get bounding box from largest contour
            x,y,w,h = cv2.boundingRect(c)

            #draw bounding box
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

            #get center of bounding box
            x_center = int(x + w/2)
            y_center = int(y + h/2)

            #bottom left
            if(i == 0):
                points.append((x_center, hdiv3-y_center))
            #bottom middle
            elif(i == 1):
                points.append((x_center+wdiv3, hdiv3-y_center))
            #bottom right
            elif(i == 2):
                points.append((x_center+2*wdiv3, hdiv3-y_center))
            #middle left
            elif(i == 3):
                points.append((x_center, 2*hdiv3-y_center))
            #middle middle
            elif(i == 4):
                points.append((x_center+wdiv3, 2*hdiv3-y_center))
            #middle right
            elif(i == 5):
                points.append((x_center+2*wdiv3, 2*hdiv3-y_center))
            #top left
            elif(i == 6):
                points.append((x_center, hf-y_center))
            #top middle
            elif(i == 7):
                points.append((x_center+wdiv3, hf-y_center))
            #top right
            elif(i == 8):
                points.append((x_center+2*wdiv3, hf-y_center))


            #draw center point
            cv2.circle(img, (x_center, y_center), 5, (0, 0, 255), -1)
        i += 1

    cv2.imshow('Cam', frame)

    c = cv2.waitKey(1)
    if c == 27:
        plt.scatter(*zip(*points))
        plt.xlim(0, wf)
        plt.ylim(0, hf)
        plt.show()
        break

cap.release()
cv2.destroyAllWindows()
