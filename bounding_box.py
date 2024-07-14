import cv2

# Load an image
image = cv2.imread('cv.jpeg')
if image is None:
    raise FileNotFoundError("Image file not found.")

# Get the dimensions of the image
height, width, _ = image.shape

# Define the size of the bounding box
box_width, box_height = 100, 100  # Change these values as needed

# Calculate the coordinates of the top-left corner of the bounding box
x = (width - box_width) // 2
y = (height - box_height) // 2

# Draw the bounding box

# (x1,y1)= start point of rect,  ( x2, y2)= end point of the rectangle )
        #      x1,y1 ------
        #      |          |
        #      |          |
        #      |          |
        #      --------x2,y2

## (x,y)= start point of rect,  ( x+box_width, y+box_height)= end point of the rectangle )

cv2.rectangle(image, (x, y), ( x+box_width, y+box_height), (0, 255, 0), 2)  

# Display the result
cv2.imshow('Bounding Box', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
