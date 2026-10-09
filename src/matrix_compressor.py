
class MatrixCompressor:

    def __init__(self, matrix):
        self.matrix = matrix

    def compress(self):
        compressed_matrix = []

        for i in range(0, 64, 4):
            row = []

            for j in range(0, 64, 4):
                ink_count = 0

                for x in range(i, i + 4):
                    for y in range(j, j + 4):
                        if self.matrix[x][y] == 1:
                            ink_count += 1

                if ink_count >= 2:
                    row.append(1)
                else:
                    row.append(0)

            compressed_matrix.append(row)

        return compressed_matrix