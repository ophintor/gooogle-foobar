def get_distance(src_coords, dest_coords):
    return abs(dest_coords[0] - src_coords[0]) + abs(dest_coords[1] - src_coords[1])

def get_closer(src_coords, dest_coords):
    # print(src_coords, dest_coords)

    if abs(src_coords[0] - dest_coords[0]) >= abs(src_coords[1] - dest_coords[1]):
        if (src_coords[0] - dest_coords[0] >=2) and (src_coords[1] >= dest_coords[1]):
            src_coords[0] -= 2
            src_coords[1] -= 1
        elif (src_coords[0] - dest_coords[0] >=2) and (src_coords[1] <= dest_coords[1]):
            src_coords[0] -= 2
            src_coords[1] += 1
        elif (dest_coords[0] - src_coords[0] >=2) and (src_coords[1] >= dest_coords[1]):
            src_coords[0] += 2
            src_coords[1] -= 1
        elif (dest_coords[0] - src_coords[0] >=2) and (src_coords[1] <= dest_coords[1]):
            src_coords[0] += 2
            src_coords[1] += 1
    else:
        if (src_coords[1] - dest_coords[1] >=2) and (src_coords[0] >= dest_coords[0]):
            src_coords[0] -= 1
            src_coords[1] -= 2
        elif (src_coords[1] - dest_coords[1] >=2) and (src_coords[0] <= dest_coords[0]):
            src_coords[0] += 1
            src_coords[1] -= 2
        elif (dest_coords[1] - src_coords[1] >=2) and (src_coords[0] >= dest_coords[0]):
            src_coords[0] -= 1
            src_coords[1] += 2
        elif (dest_coords[1] - src_coords[1] >=2) and (src_coords[0] <= dest_coords[0]):
            src_coords[0] += 1
            src_coords[1] += 2

    # print(src_coords)
    return src_coords

# screw recursivity today :)
def solution(src, dest):
    close_enough = False
    src_coords = [src%8, int(src/8)]
    dest_coords = [dest%8, int(dest/8)]
    steps = 0

    while not close_enough:
        distance = get_distance(src_coords, dest_coords)

        if src_coords in ([0,0], [0,7], [7,0], [7,7]) and distance == 2 and (src_coords[0] - dest_coords[0] != 0 and src_coords[1] - dest_coords[1] != 0):
            close_enough = True
            return (steps + 4)
        elif distance == 1:
            close_enough = True
            return (steps + 3)
        elif distance == 2:
            close_enough = True
            return (steps + 2)
        elif distance == 3 and (src_coords[0] - dest_coords[0] != 0 and src_coords[1] - dest_coords[1] != 0):
            close_enough = True
            return (steps + 1)
        elif distance == 3 and (src_coords[0] - dest_coords[0] == 0 or src_coords[1] - dest_coords[1] == 0):
            close_enough = True
            return (steps + 3)
        elif distance == 4 and (abs(src_coords[0] - dest_coords[0]) == 1 or abs(src_coords[1] - dest_coords[1]) == 1):
            close_enough = True
            return (steps + 2)
        else:
            src_coords = get_closer(src_coords, dest_coords)
            steps += 1


# print(0,6,":",solution(0,6))

# for i in range(0,63):
#     for j in range(0,63):
#         if i<j:
#             print(i,j,solution(i,j))

# for j in range(1,64):
#     if (j%8) == 0: print ("---")
#     print(0,j,solution(0,j))

# print("--")

i=0
print(i)
print("-" * 20, end = ' ')
for j in range(0,64):
    if (j%8) == 0: print ("\n")
    if j != i:
        print(solution(i,j), end = ' ')
    else:
        print ("*", end = ' ')
print("\n\n")
