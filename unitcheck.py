def unit_check(unit_clause, positive_literals, negative_literals, all_literals, truthvalues):
    print("unit")
    truthvalues[unit_clause] = 1
    truthvalues[-unit_clause] = 0
    all_literals.remove(unit_clause)

    if unit_clause in negative_literals:
        negative_literals.remove(unit_clause)
    if -unit_clause in negative_literals:
        negative_literals.remove(-unit_clause)
    if unit_clause in positive_literals:
        positive_literals.remove(unit_clause)
    if -unit_clause in positive_literals:
        positive_literals.remove(-unit_clause)
