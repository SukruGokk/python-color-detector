# @author: Şükrü Erdem Gök Github: https://github.com/SukruGokk
# @date: 21/06/2020
# @os: Windows 10
# @version: Python 3.8

# Opencv2 color detector

# Lib
import cv2
import numpy as np

# Capture camera video
cam = cv2.VideoCapture(0)

while True:

    # Define image
    ret, img = cam.read()

    #Copy of pure image
    pureCopy = img.copy()

    # Cvt filter
    cvt = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Copy for colors
    blue = cvt.copy()
    red = cvt.copy()
    green = cvt.copy()

    # Red color
    low_red = np.array([170, 50, 50])
    high_red = np.array([180, 255, 255])

    # Red mask
    red_mask = cv2.inRange(red, low_red, high_red)

    # Blue color
    low_blue = np.array([94, 80, 2])
    high_blue = np.array([126, 255, 255])

    # Blue mask
    blue_mask = cv2.inRange(blue, low_blue, high_blue)

    # Green color
    low_green = np.array([25, 52, 72])
    high_green = np.array([102, 255, 255])

    # Green mask
    green_mask = cv2.inRange(green, low_green, high_green)

    # Contours for red
    _, cnts,_ = cv2.findContours(red_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    max_width = 0
    max_heigth = 0
    max_index = -1

    # To get x, y, w, h
    for i in range(len(cnts)):
        cnt = cnts[i]
        x, y, w, h = cv2.boundingRect(cnt)
        if (w > max_width and h > max_heigth):
            max_width = w
            max_heigth = h
            max_index = i

    # I used try-except because if there is no red color
    try:
        x, y, w, h = cv2.boundingRect(cnts[max_index])
        cv2.rectangle(pureCopy, (x, y), (x + w, y + h), (0, 0, 255), 2)
    except:
        pass

    # Contours for blue
    _, cnts,_ = cv2.findContours(blue_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    max_width = 0
    max_heigth = 0
    max_index = -1

    # To get x, y, w, h
    for i in range(len(cnts)):
        cnt = cnts[i]
        x, y, w, h = cv2.boundingRect(cnt)
        if (w > max_width and h > max_heigth):
            max_width = w
            max_heigth = h
            max_index = i

    # I wrote why I used try-except at 61. line
    try:
        x, y, w, h = cv2.boundingRect(cnts[max_index])
        cv2.rectangle(pureCopy, (x, y), (x + w, y + h), (255, 0, 0), 2)
    except:
        pass

    # Contours for green
    _, cnts,_ = cv2.findContours(green_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    max_width = 0
    max_heigth = 0
    max_index = -1

    # To get x, y, w, h
    for i in range(len(cnts)):
        cnt = cnts[i]
        x, y, w, h = cv2.boundingRect(cnt)
        if (w > max_width and h > max_heigth):
            max_width = w
            max_heigth = h
            max_index = i

    # 61.line :)
    try:
        x, y, w, h = cv2.boundingRect(cnts[max_index])
        cv2.rectangle(pureCopy, (x, y), (x + w, y + h), (0, 255, 0), 2)
    except:
        pass

    # Show the image
    cv2.imshow("COLOR DETECT", pureCopy)

    # To except press ESC
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Release the camera
cam.release()