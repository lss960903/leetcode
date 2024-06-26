## 数组
1. for loop: for i in (range(len(nums)))
2. max: float('inf'), 
3. ans = [float('inf')]*len(nums)
4. 平方: nums[i] ** 2
5. 初始化矩阵: `grid = [[0] * n for _ in range(n)]`
6. coner case: if not t or not s: return ""
7. divmod(num, 10) - return tuple(quotient , remainder)

## Dict
```
dict.get('b', 0) 如果'b'在dict中为key return value的值 否则return 0
dict1 == dict2
for key in dict1
dict.pop('a') same as `del dict('a')`
dict['a'] = dict.get('a', 0) + 1
dict.popitem() remove last added element
```

## String
s = "abcdfg" s[1:4] = "bcd"

## Set
set = {}
add()
remove()

## List
list.append('')
list.count('')
list.remove('') passing element
list.pop(1) passing index
list.reverse()
list.insert(0, 'a') 在index=0 的位置插入 list 长度增加
sort() - sorts the list ascending by default.

**降序**：thislist.sort(reverse = True)
**自定义**：
```python
# A function that returns the length of the value:
def myFunc(e):
  return len(e)
cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
```