import cv2
import time
cap = cv2.VideoCapture(0)


while True:

    retval, image = cap.read()

    if retval:

        cv2.imshow("My first cv app", image)


    key = cv2.waitKey(1)

    if key == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()