import os

class Color(object):
    RED = True
    BLACK = False
    
class Node:
    def __init__(self, val,leftChild = None, rightChil = None, parent = None,color = None, size = 0, root = None):
        self.value = val
        self.leftChild = None
        self.rightChild = None
        self.parent = None
        self.color = None
        self.size = 0
        self.root = None
        

    def insert(self, data):
        if self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True
        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print (str(self.value), end = ' ')
            if self.rightChild:
                self.rightChild.inorder()

    def treeSize(self,root,size = 0):
        self.size = 0

        
class RBTree:
    __slots__ = {'root'}
    
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True
        
    def _insert(self,z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.value < x.value:
                x = x.leftChild
            else:
                x = x.rightChild
        z.parent = y
        if y is None:
            self.root = z
        elif z.value <y.value:
            y.leftChild = z
        z.leftChild = None
        z.rightChild = None
        z.color = 1
        self._insertFixup(z)

    def _insertFixup(self,z):
        while z.parent.color is 1:
            if z.parent == z.parent.parent.leftChild:
                y = z.parent.parent.rightChild
                if y.color is 1:
                    z.parent.color = 0
                    y.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.rightChild:
                        z = z.parent
                        self._rotateLeft(z)
                    z.parent.color = 0
                    z.parent.parent = 1
                    self._rotateRight(z.parent.parent)
            else:
                y=z.parent.parent.leftChild
                if y.color is 1:
                    z.parent.color = 0
                    y.color = 0
                    z.parent.parent.color = 1
                    z = z.parent.parent
                else:
                    if z == z.parent.leftChild:
                        z = z.parent
                        self._rotateRight(z)
                    z.parent.color = 0
                    z.parent.parent = 1
                    self._rotateleft(z.parent.parent)
        self._root.color = 0

    def _rotateLeft(self,x):
        y = x.rightChild
        x.rightChild = y.leftChild
        if y.leftChild is not None:
            y.leftChild.parent = x
        y.parent = x.parent
        if x.parent is not None:
            self.root = y
        elif x == x.parent.leftChild == y:
            x.parent.leftChild = y
        else:
            x.parent.rightChild = y
        y.leftChild = x
        x.parent = y

    def _rotateRight(self,x):
        x = y.leftChild
        y.leftChild = x.rightChild
        if x.rightChild is not None:
            x.rightChild.parent = y
        x.parent = y.parent
        if y.parent is None:
            self.root = x
        elif y == y.parent.rightChild:
            y.parent.rightChild = x
        else:
            y.parent.leftChild = x
        x.rightChild  = y
        y.parent = x
        
    def find(self,data):
        x = self.root
        if x is not None or data != x.value:
            if data < x.value:
                x = x.leftChild
            else:
                x = x.rightChild
            return x
        a = self.predecessor(x)
        b = self.successor(x)
        if x is None or data == x.value:
            f = open("search01.txt","r")
            lines = f.readlines()
            p = f.tell(data)
            f.close()
            
            f = open("search01.txt","a")
            f.seek(p)
            f.write("NIL")
            f.close()
            
            f = open("search01.txt","r")
            lines = f.readlines()
            lines.sort()
            f.tell(data)
            f.seek(-2,1)
            smaller = f.read()
            f.seek(3,1)
            bigger = f.read()
            f.close()
            print(smaller)
            print(bigger)
            
            
        if a is None:
            print( "NIL",x,b)
        elif b is None:
            print(a,x,"NIL")
        elif a is None and b is None:
            print("NIL",x,"NIL")
        else:
            print(a,x,b)
    
            
    def successor(self,x):
        if x.rightChild is not None:
            return tree_minimum(x.rightChild)
        y = x.parent
        while y is not None and x == y.rightChild:
            x = y
            y = y.parent
        return y

    def predecessor(self,x):
        if x. leftChild is not None:
            return tree_maximum(x.leftChild)
        y = x.parent
        while y is not None and x == y.leftChild:
            x = y
            y = y.parent
        return y
        
    def inorder(self):
        print( "inorder" )
        self.root.inorder()

    def print(self, tree, level):
        if tree.rightChild is not None:
            self.print( tree.rightChild, level +1)
        for i in range(level):
            print("NIL ", end ='')
        print(tree.value)
        if tree.leftChild is not None:
            self.print( tree.leftChild, level + 1)

    def tree_minimum(x):
        while x.leftChild is not None:
            x = x.leftChild
        return x

    def tree_maximum(x):
        while x.rightChild is not None:
            x = x.rightChild
        return x

    def treeSize(self,root,size = 0):
        if root is None:
            return -1
        if root is not None:
            size += 1
            if root.leftChild is not None:
                size +=1
                self.treeSize(root.leftChild, size)
            if root.rightChild is not None:
                size +=1
                self.treeSize(root.rightChild,size)
            return size

    def transplant(self,u,v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.leftChild:
            u.parent.leftChild = v
        else:
            u.parent.rigghtChild = v
        v.parent = u.parent

    def rbt_delete(self,data):
        y = data
        y_original_color = y.color
        if data.leftChild is None:
            x = data.rightChild
            rbt.transplant(self,data,data.rightChild)
        elif data.rightChild is None:
            x = z.leftChild
            rbt.transplant(self,data,data.leftChild)
        else:
            y = rbt.tree_minimum(data.rightChild)
            y_original_color = y.color
            x = y.rightChild
            if y.parent == data:
                x.parent = y
            else:
                rbt.transplant(self,y,y.rightChild)
                y.rightChild = data.rightChld
                y.rightChild.parent = y
            rbt.transplant(self,data,y)
            y.leftChild = data.leftChild
            y.leftChild.parent = y
            y.color = data.color
        if y_original_color == 0:
            rbt.rbt_delete_fixup(self,x)

    def rbt_delete_fixup(self,x):
        while x is not self.root and x.color == 0:
            if x == x.parent.leftChild:
                w = x.parent.rightChild
                if w.color == 1:
                    w.color = 0
                    x.parent.color = 1
                    rbt._rotateLeft(self,x.parent)
                    w = x.parent.rightChild
                if w.leftChild.color == 0 and w.rightChild.color ==0:
                    w.color = 1
                    x = x.parent
                elif w.rightChild.color == 0:
                        w.leftChild.color = 0
                        w.color = 1
                        rbt._rotateRight(self,w)
                        w = x.parent.rightChild

                        w.color = x.parent.color
                        x.parent.color = 0
                        w.rightChild.color = 0
                        rbt._rotateLeft(self,x.parent)
                        x = self.root
            else:
                w = x.parent.leftChild
                if w.color == 1:
                    w.color = 0
                    x.parent.color = 1
                    rbt._rotateRight(self,x.parent)
                    w = x.parent.leftChild
                if w.rightChild.color == 0 and w.leftChild.color == 0:
                    w.color = 1
                    x = x.parent
                elif w.leftChild.color == 0:
                        w.rightChild.color = 0
                        w.color = 1
                        rbt._rotateLeft(self,w)
                        w = x.parent.leftChild

                        w.color = x.parent.color
                        x.parent.color = 0
                        w.leftChild.color = 0
                        rbt._rotateRight(self,x.parent)
                        x = self.root

 
def read_input():
    f = open("test01.txt", "r")
    lines = f.readlines()
    for line in lines:
        rbt.insert(line)
    f.close()

def oper_search():
    f = open("search01.txt","r")
    lines = f.readlines()
    for line in lines:
        data = line
        rbt.find(data)
    f.close()

if __name__ == "__main__":
    rbt = RBTree()
    read_input()
    rbt.print(rbt.root,0)
    oper_search()
    f = open("output.txt","w")
    x = "".join(repr(rbt.print(rbt.root,0)))
    f.write(x)
    print (x)
    f.close()


    
