
from lcs_comparator import LCSComparator


string1 = "ABCBDAB"
string2 = "BDCABA"

comparator = LCSComparator(string1, string2)

lcs_string, lcs_length, similarity = comparator.compare()

print("String 1:", string1)
print("String 2:", string2)
print("LCS:", lcs_string)
print("LCS Length:", lcs_length)
print("Similarity:", round(similarity, 2), "%")