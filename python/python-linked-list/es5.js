function Node(element) {
  this.node = element
  this.next = null
}

function LinkedList() {
  this.header = new Node('head') // 头结点
  this.find = find               // 查找节点
  this.insert = insert           // 插入节点
  this.remove = remove           // 删除节点
  this.findPrev = findPrev       // 查找前一个节点
  this.display = display         // 显示链表
}

// 查找
function find(item) {
  var currNode = this.header
  while(currNode.element != item) {
    currNode = currNode.next
  }
  return currNode
}

// 插入节点
function insert(newElement, item) {
  var newNode = new Node(newElement)
  var currNode = this.find(item)
  newNode.next = currNode.next
  currNode.next = newNode
}