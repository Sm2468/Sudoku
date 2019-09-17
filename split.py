import random


def random_choice(literals):
    # hierin wil ik eerst random splitten en dan heuristiek toevoegen

    new_choice = random.choice(literals)

    print(new_choice)
    print(literals)

    return new_choice
