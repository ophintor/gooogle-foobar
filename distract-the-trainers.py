from fractions import gcd

def is_infinite(a,b):
    z = (a + b) / gcd(a, b)
    return ((z - 1) & z) != 0


def all_pairs(banana_list):
    if len(banana_list) < 2:
        yield []
        return
    if len(banana_list) % 2 == 1:
        for i in range(len(banana_list)):
            for result in all_pairs(banana_list[:i] + banana_list[i+1:]):
                yield result
    else:
        a = banana_list[0]
        for i in range(1,len(banana_list)):
            pair = (a,banana_list[i])
            for rest in all_pairs(banana_list[1:i] + banana_list[i+1:]):
                yield [pair] + rest


def solution(banana_list):
    minimum = len(banana_list)
    for pairs in all_pairs(banana_list):
        if minimum == 0:
            break
        current = len(banana_list)
        for pair in pairs:
            if is_infinite(*pair):
                current -= 2
        if current < minimum:
            minimum = current

    print(minimum)
    return minimum




solution([1, 1])
solution([1, 7, 3, 21, 13, 19])
solution([1, 7, 1, 1])

# is_infinite(1,4)
# is_infinite(21,19)
