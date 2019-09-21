# update list of clauses
def update(clauses, truthvalues):
    for clause in [*clauses]:
        clause_not_removed = True
        for literal in [*truthvalues]:

            if (literal in clause) & clause_not_removed:
                # verwijder de clause waarin een waarde staat die al waar is.
                if truthvalues[literal]:
                    clauses.remove(clause)
                    clause_not_removed = False
                if -literal in clause:
                    clause.remove(-literal)

                # verwijder een literal uit een clause waarvan je weet dat die niet waar is.
                if not truthvalues[literal]:
                    clause.remove(literal)
                if -literal in clause:
                    clauses.remove(clause)
                    clause_not_removed = False
