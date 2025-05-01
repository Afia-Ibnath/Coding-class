import cv2

import numpy as np

import pyautogui

cap = cv2.VideoCapture(0)

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:

        break

# Flip frame for mirror effect

    frame = cv2.flip(frame, 1)

# Convert to HSV and create skin mask

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, np.array([0, 20, 70]), np.array([20, 255, 255]))

# Find contours

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:

        max_contour = max(contours, key=cv2.contourArea)

        if cv2.contourArea(max_contour) > 1000:

            x, y, w, h = cv2.boundingRect(max_contour)

            center_x, center_y = x + w // 2, y + h // 2

# Draw rectangle and center

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

# Get scroll gesture

            gesture = "Center"

            if center_y < frame.shape[0] // 3:

                gesture = "Up"

                pyautogui.scroll(30) # Scroll up

            elif center_y > 2 * frame.shape[0] // 3:

                gesture = "Down"

                pyautogui.scroll(-30) # Scroll down

# Show gesture

                cv2.putText(frame, f"Gesture: {gesture}", (10, 30),

                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

# Show frame

                cv2.imshow('Hand Scroll Control', frame)

# Exit on 'q'

        if cv2.waitKey(1) & 0xFF == ord('q'):

            break

# Cleanup

cap.release()

cv2.destroyAllWindows()