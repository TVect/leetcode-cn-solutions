"""
编写一个算法来判断一个数 n 是不是快乐数。
「快乐数」定义为：
    对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，
    也可能是 无限循环 但始终变不到 1。如果 可以变为  1，那么这个数就是快乐数。
如果 n 是快乐数就返回 True ；不是，则返回 False 。

示例：
    输入：19
    输出：true
    解释：
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    # hashset
    def isHappy_1(self, n: int) -> bool:
        all_n = set()
        while n != 1 and n not in all_n:
            all_n.add(n)
            tmp = 0
            while n:
                n, mod = divmod(n, 10)
                tmp += (mod * mod)
            n = tmp
        return n == 1

    # 快慢指针法
    def isHappy(self, n: int) -> bool:

        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += (digit ** 2)
            return total_sum

        slow = n
        fast = get_next(n)
        while fast != 1 and slow != fast:
            slow = get_next(slow)
            fast = get_next(get_next(fast))
        return fast == 1


n = 19
print(Solution().isHappy(n))
