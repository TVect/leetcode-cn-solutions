"""
这里有 n 个航班，它们分别从 1 到 n 进行编号。
我们这儿有一份航班预订表，表中第 i 条预订记录 bookings[i] = [j, k, l] 意味着我们在从 j 到 k 的每个航班上预订了 l 个座位。
请你返回一个长度为 n 的数组 answer，按航班编号顺序返回每个航班上预订的座位数。

示例：
    输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
    输出：[10,55,45,25,25]

提示：
    1 <= bookings.length <= 20000
    1 <= bookings[i][0] <= bookings[i][1] <= n <= 20000
    1 <= bookings[i][2] <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/corporate-flight-bookings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from functools import reduce
from typing import List


class Solution:

    # 朴素做法
    def corpFlightBookings_1(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        for booking in bookings:
            for idx in range(booking[0]-1, booking[1]):
                res[idx] += booking[2]
        return res

    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # diff[i] 表示 第 i 站有多少人上或者下
        diff = [0] * n
        for booking in bookings:
            diff[booking[0] - 1] += booking[2]
            if booking[1] < n:
                diff[booking[1]] -= booking[2]
        # 做部分和累加得到最终结果
        for idx in range(1, n):
            diff[idx] += diff[idx-1]
        return diff


bookings, n = [[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5
print(Solution().corpFlightBookings(bookings, n))
