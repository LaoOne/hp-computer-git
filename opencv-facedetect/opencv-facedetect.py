#Encoding= utf-8
import cv2
image = cv2.imread(r'C:\Users\Paddy\dell-computer-git\hp-computer-git\opencv-facedetect\IMG.jpg')
cv2.imshow('Faces',image)
cv2.waitKey(0)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Gray',gray)
#加载人脸分类检测器 
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
detector.load(r'C:\Users\Paddy\dell-computer-git\hp-computer-git\opencv-facedetect\haarcascade_frontalface_default.xml')
#识别人脸，得到矩形区域
rects = detector.detectMultiScale(gray,scaleFactor=1.05,minNeighbors =7,
	minSize=(90,90),flags = cv2.CASCADE_SCALE_IMAGE)
#遍历list中识别到的人脸，画绿色线宽2pixcel的边框
for (x,y,w,h) in rects:
	cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)

cv2.imshow('Faces',image)
cv2.waitKey(0)