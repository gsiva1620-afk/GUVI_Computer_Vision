import cv2
import matplotlib.pyplot as plt

img=cv2.imread("image1.jpg")
print(img.shape)
cv2.rectangle(img,(500,500),(1000,1000),(20005,0,0),6)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()