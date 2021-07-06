def get_distance(src_coords, dest_coords):
    return abs(dest_coords[0] - src_coords[0]) + abs(dest_coords[1] - src_coords[1])

# screw recursivity today :) (please forgive me)
def solution(src, dest):
    src_coords  = [int(src/8), src%8]
    dest_coords = [int(dest/8), dest%8]

    distance = get_distance(src_coords, dest_coords)

    if distance == 0:
        return 0
    elif src in (0, 7, 56, 63) and distance == 2 and (src_coords[0] - dest_coords[0] != 0 and src_coords[1] - dest_coords[1] != 0):
        return 4
    elif distance == 1 or distance == 5:
        return 3
    elif distance == 2:
        return 2
    elif distance == 3:
        if (src_coords[0] - dest_coords[0] != 0 and src_coords[1] - dest_coords[1] != 0):
            return 1
        else:
            return 3
    elif distance == 4:
        if (abs(src_coords[0] - dest_coords[0]) - abs(src_coords[1] - dest_coords[1]) == 0):
            return 4
        else:
            return 2
    elif distance == 6:
        if (abs(src_coords[0] - dest_coords[0]) <= 1 or abs(src_coords[1] - dest_coords[1]) <= 1):
            return 4
        else:
            return 2
    elif distance == 7:
        if (abs(src_coords[0] - dest_coords[0]) == 0 or abs(src_coords[1] - dest_coords[1]) == 0):
            return 5
        else:
            return 3
    elif distance == 8 or distance == 10 or distance == 12:
        return 4
    elif distance == 9:
        if (abs(src_coords[0] - dest_coords[0]) <= 2 or abs(src_coords[1] - dest_coords[1]) <= 2):
            return 5
        else:
            return 3
    elif distance == 11 or distance == 13:
        return 5
    elif distance == 14:
        return 6





# print(0,6,":",solution(0,6))

# for i in range(0,63):
#     for j in range(0,63):
#         if i<j:
#             print(i,j,solution(i,j))

# for j in range(1,64):
#     if (j%8) == 0: print ("---")
#     print(0,j,solution(0,j))

# print("--")

i=63
print(i)
print("-" * 20, end = ' ')
for j in range(0,64):
    if (j%8) == 0: print ("\n")
    if j != i:
        print(solution(i,j), end = ' ')
    else:
        print ("*", end = ' ')
print("\n\n")
