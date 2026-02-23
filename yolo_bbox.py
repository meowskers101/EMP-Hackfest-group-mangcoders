from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import streamlit as st

st.title("Animal Detector")

image_input = st.file_uploader(
    "Import your image here to see if you have spotted any animals (JPG ONLY!)",
    type=["jpg", "jpeg"]
)

model = YOLO("yolov8n.pt")

if image_input is not None:
    # Convert uploaded image to numpy array
    img = Image.open(image_input)
    img_np = np.array(img)

    # Convert RGB → BGR for OpenCV drawing
    img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

    # Run detection
    results = model(img_np)
    r = results[0]

    # Draw detections
    for box in r.boxes:
        cls_id = int(box.cls[0])
        label = r.names[cls_id]
        conf = float(box.conf[0])

        x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)

        # Draw rectangle
        cv2.rectangle(img_cv, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Draw label
        text = f"{label} {conf:.2f}"
        cv2.putText(
            img_cv,
            text,
            (x1, y1 - 8),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

    # Convert BGR → RGB for Streamlit display
    img_final = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)

    # Show result in Streamlit
    st.image(img_final, caption="YOLO Detection Result", use_container_width=True)

else:
    st.write("Please upload an image.")