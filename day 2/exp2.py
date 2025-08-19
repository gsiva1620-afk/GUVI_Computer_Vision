import cv2
import matplotlib.pyplot as plt

img = cv2.imread("image1.jpg")
print(img)

m = cv2.circle(img,(500,500),(1000,1000),(255,0,0),4)

plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()