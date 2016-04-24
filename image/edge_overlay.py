import sys
from os import path
import cv2

d = path.dirname(__file__)
argvs = sys.argv
img = cv2.imread(path.join(d, argvs[1]))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_gray_smooth = cv2.GaussianBlur(img_gray, (11, 11), 0)
ret, th = cv2.threshold(img_gray_smooth, 130, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
cv2.imwrite(path.join(d, "edge_"+argvs[1]), img)
