class BiQueue(object):
    "双端队列"
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        self.__list. insert(0, item)

    def add_rear(self, item):
        "入队，从队尾插入 item"
        self.__list.append(item)

    def pop_front(self):
        "出队，从队头弹出一个元素"
        if self.is_empty():
            return None
        return self.__list.pop(0)

    def pop_rear(self):
        "出队，从队头弹出一个元素"
        if self.is_empty():
            return None
        return self.__list.pop()

    def is_empty(self):
        "判断栈是否为空"
        return self.__list == []

    def size(self):
        "返回栈中元素的个数"
        return len(self.__list)


if __name__ == "__main__":
    bq = BiQueue()
    bq.add_front(1)
    bq.add_front(2)
    bq.add_front(3)
    bq.add_front(4)
    bq.add_rear(5)
    bq.add_rear(6)
    bq.add_rear(7)
    bq.add_rear(8)
    print(bq.pop_front())
    print(bq.pop_front())
    print(bq.pop_front())
    print(bq.pop_front())
    print(bq.pop_rear())
    print(bq.pop_rear())
    print(bq.pop_rear())
    print(bq.pop_rear())
    print(bq.pop_rear())
