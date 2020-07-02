class Node(object):
    """节点"""
    def __init__(self, ele):
        self.ele = ele
        self.next = None
        self.prev = None


class DoubleLinkList(object):
    """双链表"""
    """中间继承了 SingleLinkList 中的 is_empty, length,"""
    def __init__(self, node=None):
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        return self.__head is None

    def length(self):
        """链表的长度"""
        cur = self.__head
        count = 0
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历"""
        cur = self.__head
        while cur is not None:
            print(cur.ele, end=" ")
            cur = cur.next
        print('')

    def add(self, item):
        """头部添加"""
        node = Node(item)
        node.next = self.__head
        self.__head = node
        if node.next:
            node.next.prev = node

    def append(self, item):
        """尾部添加"""
        node = Node(item)
        if (self.is_empty()):
            self.__head = node
            return
        cur = self.__head
        while cur.next is not None:
            cur = cur.next
        node.prev = cur
        cur.next = node

    def insert(self, pos, item):
        """插入"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            index = 0
            cur = self.__head
            while index < pos:
                cur = cur.next
                index += 1
            # 退出循环的时候 cur 指向 pos 的位置
            node = Node(item)
            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node

    def remove(self, item):
        """删除元素"""
        cur = self.__head
        while cur is not None:
            if(cur.ele == item):
                # 头结点就是要删除的元素
                if (self.__head == cur):
                    self.__head = cur.next
                    if cur.next:
                        # 判断链表是否只有一个节点
                        cur.next.prev = None
                else:
                    cur.prev.next = cur.next
                    if cur.next:
                        # 判断是否为链表的最后一个节点
                        cur.next.prev = cur.prev
                return True
            else:
                cur = cur.next
        # 跳出循环的时候就是最后一项，缺少最后一项
        return False

    def search(self, item):
        """查看元素是否存在"""
        cur = self.__head
        while cur != None:
            if (cur.ele == item):
                return True
                break
            else:
                cur = cur.next
        return False


if __name__ == "__main__":
    dll = DoubleLinkList()
    dll.append(0)
    print(dll.is_empty())
    print(dll.length())
    dll.append(1)
    print(dll.is_empty())
    print(dll.length())
    dll.append(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.append(6)
    dll.add(-1)
    dll.add(-2)
    dll.add(-3)
    print(dll.is_empty())
    print(dll.length())
    dll.travel()
    dll.insert(1, '11111')
    dll.insert(-1, '------')
    dll.insert(13, '00000')
    dll.travel()
    print(dll.search(6))
    dll.remove('11111')
    dll.travel()
    dll.remove('------')
    dll.travel()
    dll.remove('00000')
    dll.travel()
