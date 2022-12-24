from typing import List


def nearestValidPoint(x: int, y: int, points: List[List[int]]) -> int:
    mindis = 9999
    coord = 9999
    for i in range(len(points)):
        if points[i][0] == x:
            if mindis > abs(y - points[i][1]):
                mindis = abs(y - points[i][1])
                coord = i
            elif mindis == abs(y - points[i][1]):
                coord = min(coord, i)
        elif points[i][1] == y:
            if mindis > abs(x - points[i][0]):
                mindis = abs(x - points[i][0])
                coord = i
            elif mindis == abs(x - points[i][0]):
                coord = min(coord, i)
    if coord == 9999:
        return -1
    return coord

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(nearestValidPoint(3,4,[[3,4]]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
