import os
import librosa
import numpy as np
import joblib
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

DATASET_FOLDER = "sample_data/audo"
MODEL_PATH = "models/svm_noise_classifier.pkl"
LABELS = {"white_noise": 0, "low_freq_hum": 1, "high_freq_hiss": 2}

def extract_features(file_path):
    y, sr = librosa.load(file_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfccs, axis=1)

def train_noise_classifier():
    X, y = [], []
    for noise_type, label in LABELS.items():
        folder_path = os.path.join(DATASET_FOLDER, noise_type)
        if os.path.exists(folder_path):
            for file in os.listdir(folder_path):
                if file.endswith(".wav"):
                    file_path = os.path.join(folder_path, file)
                    features = extract_features(file_path)
                    X.append(features)
                    y.append(label)

    if not X:
        raise ValueError("No training data found.")

    X = np.array(X)
    y = np.array(y)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)
    svm_model = SVC(kernel="linear")
    svm_model.fit(X_train, y_train)
    
    os.makedirs("models", exist_ok=True)
    joblib.dump((svm_model, scaler), MODEL_PATH)
    print("Model trained and saved as 'models/svm_noise_classifier.pkl'.")

def classify_noise(audio_path):
    if not os.path.exists(MODEL_PATH):
        train_noise_classifier()

    svm_model, scaler = joblib.load(MODEL_PATH)
    features = extract_features(audio_path).reshape(1, -1)
    features = scaler.transform(features)
    
    noise_labels = {0: "White Noise", 1: "Low-Frequency Hum", 2: "High-Frequency Hiss"}
    prediction = svm_model.predict(features)
    
    return noise_labels.get(prediction[0], "Unknown Noise")
