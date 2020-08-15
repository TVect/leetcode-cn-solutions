"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。它应该支持以下操作： 获取数据 get 和 写入数据 put 。

获取数据 get(key) - 如果关键字 (key) 存在于缓存中，则获取关键字的值（总是正数），否则返回 -1。
写入数据 put(key, value) - 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字/值」。
当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。


进阶:

你是否可以在 O(1) 时间复杂度内完成这两种操作？


示例:

LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得关键字 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得关键字 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lru-cache
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    # Hash + 双向链表
    def __init__(self, capacity: int):
        self.node_dict = {}
        # self.head ：dummy node
        # self.head.next 指向链表的第一个节点, self.head.prev 指向链表的最后一个节点
        self.head = Node()
        self.head.next = self.head
        self.head.prev = self.head

        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key in self.node_dict:
            node = self.node_dict[key]
            self.del_node_from_list(node)
            self.add_node_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.node_dict:
            node = self.node_dict[key]
            node.value = value
            # move a node to the head
            self.del_node_from_list(node)
            self.add_node_to_head(node)
        else:
            # add a node to the head
            node = Node(key, value)
            self.add_node_to_head(node)
            self.node_dict[key] = node
            self.size += 1
            if self.size > self.capacity:
                node_to_remove = self.head.prev
                self.del_node_from_list(node_to_remove)
                del self.node_dict[node_to_remove.key]
                self.size -= 1

    def del_node_from_list(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_node_to_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def show_nodes(self):
        rets = []
        node = self.head.next
        while node != self.head:
            rets.append([node.key, node.value])
            node = node.next
        return rets


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


attrs = ["LRUCache", "put", "put", "get", "get", "put", "get", "get", "get"]
args = [[2], [2, 1], [3, 2], [3], [2], [4, 3], [2], [3], [4]]

attrs = ["LRUCache","put","put","get","put","put","get"]
args = [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]

cache = LRUCache(args[0][0])
for attr, arg in zip(attrs[1:], args[1:]):
    func = getattr(cache, attr)
    print(attr, arg, func(*arg))
    # print(cache.show_nodes())
