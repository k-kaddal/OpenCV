import cv2 as cv
import numpy as np
from numpy.lib.function_base import blackman

capture = cv.VideoCapture('vids/london_bus.mp4')

# CREATE AN IMAGE
blank = np.zeros((500,500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# # 1. Paint the image a certain color
# blank[250:500, 250:500] = 0,255,0
# cv.imshow('Green', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]), (0,255,0), thickness=-1)
cv.imshow('rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), blank.shape[1]//2, (0,0,255), thickness=1)
cv.imshow('circle', blank)

# 4. Draw a line
cv.line(blank, (250,0), (250,blank.shape[0]), (0,0,255), thickness=1)
cv.imshow('line', blank)

# 4. Put Text
cv.putText(blank, 'XOX', (225,255), cv.FONT_HERSHEY_TRIPLEX, 0.7, (255,0,0), 1)
cv.imshow('text', blank)


# # SCREEN VIDEO
# while True:
#     isTrue, frame = capture.read()

#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF=='d':
#         break


cv.waitKey(0)
