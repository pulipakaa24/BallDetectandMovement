import cv2
import numpy as np
frame = None
def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Get the HSV color values at the clicked position
        hsv = cv2.cvtColor(np.uint8([[frame[y, x]]]), cv2.COLOR_BGR2HSV)[0][0]
        print(f"Color at ({x}, {y}): H={hsv[0]}, S={hsv[1]}, V={hsv[2]}")

# Open a camera capture
cap = cv2.VideoCapture(0)  # Use 0 for default camera, change to another number if you have multiple cameras

if not cap.isOpened():
    print("Error: Unable to open camera.")
    exit()

cv2.namedWindow("origFrame")
cv2.setMouseCallback("origFrame", on_mouse)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to capture frame.")
        break

    # Convert the BGR image to HSV
    blurFrame = cv2.GaussianBlur(frame, (17,17), 0)
    hsv = cv2.cvtColor(blurFrame, cv2.COLOR_BGR2HSV)

    # Define the color range you want to detect (here, it's green)
    lower_green = np.array([40, 50, 50])  # HSV values for lower bound
    upper_green = np.array([60, 255, 255])  # HSV values for upper bound

    # Threshold the image to get a binary mask
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Apply the mask to the original image
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame, mask, and the result
    cv2.imshow("origFrame", frame)
    cv2.imshow("Mask", mask)
    cv2.imshow("Result", result)

    # Break the loop if 'ESC' key is pressed
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()