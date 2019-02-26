import numpy as np
import cv2


cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    dst = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # blur_frame = cv2.GaussianBlur(frame, (3, 3), 0) 

    # retval, dst = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

    # Display the resulting frame
    cv2.imshow('frame', dst)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        height, width = dst.shape
        res = cv2.resize(dst, (int(0.4*width), int(0.4*height)),
                         interpolation=cv2.INTER_CUBIC)
        cv2.imwrite('1.png', res)
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
