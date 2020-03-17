import cv2

cap = cv2.VideoCapture(0)

while True:

    retval, image = cap.read()

    print(type(image))

    if retval:

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        cv2.imshow("My capture", gray)


    key = cv2.waitKey(1)

    if key == ord("q"):
        break