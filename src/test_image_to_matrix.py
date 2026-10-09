from image_to_matrix import ImageToMatrixConverter


image_path = "images/sign1.jpeg"

converter = ImageToMatrixConverter(image_path)

matrix = converter.convert()

print("Rows:", len(matrix))
print("Columns:", len(matrix[0]))

print("\n64 x 64 Matrix:\n")

for row in matrix:
    print("".join(map(str, row)))