import numpy as np
import scipy.signal as signal
import librosa

def low_pass_filter(input_signal, sr, cutoff_freq=3000, order=50):
    """Applies a Low-Pass FIR filter using Hamming window."""
    nyquist = sr / 2
    cutoff = cutoff_freq / nyquist
    h = signal.firwin(order + 1, cutoff, window='hamming')
    return signal.lfilter(h, 1, input_signal)

def high_pass_filter(input_signal, sr, cutoff_freq=3000, order=50):
    """Applies a High-Pass FIR filter using Hamming window."""
    nyquist = sr / 2
    cutoff = cutoff_freq / nyquist
    h = signal.firwin(order + 1, cutoff, pass_zero=False, window='hamming')
    return signal.lfilter(h, 1, input_signal)

def wiener_filter(input_signal):
    """Applies Wiener filtering for noise reduction."""
    return signal.wiener(input_signal)

def apply_filter(audio_path, filter_type):
    """Loads audio and applies the selected filter."""
    y, sr = librosa.load(audio_path, sr=None)
    
    if filter_type == "low-pass":
        filtered_audio = low_pass_filter(y, sr)
    elif filter_type == "high-pass":
        filtered_audio = high_pass_filter(y, sr)
    elif filter_type == "wiener":
        filtered_audio = wiener_filter(y)
    else:
        raise ValueError("Invalid filter type. Choose 'low-pass', 'high-pass', or 'wiener'.")
    
    librosa.output.write_wav("data/filtered_audio.wav", filtered_audio, sr)
    print(f"Filtered audio saved as 'data/filtered_audio.wav'.")
    return filtered_audio, sr
