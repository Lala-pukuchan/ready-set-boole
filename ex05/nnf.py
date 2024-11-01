from class_dir.Tree import Tree


if __name__ == "__main__":
    t1 = Tree("AB&!")
    #    !
    #  &
    #A   B
    print(t1.nnf())
    # De Morgan’s laws
    # !(A AND B)
    # !A OR !B
    # Expected output: A!B!|
    t2 = Tree("AB|!")
    #    !
    #  |
    #A   B
    print(t2.nnf())
    # De Morgan’s laws
    # !(A OR B)
    # !A AND !B
    # Expected output: A!B!&
    t3 = Tree("AB>")
    #    >
    #A   B
    print(t3.nnf())
    # Material conditions
    # A => B
    # !A OR B
    # Expected output: A!B|
    t4 = Tree("AB=")
    #    =
    #A   B
    print(t4.nnf())
    # A <=> B
    # A AND B is true/false
    # (A AND B) OR (!A AND !B)
    # Expected output: AB&A!B!&|
    t5 = Tree("AB|C&!")
    #    !
    #  &
    #    C
    #  |
    #A   B
    print(t5.nnf())
    # !((A OR B) AND C)
    # !(A OR B) OR !C
    # (!A AND !B) OR !C
    # Expected output: A!B!&C!|
