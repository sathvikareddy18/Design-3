class LRUCache:

    class Node:
        def __init__(self,key,value):
            self.key=key
            self.value=value
            self.prev=None
            self.next=None

    def __init__(self, capacity: int):
        self.head=self.Node(-1,-1)
        self.tail=self.Node(-1,-1)
        self.capacity=capacity
        self.smap={}
        self.head.next=self.tail
        self.tail.prev=self.head
    
    def removenode(self,node):
        node.next.prev=node.prev
        node.prev.next=node.next
        node.prev=None
        node.next=None

    def addtohead(self,node):
        node.prev=self.head
        node.next=self.head.next
        self.head.next=node
        node.next.prev=node 

    def get(self, key: int) -> int:
        if key not in self.smap:
            return -1
        node=self.smap[key]
        self.removenode(node)
        self.addtohead(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        if key in self.smap:
            node=self.smap[key]
            node.value=value
            self.removenode(node)
            self.addtohead(node)
        else:
            if len(self.smap)==self.capacity:
                lastnode=self.tail.prev
                self.removenode(lastnode)
                del self.smap[lastnode.key]
            newnode=self.Node(key,value)
            self.addtohead(newnode)
            self.smap[newnode.key]=newnode
        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)