# Question
> Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.

Input:
```
array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [1, 6, -1, 10]
```

Output:
```
true
```
# Solution
## 思路
用一個 for 迴圈尋遍 sequence list, 每個目標值得 index 應該為該範圍最小，若否的話就 return False。

* 判斷目標值是否在該 list 內，若無 return False。
* 判斷目標 index 值是否為該範圍 list 最小，若無 return False。
* 尋遍過的目標值改為 None 避免重複判斷。