import cv2
import numpy as np

# 1. Open your computer's webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Running pure OpenCV loop... Press 'q' to quit.")

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # --- PURE OPENCV PIXEL MANIPULATION ---

    # Step A: Convert the BGR frame to Grayscale. 
    # This collapses the 3 color channels (Blue, Green, Red) into a single intensity channel (0 to 255).
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Step B: Apply a Blur to smooth out camera noise and grain.
    # cv2.GaussianBlur takes a "kernel size" (must be odd numbers, like 15x15).
    blurred_frame = cv2.GaussianBlur(gray_frame, (15, 15), 0)

    # Step C: Thresholding (The core of traditional CV).
    # Every pixel above a brightness value of 120 becomes pure white (255), 
    # and everything darker becomes pure black (0).
    _, thresh_frame = cv2.threshold(blurred_frame, 120, 255, cv2.THRESH_BINARY)

    # Step D: Draw text directly onto the pixel array using OpenCV
    cv2.putText(
        thresh_frame, 
        "PURE OPENCV THRESHOLD", 
        (30, 50),                      # X, Y coordinates on screen
        cv2.FONT_HERSHEY_SIMPLEX, 
        0.8,                           # Font scale
        (255, 255, 255),               # Color (White text)
        2                              # Thickness
    )

    # 3. Display the processed frame
    cv2.imshow("Pure OpenCV Window", thresh_frame)

    # Exit condition: Press 'q' on keyboard
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up resources
cap.release()
cv2.destroyAllWindows()