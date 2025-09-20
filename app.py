import streamlit as st
from deepface import DeepFace
from PIL import Image
import numpy as np

st.set_page_config(page_title="Facial Emotion Detector", page_icon="😀")

st.title("😀 Facial Emotion Detector")

# Upload image
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Analyzing emotions..."):
        # Analyze emotions
        result = DeepFace.analyze(np.array(image), actions=['emotion'], enforce_detection=False)

    # Extract results
    emotions = result[0]["emotion"]

    st.subheader("Detected Emotions")
    emoji_map = {
        "happy": "😀",
        "sad": "😢",
        "angry": "😡",
        "surprise": "😮",
        "fear": "😨",
        "disgust": "🤢",
        "neutral": "😐"
    }

    for emotion, score in emotions.items():
        st.write(f"{emoji_map.get(emotion, '🙂')} {emotion}: {score:.2f}%")

    # Optional: Bar chart visualization
    st.bar_chart(emotions)
