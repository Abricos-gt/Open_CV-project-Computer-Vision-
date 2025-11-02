import cv2
import matplotlib.pyplot as plt
img = cv2.imread("image.jpg")
def cv2_imshow(img):
   # img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    grayscale_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(grayscale_img, 128, 100, cv2.THRESH_BINARY)
    plt.imshow(thresh)
    plt.axis('off')
    plt.show()
cv2_imshow(img)

 