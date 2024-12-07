# corner-and-edge-detection
**Edge Detection Using OpenCV**
This project demonstrates real-time edge detection using OpenCV in Python. It utilizes computer vision techniques to process video feeds, identifying edges in frames captured from a connected camera or video source.

# Features
**1. Real-Time Edge Detection:** Processes video frames in real time and highlights edges using popular algorithms such as Canny or Sobel.
**2. Camera Integration:** Captures input directly from a webcam or other connected video devices.
**3. Customizable Parameters:** Adjust thresholds and other settings for edge detection to suit specific requirements.
**4. Error Handling:** Detects and notifies users of issues with camera availability or feed access.

**Technologies Used**
**Python:** Main programming language for implementation.
**OpenCV:** Library for computer vision and image processing.

**How to Run ?**
1. Clone the Repository:

[git clone <repository_url>
cd edge-detection
](url)

2. Set Up Virtual Environment:

[python -m venv v_env
source v_env/bin/activate   # On Windows: v_env\Scripts\activate
pip install -r requirements.txt](url)

3. Run the Project:

[python File_name.py](url)

4. Quit the Application:

Press the **Q key** to close the video feed window.

**Common Issues**

**1. Camera Not Detected:** Ensure the camera is connected and available. Try changing the camera index in the script.

**2. Dependencies:** Install required packages using the requirements.txt file.

**Future Enhancements**
1. Add support for edge detection in pre-recorded video files.
2. Implement GUI for parameter adjustment in real time.
3. Integrate advanced edge-detection techniques like HED (Holistically-Nested Edge Detection).
