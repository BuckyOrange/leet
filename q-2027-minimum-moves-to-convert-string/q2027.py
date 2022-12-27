def minimumMoves(s: str) -> int:
    # i is the operation time and j is the index
    i, j = 0, 0
    while j < len(s):
        if s[j] == 'X':
            i += 1
            j += 3
        else:
            j += 1
    return i
if __name__ == '__main__':
    print(minimumMoves('OOXX'))

