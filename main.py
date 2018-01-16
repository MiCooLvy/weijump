# -*- coding:utf-8 -*-
"""
微信跳一跳 AI 程序
by Kenn
01/15/2018
"""
import cv2
from utils import device as dv


def get_center_point(grad):
    """
    横向扫描，估算顶点坐标，并计算中心点坐标
    :param grad:
    """
    row, col = grad.shape
    for i in range(600, row - 500):
        div = []
        s = []
        for j in range(col):
            if grad[i][j] == 255:
                print("(" + str(i) + ", " + str(j) + ") ")
                if len(s) == 0:
                    s.append(j)
                elif j - s[-1] == 1:
                    s.append(j)
                else:
                    div.append(s.copy())
                    s.clear()
                    s.append(j)
            elif j == col - 1:
                div.append(s.copy())
                s.clear()
        print(div)

    cv2.circle(grad, (788, 850), 10, 255)
    cv2.imshow('image', grad)
    cv2.waitKey(0)


def calc_center_point(grad):
    row, col = grad.shape


def main():
    # dv.init()

    print("\nStarting...")
    image = cv2.imread("sc.png")
    x, y, z = image.shape
    subimg = image[500:1200, 100:y - 100]
    gray = cv2.cvtColor(subimg, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("gray.png", gray)

    gradX = cv2.Sobel(gray, ddepth=cv2.cv2.CV_32F, dx=1, dy=0, ksize=-1)
    gradY = cv2.Sobel(gray, ddepth=cv2.cv2.CV_32F, dx=0, dy=1, ksize=-1)

    # subtract the y-gradient from the x-gradient
    gradient = cv2.subtract(gradX, gradY)
    gradient = cv2.convertScaleAbs(gradient)
    # kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
    # closed = cv2.morphologyEx(gradient, cv2.MORPH_CLOSE, kernel)
    # perform a series of erosions and dilations
    # closed = cv2.erode(gradient, None, iterations=4)
    closed = cv2.dilate(gradient, None, iterations=1)

    cr, cc = closed.shape
    # for i in range(cr):
    #     for j in range(cc):
    #         if closed[i][j] < 100:
    #             closed[i][j] = 0
    #         else:
    #             closed[i][j] = 255

    cv2.circle(closed, (718, 795), 10, 255)

    cv2.imwrite("gradient.png", closed)

    # get_center_point(gradient)
    calc_center_point(gradient)


if __name__ == '__main__':
    main()
