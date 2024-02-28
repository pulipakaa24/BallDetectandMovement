import cv2
import numpy as np

def white_balance(img):
    # Calculate the average color of the image
    avg_color = np.mean(img, axis=(0, 1))

    # Calculate the scaling factor for each channel
    scale = [128.0 / val for val in avg_color]

    # Apply the scaling factor to each channel
    balanced_img = cv2.multiply(img, np.array(scale))

    return balanced_img

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Unable to capture frame.")
        break
    frame = white_balance(frame)
    cv2.imshow("Balanced", frame)
    if cv2.waitKey(30) == 27:
        break

cap.release()
cv2.destroyAllWindows()