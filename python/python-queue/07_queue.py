class Queue(object):
    "队列"
    def __init__(self):
        self.__list = []

    def enqueue(self, item):
        "入队，从队尾插入 item"
        self.__list.append(item)

    def dequeue(self):
        "出队，从队头弹出一个元素"
        if self.is_empty():
            return None
        return self.__list.pop(0)

    def is_empty(self):
        "判断栈是否为空"
        return self.__list == []

    def size(self):
        "返回栈中元素的个数"
        return len(self.__list)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
