import collections
import sys,_collections
input = sys.stdin.readline

n = int(input())
arr = list(int(input()) for _ in range(n))
arr.sort()
dict_arr = collections.Counter(arr)
common = dict_arr.most_common(2)
print(int(round(sum(arr)/n,0)))
print(arr[n//2])
if len(common) ==1:
    print(common[0][0])
else:
    print(common[0][0] if common[1][1]!=common[0][1] else common[1][0])
print(arr[-1]-arr[0])
