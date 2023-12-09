# -*- coding:utf-8 -*-


class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        answer: int = 0

        for operation in operations:
            if "++" in operation:
                answer += 1
            elif "--" in operation:
                answer -= 1

        return answer
