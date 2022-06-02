# Question
> Write a function that takes in a non-empty array of distinct integers and an
integer representing a target sum. If any two numbers in the input array sum
up to the target sum, the function should return them in an array, in any
order. If no two numbers sum up to the target sum, the function should return
an empty array.

Input:
```
array = [3, 5, -4, 8, 11, 1, -1, 6]
targetSum = 10
```

Output:
```
[-1, 11]
```
# Solution
## 思路
一個 for 迴圈，從第一個開始把每個 element 尋遍，並且 copy 原本 array 並刪除自身，用 count 尋找是否有值為 target_num - element 的值在 list 中(因為 x+y = target_sum 的話 y = target_sum - x)，這邊主要求的是 y ，所以只要找到有的話就 return 該兩值的 array。

* list.copy() 做深拷貝否則則是只有複製指標
* list.remove() 刪除本身 element 避免尋遍時找到自己
* 尋找 array 中非自身數字的值剛好相加為 target_sum 所以該值為 target_sum - 自身值