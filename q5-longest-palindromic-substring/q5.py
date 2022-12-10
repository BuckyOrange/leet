class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxtmp = s[0]

        for i in range(1, len(s)):
            dtmp = ''
            if s[i] == s[i - 1]:
                dtmp = s[i] + s[i - 1]
                da = i - 2
                db = i + 1
                while da >= 0 and db <= len(s) - 1 and s[da] == s[db]:
                    dtmp = s[da] + dtmp + s[db]
                    da -= 1
                    db += 1

            tmp = s[i]
            a = i - 1
            b = i + 1
            while a >= 0 and b <= len(s) - 1 and s[a] == s[b]:
                tmp = s[a] + tmp + s[b]
                a -= 1
                b += 1

            maxtmp = max([maxtmp, tmp, dtmp], key=lambda x: len(x))
        return maxtmp