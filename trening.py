import cv2
import numpy as np
#img = cv2.imread("Test_Pictures/images.jpeg")
#cv2.imshow('Result', img)

#cv2.waitKey(0)
#cap = cv2.VideoCapture('test_videos/video.mp4')


# cap = cv2.VideoCapture(0) # с камеры
# cap.set(3, 500) # set wide
# cap.set(4, 300) # set high
#
# while True:
#     succes, img = cap.read()
#     cv2.imshow('qResult', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# img = cv2.imread("Test_Pictures/images.jpeg")
# new_img = cv2.resize(img, (2000, 2000))
# new_img = cv2.resize(img, (img.shape[1] * 3, img.shape[0] * 2))
# cv2.imshow("ekfa", new_img[0:100, 0:150])
# cv2.waitKey(0)
#
# img3 = cv2.GaussianBlur(new_img,(3,3),0 )# размытие по гауссу (кортеж размытия)
# img5 = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY) #привод картинки к черно белому
#
# img6 = cv2.Canny(img5, 10, 10) #определение угла создается бинарная картинка
# kernel = np.ones((5, 5), np.uint8)
# img7 = cv2.dilate(img6, kernel, iterations = 1)
# cv2.imshow('Result', img7)

#print(img.shape)
#cv2.waitKey(0)



# #третий урок создание матриц своих фотографий
#
# photo = np.zeros((1000, 1000, 3), dtype="uint8") # create matrix
# # shape - y , x
# photo[100:150, 200: 280] = 255, 210 , 210 # обратиться к в сей матрице в opencv BGR!!!!
# cv2.rectangle(photo, (10, 10), (100, 100), (241,23,21), thickness=1)
# cv2.line(photo, (100,100), (200, 200), (1,234,1), thickness=2)
# cv2.circle(photo, (photo.shape[1]// 2, photo.shape[0] // 2), 100, (102, 102,102), thickness=cv2.FILLED)
# cv2.putText(photo, "Kirill_Lesnyak", (100,100), cv2.FONT_HERSHEY_COMPLEX, 2, (0,200,150))
# cv2.imshow("Photo", photo)
# cv2.waitKey(0)

#cap = cv2.VideoCapture('test_videos/video.mp4')
# cap = cv2.VideoCapture(0) # с камеры
# cap.set(3, 500) # set wide
# cap.set(4, 300) # set high
# while True:
#     succes, img = cap.read()
#     img = cv2.resize(img, (img.shape[1] // 2, img.shape[0] // 2))
#     img = cv2.GaussianBlur(img, (9, 9), 0)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     img = cv2.Canny(img, 10, 20)
#     kernel = np.ones((5,5), np.uint8)
#     img = cv2.dilate(img, kernel, iterations=1)
#     img = cv2.erode(img, kernel, iterations=1)
#     cv2.imshow('qResult', img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
def rotate(img_z, angle): # поворот на градусы
    height, widht = img_z.shape[:2]
    point = (widht // 2, height // 2)
    a = cv2.getRotationMatrix2D(point, angle, 1) # matrix for rotate
    return cv2.warpAffine(img_z, a, (widht, height))

def tranfrom(img_param, x, y): #смещение изображение
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_param, mat, (img.shape[1], img_param.shape[0]))

def make_bin_picture(img_param): #создает бинарное изображение (проще обрабатывать)
    img_param = cv2.cvtColor(img_param, cv2.COLOR_BGR2GRAY)
    img_param = cv2.GaussianBlur(img_param, (5, 5), 0)  # только нечетные числа в гауссе
    img_param = cv2.Canny(img_param, 100, 140)  #какие точки из серого изображения мы выбираем (нижний порог насыщенности, верхний)
    #con, hir = cv2.findContours(img_param, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)# перваяя переменная - список со всеми позициями контура, вторая - иерархия обьектов

# img = cv2.imread("Test_Pictures/NOR.jpg")
# #img = cv2.flip(img, 1) # отзеркалить кaртинку
# img = tranfrom(img, 30, 10)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img = cv2.GaussianBlur(img, (5,5), 0) # только нечетные числа в гауссе
# img = cv2.Canny(img,100,140) #какие точки из серого изображения мы выбираем (нижний порог насыщенности, верхний)
# con, hir = cv2.findContours(img,cv2.RETR_LIST , cv2.CHAIN_APPROX_NONE) # перваяя переменная - список со всеми позициями контура, вторая - иерархия обьектов
# new_img = np.zeros(img.shape, dtype="uint8")
# cv2.drawContours(new_img, con,-1, (200,100,100)) #записать отдельные контуры в матрицу
# cv2.imshow("RESULT111", img)
# cv2.waitKey(0)
# cv2.imshow("RESULT222", new_img)
# cv2.waitKey(0)


#урок 6

photo = cv2.imread("Test_Pictures/PORT.jpg")
img = np.zeros(photo.shape[:2], dtype="uint8")

#img = np.zeros((1350, 1350), dtype = "uint8" )
circle = cv2.circle(img.copy(), (750, 750), 1500, (100,2,3), -1)
square = cv2.rectangle(img.copy(), (250,250), (1000, 1000), 255, -1)
#cv2.imshow("Result", square)

img = cv2.bitwise_and(photo, photo, mask=circle)

# img = cv2.bitwise_and(circle, square) # находит пересечение
# img = cv2.bitwise_or(circle, square) # находит обьединение
# img = cv2.bitwise_not(circle, square) # инверсия
cv2.imshow("Task1", img)
cv2.waitKey(0)
if cv2.waitKey(1) & 0xFF == ord('q'):
         exit()
