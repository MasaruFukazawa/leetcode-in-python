#
# problems : digit-frequency-score
#


class Solution:
    def digitFrequencyScore(self, n: int) -> int:

        ns: list[int] = list(map(int, list(str(n))))

        sum: int = 0

        for n in ns:
            sum += int(n)

        return sum
