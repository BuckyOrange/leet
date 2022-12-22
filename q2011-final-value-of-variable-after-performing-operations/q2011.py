class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        tmp = 0
        for i in operations:
            if i[0] == '+' or i[-1] == '+':
                tmp += 1
            else:
                tmp -= 1
        return tmp