from collections import deque


def make_watchlist(clauses, all_literals):
    watchlist = [deque() for i in range(2 * len(all_literals))]
    for clause in clauses:
        # Make the clause watch its first literal
        watchlist[clause[0]].append(clause)
    return watchlist


def update_watchlist(watchlist, literal, assignment):
    # Loop until there's nothing in list of clauses watching this literal
    alternative_found = False
    while watchlist[literal]:
        clause = watchlist[literal][0] #get first watched clause

        # Default to say no alternative was found
        alternative_found = False

        # Look for alternative literal for the clause to watch
        for alternative in clause:

            # Get the variable and negation piece of the literal in clause
            v = alternative >> 1
            a = alternative & 1

            if assignment[v] is None or assignment[v] == a ^ 1:
                alternative_found = True
                del watchlist[literal][0]
                watchlist[alternative].append(clause)
                break

        # No alternative has been found after looking through clause
        if not alternative_found:
            return False, watchlist
    # Alternative is found (or loop condition fails?)
    return True, watchlist

