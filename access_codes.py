# def solution(l):
#     codes = []
#     l.sort()

#     if 2 <= len(l) <= 2000:
#         for i in range(0, len(l)):
#             for j in range(i+1, len(l)):
#                 if l[j]%l[i] == 0:
#                     for k in range(j+1, len(l)):
#                         if l[k]%l[j] == 0:
#                             print(l[i], l[j], l[k])
#                             codes.append((l[i], l[j], l[k]))

#     solution = len((codes))
#     print("counter: " + str(solution))
#     return solution


def solution(l):
    c = [0] * len(l)
    count = 0
    for i in range(0,len(l)):
        for j in range(0, i):
            if l[i] % l[j] == 0:
                print(c)
                c[i] = c[i] + 1
                count = count + c[j]
                print (count)


    print("--solution--")
    print (count)
    return count

# solution([1,1,1])
# solution([1,1,2,3,4,5,6])
# solution([3,2,1,4,5,6])
# solution([1])
solution([2, 2, 2, 2, 4, 4, 5, 6, 8, 8, 8])
