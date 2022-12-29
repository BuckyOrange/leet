def findTheDifference(s: str, t: str) -> str:
    return chr((sum(ord(i) for i in t) - (sum(ord(i) for i in s))))


if __name__ == '__main__':
    s = "abcd"
    t = "abcde"
    print(findTheDifference(s,t))