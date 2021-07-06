def count_of_divisions_by_2(n):
    x = 0
    while n%2 == 0:
        n /= 2
        x += 1
    return x

def solution(n):
    ops = 0
    n = int(n)

    while n>1:
        if n%2 == 0:
            n /= 2
        elif n == 3:
            n = 2
        elif (count_of_divisions_by_2(n+1) > count_of_divisions_by_2(n-1)):
            n += 1
        else:
            n -= 1

        ops += 1


    # print(ops)
    return ops

# for i in range(1,100):
#     print(i, solution(i))
