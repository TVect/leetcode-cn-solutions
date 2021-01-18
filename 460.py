"""
请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。

实现 LFUCache 类：
    LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
    int get(int key) - 如果键存在于缓存中，则获取键的值，否则返回 -1。
    void put(int key, int value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。
                                    当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。
                                    在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最久未使用 的键。
    注意「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。

进阶：
    你是否可以在 O(1) 时间复杂度内执行两项操作？
 
示例：

输入：
    ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
    [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
输出：
    [null, null, null, 1, null, -1, 3, null, -1, 3, 4]

解释：
    LFUCache lFUCache = new LFUCache(2);
    lFUCache.put(1, 1);
    lFUCache.put(2, 2);
    lFUCache.get(1);      // 返回 1
    lFUCache.put(3, 3);   // 去除键 2
    lFUCache.get(2);      // 返回 -1（未找到）
    lFUCache.get(3);      // 返回 3
    lFUCache.put(4, 4);   // 去除键 1
    lFUCache.get(1);      // 返回 -1（未找到）
    lFUCache.get(3);      // 返回 3
    lFUCache.get(4);      // 返回 4
 

提示：
    0 <= capacity, key, value <= 10^4
    最多调用 10^5 次 get 和 put 方法

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lfu-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Node:
    def __init__(self, key=None, value=None, freq=1):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.freq = freq


class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key2node = {}
        self.freq2nodelist = {}
        self.min_freq = 0

    def add_node_to_linkedlist(self, node):
        if node.freq not in self.freq2nodelist:
            head, tail = Node(key="head", value="head"), Node(key="tail", value="tail")
            head.prev, head.next = tail, tail
            tail.prev, tail.next = head, head
            self.freq2nodelist[node.freq] = head
        head = self.freq2nodelist[node.freq]
        node.next = head.next
        node.next.prev = node
        head.next = node
        node.prev = head

    def remove_node_from_linkedlist(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def get(self, key: int) -> int:
        if key in self.key2node:
            node = self.key2node[key]

            # 将 node 节点从老的 freq 链表中删除
            self.remove_node_from_linkedlist(node)

            if node.freq == self.min_freq and self.freq2nodelist[node.freq].next == self.freq2nodelist[node.freq].prev:
                # 移除 node 之后，node.freq 对应的链表为空
                self.min_freq += 1

            node.freq += 1
            # 将 node 节点更新到新的 freq 链表中
            self.add_node_to_linkedlist(node)

            return self.key2node[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key2node:
            node = self.get(key)
            self.key2node[key].value = value
        else:
            node = Node(key, value)
            if len(self.key2node) >= self.capacity:
                node_to_remove = self.freq2nodelist[self.min_freq].prev.prev
                self.remove_node_from_linkedlist(node_to_remove)
                del self.key2node[node_to_remove.key]
            self.add_node_to_linkedlist(node)
            self.min_freq = 1
            self.key2node[key] = node


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


attrs = ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
args = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]

cache = LFUCache(args[0][0])
for attr, arg in zip(attrs[1:], args[1:]):
    func = getattr(cache, attr)
    print(attr, arg, func(*arg))
