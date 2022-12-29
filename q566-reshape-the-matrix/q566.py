from typing import List


def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    if len(mat) * len(mat[0]) != r * c:
        return mat

    ans = [[0] * c for _ in range(r)]
    n = len(mat[0])
    for x in range(r * c):
        ans[x // c][x % c] = mat[x // n][x % n]

    return ans


if __name__ == '__main__':
    mat = [[1, 2], [3, 4]]
    r = 1
    c = 4
    print(matrixReshape(mat, r, c))

