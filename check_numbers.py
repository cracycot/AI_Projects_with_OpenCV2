import cv2
import easyocr
import numpy
import numpy as np
from matplotlib import  pyplot as pl
import imutils
img = cv2.imread("Test_Pictures/Macan.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_filter = cv2.bilateralFilter(gray, 11, 15, 15) #убирает шум с изображения
edges = cv2.Canny(img_filter, 30, 50)
cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # находим контуры
cont = imutils.grab_contours(cont) # забираем контуры списком
cont = sorted(cont, key = cv2.contourArea, reverse=True) # сортировка по квадратам

pos = None
for c in cont:
    approx = cv2.approxPolyDP(c, 10, True) # ищем контуры более похожие на квадрат
    if len(approx) == 4:
        pos = approx
        break

mask = numpy.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
bitwise_img = cv2.bitwise_and(img, img, mask = mask)

(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
crop = gray[x1:x2, y1:y2]

text = easyocr.Reader(['en'])
text = text.readtext(crop)
print(text)

pl.imshow(cv2.cvtColor(crop, cv2.COLOR_BGR2RGB))
pl.show()
