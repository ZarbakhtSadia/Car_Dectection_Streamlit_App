# Smart Car Detection with YOLOv8

The **Smart Car Detection** application enables efficient and accurate car detection in both images and videos using the advanced **YOLOv8** model. With an intuitive interface built with **Streamlit**, this tool provides a seamless experience for car detection in real-time.

## Features
- **Car Detection for Images**: Upload an image to detect cars automatically.
- **Car Detection for Videos**: Upload a video, and the app will process each frame for car detection.
- **Downloadable Results**: Once the detection is complete, you can easily download the output image or video.

## Requirements
To run the application, you will need:
- Python 3.x
- Streamlit
- YOLOv8 model (for object detection)
- OpenCV
- Numpy

Install the necessary libraries using the following command:
```bash
pip install streamlit opencv-python ultralytics numpy
```

## Getting Started
### 1. Clone the repository:
```bash
git clone https://github.com/your-username/car-detection-yolo.git
cd car-detection-yolo
```

### 2. Run the Streamlit application:
```bash
streamlit run app.py
```
**3.** Once the app starts, open your browser and go to the following URL (usually `http://localhost:8501`).

**4.** **Choose the Input Type**:
- **Image**: Upload an image file (JPG, JPEG, PNG) to detect cars.
- **Video**: Upload a video file (MP4, AVI, MOV) to process frame-by-frame.

**5.** The application will display the detection results and allow you to download the processed medi

## How It Works

- **Image Processing**: The YOLOv8 model quickly detects cars in the uploaded image, highlighting the vehicles in real-time.
  
- **Video Processing**: For videos, the app processes each frame, running car detection on them and displaying the results as the video plays.
  
- **Efficient Results**: After processing, the application allows users to download the detected output for further use.

## Powered by YOLOv8

## Powered by YOLOv8

This application uses **YOLOv8**, a powerful and efficient model for detecting objects in images and videos. YOLOv8 ensures quick and accurate car detection, making the app reliable for real-time use.


