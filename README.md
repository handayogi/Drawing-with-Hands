# Drawing with Hands

> Multimedia Technology Course at Sumatera Institute of Technology (ITERA)

This project allows users to draw on video frames in real-time using hand gestures as input. The project uses Python Libraries such as `OpenCV`, `MediaPipe`, and `NumPy`.
The application detect hands and fingers movement, allowing users to create and manipulate lines directly on the video frames. Additionally, the program includes features
to change the line color and erase drawings using specific hand gestures. It offers an interactive and intuitive way to engage with real-time video processing through simple fingers movements.

## Library explanation:
- `Open Source Computer Vision Library (OpenCV)` is an open-source library that use for image and video processing.  
In this project, OpenCV is used to:
  - Read input from the camera in real-time.
  - Draw lines on video frames (`cv2.line` function).
  - Display the final result with a combination of image layers and original video (`cv2.imshow` and `cv2.addWeighted` function).
  - Handle image manipulation such as color conversion from BGR to RGB.
- `MediaPipe` is a library framework used for AI-based multimedia data processing solutions such as hand, face, and body detection.  
In this project, MediaPipe is used to:
  - Identify hands positions and landmarks in real-time.
  - Find specific landmarks such as the tip of the thumb, index finger, ring finger, and pinky finger.
- `NumPy` is a library for efficient numerical computation.  
In this project, NumPy is used to:
  - Create an empty image layer (`np.zeros_like` function).
  - Manipulate an image array to ensure compatibility with OpenCV.

Check the Doc here:
- [OpenCV](https://docs.opencv.org/4.x/)
- [MediaPipe Hand Landmarks](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker)
- [NumPy](https://numpy.org/doc/)

## Contributors
| Nama                            | NIM       | GitHub Username |
| ------------------------------- | --------- | --------------- |
| Handayogi Tambunan              | 121140114 | handayogi       |
| Yanto Pernando Halomoan Hutapea | 121140127 | hahahahah       |

<a href="https://github.com/handayogi/Drawing-with-Hands/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=handayogi/Drawing-with-Hands" alt="contrib.rocks image" />
</a>
