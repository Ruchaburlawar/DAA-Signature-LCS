
import csv
import os


results_path = "results/comparison_results.csv"


def get_group(filename):
    if filename.startswith("person1_"):
        return "person1"
    elif filename.startswith("person2_"):
        return "person2"
    else:
        return "sign"


same_group_scores = []
different_group_scores = []

group_pair_scores = {}

with open(results_path, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        image1 = row["Signature 1"]
        image2 = row["Signature 2"]

        group1 = get_group(image1)
        group2 = get_group(image2)

        score = float(row["Similarity (%)"])

        if group1 == group2:
            same_group_scores.append(score)
        else:
            different_group_scores.append(score)

        pair_name = tuple(sorted([group1, group2]))

        if pair_name not in group_pair_scores:
            group_pair_scores[pair_name] = []

        group_pair_scores[pair_name].append(score)


def print_summary(title, scores):
    print("\n" + title)

    if len(scores) == 0:
        print("No comparisons found.")
        return

    average = sum(scores) / len(scores)

    print("Number of comparisons:", len(scores))
    print("Average similarity:", round(average, 2), "%")
    print("Minimum similarity:", min(scores), "%")
    print("Maximum similarity:", max(scores), "%")


print_summary("Comparisons within the same group", same_group_scores)

print_summary("Comparisons between different groups", different_group_scores)

print("\nAverage similarity for each group pair:")

for pair_name in sorted(group_pair_scores):
    scores = group_pair_scores[pair_name]
    average = sum(scores) / len(scores)

    print(
        pair_name[0],
        "vs",
        pair_name[1],
        ":",
        round(average, 2),
        "%"
    )

# Save the analysis to a text file
report_path = "results/analysis_summary.txt"

with open(report_path, "w") as file:
    file.write("Signature Matching - Results Analysis\n")
    file.write("=====================================\n")

    file.write(
        "\nSame-group average similarity: "
        + str(round(sum(same_group_scores) / len(same_group_scores), 2))
        + "%\n"
    )

    file.write(
        "Different-group average similarity: "
        + str(round(sum(different_group_scores) / len(different_group_scores), 2))
        + "%\n"
    )

    file.write("\nGroup pair averages:\n")

    for pair_name in sorted(group_pair_scores):
        scores = group_pair_scores[pair_name]
        average = sum(scores) / len(scores)

        file.write(
            pair_name[0] + " vs " + pair_name[1]
            + ": " + str(round(average, 2)) + "%\n"
        )

print("\nAnalysis saved to:", report_path)