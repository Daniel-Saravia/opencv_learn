import cv2 as cv

# Initialize video capture for the specified video file
cap = cv.VideoCapture('Videos/dog.mp4')

# Check if the video file was opened successfully
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get the video's frames per second (FPS) for proper playback timing
fps = cap.get(cv.CAP_PROP_FPS)
delay = int(1000 / fps)

# Process video frames
while cap.isOpened():
    ret, frame = cap.read()  # Read a single frame

    if not ret:  # Exit the loop if the frame cannot be read
        print("Stream ended or cannot read frame. Exiting...")
        break

    # Convert the frame to grayscale
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Display the grayscale frame
    cv.imshow('Frame', gray)

    # Break the loop if 'q' is pressed
    if cv.waitKey(delay) == ord('q'):
        break

# Release resources and close all OpenCV windows
cap.release()
cv.destroyAllWindows()
