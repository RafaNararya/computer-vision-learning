import cv2

# VideoCapture(0) would open default webcam
# VideoCapture("videofile") loads in a video file
'''capture = cv2.VideoCapture("video.mp4")


# to check if the video was opened correctly
if not capture.isOpened():
    print("Video not opened brodie")
    exit()

# .read() returns a boolean first if a frame was read successfully 
# then returns a matrix of the frame
while True:
    ret, frame = capture.read()

    print(frame)
    if not ret:
        break

    cv2.imshow("Video", frame)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()'''

# 0 corresponds to the default built-in webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Display the live feed
    cv2.imshow("Live Feed", frame)

    # Press 'q' to exit the loop safely
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()