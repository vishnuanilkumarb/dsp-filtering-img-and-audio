import argparse
import librosa
import numpy as np
import matplotlib.pyplot as plt
from dsp import low_pass_filter, high_pass_filter, wiener_filter, classify_noise
from dsp.image_processing import apply_filter
import cv2

def process_audio(audio_path, filter_type):
    y, sr = librosa.load(audio_path, sr=None)
    if filter_type == 'low-pass':
        filtered_audio = low_pass_filter(y, sr)
    elif filter_type == 'high-pass':
        filtered_audio = high_pass_filter(y, sr)
    elif filter_type == 'wiener':
        filtered_audio = wiener_filter(y)
    else:
        raise ValueError("Invalid filter type. Choose 'low-pass', 'high-pass', or 'wiener'.")
    
    librosa.output.write_wav("data/filtered_audio.wav", filtered_audio, sr)
    print("Filtered audio saved as 'data/filtered_audio.wav'.")

def process_image(image_path, filter_type):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    filtered_image = apply_filter(image, filter_type)
    cv2.imwrite("data/filtered_image.png", filtered_image)
    print("Filtered image saved as 'data/filtered_image.png'.")
    plt.imshow(filtered_image, cmap='gray')
    plt.title(f"Filtered Image - {filter_type}")
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="DSP-Based Noise Reduction & Image Enhancement")
    parser.add_argument("file", help="Path to the input file (audio or image)")
    parser.add_argument("--type", choices=["audio", "image"], required=True, help="Specify if the input is 'audio' or 'image'")
    parser.add_argument("--filter", choices=["low-pass", "high-pass", "wiener", "adaptive-contrast"], required=True, help="Filter type to apply")
    args = parser.parse_args()

    if args.type == "audio":
        process_audio(args.file, args.filter)
    else:
        process_image(args.file, args.filter)

if __name__ == "__main__":
    main()
