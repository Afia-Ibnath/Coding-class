import cv2

# Load the image

image = cv2.imread('dorja.jpg')

# Resize the window to a specific size without resizing the image

cv2.namedWindow('boy Image', cv2.WINDOW_NORMAL) # Create a resizable window

cv2.resizeWindow('boy Image', 700, 600) # Set the window size to 800x500 (width x height)

# Display the image in the resized window

cv2.imshow('boy Image', image)

cv2.waitKey(0) # Wait for a key press

cv2.destroyAllWindows() # Close the window

# Print image properties

print(f"Image Dimensions: {image.shape}") # Height, Width, Channels