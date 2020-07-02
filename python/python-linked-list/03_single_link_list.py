class Node(object):
    """节点"""
    def __init__(self, ele):
        self.ele = ele
        self.next = None


class SingleLinkList(object):
    """单链表"""
    def __init__(self, node=None):
        self.__head = None

    def is_empty(self):
        """链表是否为空"""
        return self.__head == None

    def length(self):
        """链表的长度"""
        cur = self.__head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历"""
        cur = self.__head
        while cur != None:
            print(cur.ele, end=" ")
            cur = cur.next
        print('')

    def add(self, item):
        """头部添加"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """尾部添加"""
        node = Node(item)
        if (self.is_empty()):
            self.__head = node
            return
        cur = self.__head
        while(cur.next != None):
            cur = cur.next
        cur.next = node

    def insert(self, pos, item):
        """插入"""
        if pos <= 0:
            self.add(item)
        elif pos > (self.length() - 1):
            self.append(item)
        else:
            index = 0
            pre = self.__head
            node = Node(item)
            while index < (pos - 1):
                pre = pre.next
                index += 1
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除元素"""
        cur = self.__head
        pre = None
        while cur is not None:
            if(cur.ele == item):
                # 头结点就是要删除的元素
                if (self.__head == cur):
                    self.__head = cur.next
                    return True
                else:
                    pre.next = cur.next
                    return True
            else:
                pre = cur
                cur = cur.next
        # 缺少最后一项
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
    ll = SingleLinkList()
    ll.append(0)
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)
    ll.insert(1, '11111')
    ll.insert(-1, '------')
    ll.insert(13, '00000')
    ll.travel()

    print(ll.search(9))
    ll.remove('11111')
    ll.travel()
    ll.remove('------')
    ll.travel()
    ll.remove('00000')
    ll.travel()
