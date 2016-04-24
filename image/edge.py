import sys
from os import path
import cv2

d = path.dirname(__file__)
argvs = sys.argv
img = cv2.imread(path.join(d, argvs[1]))
edges = cv2.Canny(img, 100, 200)
cv2.imwrite(path.join(d, "edge_"+argvs[1]), edges)
