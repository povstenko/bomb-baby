def solution(x, y):
    M = int(x)
    F = int(y)
    generations = 0

    while M != F:
        if M > F:
            subs = (M-F)//F + ((M-F) % F > 0)
            generations += subs
            M = M - subs * F
        else:
            subs = (F-M)//M + ((F-M) % M > 0)
            generations += subs
            F = F - subs * M

    return str(generations) if(M, F) == (1, 1) else 'impossible'



print(solution('4', '7'))
print(solution('2', '1'))
