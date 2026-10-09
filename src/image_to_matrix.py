from PIL import Image


class ImageToMatrixConverter:

    def __init__(self, image_path, threshold=128):
        self.image_path = image_path
        self.threshold = threshold

    def convert(self):
        image = Image.open(self.image_path)

        # Convert image to grayscale
        image = image.convert("L")

        # Resize to 64 x 64
        image = image.resize((64, 64))

        # Convert pixels into 0 and 1
        matrix = []

        for y in range(64):
            row = []

            for x in range(64):
                pixel = image.getpixel((x, y))

                if pixel < self.threshold:
                    row.append(1)
                else:
                    row.append(0)

            matrix.append(row)

        return matrix