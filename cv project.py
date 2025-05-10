import streamlit as st
import cv2
import numpy as np
from PIL import Image

# Web App Title
st.title("🍃 Leaf Segmentation Web App")

# Upload an image
uploaded_file = st.file_uploader("Upload a Leaf Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Step 1: Read the uploaded image
    image = Image.open(uploaded_file)
    image_np = np.array(image)

    st.subheader("Original Image")
    st.image(image_np, channels="RGB")

    # Step 2: Resize image
    resized = cv2.resize(image_np, (600, 400))

    # Step 3: Convert to HSV
    hsv = cv2.cvtColor(resized, cv2.COLOR_RGB2HSV)

    # Step 4: Define green color range
    lower_green = np.array([30, 50, 50])
    upper_green = np.array([90, 255, 255])

    # Step 5: Create a mask
    mask = cv2.inRange(hsv, lower_green, upper_green)

    # Step 6: Morphological operations
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # Step 7: Apply mask
    segmented = cv2.bitwise_and(resized, resized, mask=mask)

    # Step 8: Show outputs
    st.subheader("Mask (Detected Leaf Region)")
    st.image(mask, channels="GRAY")

    st.subheader("Segmented Leaf Image")
    st.image(segmented, channels="RGB")
