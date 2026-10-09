
from image_to_matrix import ImageToMatrixConverter
from matrix_compressor import MatrixCompressor
from density_profiler import DensityProfiler
from row_col_compressor import RowColCompressor
from lcs_comparator import LCSComparator


def get_fingerprint(image_path):
    # Stage 2: Image to binary matrix
    converter = ImageToMatrixConverter(image_path)
    matrix = converter.convert()

    # Stage 3: Compress 64x64 to 16x16
    compressor = MatrixCompressor(matrix)
    compressed_matrix = compressor.compress()

    # Stage 4: Get row and column profiles
    profiler = DensityProfiler(compressed_matrix)
    row_profile = profiler.get_row_profile()
    column_profile = profiler.get_column_profile()

    # Stage 5: Generate 16-character fingerprint
    fingerprint_compressor = RowColCompressor(
        row_profile, column_profile
    )
    fingerprint = fingerprint_compressor.compress()

    return fingerprint


# Enter the paths of the two signature images
image1 = "images/sign1.jpeg"
image2 = "images/sign2.jpeg"

fingerprint1 = get_fingerprint(image1)
fingerprint2 = get_fingerprint(image2)

print("Signature 1 Fingerprint:", fingerprint1)
print("Signature 2 Fingerprint:", fingerprint2)

# Stage 6: Compare fingerprints using LCS
comparator = LCSComparator(fingerprint1, fingerprint2)

lcs_string, lcs_length, similarity = comparator.compare()

print("\nLongest Common Subsequence:", lcs_string)
print("LCS Length:", lcs_length)
print("Similarity:", round(similarity, 2), "%")