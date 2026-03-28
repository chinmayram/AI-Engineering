"""
Machine Learning Model Implementation
This module contains the ML model training and prediction logic.
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MLModel:
    """Machine Learning Model wrapper for training and predictions."""
    
    def __init__(self, model_type='random_forest', random_state=42):
        """
        Initialize the ML model.
        
        Args:
            model_type (str): Type of model to use
            random_state (int): Random state for reproducibility
        """
        self.model_type = model_type
        self.random_state = random_state
        self.model = None
        self.scaler = StandardScaler()
        self.is_trained = False
        
        logger.info(f"Initialized {model_type} model")
    
    def build_model(self, **kwargs):
        """
        Build the ML model with specified parameters.
        
        Args:
            **kwargs: Model-specific parameters
        """
        if self.model_type == 'random_forest':
            self.model = RandomForestClassifier(
                random_state=self.random_state,
                **kwargs
            )
        else:
            raise ValueError(f"Unknown model type: {self.model_type}")
        
        logger.info(f"Built {self.model_type} model")
    
    def train(self, X, y, test_size=0.2):
        """
        Train the ML model.
        
        Args:
            X (array-like): Feature matrix
            y (array-like): Target vector
            test_size (float): Test set proportion
            
        Returns:
            dict: Training metrics
        """
        if self.model is None:
            self.build_model()
        
        # Split data
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=test_size, random_state=self.random_state
        )
        
        # Scale features
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        
        # Train model
        self.model.fit(X_train_scaled, y_train)
        self.is_trained = True
        
        # Evaluate
        y_pred = self.model.predict(X_test_scaled)
        metrics = {
            'accuracy': accuracy_score(y_test, y_pred),
            'precision': precision_score(y_test, y_pred, average='weighted'),
            'recall': recall_score(y_test, y_pred, average='weighted'),
            'f1': f1_score(y_test, y_pred, average='weighted')
        }
        
        logger.info(f"Model trained. Accuracy: {metrics['accuracy']:.4f}")
        return metrics
    
    def predict(self, X):
        """
        Make predictions on new data.
        
        Args:
            X (array-like): Feature matrix
            
        Returns:
            array: Predictions
        """
        if not self.is_trained:
            raise ValueError("Model must be trained before making predictions")
        
        X_scaled = self.scaler.transform(X)
        return self.model.predict(X_scaled)
    
    def save_model(self, filepath):
        """Save the trained model to disk."""
        if self.model is None:
            raise ValueError("No model to save")
        
        joblib.dump(self.model, filepath)
        logger.info(f"Model saved to {filepath}")
    
    def load_model(self, filepath):
        """Load a trained model from disk."""
        self.model = joblib.load(filepath)
        self.is_trained = True
        logger.info(f"Model loaded from {filepath}")


def main():
    """Example usage of the ML model."""
    # Generate sample data
    from sklearn.datasets import load_iris
    
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Create and train model
    model = MLModel(model_type='random_forest')
    metrics = model.train(X, y)
    
    print("\nTraining Metrics:")
    for metric_name, metric_value in metrics.items():
        print(f"  {metric_name}: {metric_value:.4f}")
    
    # Make predictions on sample
    sample_predictions = model.predict(X[:5])
    print(f"\nSample predictions: {sample_predictions}")


if __name__ == "__main__":
    main()
