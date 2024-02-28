import cv2
import numpy as np

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Unable to open camera.")
    exit()

while True:
    ret, img = cap.read()

    if not ret:
        print("Error: Unable to capture frame.")
        break

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve circle detection
    gray_blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    # Use HoughCircles to detect circles
    circles = cv2.HoughCircles(
        gray_blurred,
        cv2.HOUGH_GRADIENT,
        dp=1,       # Inverse ratio of accumulator resolution to image resolution
        minDist=50,  # Minimum distance between detected centers
        param1=50,   # Lower threshold for the internal Canny edge detector
        param2=30,   # Threshold for center detection
        minRadius=5, # Minimum radius to be detected
        maxRadius=100 # Maximum radius to be detected
    )

    # If circles are found, draw them on the original image
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw the outer circle
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

    # Display the result
    cv2.imshow("Detected Circles", img)

    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()
