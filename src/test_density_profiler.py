
from image_to_matrix import ImageToMatrixConverter
from matrix_compressor import MatrixCompressor
from density_profiler import DensityProfiler


image_path = "images/sign1.jpeg"

converter = ImageToMatrixConverter(image_path)
matrix = converter.convert()

compressor = MatrixCompressor(matrix)
compressed_matrix = compressor.compress()

profiler = DensityProfiler(compressed_matrix)

row_profile = profiler.get_row_profile()
column_profile = profiler.get_column_profile()

print("Row Profile:")
print(row_profile)

print("\nColumn Profile:")
print(column_profile)

print("\nRow profile length:", len(row_profile))
print("Column profile length:", len(column_profile))