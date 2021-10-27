import cv2 as cv

capture = cv.VideoCapture('vids/london_bus.mp4')

# CHANGE RESOLUTION : workd only for cameras
def changeRes(width, height):
    capture.set(3, height)
    capture.set(4, width)


# RESIZE FRAMES : works for images, videos and cameras
def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# SCREEN VIDEO
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, 0.2)

    # cv.imshow('Video', frame)
    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xFF=='d':
        break


capture.release()
cv.destroyAllWindows()