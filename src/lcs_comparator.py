
class LCSComparator:

    def __init__(self, string1, string2):
        self.string1 = string1
        self.string2 = string2

    def compare(self):
        m = len(self.string1)
        n = len(self.string2)

        # Create a DP table filled with zeros
        dp = []

        for i in range(m + 1):
            row = []

            for j in range(n + 1):
                row.append(0)

            dp.append(row)

        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):

                if self.string1[i - 1] == self.string2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    if dp[i - 1][j] > dp[i][j - 1]:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]

        # Traceback to reconstruct the LCS
        i = m
        j = n
        lcs_string = ""

        while i > 0 and j > 0:

            if self.string1[i - 1] == self.string2[j - 1]:
                lcs_string = self.string1[i - 1] + lcs_string
                i -= 1
                j -= 1

            elif dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1

            else:
                j -= 1

        lcs_length = dp[m][n]

        # Calculate similarity percentage
        shorter_length = min(m, n)

        if shorter_length == 0:
            similarity = 0
        else:
            similarity = (lcs_length / shorter_length) * 100

        return lcs_string, lcs_length, similarity