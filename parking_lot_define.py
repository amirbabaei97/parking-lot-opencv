import cv2
import json

# Initialize the list of rectangles and boolean indicating
# whether cropping is being performed or not
rectangles = []
current_rectangle = []
cropping = False


def click_and_crop(event, x, y, flags, param):
    # Grab references to the global variables
    global rectangles, current_rectangle, cropping, image

    # Define the width and height of the rectangle
    rectangle_width = 500
    rectangle_height = 200

    # If the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        # Calculate the ending x and y coordinates based on the fixed width and height
        end_x = x + rectangle_width
        end_y = y + rectangle_height

        # Ensure the ending coordinates are within the image
        end_x = min(end_x, image.shape[1] - 1)
        end_y = min(end_y, image.shape[0] - 1)

        # Store the rectangle
        rectangle = [(x, y), (end_x, end_y)]
        rectangles.append(tuple(rectangle))

        # Draw the rectangle on the image
        cv2.rectangle(image, rectangle[0], rectangle[1], (0, 255, 0), 5)
        cv2.imshow("image", image)


# Load the image, clone it, and setup the mouse callback function
image = cv2.imread("parking_lot.png")
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

# Keep looping until the 'q' key is pressed
while True:
    # Display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF

    # If the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()
        rectangles = []

    # If the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break

# Save the rectangles coordinates to a json file
with open('parking_spaces.json', 'w') as outfile:
    json.dump(rectangles, outfile)

# Close all open windows
cv2.destroyAllWindows()
