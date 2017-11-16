#Encoding= utf-8
import cv2
image = cv2.imread(r'C:\Users\Paddy\dell-computer-git\hp-computer-git\opencv-facedetect\IMG.jpg')
cv2.imshow('Faces',image)
cv2.waitKey(0)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray',gray)
#���������������� 
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
detector.load(r'C:\Users\Paddy\dell-computer-git\hp-computer-git\opencv-facedetect\haarcascade_frontalface_default.xml')
#ʶ���������õ���������
rects = detector.detectMultiScale(gray,scaleFactor=1.05,minNeighbors =7,
	minSize=(90,90),flags = cv2.CASCADE_SCALE_IMAGE)
#����list��ʶ�𵽵�����������ɫ�߿�2pixcel�ı߿�
for (x,y,w,h) in rects:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('Faces',image)
cv2.waitKey(0)