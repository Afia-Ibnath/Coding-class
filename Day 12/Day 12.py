import cv2
import numpy as np
import matplotlib.pyplot as plt

def show_image(title, image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(title)
    plt.axis('off')
    plt.show()

def edge_detection(image_path):
    image= cv2.imread(image_path)
    if image is None:
        print("Error:Image not found")
        return
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    show_image("Original Image", image)

    while True:
        print("\nChoose an option:")
        print("1. Sobal Edge Detection")
        print("2. Canny Edge Detection")
        print("3. Laplacian Edge Detection")
        print("4. Gassian Blur")
        print("5. Median Blur")
        print("6. Red Filter")
        print("7. Blue Filter")
        print("8. Green Filter")
        print("9. Exit")

        choice = input(" Enter your choice")
    
        if choice =="6":
           red_filter = image.copy()
           red_filter[:, :, 0] = 0
           red_filter[:, :, 1] = 0
           show_image("Red Filter", red_filter)
        elif choice =="7":
           blue_filter = image.copy()
           blue_filter[:, :, 1] = 0
           blue_filter[:, :, 2] = 0
           show_image("Blue Filter", blue_filter)
        elif choice =="8":
           green_filter = image.copy()
           green_filter[:, :, 0] = 0
           green_filter[:, :, 1] = 0
           show_image("Green Filter", green_filter)
        else:
            print(" Invalid input")
edge_detection("Girl.jpg")