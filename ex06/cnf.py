from class_dir.Tree import Tree


if __name__ == "__main__":
    """
    CNF: Conjunctive Normal Form

    to achieve the required structure of AND of OR clauses
    A ∧ (B ∨ (C ∧ D))

    we need to apply the distributive laws
    A ∨ (B ∧ C) ⇔ (A ∨ B) ∧ (A ∨ C)

    it should be
    (ONE/GROUP) ^ (ONE/GROUP) ^ (ONE/GROUP) ^ ...
    or
    (ONE/GROUP) ∨ (ONE/GROUP) ∨ (ONE/GROUP) ∨ ...
    """
    t1 = Tree("AB&!")
    #    !
    #  &
    # A   B
    print('1:', t1.cnf(), 'Expected output: A!B!|')
    # De Morgan’s laws
    # !(A AND B)
    # !A OR !B
    # Expected output: A!B!|
    # --------------------------------
    t2 = Tree("AB|!")
    #    !
    #  |
    # A   B
    print('2:', t2.cnf(), 'Expected output: A!B!&')
    # De Morgan’s laws
    # !(A OR B)
    # !A AND !B
    # Expected output: A!B!&
    # --------------------------------
    t3 = Tree("AB|C&")
    #    &
    #  |   C
    # A   B
    print('3:', t3.cnf(), 'Expected output: AB|C&')
    # (A OR B) AND C
    # Expected output: AB|C&
    # --------------------------------
    t4 = Tree("AB|C|D|")
    #       |
    #     |   D
    #   |   C
    # A   B
    print('4:', t4.cnf(), 'Expected output: ABCD|||')
    # ((A OR B) OR C) OR D
    # Expected output: ABCD|||
    # --------------------------------
    t5 = Tree("AB&C&D&")
    #        &
    #      &   D
    #    &   C
    # A   B
    print('5:', t5.cnf())
    # --------------------------------
    t6 = Tree("AB&!C!|")
    print('6:', t6.cnf())
    # --------------------------------
    t7 = Tree("AB|!C!&")
    print('7:', t7.cnf())
    # --------------------------------
    t8 = Tree("AB&C|")
    # C ∨ (A ∧ B)
    # (C ∨ A) ∧ (C ∨ B)
    # Expected output: AC|BC|&
    print('8:', t8.cnf(), 'Expected output: AC|BC|&')
    # --------------------------------
    t9 = Tree("ABCD&|&")
    # (A ∧ B ∧ C) ∨ D
    # (A ∨ D) ∧ (B ∨ D) ∧ (C ∨ D)
    # Expected output: ABC|BD|&&
    print('9:', t9.cnf(), 'Expected output: ABC|BD|&&')