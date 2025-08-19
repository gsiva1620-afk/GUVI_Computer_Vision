import cv2   
import matplotlib.pyplot as plt
import numpy as np


img = np.ones((500,500),dtype=np.uint8)
circle = cv2.circle(img.copy(),(250,250),250,(255,255,255),-1)
rect = cv2.rectanglee(img.copy(),(50,50),(250,250),(255,255,255),-1)

plt.imshow(cv2.cvtColor(rect,cv2.COLOR_BGR2RGB))
plt.show()