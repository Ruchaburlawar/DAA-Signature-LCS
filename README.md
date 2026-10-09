# Offline Signature Matching Using LCS

## Project Overview

This project compares handwritten signature images using the Longest Common Subsequence (LCS) algorithm. Each signature image is converted into a fixed-length hexadecimal fingerprint, and two fingerprints are compared to calculate a structural similarity percentage.

## Objectives

* Convert a signature image into a 64×64 binary matrix.
* Compress the matrix into a 16×16 matrix.
* Calculate row and column density profiles.
* Generate a 16-character hexadecimal fingerprint.
* Compare fingerprints using LCS dynamic programming.
* Calculate and analyze similarity scores.

## Technologies Used

* Python
* Pillow (PIL)
* CSV and other Python standard-library modules

## Project Structure

* `images/` — Input signature images
* `src/` — Python source code and test scripts
* `results/` — Comparison results and analysis
* `requirements.txt` — Required Python packages

## How to Run

Install the dependency:

```bash
pip install -r requirements.txt
```

Run the complete comparison program:

```bash
python src/main.py
```

Run the all-signatures comparison:

```bash
python src/test_all_signatures.py
```

## Algorithm

1. Convert the image to grayscale and resize it to 64×64.
2. Apply thresholding to create a binary matrix.
3. Compress the matrix to 16×16 using 4×4 blocks.
4. Calculate row and column ink-density profiles.
5. Convert the profiles into a 16-character hexadecimal fingerprint.
6. Apply LCS dynamic programming to compare fingerprints.

## Similarity Formula

Similarity (%) = (LCS length / length of the shorter fingerprint) × 100

## Limitations

This is an educational signature-comparison model. Similarity scores indicate structural resemblance and do not establish whether a signature is authentic or forged. Results may be affected by image quality, signature position, scale, and the fingerprint-compression method.

## Evaluation

The project is evaluated on image conversion, matrix compression, density profiling, fingerprint compression, LCS implementation, code quality, and results analysis.
