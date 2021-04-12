def solution(x, y):
    M = int(x)
    F = int(y)
    generations = 0

    while M != 0 and F != 0:
        if M < F:
            generations += F/M
            F = F % M
        else:
            generations += M/F
            M = M % F

    return str(generations - 1) if(x, y) == (1, 1) else 'impossible'



print(solution('4', '7'))
print(solution('2', '1'))
