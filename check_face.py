import cv2
import numpy as np

def make_bin_picture(img_param): #создает бинарное изображение (проще обрабатывать)
    img_param = cv2.cvtColor(img_param, cv2.COLOR_BGR2GRAY)
    img_param = cv2.GaussianBlur(img_param, (5, 5), 0)  # только нечетные числа в гауссе
    img_param = cv2.Canny(img_param, 100, 140)  #какие точки из серого изображения мы выбираем (нижний порог насыщенности, верхний)
    return img_param
def vid_cam():
    cap = cv2.VideoCapture(0)  # с камеры
    cap.set(3, 500) # set wideq
    cap.set(4, 300) # set high
    #
    while True:
        succes, img = cap.read()
        #img = cv2.imread("Test_Pictures/People.jpg")
        grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        grey2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = cv2.CascadeClassifier("Weight/faces.xml")# подтягиваем файл с натренированной моделью
        laught = cv2.CascadeClassifier("Weight/laught.xml")
        results_faces = faces.detectMultiScale(grey, scaleFactor=1.12, minNeighbors=5)# находим все координаты искомых обьектов min similar objects
        results_laught = laught.detectMultiScale(grey2, scaleFactor=60, minNeighbors=1)
        for (x, y, w, h) in results_faces:
            cv2.rectangle(img, (x, y), (x + w, y + h), (150, 200, 50), thickness=3)
        for (x, y, w, h) in results_laught:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 200, 200), thickness=3)
        #cv2.imshow("Your face", img)
        #cv2.waitKey(0)
        cv2.imshow('qResult', img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

vid_cam()
# if cv2.waitKey(1) & 0xFF == ord('q'):
#          exit()



