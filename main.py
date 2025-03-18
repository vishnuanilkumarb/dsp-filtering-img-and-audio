import argparse
import os
import librosa
import joblib
import numpy as np
from dsp.audio_processing import process_audio
from dsp.image_processing import process_image
from dsp.noise_classifier import train_noise_classifier, classify_noise

DATASET_FOLDER = "sample_data/audio"
MODEL_PATH = "models/svm_noise_classifier.pkl"

def main():
    parser = argparse.ArgumentParser(description="DSP-Based Noise Reduction & Image Enhancement")
    parser.add_argument("file", help="Path to the input file (audio or image)")
    parser.add_argument("--type", choices=["audio", "image"], required=True, help="Specify if the input is 'audio' or 'image'")
    parser.add_argument("--filter", choices=["low-pass", "high-pass", "wiener", "adaptive-contrast", "classify"], required=True, help="Filter type to apply")
    args = parser.parse_args()

    if args.type == "audio":
        if args.filter == "classify":
            if not os.path.exists(MODEL_PATH):
                print(" Model not found! Training now...")
                train_noise_classifier()
            noise_type = classify_noise(args.file)
            print(f"Predicted Noise Type: {noise_type}")
        else:
            process_audio(args.file, args.filter)

    elif args.type == "image":
        process_image(args.file, args.filter)

if __name__ == "__main__":
    main()
