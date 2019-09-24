import operator


def heuristic1(clauses):
    # count how many times all literals occur and then pick the highest value for the split.

    print("heuristics1")

    diction = {}
    #small_diction = {}
    for clause in clauses:
        for literal in clause:
            #if len(clause) == 2:
            #    if literal not in small_diction:
            #        small_diction[literal] = 1
            #    else:
            #        small_diction[literal] += 1
            if literal not in diction:
                diction[literal] = 1
            else:
                diction[literal] += 1

    max_lit_dict = max(diction, key=diction.get)
    #max_lit_small_dict = max(small_diction, key=diction.get)

    return max_lit_dict
