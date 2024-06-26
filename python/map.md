## [349: 两个数组的交集] (https://leetcode.com/problems/intersection-of-two-arrays/description/)
给定两个数组，编写一个函数来计算它们的交集。
**使用Dict**
```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # 使用哈希表存储一个数组中的所有元素
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
        
        # 使用集合存储结果
        res = set()
        for num in nums2:
            if num in table:
                res.add(num)
                del table[num]
        
        return list(res)

```
time: O(n+m)
space: O(n+m)

## [202: Happy Number](https://leetcode.com/problems/happy-number/description/)
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。

如果 n 是快乐数就返回 True ；不是，则返回 False 。
```python
class Solution:
    def isHappy(self, n: int) -> bool:
        record = set()
        while True:
            cal = self.calculate(n)
            if cal == 1:
                return True
            elif cal in record:
                return False
            else:
                record.add(cal)
                n = cal
        return False
    #拆分一个数字的每一位数 并平方取和
    def calculate(self, n):
        new_sum = 0
        while n:
            n,r = divmod(n, 10)
            new_sum += r ** 2
        return new_sum
```