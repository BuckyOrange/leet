class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # sorted the list from lowest to highest, then compare each with first one
        # if not, pop last char and continue to compare
        strs.sort(key=lambda x: len(x))
        flag = True
        while strs[0] and flag:
            for i in strs:
                if strs[0] != i[:len(strs[0])]:
                    strs[0] = strs[0][:-1]
                    flag = False

            flag = not flag

        return strs[0]
