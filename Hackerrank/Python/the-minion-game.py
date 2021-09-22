def minion_game(string):
    vowel=["A","E","I","O","U"]
    K=0
    S=0
    for i,w in enumerate(string):
        if w in vowel:
            K+=len(string)-i
        else:
            S+=len(string)-i
    if K>S:
        print("Kevin",K)
    elif K<S:
        print("Stuart",S)
    else:
        print("Draw")    