def resolve(literal, truthvalues):
    variable = abs(literal)
    polarity = variable == literal
    # Only write to resolved and unprocessed when necessary.
    if variable not in truthvalues:
        truthvalues[variable] = polarity
        unprocessed.add(_literal)
    # We encountered a contradiction.
    elif resolved[_variable] != _polarity:
        return False
    return True
