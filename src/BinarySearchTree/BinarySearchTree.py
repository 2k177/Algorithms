class BinaryuSearchTree:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def addChild(self,data):
        if data == self.data:
            return                                          #the node already exists
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinaryuSearchTree(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinaryuSearchTree(data)

    def inOrderTraversal(self):
        element = []
        if self.left:
            element += self.left.inOrderTraversal()
        element.append(self.data)
        if self.right:
            element+=self.right.inOrderTraversal()
        return element

def buildTree(elements):
    print "Building the Binary Search Tree: ", elements
    root = BinaryuSearchTree(elements[0])
    for item in range(1,len(elements)):
        root.addChild(elements[item])
    return root

if __name__=='__main__':
    languages = ["Hindi", "English", "Kannada", "Tamil",
                 "Telugu","English","Urdu","Bengali"]
    languageTree = buildTree(languages)
    numbers_tree = buildTree([17, 4, 1, 20, 9, 23, 18, 34])
    print "In order traversal gives the sorted list: ", numbers_tree.inOrderTraversal()
