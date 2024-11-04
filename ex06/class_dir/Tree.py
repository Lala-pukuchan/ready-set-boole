from .Branch import Branch


class Tree:
    def __init__(self, formular: str):
        self.tree = []
        for s in formular:
            if s.isalpha():
                self.tree.append(Branch(s, None, None))
            elif s == "!":
                root = self.tree.pop()
                self.tree.append(Branch(s, root, None))
            elif s in "&=>^|":
                right = self.tree.pop()
                left = self.tree.pop()
                self.tree.append(Branch(s, left, right))

    def __repr__(self):
        return f"Tree(tree={self.tree})"

    def __str__(self):
        return str(self.tree[0])

    def nnf(self):
        root = self.tree[0]
        root.nnf()
        return self
    
    def cnf(self):
        root = self.tree[0]
        root.nnf()
        root.cnf()
        return self
