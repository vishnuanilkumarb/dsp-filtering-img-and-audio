import cv2
import numpy as np
from skimage import exposure

def apply_filter(image, filter_type):
    """Applies the selected filter to the image."""
    if filter_type == "low-pass":
        kernel = np.ones((5, 5), np.float32) / 25  # Blurring kernel
        return cv2.filter2D(image, -1, kernel)

    elif filter_type == "high-pass":
        kernel = np.array([[-1, -1, -1], 
                           [-1,  8, -1], 
                           [-1, -1, -1]])  # Edge detection
        return cv2.filter2D(image, -1, kernel)

    elif filter_type == "adaptive-contrast":
        return exposure.equalize_adapthist(image, clip_limit=0.03)

    else:
        raise ValueError("Invalid filter type. Choose 'low-pass', 'high-pass', or 'adaptive-contrast'.")

def process_image(image_path, filter_type):
    """Loads image and applies filtering."""
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        raise ValueError("Could not load the image. Check the file path.")

    filtered_image = apply_filter(image, filter_type)
    cv2.imwrite("data/filtered_image.png", (filtered_image * 255).astype(np.uint8))
    print(f"Filtered image saved as 'data/filtered_image.png'.")
    return filtered_image
