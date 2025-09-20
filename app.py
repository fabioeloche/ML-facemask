import streamlit as st
import sys
import os

# Add src directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Page configuration
st.set_page_config(
    page_title="Facial Emotion Recognition System",
    page_icon="😀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main navigation
def main():
    st.sidebar.title("🎭 Emotion Recognition System")
    
    # Navigation menu
    page = st.sidebar.selectbox(
        "Navigate to:",
        [
            "📊 Project Summary",
            "😀 Emotion Detection", 
            "📈 Data Analysis",
            "🎯 Model Performance"
        ]
    )
    
    # Route to appropriate page
    if page == "📊 Project Summary":
        from app_pages.project_summary import show_project_summary
        show_project_summary()
    elif page == "😀 Emotion Detection":
        from app_pages.emotion_detection import show_emotion_detection
        show_emotion_detection()
    elif page == "📈 Data Analysis":
        from app_pages.data_analysis import show_data_analysis
        show_data_analysis()
    elif page == "🎯 Model Performance":
        from app_pages.model_performance import show_model_performance
        show_model_performance()

if __name__ == "__main__":
    main()