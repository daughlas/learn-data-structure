# coding:utf-8
class Node(object):
    def __init__(self, item):
        self.elem = item
        self.l_child = None
        self.r_child = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, item):
        # 往最后添加，向完全二叉树去努力
        node = Node(item)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            # 队列不为空就一直可以进行
            cur_node = queue.pop(0)
            if cur_node.l_child is None:
                cur_node.l_child = node
                return
            else:
                queue.append(cur_node.l_child)

            if cur_node.r_child is None:
                cur_node.r_child = node
                return
            else:
                queue.append(cur_node.r_child)

    def breadth_travel(self):
        if self.root is None:
            return None
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=" ")
            if cur_node.l_child is not None:
                queue.append(cur_node.l_child)
            if cur_node.r_child is not None:
                queue.append(cur_node.r_child)
    
    def pre_order_travel(self, root):
        if root is None:
            return
        print(root.elem, end=" ")
        self.pre_order_travel(root.l_child)
        self.pre_order_travel(root.r_child)
    
    def mid_order_travel(self, root):
        if root is None:
            return
        self.mid_order_travel(root.l_child)
        print(root.elem, end=" ")
        self.mid_order_travel(root.r_child)
    
    def rear_order_travel(self, root):
        if root is None:
            return
        self.rear_order_travel(root.l_child)
        self.rear_order_travel(root.r_child)
        print(root.elem, end=" ")


if __name__ == "__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    tree.breadth_travel()
    print('\n--------')
    tree.pre_order_travel(tree.root)
    print('\n--------')
    tree.mid_order_travel(tree.root)
    print('\n--------')
    tree.rear_order_travel(tree.root)
    print('\n--------')

