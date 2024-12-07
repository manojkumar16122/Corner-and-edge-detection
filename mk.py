import cv2
import numpy as np

def detect_corners(image):
    """
    Detects corners in the given image using Harris Corner Detection.

    Args:
        image (numpy.ndarray): Input image in BGR format.

    Returns:
        numpy.ndarray: Image with corners marked.
    """
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    # Apply Harris corner detection
    corners = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

    # Dilate corner regions for visibility
    corners = cv2.dilate(corners, None)

    # Mark the corners on the original image in red
    result = image.copy()
    result[corners > 0.01 * corners.max()] = [0, 0, 255]  # Red color for corners

    return result

def detect_edges(image):
    """
    Detects edges in the given image using the Canny edge detection algorithm.

    Args:
        image (numpy.ndarray): Input image in BGR format.

    Returns:
        numpy.ndarray: Image with edges detected.
    """
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray, 100, 200)

    # Convert edges to BGR format for display
    edges_bgr = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

    return edges_bgr

def main():
    """
    Main function to perform real-time corner and edge detection using webcam feed.
    """
    # Try multiple camera indices if the default (0) fails
    camera_index = 0
    while camera_index < 3:  # Test indices 0, 1, 2
        cap = cv2.VideoCapture(camera_index)
        if cap.isOpened():
            print(f"Camera opened successfully with index {camera_index}.")
            break
        else:
            print(f"Camera index {camera_index} not working. Trying next...")
            camera_index += 1
            cap.release()

    if not cap.isOpened():
        print("Error: Unable to access the camera after testing multiple indices.")
        return

    # Get the frame width and height
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # Define the codec and create VideoWriter object to save the output
    out = cv2.VideoWriter('output_with_corners_and_edges.avi', 
                          cv2.VideoWriter_fourcc(*'XVID'), 
                          20.0, 
                          (frame_width, frame_height))

    print("Press 'Esc' to exit the program.")

    while True:
        # Capture a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to capture video.")
            break

        # Perform corner detection
        frame_with_corners = detect_corners(frame)

        # Perform edge detection
        frame_with_edges = detect_edges(frame)

        # Combine both results side-by-side
        combined_frame = np.hstack((frame_with_corners, frame_with_edges))

        # Display the combined result
        cv2.imshow("Real-Time Corner and Edge Detection", combined_frame)

        # Save the combined frame to the output video
        out.write(combined_frame)

        # Exit if the user presses the 'Esc' key
        if cv2.waitKey(1) & 0xFF == 27:  # 27 is the ASCII code for the Esc key
            break

    # Release the webcam and video writer, and close all OpenCV windows
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()