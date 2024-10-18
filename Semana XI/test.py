import cv2 as cv

img = cv.imread("/Users/miguelcamargorojas/Documents/UP/PDI-Ago-dic24/images/apple.jpg")
img_hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("PRUEBA", img_hsv)
cv.waitKey()