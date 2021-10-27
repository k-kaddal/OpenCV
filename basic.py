import cv2 as cv

capture = cv.VideoCapture('vids/london_bus.mp4')

# SCREEN VIDEO
while True:
    isTrue, frame = capture.read()

    # convert to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('Video', gray)

    if cv.waitKey(20) & 0xFF=='d':
        break


capture.release()
cv.destroyAllWindows()