# Import necessary libraries
import cv2
import numpy as np
import os
import urllib.request
# Function to apply Gaussian blur to an image
def apply_blur(img, k):
    return cv2.GaussianBlur(img, (k, k), 0)

# Function to pixelate a specific region in an image
def pixelate_region(image, startX, startY, endX, endY, blocks=10):
    region = image[startY:endY, startX:endX]
    (h, w) = region.shape[:2]
    xSteps = np.linspace(0, w, blocks + 1, dtype="int")
    ySteps = np.linspace(0, h, blocks + 1, dtype="int")
    for i in range(1, len(ySteps)):
        for j in range(1, len(xSteps)):
            xStart = xSteps[j - 1]
            yStart = ySteps[i - 1]
            xEnd = xSteps[j]
            yEnd = ySteps[i]
            roi = region[yStart:yEnd, xStart:xEnd]
            (B, G, R) = [int(x) for x in cv2.mean(roi)[:3]]
            cv2.rectangle(region, (xStart, yStart), (xEnd, yEnd), (B, G, R), -1)
    image[startY:endY, startX:endX] = region
    return image


# Function to pixelate the face in an image
def pixelate_face(image, blocks=10):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        image = pixelate_region(image, y, x, y + h, x + w, blocks)
    return image

# Function to download the Haarcascade file if not exists
def download_haarcascade_file():
    url = 'https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml'
    filename = 'haarcascade_frontalface_default.xml'
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        urllib.request.urlretrieve(url, filename)
        print(f"{filename} downloaded successfully.")
if __name__ == "__main__":
    # Download Haarcascade file if not exists
    download_haarcascade_file()
    # Load the Haarcascade classifier for face detection
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Capture video stream and apply pixelation to detected faces
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Apply pixelation to detected faces
        frame = pixelate_face(frame)
        # Display the resulting frame
        cv2.imshow('Face Blur', frame)
        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()