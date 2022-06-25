import cv2
filePath = 'nobara.jpg'
windowTitle = 'NOBARA'
readCvImage = cv2.imread(filePath,1)
cv2.imshow(windowTitle,readCvImage)
cv2.waitKey(0)
cv2.destroyAllWindow()