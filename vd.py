# importing libraries
import cv2
import os

# going through every directory in test images
for root, dirs, files in os.walk("./testimgs", topdown=True):
   # don't need roots and directories because we already have set condition of testimgs folder and only care about files
   for name in files:
      # making sure we are reading only .jpg files
      if name.endswith('.jpg'):
         # building path of image
         img_path = os.path.join(root, name)
         # reading, resizing, filtering, and showing image at that path
         img = cv2.imread(img_path, flags=None)
         img = cv2.resize(img, (24, 24))
         img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
         cv2.imshow('car', img)
         #prevent program from crashing
         cv2.waitKey(0)