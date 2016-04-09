class Tree(object):
    """Single class implementation of BST."""

    def __init__(self, data):
        """Initialize."""
        try:
            self.left = None
            self.right = None
            self.parent = None
            self.data = data
            self.__size = 1
        except TypeError:
            return("Please plant a root ex. 'Tree(10)'")

    def insert(self, data):
        """Insert data into tree."""
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                    print(self.left.data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                    print(self.right.data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
        self.__size += 1

    def contains(self, data):
        """Check tree for data."""
        try:
            if self.data:
                if data < self.data:
                    if self.left.data and data == self.left.data:
                        print("True")
                        return True
                    else:
                        self.left.contains(data)
                elif data > self.data:
                    if self.right.data and data == self.right.data:
                        print("True")
                        return True
                    else:
                        self.right.contains(data)
                elif data == self.data:
                    print("True")
                    return True
        except AttributeError:
            print("False")
            return False

    def size(self):
        """Return size of tree."""
        print(self.__size)
        return self.__size

    def depth(self):
        """Return depth of the tree."""
        if self is None:
            return 0
        else:
            depth_size = max(Tree.depth(self.left), Tree.depth(self.right)) + 1
            return depth_size

    def balance(self):
        """Balance the tree."""
        if self is None:
            return 0
        else:
            balance_left = Tree.depth(self.left)
            balance_right = Tree.depth(self.right)
            return balance_left - balance_right

    def in_order(self):
        """In order traversal."""
        if self:
            yield from self.in_order(self.left)
            yield self.data
            yield from self.in_order(self.right)
            return [node for node in bst.in_order()]

bst = Tree(10)
bst.insert(11)
bst.insert(1)
bst.insert(3)
bst.insert(4)
bst.insert(5)
bst.insert(2)
bst.insert(9)
print("***********************")
# bst.contains(1)
# bst.contains(5)
# bst.contains(200)
# bst.contains(45)

bst.size()
print(bst.in_order())
