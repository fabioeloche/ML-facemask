# ====================================================================
# FIX CRITICO PER CLOUD RUN (DEEPFACE/OPENCV HEADLESS)
# Queste righe DEVONO stare all'inizio per forzare le librerie a
# operare in modalità senza schermo (headless), risolvendo l'errore
# di sistema libGL.so.1 che blocca l'importazione di DeepFace.
# ====================================================================
import os
os.environ['QT_QPA_PLATFORM'] = 'offscreen'
os.environ['QT_ASSISTANT_IGNORE_VERSIONS'] = '1' 

# --------------------------------------------------------------------
# INIZIO DEL TUO CODICE APPLICATIVO
# --------------------------------------------------------------------
import streamlit as st
import sys

# === DEEPFACE AGGIUNTO QUI ===
# Questa riga DEVE stare qui, in modo che DeepFace venga caricato
# nel contesto principale DOPO i fix ambientali e prima che Streamlit
# inizi a renderizzare le pagine.
from deepface import DeepFace
# =============================


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
        try:
            # L'importazione di emotion_detection qui DEVE chiamare DeepFace
            # senza problemi grazie al fix 'os.environ' e all'importazione
            # DeepFace all'inizio del file.
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