
from image_to_matrix import ImageToMatrixConverter
from matrix_compressor import MatrixCompressor
from density_profiler import DensityProfiler
from row_col_compressor import RowColCompressor


image_path = "images/sign1.jpeg"

converter = ImageToMatrixConverter(image_path)
matrix = converter.convert()

compressor = MatrixCompressor(matrix)
compressed_matrix = compressor.compress()

profiler = DensityProfiler(compressed_matrix)

row_profile = profiler.get_row_profile()
column_profile = profiler.get_column_profile()

fingerprint_compressor = RowColCompressor(
    row_profile, column_profile
)

fingerprint = fingerprint_compressor.compress()

print("Row Profile:", row_profile)
print("Column Profile:", column_profile)

print("\nSignature Fingerprint:", fingerprint)
print("Fingerprint Length:", len(fingerprint))