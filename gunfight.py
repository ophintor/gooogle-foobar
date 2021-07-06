from math import ceil, hypot, atan2
from fractions import gcd
import time

def calculate_distance(a, b):
    return hypot(a[0]-b[0], a[1]-b[1])


def shorter_from(vec1, vec2):
    if calculate_distance(*vec1) > calculate_distance(*vec2):
        return vec2[1]
    else:
        return vec1[1]


def get_mirrored_points(dimensions, my_position, their_position, max_shot):
    mirrored_points = set()

    x_multiplier = max(1,int(ceil(max_shot/dimensions[0])))
    y_multiplier = max(1,int(ceil(max_shot/dimensions[1])))

    for x_block in xrange(-x_multiplier-2, x_multiplier+2):
        x_target = their_position[0] + (dimensions[0] * x_block)
        if x_block % 2 != 0: x_target = dimensions[0] - x_target

        for y_block in xrange(-y_multiplier-1, y_multiplier+1):
            y_target = their_position[1] + (dimensions[1] * y_block)
            if y_block % 2 != 0: y_target = dimensions[1] - y_target

            if (calculate_distance(my_position, (x_target,y_target)) <= max_shot):
                mirrored_points.add((x_target,y_target))

    return mirrored_points


def get_angles(targets, my_position):
    angles = {}

    for target in targets:
        angle = atan2(target[1]-my_position[1], target[0]-my_position[0])
        if angle not in angles:
            angles[angle]=target
        else:
            angles[angle]=shorter_from((my_position,target),(my_position,angles[angle]))

    return angles


def remove_blockers(angles, selfs, my_position):
    for self in selfs:
        angle = atan2(self[1]-my_position[1], self[0]-my_position[0])
        if angle in angles and my_position!=self and shorter_from((my_position,self),(my_position,angles[angle])) != angles[angle]:
            angles.pop(angle, None)

    return angles


def solution(dimensions, my_position, their_position, max_shot):
    targets = get_mirrored_points(dimensions, my_position, their_position, max_shot)
    selfs = get_mirrored_points(dimensions, my_position, my_position, max_shot)
    target_angles = remove_blockers(get_angles(targets, my_position), selfs, (my_position[0],my_position[1]))
    print("Solution: %d" % len(target_angles))
    return len(target_angles)




solution([3,2], [1,1], [2,1], 4)                # 7
solution([300,275], [150,150], [185,100], 500)  # 9
solution([2,5],[1,2],[1,4],11)                  # 27
solution([23,10], [6,4], [3,2], 23)             # 8
solution([42,59], [34,44], [6,34], 5000)        # 30904 ?

start_time = time.time()
solution([10,10], [4,4], [3,3], 5000)           # 739323
print("--- %s seconds ---" % (time.time() - start_time))
