"""
Model Utilities for Emotion Recognition System

This module provides utility functions for model operations,
predictions, and evaluation.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple, Optional
from deepface import DeepFace
import cv2
from PIL import Image
import json

class EmotionPredictor:
    """
    Handles emotion prediction using trained models
    """
    
    def __init__(self, model_name: str = "emotion"):
        self.model_name = model_name
        self.emotions = ['happy', 'sad', 'angry', 'surprise', 'fear', 'disgust', 'neutral']
        
    def predict_emotion(self, image: np.ndarray) -> Dict:
        """
        Predict emotion from image
        
        Args:
            image: Input image as numpy array
            
        Returns:
            Emotion prediction results
        """
        try:
            result = DeepFace.analyze(
                image, 
                actions=['emotion'], 
                enforce_detection=False
            )
            
            emotions = result[0]["emotion"]
            dominant_emotion = max(emotions, key=emotions.get)
            
            return {
                "emotions": emotions,
                "dominant_emotion": dominant_emotion,
                "confidence": emotions[dominant_emotion],
                "success": True
            }
        except Exception as e:
            return {
                "emotions": {},
                "dominant_emotion": None,
                "confidence": 0,
                "success": False,
                "error": str(e)
            }
    
    def batch_predict(self, images: List[np.ndarray]) -> List[Dict]:
        """
        Predict emotions for multiple images
        
        Args:
            images: List of images
            
        Returns:
            List of prediction results
        """
        results = []
        for image in images:
            result = self.predict_emotion(image)
            results.append(result)
        return results
    
    def get_emotion_insights(self, predictions: List[Dict]) -> Dict:
        """
        Generate insights from emotion predictions
        
        Args:
            predictions: List of prediction results
            
        Returns:
            Insights and statistics
        """
        if not predictions:
            return {"error": "No predictions provided"}
        
        # Count emotions
        emotion_counts = {emotion: 0 for emotion in self.emotions}
        total_confidence = 0
        successful_predictions = 0
        
        for pred in predictions:
            if pred["success"]:
                emotion_counts[pred["dominant_emotion"]] += 1
                total_confidence += pred["confidence"]
                successful_predictions += 1
        
        # Calculate statistics
        avg_confidence = total_confidence / successful_predictions if successful_predictions > 0 else 0
        most_common_emotion = max(emotion_counts, key=emotion_counts.get)
        
        return {
            "total_predictions": len(predictions),
            "successful_predictions": successful_predictions,
            "success_rate": successful_predictions / len(predictions),
            "emotion_distribution": emotion_counts,
            "most_common_emotion": most_common_emotion,
            "average_confidence": avg_confidence
        }

class ModelEvaluator:
    """
    Evaluates model performance and generates metrics
    """
    
    def __init__(self):
        self.emotions = ['happy', 'sad', 'angry', 'surprise', 'fear', 'disgust', 'neutral']
    
    def calculate_metrics(self, y_true: List[str], y_pred: List[str]) -> Dict:
        """
        Calculate performance metrics
        
        Args:
            y_true: True labels
            y_pred: Predicted labels
            
        Returns:
            Performance metrics
        """
        from sklearn.metrics import accuracy_score, precision_recall_fscore_support
        
        accuracy = accuracy_score(y_true, y_pred)
        precision, recall, f1, support = precision_recall_fscore_support(
            y_true, y_pred, average='weighted'
        )
        
        return {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1_score": f1,
            "support": support
        }
    
    def generate_report(self, y_true: List[str], y_pred: List[str]) -> str:
        """
        Generate detailed classification report
        
        Args:
            y_true: True labels
            y_pred: Predicted labels
            
        Returns:
            Classification report
        """
        from sklearn.metrics import classification_report
        return classification_report(y_true, y_pred, target_names=self.emotions)

def preprocess_image(image: np.ndarray, target_size: Tuple[int, int] = (48, 48)) -> np.ndarray:
    """
    Preprocess image for emotion recognition
    
    Args:
        image: Input image
        target_size: Target size for resizing
        
    Returns:
        Preprocessed image
    """
    # Convert to grayscale if needed
    if len(image.shape) == 3:
        image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    
    # Resize image
    image = cv2.resize(image, target_size)
    
    # Normalize
    image = image.astype(np.float32) / 255.0
    
    return image

def load_model_config(config_path: str) -> Dict:
    """
    Load model configuration from file
    
    Args:
        config_path: Path to configuration file
        
    Returns:
        Model configuration
    """
    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print(f"Configuration file not found: {config_path}")
        return {}
    except json.JSONDecodeError:
        print(f"Invalid JSON in configuration file: {config_path}")
        return {}

def save_prediction_results(results: List[Dict], output_path: str):
    """
    Save prediction results to file
    
    Args:
        results: Prediction results
        output_path: Output file path
    """
    df = pd.DataFrame(results)
    df.to_csv(output_path, index=False)
    print(f"Results saved to {output_path}")

# Example usage
if __name__ == "__main__":
    # Initialize predictor
    predictor = EmotionPredictor()
    
    # Example prediction (would need actual image)
    print("Emotion predictor initialized successfully!")
    print("Use predictor.predict_emotion(image) to predict emotions from images.")
