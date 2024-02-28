import cv2
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np

frame = None
lower_green = np.array([30, 50, 50]) 
upper_green = np.array([40, 255, 255])

# Function to handle button click event
def button_click():
    global lower_green
    global upper_green
    height, width, _ = frame.shape
    cx = width // 2
    cy = height // 2
    # Get the HSV color values at the clicked position
    hsv = cv2.cvtColor(np.uint8([[frame[cy, cx]]]), cv2.COLOR_BGR2HSV)[0][0]
    lower_green = np.array([max(hsv[0] - 5, 0), max(hsv[1] - 10, 0), max(hsv[2] - 100, 0)])
    upper_green = np.array([min(hsv[0] + 5, 255), min(hsv[1] + 50, 255), 255])
    print(f"Color at ({cx}, {cy}): H={hsv[0]}, S={hsv[1]}, V={hsv[2]}")

# OpenCV video capture
cap = cv2.VideoCapture(0)

# Create Tkinter window
root = tk.Tk()
root.title("OpenCV with Buttons")

# Function to update OpenCV window
def update():
    global frame
    global lower_green
    global upper_green
    ret, frame = cap.read()
    if ret:
        # Convert the BGR image to HSV
        blurFrame = cv2.GaussianBlur(frame, (17,17), 0)
        hsv = cv2.cvtColor(blurFrame, cv2.COLOR_BGR2HSV)

        # Threshold the image to get a binary mask
        mask = cv2.inRange(hsv, lower_green, upper_green)

        # Apply the mask to the original image
        result = cv2.bitwise_and(frame, frame, mask=mask)

        # Convert OpenCV image to Tkinter format
        img = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
        img = Image.fromarray(img)
        img = ImageTk.PhotoImage(image=img)

        # Update the OpenCV window
        panel.img = img
        panel.config(image=img)
        panel.after(10, update)

# Create a button in Tkinter
button = tk.Button(root, text="Click me", command=button_click)
button.pack(pady=10)

# Create a panel to display OpenCV image
panel = tk.Label(root)
panel.pack()

# Start updating the OpenCV window
update()

# Run the Tkinter main loop
root.mainloop()

# Release the video capture object
cap.release()