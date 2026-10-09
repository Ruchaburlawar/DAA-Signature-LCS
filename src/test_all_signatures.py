
import os
import csv

from main import get_fingerprint
from lcs_comparator import LCSComparator


image_folder = "images"
results_folder = "results"

os.makedirs(results_folder, exist_ok=True)

# Get all signature image files
image_files = []

for filename in os.listdir(image_folder):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        image_files.append(filename)

image_files.sort()

# Generate fingerprints
fingerprints = {}

for filename in image_files:
    image_path = os.path.join(image_folder, filename)
    fingerprints[filename] = get_fingerprint(image_path)

# Compare every pair of signatures
results = []

for i in range(len(image_files)):
    for j in range(i + 1, len(image_files)):
        image1 = image_files[i]
        image2 = image_files[j]

        comparator = LCSComparator(
            fingerprints[image1],
            fingerprints[image2]
        )

        lcs_string, lcs_length, similarity = comparator.compare()

        results.append([
            image1,
            image2,
            fingerprints[image1],
            fingerprints[image2],
            lcs_length,
            round(similarity, 2)
        ])

# Save results to CSV
csv_path = os.path.join(results_folder, "comparison_results.csv")

with open(csv_path, "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Signature 1",
        "Signature 2",
        "Fingerprint 1",
        "Fingerprint 2",
        "LCS Length",
        "Similarity (%)"
    ])

    writer.writerows(results)

print("Total images:", len(image_files))
print("Total comparisons:", len(results))
print("Results saved to:", csv_path)