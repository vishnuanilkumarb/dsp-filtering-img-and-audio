import librosa
import numpy as np
from sklearn.svm import SVC
import joblib
import matplotlib.pyplot as plt

# Load an audio file
def extract_features(audio_path):
    y, sr = librosa.load(audio_path, sr=None)
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    return np.mean(mfccs, axis=1)

# Load a pre-trained SVM model
model = joblib.load('svm_noise_classifier.pkl')

# Predict noise type
audio_path = '../data/sample_audio.wav'
features = extract_features(audio_path).reshape(1, -1)
prediction = model.predict(features)

# Display results
print(f"Predicted Noise Type: {prediction[0]}")

# Recommend best filter
filter_recommendation = {
    'White Noise': 'Use Wiener Filter',
    'Low-Frequency Hum': 'Use High-Pass Filter',
    'High-Frequency Hiss': 'Use Low-Pass Filter'
}

print(f"Recommended Filter: {filter_recommendation.get(prediction[0], 'Try different filters')}")
