class Branch:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Branch(value={self.value}, left={self.left}, right={self.right})"

    def __str__(self):
        left_str = str(self.left) if self.left else ""
        right_str = str(self.right) if self.right else ""
        return f"{left_str}{right_str}{self.value}"

    def nnf(self):
        if self.value == ">":
            # Material conditions (A ⇒ B) ⇔ (¬A ∨ B)
            new_left = Branch("!", self.left)
            self.left = new_left
            self.value = "|"
        elif self.value == "^":
            # Conjunction conditions A XOR B≡(A∧¬B)∨(¬A∧B)
            new_left = Branch("&", self.left, Branch("!", self.right))
            new_right = Branch("&", Branch("!", self.left), self.right)
            self.value = "|"
            self.left = new_left
            self.right = new_right
        elif self.value == "=":
            # Equivalence conditions (A ⇔ B) ⇔ ((A ⇒ B) ∧ (B ⇒ A))
            new_left = Branch("&", self.left, self.right)
            new_right = Branch("&", Branch("!", self.left), Branch("!", self.right))
            self.value = "|"
            self.left = new_left
            self.right = new_right
        elif self.value == "!" and not self.left.value.isalpha():
            # recursively call nnf() on the left child
            self.left.nnf()
            # De Morgan’s laws ¬(A ∨ B) ⇔ (¬A ∧ ¬B)/ ¬(A ∧ B) ⇔ (¬A ∨ ¬B)
            new_left = Branch("!", self.left.left)
            new_right = Branch("!", self.left.right)
            self.value = "&" if self.left.value == "|" else "|"
            self.left = new_left
            self.right = new_right

        # Elimination of double negation (¬¬A) ⇔ A
        if self.left:
            while self.left.value == "!" and self.left.left.value == "!":
                self.left = self.left.left.left
            self.left.nnf()
        if self.right:
            while self.right.value == "!" and self.right.left.value == "!":
                self.right = self.right.left.left
            self.right.nnf()

    def cnf(self):
        if self.value == "|":
            # Distributive laws A ∨ (B ∧ C) ⇔ (A ∨ B) ∧ (A ∨ C)
            if self.right.value == "&":
                new_left = Branch("|", self.left, self.right.left)
                new_right = Branch("|", self.left, self.right.right)
                self.value = "&"
                self.left = new_left
                self.right = new_right
            elif self.left.value == "&":
                new_left = Branch("|", self.left.left, self.right)
                new_right = Branch("|", self.left.right, self.right)
                self.value = "&"
                self.left = new_left
                self.right = new_right
        if self.left:
            self.left.cnf()
        if self.right:
            self.right.cnf()