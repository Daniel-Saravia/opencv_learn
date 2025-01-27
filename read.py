import cv2 as cv

# img = cv.imread('Photos/malenia.jpeg')

# cv.imshow('malenia', img)

capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTue, fame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xff==ord('d'):
        break
capture.release()
cv.destroyAllWindows

cv.waitKey(0)