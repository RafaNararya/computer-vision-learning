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

# Resizes the image but does not preserve the aspect ratio
resize = cv2.resize(image, (1000, 1000))
cv2.imshow("Resized", resize)
cv2.waitKey(0)

ratio = 1000 / w
dim = (1000, int(h * ratio))
resize_aspect = cv2.resize(image, dim)
cv2.imshow("Resized Image", resize_aspect)
cv2.waitKey(0)

# Drawing a rectangle
# Rectangle function takes in 5 arguments
# image, top-left corner coordinate, bottom-right corner coordinate, color (BGR Format), Line Width (Pixels)
output = image.copy()
rectangle = cv2.rectangle(output, (0, 0), (600, 400), (255, 0, 0), 2)
cv2.imshow("Rectangle", rectangle)
cv2.waitKey(0)

# Text 
# putText function takes in 7 arguments
# image, text displayed, coordinates (width, height) from top left, font, font size, color (BGR), Line Width
output2 = image.copy()
text = cv2.putText(output2, "TextExample", (0, 100), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)
cv2.imshow("Text", text)
cv2.waitKey(0)

# imshow() takes 2 args, name, and "size". If want a specific area, need to specify
# if want to show it all, just put in the argument of the entire read image
# .waitKey(0) makes it close on any button press, and destroyAllWindows() closes all windows on button press
cv2.imshow("Full", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
