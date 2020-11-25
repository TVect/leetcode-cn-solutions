"""
统计所有小于非负整数 n 的质数的数量。

示例 1：
    输入：n = 10
    输出：4
    解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
示例 2：
    输入：n = 0
    输出：0
示例 3：
    输入：n = 1
    输出：0

提示：
    0 <= n <= 5 * 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-primes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math


class Solution:

    def countPrimes_1(self, n: int) -> int:
        if n <= 2:
            return 0
        primes = [2]
        for num in range(3, n):
            square_root = math.sqrt(num)
            i = 0
            while i < len(primes) and primes[i] <= square_root:
                if num % primes[i] == 0:
                    break
                i += 1
            else:
                primes.append(num)
        return len(primes)

    # 厄拉多塞筛法
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        records = [1] * n
        records[0], records[1], records[2] = 0, 0, 1
        for num in range(2, int(math.sqrt(n))+1):
            if records[num] == 1:
                for idx in range(num+num, n, num):
                    records[idx] = 0
        return sum(records)


n = 5000000
# n = 100
# n = 10
print(Solution().countPrimes(n))
