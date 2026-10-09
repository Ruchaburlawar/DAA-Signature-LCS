from image_to_matrix import ImageToMatrixConverter
from matrix_compressor import MatrixCompressor


image_path = "images/sign1.jpeg"

converter = ImageToMatrixConverter(image_path)
matrix = converter.convert()

compressor = MatrixCompressor(matrix)
compressed_matrix = compressor.compress()

print("Rows:", len(compressed_matrix))
print("Columns:", len(compressed_matrix[0]))

print("\n16 x 16 Compressed Matrix:\n")

for row in compressed_matrix:
    print("".join(map(str, row)))