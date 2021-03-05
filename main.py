"""
Project by Clinton Anani
A simple intro to openCV
This project demonstrates reading images and videos, as
well as writing them to local storage

github: yendiDev
email: kceequan01@gmail.com

"""

import cv2

# load image
img = cv2.imread('lena.jpg', -1)

# show image
# cv2.imshow('Lena Image', img)
# cv2.waitKey(2000)
# cv2.destroyAllWindows()

# write image to new file
# cv2.imwrite('lena_copy.jpg', img)

# showing video
cap = cv2.VideoCapture(0)

# fourcc for video
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# video writer class
writer = cv2.VideoWriter('recorded_video.avi', fourcc, 20.0, (640, 480))

while cap.isOpened():
    return_val, frame = cap.read()
    if return_val:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        writer.write(frame)
        cv2.imshow('Recording...', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()