# PicTruth: Image Morphing Detection using Edge and Color Variance
# Written by: Priyanka Priyadarshini Das
# Course: Problem Solving with Python

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
from scipy.ndimage import sobel


def detect_edges(image):
    """
    This function detects edges in an image using the Sobel filter.
    If the image is colored, it is first converted to grayscale.
    """

    # Convert to grayscale if image is colored
    if image.ndim == 3:
        image = np.mean(image, axis=2)

    # Apply Sobel filter in horizontal and vertical directions
    sobel_x = sobel(image, axis=0, mode='constant')
    sobel_y = sobel(image, axis=1, mode='constant')

    # Compute edge magnitude
    edges = np.hypot(sobel_x, sobel_y)

    return edges


def analyze_image(image_path):
    """
    This function analyzes an image to detect possible morphing or editing.
    It calculates edge variance and color variance and compares them
    with predefined thresholds.
    """

    # Load the image
    image = imread(image_path)

    # Normalize pixel values
    image = image / 255.0

    # Detect edges
    edges = detect_edges(image)

    # Calculate edge variance
    edge_variance = np.var(edges)

    # Calculate color variance (only for color images)
    color_variance = 0
    if image.ndim == 3:
        color_variance = np.var(image, axis=(0, 1)).mean()

    # Threshold values (chosen experimentally)
    edge_threshold = 0.1
    color_threshold = 0.05

    # Decision based on thresholds
    if edge_variance > edge_threshold or color_variance > color_threshold:
        print("The image might be edited.")
    else:
        print("The image is likely not edited.")

    # Display original image and edge-detected image
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title("Original Image")
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title("Edge Detection")
    plt.axis("off")

    plt.show()


# ---- MAIN FUNCTION CALL ----
# Replace 'XYZ.jpg' with your test image name
analyze_image('XYZ.jpg')
