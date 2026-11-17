import cv2

# Reads in an image, extracts the height and width
# .shape returns a tuple of (height, weight, length)
image = cv2.imread('image.jpg')
h, w = image.shape[:2]
print("Height = {}, Width = {}".format(h, w))

# image[100:100] takes a single pixel at coordinate 100:100
# this also returns an array of RGB values in (B, G, R) order
# image [100,100,0] just means taking the 0th index of what image[100:100] was
(B, G, R) = image[100,100]
print("R = {}, G = {}, B = {}".format(R, G, B))
B = image[100,100,0]
print("B = {}".format(B))

# image [0: 500, 0:500] means that we want 500 pixels of height and width starting
# from the top left of the image [0, 0]
roi = image[0: 500, 0: 500]
cv2.imshow("ROI", roi)
cv2.waitKey(0)

resize = cv2.resize(image, (1000, 1000))
cv2.imshow("Resized", resize)
cv2.waitKey(0)

# imshow() takes 2 args, name, and "size". If want a specific area, need to specify
# if want to show it all, just put in the argument of the entire read image
# .waitKey(0) makes it close on any button press, and destroyAllWindows() closes all windows on button press
cv2.imshow("Full", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
