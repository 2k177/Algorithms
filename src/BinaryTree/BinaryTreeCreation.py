"""Binary tree creation"""

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value


if __name__ == "__main__":
    root = Node(1)
    '''
    1
    / \
    None None
    '''
    root.left = Node(2)
    root.right = Node(3)
    '''
       1
      /  \
     2    3
    / \  / \
   None None None None
    '''

    root.left.left = Node(4)
    '''
        1
       / \
      2   3
     / \ / \
    4 None None None
   / \
   None None
    '''