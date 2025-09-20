import streamlit as st
from deepface import DeepFace
from PIL import Image
import numpy as np
import time

def show_emotion_detection():
    st.title("😀 Emotion Detection")
    
    st.markdown("""
    Upload an image containing a face to analyze the emotional expression. 
    The system will detect and classify emotions with confidence scores.
    """)
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose an image file", 
        type=["jpg", "jpeg", "png"],
        help="Upload an image with a clear view of a face"
    )
    
    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        
        # Analyze emotions
        if st.button("🔍 Analyze Emotions", type="primary"):
            with st.spinner("Analyzing emotions..."):
                try:
                    # Perform emotion analysis
                    result = DeepFace.analyze(
                        np.array(image), 
                        actions=['emotion'], 
                        enforce_detection=False
                    )
                    
                    # Extract results
                    emotions = result[0]["emotion"]
                    
                    st.success("✅ Analysis completed successfully!")
                    
                    # Display results
                    st.subheader("🎭 Detected Emotions")
                    
                    # Emoji mapping
                    emoji_map = {
                        "happy": "😀",
                        "sad": "😢", 
                        "angry": "😡",
                        "surprise": "😮",
                        "fear": "😨",
                        "disgust": "🤢",
                        "neutral": "😐"
                    }
                    
                    # Create columns for better layout
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.markdown("### Emotion Scores")
                        for emotion, score in emotions.items():
                            emoji = emoji_map.get(emotion, "🙂")
                            st.write(f"{emoji} **{emotion.title()}**: {score:.2f}%")
                    
                    with col2:
                        st.markdown("### Visual Representation")
                        st.bar_chart(emotions)
                    
                    # Dominant emotion
                    dominant_emotion = max(emotions, key=emotions.get)
                    dominant_score = emotions[dominant_emotion]
                    
                    st.info(f"""
                    🎯 **Dominant Emotion**: {emoji_map.get(dominant_emotion, "🙂")} {dominant_emotion.title()} 
                    with {dominant_score:.2f}% confidence
                    """)
                    
                    # Business insights
                    st.subheader("💼 Business Insights")
                    if dominant_emotion in ["happy", "surprise"]:
                        st.success("😊 **Positive Sentiment**: Customer appears satisfied and engaged")
                    elif dominant_emotion in ["sad", "angry", "fear"]:
                        st.warning("😟 **Negative Sentiment**: Customer may need immediate attention")
                    else:
                        st.info("😐 **Neutral Sentiment**: Customer shows standard engagement level")
                    
                except Exception as e:
                    st.error(f"❌ Error during analysis: {str(e)}")
                    st.info("Please ensure the image contains a clear, detectable face.")
    
    # Additional features
    st.markdown("---")
    st.subheader("📋 Analysis Features")
    
    features = [
        "✅ Real-time emotion detection",
        "✅ 7 emotion categories supported", 
        "✅ Confidence scoring for each emotion",
        "✅ Business sentiment insights",
        "✅ Batch processing capability"
    ]
    
    for feature in features:
        st.markdown(feature)
