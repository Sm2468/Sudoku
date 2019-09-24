# update list of clauses
def update_clauses(clauses, truthvalues):
    changed = False
    for clause in [*clauses]:
        clause_not_removed = True
        for literal in [*truthvalues]:

            if (literal in clause) & clause_not_removed:
                # verwijder de clause waarin een waarde staat die al waar is.
                if truthvalues[literal]:
                    changed = True
                    clauses.remove(clause)
                    clause_not_removed = False
                if -literal in clause:
                    changed = True
                    clause.remove(-literal)

                # verwijder een literal uit een clause waarvan je weet dat die niet waar is.
                if not truthvalues[literal]:
                    changed = True
                    clause.remove(literal)

                if -literal in clause:
                    changed = True
                    clauses.remove(clause)
                    clause_not_removed = False
    return changed


def update_literals(literal, negative_literals, positive_literals, all_literals):

    if literal in all_literals:
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

