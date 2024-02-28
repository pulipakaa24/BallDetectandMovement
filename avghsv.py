import cv2
import numpy as np

# Open a camera capture
cap = cv2.VideoCapture(0)  # Use 0 for default camera, change to another number if you have multiple cameras

if not cap.isOpened():
    print("Error: Unable to open camera.")
    exit()

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error: Unable to capture frame.")
        break

    # Convert the BGR image to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the center of the frame
    center_x, center_y = frame.shape[1] // 2, frame.shape[0] // 2
    roi_size = 50  # Size of the region of interest (adjust as needed)

    # Define the region of interest (ROI)
    roi = hsv[center_y - roi_size // 2 : center_y + roi_size // 2, center_x - roi_size // 2 : center_x + roi_size // 2, :]

    # Calculate the average HSV values for the ROI
    average_hsv_roi = np.mean(roi, axis=(0, 1))

    # Display the original frame, draw the ROI, and show the average HSV values
    cv2.imshow("Original Frame", frame)
    cv2.rectangle(frame, (center_x - roi_size // 2, center_y - roi_size // 2), (center_x + roi_size // 2, center_y + roi_size // 2), (0, 255, 0), 2)
    cv2.imshow("ROI", frame)
    print("Average HSV values for ROI:", average_hsv_roi)

    # Break the loop if 'ESC' key is pressed
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()
