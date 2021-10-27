import cv2 as cv

capture = cv.VideoCapture('vids/london_bus.mp4')

# SCREEN VIDEO
while True:
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF=='d':
        break


capture.release()
cv.destroyAllWindows()