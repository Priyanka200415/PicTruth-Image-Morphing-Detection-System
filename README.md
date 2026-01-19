# PicTruth – Image Morphing Detection System

PicTruth is a Python-based image forensics project developed as part of the **Problem Solving with Python** course.  
The objective of this project is to detect whether an image has been digitally edited or morphed by analysing **edge variance** and **colour distribution statistics**.

---

## Project Details

- **Project Title:** PicTruth (Detection of Morphing Techniques)
- **Course:** Problem Solving with Python
- **Institution:** XIM University
- **Date of Submission:** 01 December 2024

---

## Submitted By

**Priyanka Priyadarshini Das (UCSE23042)**
**Ishika Bandopadhyay (UCSE23027)**
---

## Motivation

In today’s digital world, images are widely used for communication and information sharing.  
However, image editing and morphing tools make it difficult to verify whether an image is authentic.

I developed PicTruth to provide a **simple and computationally efficient method** to detect possible image manipulation using basic image processing techniques, without relying on heavy machine learning models.

---

## Project Objectives

- To detect possible image manipulation using edge detection
- To analyse colour inconsistencies caused by image editing
- To visualise detected edges for better interpretation
- To classify images as **likely not edited** or **might be edited**

---
## Contribution

- Documentation improvements
- Project review
- Running TestCases

---
## Key Features

- Works for both **grayscale and colour images**
- Uses **Sobel edge detection** for identifying edge inconsistencies
- Analyses **RGB colour variance**
- Displays original image and edge-detected image side by side
- Lightweight and easy to run

---

## Technologies Used

- **Programming Language:** Python
- **Libraries Used:**
  - NumPy
  - Matplotlib
  - SciPy (Sobel filter)

---

## System Workflow

1. Load the input image
2. Normalize pixel values
3. Convert image to grayscale (if required)
4. Apply Sobel filter for edge detection
5. Calculate edge variance
6. Calculate colour variance (for RGB images)
7. Compare values with predefined thresholds
8. Display result and visual output

---

## Output

- Message indicating:
  - *“The image is likely not edited”*  
  - or *“The image might be edited”*
- Visualization of:
  - Original Image
  - Edge-detected Image

---

## Challenges Faced

- Selecting appropriate threshold values
- Handling different image formats
- Ensuring compatibility with both colour and grayscale images

---

## Future Enhancements

- Adaptive thresholding using machine learning
- Support for more manipulation techniques
- GUI-based image upload interface
- Improved detection accuracy

---

## Conclusion

PicTruth provides a simple yet effective approach for detecting image morphing and manipulation.  
By combining edge variance analysis and colour distribution statistics, the system offers a strong foundation for image authenticity verification and digital forensics.

---

**Submitted to XIM University – Problem Solving with Python Course**
