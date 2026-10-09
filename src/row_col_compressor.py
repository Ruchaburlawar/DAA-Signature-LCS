
class RowColCompressor:

    def __init__(self, row_profile, column_profile):
        self.row_profile = row_profile
        self.column_profile = column_profile

    def compress_profile(self, profile):
        averages = []

        for i in range(0, 16, 2):
            average = (profile[i] + profile[i + 1]) / 2
            averages.append(average)

        return averages

    def convert_to_hex(self, averages, maximum):
        fingerprint_part = ""

        for value in averages:
            if maximum == 0:
                level = 0
            else:
                level = round((value / maximum) * 15)

            character = format(level, "X")
            fingerprint_part += character

        return fingerprint_part

    def compress(self):
        row_averages = self.compress_profile(self.row_profile)
        column_averages = self.compress_profile(self.column_profile)

        all_averages = row_averages + column_averages
        maximum = max(all_averages)

        row_string = self.convert_to_hex(row_averages, maximum)
        column_string = self.convert_to_hex(column_averages, maximum)

        fingerprint = row_string + column_string

        return fingerprint