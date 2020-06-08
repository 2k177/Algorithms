from collections import deque
class Stack():
    def __init__(self):
        self.container = deque()

    def push(self,data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def isEmpty(self):
        return len(self.container)==0

    def sizeOfStack(self):
        return len(self.container)

def isMached(ch1,ch2):
    matchDict = {
        '}' : '{',
        ')' : '(',
        ']' : '['
    }
    return matchDict[ch1]==ch2

def isBalanced(s):
    stack = Stack()
    for ch in s:
        if ch=='(' or ch=='{' or ch=='[':
            stack.push(ch)
        if ch==')' or ch=='}' or ch==']':
            if stack.isEmpty():
                return False
            if not isMached(ch,stack.pop()):
                return False

    return stack.sizeOfStack()==0

if __name__ == '__main__':
    print(isBalanced("({a+b})"))
    print(isBalanced("aaa[aa[aa]]"))
    print(isBalanced("aaa[a{(})a]"))