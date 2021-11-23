T = int(input())

for t in range(T):

    S = list(input())
    F = list(input())

    total = 0

    # for each letter in our string (S),
    # check it against the allowed letters (F)
    for letter in S:
        steps = 13 # maximum number of operations
        for i in range(len(F)):
            cur = abs(ord(F[i]) - ord(letter)) # check operations needed
            if cur > 13: # take the cyclic system to our advantage (clock or counter-clockwise)
                cur = 26 - cur
            if cur < steps: # record it if it's current minimum
                steps = cur

        total += steps # add it to our total and move on to next letter


    print("Case #" + str(t+1) + ":", total)