import cv2
import numpy as np

# Load an image
image = cv2.imread('cv.jpeg')
if image is None:
    raise FileNotFoundError("Image file not found.")

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray Boxes', gray)
# Use edge detection (Canny)
edges = cv2.Canny(gray, threshold1=50, threshold2=150)
cv2.imshow('edges Boxes', edges)

# Find contours
black_image=np.zeros_like(image)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(black_image, contours, -1, (255,0,0),2)
# Draw bounding boxes
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(black_image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Display the result
cv2.imshow('Bounding Boxes', black_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
