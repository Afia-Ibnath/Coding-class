import cv2
import numpy as np
def apply_filter(pic, filter_name):
    '''Applies the chosen color filter to the picture.'''
    new_pic = pic.copy()
    

    if filter_name =="red":
        new_pic[:,:, 1]= 0
        new_pic[:,:, 0]= 0
    elif filter_name =="blue":
        new_pic[:,:, 1]= 0
        new_pic[:,:, 2]= 0
    elif filter_name =="green":
        new_pic[:,:, 0]= 0
        new_pic[:,:, 2]= 0    
    elif filter_name =="more_red":
        new_pic[:,:, 2]= cv2.add(new_pic[:,:,2], 50)   
    elif filter_name =="less_blue":
        new_pic[:,:, 0]= cv2.subtract(new_pic[:,:,0], 50)       
    
    return new_pic


pic_path = "Girl.jpg"
pic = cv2.imread(pic_path)

if pic is None:
    print("Error: Picture not found!")
else:
    filter_name = "original"

    print("Press these keys to try different filters:")
    print("r - Red filter")
    print("b - Blue filter")
    print("g - Green filter")
    print("i - More red")
    print("d - Less blue")
    print("q - Quit")
    

    while True:
     
        new_pic = apply_filter(pic, filter_name)
        cv2.imshow("Filtered Picture", new_pic)
        key = cv2.waitKey(0) & 0xFF

        if key == ord('r'):
            filter_name = "red"
        elif key == ord('b'):
            filter_name = "blue"
        elif key == ord('g'):
            filter_name = "green"
        elif key == ord('i'):
            filter_name = "more_red"
        elif key == ord('d'):
            filter_name = "less_blue"
        elif key == ord('q'):
            print("Goodbye!")
            break
        else:
            print("Invalid key! Please use 'r', 'b', 'g', 'i', 'd', or 'q'.")

cv2.destroyAllWindows()

