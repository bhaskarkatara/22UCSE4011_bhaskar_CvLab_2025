import cv2

# Open the webcam bascially your first webcam
cap = cv2.VideoCapture(0)

# Check if the webcam is opened correctly
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Capture a single frame from the webcam
ret, frame = cap.read()

# If the frame was successfully captured
if ret:
    # Print the number of pixels (width * height * channels)
    height, width, channels = frame.shape
    num_pixels = width * height
    print(f"Number of pixels in the image: {num_pixels}")

    # Save the captured image in JPG format
    cv2.imwrite('captured_image.jpg', frame)
    
    # Show the captured image
    cv2.imshow('Captured Image', frame)
    
    # Wait for a key press to close the image window
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Error: Could not read frame from webcam.")


# Release the webcam
cap.release()
