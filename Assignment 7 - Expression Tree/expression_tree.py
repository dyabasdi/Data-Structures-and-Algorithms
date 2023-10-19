import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack ():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node ():
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

class Tree():
    def __init__ (self):
        self.root = None
    def create_tree (self, expr):
        stack = Stack()
        expr_list = expr.split()
        self.root = Node()
        current = self.root
        for i in range(len(expr_list)):
            if expr_list[i] == '(':
                current.lChild = Node()
                stack.push(current)
                current = current.lChild
            elif expr_list[i] in operators:
                current.data = expr_list[i]
                stack.push(current)
                current.rChild = Node()
                current = current.rChild
            elif expr_list[i] == ')':
                if stack.is_empty():
                    break
                else:
                    current = stack.pop()
            elif expr_list[i] not in operators:
                current.data = expr_list[i]
                current = stack.pop()
        
    def evaluate (self, aNode):
        if aNode.data in operators:
            if aNode.data == '+':
                return self.evaluate(aNode.lChild) + self.evaluate(aNode.rChild)
            elif aNode.data == '-':
                return self.evaluate(aNode.lChild) - self.evaluate(aNode.rChild)
            elif aNode.data == '*':
                return self.evaluate(aNode.lChild) * self.evaluate(aNode.rChild)
            elif aNode.data == '/':
                return self.evaluate(aNode.lChild) / self.evaluate(aNode.rChild)
            elif aNode.data == '//':
                return self.evaluate(aNode.lChild) // self.evaluate(aNode.rChild)
            elif aNode.data == '%':
                return self.evaluate(aNode.lChild) % self.evaluate(aNode.rChild)
            elif aNode.data == '**':
                return self.evaluate(aNode.lChild) ** self.evaluate(aNode.rChild)
        else:
            return float(aNode.data)
    def pre_order (self, aNode):
        if aNode.data in operators:
            return aNode.data + ' ' + self.pre_order(aNode.lChild) + ' ' + self.pre_order(aNode.rChild)
        else:
            return aNode.data
    def post_order (self, aNode):
        if aNode.data in operators:
            return self.post_order(aNode.lChild) + ' ' + self.post_order(aNode.rChild) + ' ' + aNode.data
        else:
            return aNode.data

def main():
    line = sys.stdin.readline()
    expr = line.strip()
    tree = Tree()
    tree.create_tree(expr)

    print(expr, "=", str(tree.evaluate(tree.root)))

    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
