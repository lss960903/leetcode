# 多路归并
「多路归并」、「堆」、「优先队列」
## 264. 丑数 II(https://leetcode.com/problems/ugly-number-ii/description/)
丑数 就是只包含质因数 2、3 和 5 的正整数。  

### approach1. 使用优先队列：
1. 起始先将最小丑数1放入队列
2. 每次从队列取出最小值x，然后将x所对应的丑数 2x、3x和5x进行入队。
3. 对步骤 2 循环多次，第n次出队的值即是答案。
为了防止同一丑数多次进队，我们需要使用数据结构set来记录入过队列的丑数。  
```java
class Solution {
    int[] nums = new int[]{2,3,5};
    public int nthUglyNumber(int n) {
        Set<Long> set = new HashSet<>();
        Queue<Long> pq = new PriorityQueue<>();
        set.add(1L);
        pq.add(1L);
        for (int i = 1; i <= n; i++) {
            long x = pq.poll();
            if (i == n) return (int)x;
            for (int num : nums) {
                long t = num * x;
                if (!set.contains(t)) {
                    set.add(t);
                    pq.add(t);
                }
            }
        }
        return -1;
    }
}
```
T:O(nlogn)  
S:O(n)

### approach2. 多路归并：

```java
class Solution {
    public int nthUglyNumber(int n) {
        // ans 用作存储已有丑数（从下标 1 开始存储，第一个丑数为 1）
        int[] ans = new int[n + 1];
        ans[1] = 1;
        // 由于三个有序序列都是由「已有丑数」*「质因数」而来
        // i2、i3 和 i5 分别代表三个有序序列当前使用到哪一位「已有丑数」下标（起始都指向 1）
        for (int i2 = 1, i3 = 1, i5 = 1, idx = 2; idx <= n; idx++) {
            // 由 ans[iX] * X 可得当前有序序列指向哪一位
            int a = ans[i2] * 2, b = ans[i3] * 3, c = ans[i5] * 5;
            // 将三个有序序列中的最小一位存入「已有丑数」序列，并将其下标后移
            int min = Math.min(a, Math.min(b, c));
            // 由于可能不同有序序列之间产生相同丑数，因此只要一样的丑数就跳过（不能使用 else if ）
            if (min == a) i2++; 
            if (min == b) i3++;
            if (min == c) i5++;
            ans[idx] = min;
        }
        return ans[n];
    }
}
```
T: O(n)
S: O(n)


## 371.Find K Pairs with Smallest Sums(https://leetcode.com/problems/find-k-pairs-with-smallest-sums/)
给定两个以 非递减顺序排列 的整数数组 nums1 和 nums2 , 以及一个整数 k 。  
定义一对值 (u,v)，其中第一个元素来自 nums1，第二个元素来自 nums2 。  
请找到和最小的 k 个数对 (u1,v1),  (u2,v2)  ...  (uk,vk) 。  

由于 nums1 和 nums2 均已按升序排序，因此每个 nums1[i] 参与构成的点序列也为升序排序，这引导我们使用「多路归并」来进行求解。
首次取出的二元组为 (0,0)，即点对 (nums1[0],nums2[0])，取完后将序列的下一位点对 `(nums1[0],nums2[1])` `(nums1[1],nums2[1])` sum较小的那个 以二元组形式放入优先队列。
```python
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        res = []
        m,n = len(nums1), len(nums2)
        heap = []
        for i in range(m):
            heappush(heap, [nums1[i] + nums2[0], i, 0])
        while len(res) < k:
            peak = heappop(heap)
            i = peak[1]
            j = peak[2]
            res.append([nums1[i], nums2[j]])
            if j < n-1:
                heappush(heap, [nums1[i]+nums2[j+1], i, j+1])
        return res
```


## 786.K-th Smallest Prime Fraction(https://leetcode.com/problems/k-th-smallest-prime-fraction/)
```python
class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        res = []
        n = len(arr)
        heap = []
        for i in range(1, n):
            heappush(heap, [arr[0]/arr[i], 0, i])
        while len(res) < k:
            peak = heappop(heap)
            i = peak[1]
            j = peak[2]
            res.append([arr[i], arr[j]])
            if i < n-1:
                heappush(heap, [arr[i+1]/ arr[j], i+1, j])
        return res[-1]
```