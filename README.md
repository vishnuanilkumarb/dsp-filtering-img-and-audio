# 📌 Project: Smart DSP-Based Noise Reduction & Image Enhancement System
## 🚀 Overview
>This project develops an AI-powered Digital Signal Processing (DSP) system for real-time noise reduction in audio signals and image enhancement using adaptive filtering techniques. It integrates MATLAB DSP algorithms, machine learning models, and a GUI for user interaction.

## 📜 Key Features
* ✅ Advanced Audio Noise Reduction – Adaptive Wiener Filtering and Spectral Subtraction for removing noise from speech/audio files.
* ✅ Real-Time Image Enhancement – Adaptive contrast enhancement, edge detection, and noise filtering for images.
* ✅ Adaptive DSP Algorithms – Implementing LMS Adaptive Filters, Wavelet Transforms, and Butterworth/Chebyshev Filtering.
 * ✅ User-Friendly GUI – Users can upload files, choose filters, and apply real-time enhancements.
  * ✅ Machine Learning Integration – Uses SVM and Neural Networks for audio noise classification and adaptive filter selection.

## 🛠️ Tools & Technologies Used
*🔹 MATLAB – Signal Processing Toolbox, Image Processing Toolbox, GUI development
 *🔹 Python (Optional) – TensorFlow/Keras for ML-based adaptive filtering
 *🔹 DSP Algorithms – FIR/IIR filters, Wiener filtering, LMS Adaptive Filtering
 *🔹 Audio Processing – audiorecorder(), filter(), spectrogram()
 *🔹 Image Processing – imfilter(), fspecial(), adaptive histogram equalization
 *🔹 Machine Learning – Speech and noise classification using SVM/Neural Networks

## 🔹 How It Works
### 1️⃣ Audio Noise Reduction Process
  `User uploads an audio file (e.g., noisy speech).
  The system analyzes noise levels using FFT and SNR calculations.
  Adaptive Filtering is applied:
  Spectral Subtraction for removing background noise.
  Wiener Filter for speech enhancement.
  Adaptive LMS Filter for real-time noise suppression.
  Enhanced audio is saved and visualized.`
### 2️⃣ Image Enhancement Process
  > User uploads an image (JPG/PNG).
  Selects an enhancement method:
  Low-Pass Filtering (Noise removal, smoothing).
  High-Pass Filtering (Edge detection, sharpening).
  Adaptive Contrast Stretching.
  Processed image is displayed & saved.
### 3️⃣ GUI Features
  > ✔ Upload & Process Audio/Images
  ✔ Select Filter Type & Adjust Parameters
  ✔ Compare Before & After Filtering
  ✔ Save & Download Enhanced Files

## 📊 Performance Evaluation
  Signal-to-Noise Ratio (SNR) – Before & after filtering.
  Peak Signal-to-Noise Ratio (PSNR) – For image quality enhancement.
  Spectrogram Analysis – Audio spectrum visualization.
## 📖 How to Run the Project
### 🔹 Clone the Repository
* bash
* Copy
* Edit
* `git clone https://github.com/vishnuanilkumarb/dsp-filters.git ||
cd DSP-Noise-Reduction-Image-Enhancement`
* run `python3 -m pip install -r requirements.txt`
* run `python3 -m main` for python.
  #### To get the sample data
  * run `python3 -m sample_data/sample_get`
### 🔹 Run the MATLAB GUI
Open MATLAB and navigate to the GUI folder.
Run the following command:
matlab
Copy
Edit
`run('GUI/dsp_filter_gui.m')`
Upload an audio/image file, select a filter, and apply enhancements.

