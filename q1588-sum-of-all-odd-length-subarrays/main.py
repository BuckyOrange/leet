from typing import List

def sumOddLengthSubarrays(arr: List[int]) -> int:

    tmp = 0
    for i in range(1, len(arr)+1,2):
        for j in range(len(arr)-i+1):
            tmp +=sum(arr[j:j+i])

    return tmp

    # sum = 0
    # n = len(arr)
    # for i, v in enumerate(arr):
    #     leftCount, rightCount = i, n - i - 1
    #     leftOdd = (leftCount + 1) // 2
    #     rightOdd = (rightCount + 1) // 2
    #     leftEven = leftCount // 2 + 1
    #     rightEven = rightCount // 2 + 1
    #     sum += v * (leftOdd * rightOdd + leftEven * rightEven)
    # return sum
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sumOddLengthSubarrays( [1,4,2,5,3]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
