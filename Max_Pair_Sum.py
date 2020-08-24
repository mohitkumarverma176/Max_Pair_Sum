def Solution(arr, n):
    sum_result = 0
    arr.sort()
    sum_result = arr[n-1] + arr[n-2]
    return sum_result
N = int(input())
arr = []
l = 0
for e in input().split():
    arr.append(int(e))
    l += 1
n = len(arr)
print(Solution(arr, n))
