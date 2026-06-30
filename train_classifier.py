import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, cohen_kappa_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
import os

def train_and_evaluate():
    df = pd.read_csv('outputs/synthetic_features.csv')
    
    # 37 features (3 indices x 12 months + 1 SAR ratio)
    feature_cols = [c for c in df.columns if c not in ['field_id', 'crop_type']]
    X = df[feature_cols]
    y = df['crop_type']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    
    y_pred = clf.predict(X_test)
    
    acc = accuracy_score(y_test, y_pred)
    kappa = cohen_kappa_score(y_test, y_pred)
    
    print(f"Random Forest Model Accuracy: {acc:.4f}")
    print(f"Cohen's Kappa: {kappa:.4f}")
    
    # Confusion matrix
    cm = confusion_matrix(y_test, y_pred, labels=clf.classes_)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=clf.classes_, yticklabels=clf.classes_)
    plt.ylabel('Actual')
    plt.xlabel('Predicted')
    plt.title('Crop Classification Confusion Matrix')
    plt.tight_layout()
    plt.savefig('outputs/confusion_matrix.png')
    print("Saved outputs/confusion_matrix.png")
    
    # Feature importances
    importances = clf.feature_importances_
    indices = np.argsort(importances)[::-1]
    
    print("\nTop 10 Feature Importances:")
    top_features = []
    top_importances = []
    for i in range(10):
        print(f"{i+1}. {feature_cols[indices[i]]}: {importances[indices[i]]:.4f}")
        top_features.append(feature_cols[indices[i]])
        top_importances.append(importances[indices[i]])
        
    plt.figure(figsize=(10, 6))
    plt.barh(range(10), top_importances[::-1], align='center')
    plt.yticks(range(10), top_features[::-1])
    plt.xlabel('Importance')
    plt.title('Top 10 Feature Importances')
    plt.tight_layout()
    plt.savefig('outputs/feature_importance.png')
    print("Saved outputs/feature_importance.png")
    
    joblib.dump(clf, 'outputs/rf_model.joblib')
    print("Saved model to outputs/rf_model.joblib")
    
if __name__ == '__main__':
    train_and_evaluate()
