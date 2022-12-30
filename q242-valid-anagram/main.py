import collections


def isAnagram(s: str, t: str) -> bool:
        # s = sorted(list(s))
        # t = sorted(list(t))

        # if s == t:
        #     return True
        # return False

        f1 = collections.Counter(s)
        f2 = collections.Counter(t)
        if f1 == f2:
            return True
        else:
            return False

if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(isAnagram(s, t))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
