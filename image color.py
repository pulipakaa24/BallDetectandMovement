import cv2
import numpy as np

img = cv2.imread("LifeCam_Images/00.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_green = np.array([30, 70, 100])  # HSV values for lower bound
upper_green = np.array([40, 255, 255])  # HSV values for upper bound
mask = cv2.inRange(hsv, lower_green, upper_green)
result = cv2.bitwise_and(img, img, mask=mask)

def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the HSV color values at the clicked position
        hsv = cv2.cvtColor(np.uint8([[img[y, x]]]), cv2.COLOR_BGR2HSV)[0][0]
        print(f"Color at ({x}, {y}): H={hsv[0]}, S={hsv[1]}, V={hsv[2]}")

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", on_mouse)
cv2.imshow("Image", img)
cv2.imshow("Mask", mask)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()