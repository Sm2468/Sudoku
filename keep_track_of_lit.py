def get_not_yet_assigned_literals(clauses, positive_literals, negative_literals):
    for clause in clauses:
        for literal in clause:

            # put negative literal in set of negative literals
            if literal < 0:
                if literal not in negative_literals:
                    negative_literals.append(literal)

            # put positive literal in set of positive literals
            else:
                if literal not in positive_literals:
                    positive_literals.append(literal)
    all_literals = positive_literals + negative_literals
    print(all_literals)

    return[positive_literals, negative_literals, all_literals]
