import cv2
import matplotlib.pyplot as plt


def CV2(img):
    cv2.namedWindow('My Image', cv2.WINDOW_NORMAL)
    cv2.imshow('My Image',img)
    print("please type ant key ")
    cv2.waitKey(0)



def matplot(img):
    plt.figure("BGR")
    plt.imshow(imgBGR)
    plt.figure("RGB")
    imgRGB = imgBGR[:, :, ::-1]
    plt.imshow(imgRGB)
    plt.show()

if __name__ == '__main__':

    imgBGR = cv2.imread('2-ck-1.JPG')
    CV2(imgBGR)
    matplot(imgBGR)
    print(imgBGR.shape)



