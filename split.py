import random


def split(literals, decisions):
    # hierin wil ik eerst random splitten en dan heuristiek toevoegen, maar daar ga ik morgen aan werken
    # (dit klopt nog niet)

    choice = random.choice(literals)
    decisions.append(choice)
    print("lit")
    print(literals)
