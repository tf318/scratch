"""
Plank Philosophy
Tam Freestone-Bayes
"""

import sys

def plank_structures(n, m):
    """Return all combos of planks of size <=m to make a plank of size n"""

    plank_combinations = []

    # base cases:

    # A zero length plank is made up of an empty combination:
    plank_combinations.append([()])

    # A plank of length 1 can only be made up of a plank of length 1:
    plank_combinations.append([(1,)])

    # build up a cache of sub-sequences starting from 2
    for x in range(2, n+1):
        sub_sequences = set()
        for i in range(x):
            for combo in plank_combinations[i]:
                sub_sequences.add((x - i,) + combo)
        plank_combinations.append(list(sub_sequences))

    # lastly filter out all the plank combinations that involve component
    # planks that are larger than m. This is not very efficient, but it works:
    for combo in plank_combinations[n]:
        if max(combo) <= m:
            yield combo

def solution_length(n, m):
    """Return total number of plank_structures(n, m) solutions"""

    return len(list(plank_structures(n, m)))

def main():
    """Parse arguments and print number of plank_structures(n, m) solutions"""
    if len(sys.argv) != 3:
        print("Usage: python plank.py [n] [m]")
        sys.exit(1)

    print(solution_length(int(sys.argv[1]), int(sys.argv[2])))

if __name__ == "__main__":
    main()
