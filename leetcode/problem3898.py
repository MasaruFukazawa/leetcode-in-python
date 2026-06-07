#
# problems : find-the-degree-of-each-vertex
#


class Solution:
    def findDegrees(self, matrix: list[list[int]]) -> list[int]:

        if len(matrix) <= 1:
            return [0]

        ans = []

        target_ids = range(len(matrix))

        for i in target_ids:
            degree = 0

            for j in target_ids:
                if i == j:
                    continue

                if matrix[i][j] == 1:
                    degree += 1

            ans.append(degree)

        return ans
