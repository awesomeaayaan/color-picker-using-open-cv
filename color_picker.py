#building color picker using track bar
import cv2
import numpy as np

def cross(x):
    pass

#create blank images either black or white(np.zeros for black and np.ones for white)
img = np.zeros((300,512,3),np.uint8)#width 300,hight 51 channel 3 and uint-unsignedinteger
cv2.namedWindow("color Picker")#name of the window

#create a switch  where we can ON or OFF for color picker
s1 = "0:off\n1:ON"
cv2.createTrackbar(s1,"color Picker",0,1,cross)#switch is fixed on the trackbar(s-string will pass,color picker windwo ,starting value-0,ending value-1,if nothing to do then cross fucntion is used)

#creating trackbar foradjusting colors RGB
cv2.createTrackbar("R","color Picker",0,255,cross)#track bar start with 0 and end with 255
cv2.createTrackbar("G","color Picker",0,255,cross)
cv2.createTrackbar("B","color Picker",0,255,cross)



while True:
    cv2.imshow("color Picker",img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord("q"):#TO exit the window
        break

#now get the trackbar position
    s = cv2.getTrackbarPos(s1,"color Picker")
    r = cv2.getTrackbarPos("R","color Picker")
    g = cv2.getTrackbarPos("G","color Picker")
    b = cv2.getTrackbarPos("B","color Picker")
   
    if s == 0:
        img[:] = 0
    else:
        img[:] = [r,g,b]
       
cv2.destroyAllWindows()       
