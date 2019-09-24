def resolve(_literal: int) -> bool:
    _variable: int = abs(_literal)
    _polarity: bool = _variable == _literal
    # Only write to resolved and unprocessed when necessary.
    if _variable not in resolved:
        resolved[_variable]: bool = _polarity
        unprocessed.add(_literal)
    # We encountered a contradiction.
    elif resolved[_variable] != _polarity:
        return False
    return True

def simplify(clauses: List[Set[int]], literals: Set[int]):
    # Remove all clauses that contain a resolved variable.
    for literal in literals:
        polar_literal: int = literal * -1
        # Remove the whole clause if it contains the resolved literal (therefore the clause resolves to True).
        clauses: List[Set[int]] = [*filter(lambda _clause: literal not in _clause, clauses)]
        # Remove the opposite literal from the clause, because the instance will resolve to False.
        clauses: List[Set[int]] = [*map(lambda _clause: remove_literal(_clause, polar_literal), clauses)]
    return clauses

sort: List[Tuple[int, int]] = [*sorted(unresolved_frq.items(), key=lambda x: x[1], reverse=True)]

# use of absolute value when checking if a literal is in a list.


def check_unit_clause(clause, truthvalues, negative_literals, positive_literals, all_literals):
    if len(clause) == 1:
        print("unit")
        print(clause)

        # unit_check(clause[0], positive_literals, negative_literals, all_literals, truthvalues)
        unit_clause = clause[0]
        truthvalues[unit_clause] = True
        truthvalues[-unit_clause] = False

        # truth value assigned, so literals can be removed from lists
        # (trying to find a better way to do this)

        update_literals(unit_clause, negative_literals, positive_literals, all_literals)

        update_clauses(clauses, truthvalues)
        stuck = False
