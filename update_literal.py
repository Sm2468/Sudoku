def updatelit(literal, negative_literals, positive_literals, all_literals):

    all_literals.remove(literal)
    if -literal in all_literals:
        all_literals.remove(-literal)

    if literal in negative_literals:
        negative_literals.remove(literal)
    if -literal in negative_literals:
        negative_literals.remove(-literal)
    if literal in positive_literals:
        positive_literals.remove(literal)
    if -literal in positive_literals:
        positive_literals.remove(-literal)
