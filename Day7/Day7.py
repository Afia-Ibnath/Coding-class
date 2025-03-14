import cv2
import numpy as np
import matplotlib.pyplot as plt

def showimg(title, image):
    plt.imshow(image, cmap="grey")
    plt.title(title)
    plt.axis('off')
    plt.show()

def edge_detection(image_path):
    """"Simple edge detection tool"""
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Image not found! ")
        return

    grey= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    showimg("Grayscale Image", grey)

    while True:
        print("/nChoose an option:")
        print("1. sobel Edge Detection")
        print("2. Canny Edge Detection")
        print("3. Laplacian Edge Detection")
        print("4. Gaussian Detection")
        print("5. Median Detection")
        print("6. Exit")

        choice = input("Enter your choice:")


        if choice == "1":
            sobel = cv2.bitwise_or(
                cv2.Sobel(grey, cv2.CV_64F, 1, 0,ksize=3).astype(np.uint8),
                cv2.Sobel(grey, cv2.CV_64F, 0, 1,ksize=3).astype(np.uint8)
            )
            showimg("Sobel Edge Detection", sobel)

        elif choice =="2":
            low = int(input("LOwer threshold: "))
            high= int(input("Upper threshold: "))
            edges = cv2.canny(grey, low,high)
            showimg("Canny Edge Detection", sobal)
        elif choice =="2":
            laplacian = np.abs(cv2.Laplacian(grey, cv2.CV_64F)).astype(np.uint8)
            showimg("Laplacian Edge Detection", laplacian)
        elif choice== "4":
            size= int(input("Blur size(odd number): "))
            size = int
edge_detection("Doremon.jpg")
