
class DensityProfiler:

    def __init__(self, matrix):
        self.matrix = matrix

    def get_row_profile(self):
        row_profile = []

        for row in self.matrix:
            count = 0

            for pixel in row:
                if pixel == 1:
                    count += 1

            row_profile.append(count)

        return row_profile

    def get_column_profile(self):
        column_profile = []

        for col in range(len(self.matrix[0])):
            count = 0

            for row in range(len(self.matrix)):
                if self.matrix[row][col] == 1:
                    count += 1

            column_profile.append(count)

        return column_profile