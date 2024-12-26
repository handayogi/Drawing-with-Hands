#### Kode-MK: IF4021 Sistem / Teknologi Multimedia
#### Prodi : Teknik Informatika
#### Dosen Pengampu : Martin C.T. Manullang

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
| Full Name                       | NIM       | GitHub Username |
| ------------------------------- | --------- | --------------- |
| Handayogi Tambunan              | 121140114 | handayogi       |
| Yanto Pernando Halomoan Hutapea | 121140127 | yanto1988       |

<a href="https://github.com/handayogi/Drawing-with-Hands/graphs/contributors">
  <a href="https://github.com/yanto1988/Drawing-with-Hands/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=handayogi/Drawing-with-Hands" alt="contrib.rocks image" />
</a>

## Logbook
| Date & Time                    | Project Progress and Updates    |
| ------------------------------ | ------------------------------- |
| December 11, 2024, at 08:28 PM | Hand Tracking using MediaPipe   |
| December 22, 2024, at 03:36 AM | Drawing with index finger tip   |
| December 22, 2024, at 10:10 PM | Line color change while drawing |
| December 23, 2024, at 01:27 AM | Clear all line on layer         |
| December 24, 2024, at 17.45 PM | Finished report                 |
## Installations
1. Install dependencies with the following command.
```sh
pip install -r requirements.txt
```
2. Run the program with the following command in the terminal.
```sh
python main.py
```
3. The program will open the camera and display new video window.

## Guide
1. Drawing
    - Move the tip of your index finger in front of the camera to draw.
    - The program will detect the movement and draw a line on the screen based on the position of your finger.

2. Change Color
   - Bring the tip of your ring finger and the tip of your thumb close together until they almost touch and the line color will change.

3. Clear Draw
   - Bring the tip of your little finger and the tip of your thumb close together until they almost touch.
   - The entire image layer will be erased, returning it to a blank state.
     
4. Close Program
   - Press the q key on the keyboard to exit the program.
