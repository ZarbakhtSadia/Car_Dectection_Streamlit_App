import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np
import tempfile
import os
import time

# Load YOLO model
model = YOLO("model.pt")  # Tell Ultralytics to fully load the model

# ----------------------- Page Config -----------------------
st.set_page_config(page_title="Smart Car Detection", layout="centered")

# ----------------------- Background Color -----------------------
page_bg_color = '''
<style>
body {
    background-color: #F4F6F7;
}
[data-testid="stAppViewContainer"] {
    background-color: #F4F6F7;
}
[data-testid="stSidebar"] {
    background-color: #D6EAF8;
}
</style>
'''
st.markdown(page_bg_color, unsafe_allow_html=True)

# ----------------------- Sidebar -----------------------
st.sidebar.title("📌 App Navigation")
input_type = st.sidebar.radio("Choose Input Type:", ["Image", "Video"])

st.sidebar.markdown("---")
st.sidebar.markdown("### 💡 Instructions")
st.sidebar.markdown("""
1. Upload an image or video.
2. Let the model detect cars.
3. View results and download!
""")

st.sidebar.markdown("---")
st.sidebar.markdown("<p style=' color: gray;'>Powered by YOLOv8 🤖</p>", unsafe_allow_html=True)

# ----------------------- Header -----------------------
st.markdown("<h1 style='text-align: center; color: #1A5276;'>🚗 Smart Car Detection</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #566573;'>Upload your media below to run car detection</h4>", unsafe_allow_html=True)
st.markdown("---")

# ----------------------- Image Section -----------------------
if input_type == "Image":
    uploaded_file = st.file_uploader("🖼️ Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, 1)
        st.image(image, caption="Original Image", channels="BGR")

        start_time = time.time()
        with st.spinner("Running YOLO detection..."):
            results = model(image)
            result = results[0]
            detected_image = result.plot()
        end_time = time.time()

        st.success(f"✅ Detection Completed in {end_time - start_time:.2f} seconds")
        st.image(detected_image, caption="Detected Image", channels="BGR")

        # Save output image temporarily
        out_path = "output_detected.jpg"
        cv2.imwrite(out_path, detected_image)
        with open(out_path, "rb") as file:
            st.download_button("⬇️ Download Detected Image", data=file, file_name="detected_image.jpg", mime="image/jpeg")

        # Removed detection results table

# ----------------------- Video Section -----------------------
elif input_type == "Video":
    uploaded_video = st.file_uploader("🎥 Upload a video", type=["mp4", "avi", "mov"])

    if uploaded_video:
        tfile = tempfile.NamedTemporaryFile(delete=False)
        tfile.write(uploaded_video.read())
        video_path = tfile.name

        cap = cv2.VideoCapture(video_path)
        stframe = st.empty()

        st.info("🔄 Processing video frame-by-frame...")
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            results = model(frame)
            result = results[0]
            detected_frame = result.plot()
            stframe.image(detected_frame, channels="BGR")

        cap.release()
        os.remove(video_path)
        st.success("🎉 Video processing completed.")

# ----------------------- Footer -----------------------
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>© 2025 SmartVision | Powered by YOLOv8 + Streamlit</p>", unsafe_allow_html=True)
