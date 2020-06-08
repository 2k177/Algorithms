class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def addChild(self,child):
        child.parent = self                                 #this child belongs to the corresponding parent of class
        self.children.append(child)                         #adding the child to the list

    def getLevel(self):
        level = 0
        p =self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def printTree(self):
        spaces = ' ' *self.getLevel()*3
        print spaces+self.data
        for child in self.children:
            child.printTree()
def buildProductTree():
    root = TreeNode("Electronics")

    laptop = TreeNode("laptop")
    laptop.addChild(TreeNode("Mac"))
    laptop.addChild(TreeNode("Surface"))
    laptop.addChild(TreeNode("Thinkpad"))

    cellphone = TreeNode("Cell Phone")
    cellphone.addChild(TreeNode("iPhone"))
    cellphone.addChild(TreeNode("Google Pixel"))
    cellphone.addChild(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.addChild(TreeNode("Samsung"))
    tv.addChild(TreeNode("LG"))

    root.addChild(laptop)
    root.addChild(cellphone)
    root.addChild(tv)

    root.printTree()
if __name__=='__main__':
    buildProductTree()