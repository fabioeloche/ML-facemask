# ====================================================================
# FIX CRITICO PER CLOUD RUN (DEEPFACE/OPENCV HEADLESS)
# Queste righe DEVONO essere le prime istruzioni eseguibili del file.
# Forzano DeepFace/OpenCV a operare in modalità senza schermo,
# risolvendo il persistente errore di sistema libGL.so.1.
# ====================================================================
import os
os.environ['QT_QPA_PLATFORM'] = 'offscreen'
os.environ['QT_ASSISTANT_IGNORE_VERSIONS'] = '1' 

# --------------------------------------------------------------------
# INIZIO DEL TUO CODICE APPLICATIVO
# --------------------------------------------------------------------
import streamlit as st
import sys

# === DEEPFACE AGGIUNTO E IMPORTATO QUI ===
# L'importazione avviene DOPO i fix ambientali e PRIMA che Streamlit
# avvii la logica dell'applicazione.
try:
    from deepface import DeepFace
    DEEPFACE_AVAILABLE = True
except ImportError:
    DEEPFACE_AVAILABLE = False
    st.warning("DeepFace not available - using demo mode")
# ========================================

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
    st.sidebar.title("Marketing New product recognition")
    
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
        try:
            # L'importazione di emotion_detection qui DEVE ora funzionare.
            from app_pages.emotion_detection import show_emotion_detection
            show_emotion_detection()
        except ImportError:
            st.warning("⚠️ Using demo version due to import issues")
            from app_pages.emotion_detection_demo import show_emotion_detection_demo
            show_emotion_detection_demo()
    elif page == "📈 Data Analysis":
        from app_pages.data_analysis import show_data_analysis
        show_data_analysis()
    elif page == "🎯 Model Performance":
        from app_pages.model_performance import show_model_performance
        show_model_performance()

if __name__ == "__main__":
    main()