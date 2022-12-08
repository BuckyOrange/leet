def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    #滑块窗口
    count = 0
    lmax = 0
    while s:
        if len(s) == lmax:
            return lmax
        if len(set(s[0:0 + count])) == count:
            count += 1
        else:
            lmax = max(lmax, count - 1)
            s = s[1:]
            count -= 1
    print(lmax)
    return lmax

