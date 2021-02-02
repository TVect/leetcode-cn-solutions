"""
给定一个包含 [0，n ) 中独特的整数的黑名单 B，写一个函数从 [ 0，n ) 中返回一个不在 B 中的随机整数。
对它进行优化使其尽量少调用系统方法 Math.random() 。

提示:
    1 <= N <= 1000000000
    0 <= B.length < min(100000, N)
    [0, N) 不包含 N，详细参见 interval notation 。

示例 1:
    输入:
        ["Solution","pick","pick","pick"]
        [[1,[]],[],[],[]]
    输出: [null,0,0,0]

示例 2:
    输入:
        ["Solution","pick","pick","pick"]
        [[2,[]],[],[],[]]
    输出: [null,1,1,1]

示例 3:
    输入:
        ["Solution","pick","pick","pick"]
        [[3,[1]],[],[],[]]
    输出: [null,0,0,2]

示例 4:
    输入:
        ["Solution","pick","pick","pick"]
        [[4,[2]],[],[],[]]
    输出: [null,1,3,1]

输入语法说明：
    输入是两个列表：调用成员函数名和调用的参数。Solution的构造函数有两个参数，N 和黑名单 B。
    pick 没有参数，输入参数是一个列表，即使参数为空，也会输入一个 [] 空列表。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/random-pick-with-blacklist
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import random
from typing import List


class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        self.possible_size = N - len(blacklist)
        self.mapping = {element: None for element in blacklist}
        idx = N - 1
        # 将 0 - self.possible 中在 blacklist 中的数映射到 self.possible - N 中可行的取值
        for element in blacklist:
            if element < self.possible_size:
                # 这里使用 dict, 加速查找是否在 blacklist 中
                while idx in self.mapping:
                   idx -= 1
                self.mapping[element] = idx
                idx -= 1

    def pick(self) -> int:
        num = random.randint(0, self.possible_size-1)
        return self.mapping.get(num, num)


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
