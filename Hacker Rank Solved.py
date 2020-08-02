#Given list is [2,3,6,6,5]. The maximum score is , second maximum is . Hence, we print  as the runner-up score.
n = int(input())
arr = map(int, input().split())
a = list(arr)
r = max(a)
while max(a) == r:
    a.remove(max(a))

print(max(a))
