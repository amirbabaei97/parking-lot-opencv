import cv2
import numpy as np
import json

# Load the parking spaces from the JSON file
with open('parking_spaces.json', 'r') as infile:
    parking_spaces = [{'top_left': top_left, 'bottom_right': bottom_right}
                      for top_left, bottom_right in json.load(infile)]

# Define the threshold for considering a parking space as occupied
threshold = 0.1


def is_space_occupied(image, space):
    # Crop the image to the parking space
    cropped_image = image[space['top_left'][1]:space['bottom_right']
                          [1], space['top_left'][0]:space['bottom_right'][0]]

    # Check if the cropped image is empty
    if cropped_image.size == 0:
        print(f"Warning: Empty cropped image for space {space}")
        return False

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)

    # Apply a binary threshold to the image
    _, threshold_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    # Calculate the proportion of the image that is white
    white_area = np.sum(threshold_image == 255)
    total_area = threshold_image.size

    # If more than the threshold of the image is white, consider the space as occupied
    return white_area / total_area > threshold


def detect_empty_spaces(image):
    empty_spaces = [
        space for space in parking_spaces if not is_space_occupied(image, space)]

    # Draw rectangles around the empty spaces
    for space in empty_spaces:
        cv2.rectangle(image, tuple(space['top_left']), tuple(
            space['bottom_right']), (0, 255, 0), 5)

    # Display the number of free and total parking spaces
    text = f'Free/Total: {len(empty_spaces)}/{len(parking_spaces)}'
    cv2.putText(image, text, (100, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 15)

    # Show the image
    cv2.imshow('Empty Spaces', image)
    cv2.waitKey(0)


# Load the image
image = cv2.imread('parking_lot.png')

if image is None:
    print("Failed to load image")
else:
    # Detect the empty spaces
    detect_empty_spaces(image)
