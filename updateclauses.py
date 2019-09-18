# update list of clauses
def update(clauses, truthvalues):
    for clause in clauses:
        for truthvalue in truthvalues:
            if truthvalue in clause:

                # extra if loop omdat ik tussendoor clauses remove, doet anders raar...
                if clause in clauses:

                    # verwijder de clause waarin een waarde staat die al waar is.
                    if truthvalues[truthvalue]:
                        clauses.remove(clause)

                    # verwijder een literal uit een clause waarvan je weet dat die niet waar is.
                    if not truthvalues[truthvalue]:
                        clause.remove(truthvalue)
