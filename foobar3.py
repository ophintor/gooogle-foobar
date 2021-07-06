def solution(x, y):
    h_pos = 1
    h_count = 2

    for i in range(1,x):
        h_pos += h_count
        h_count += 1

    v_pos = 0
    v_count = x

    for j in range(1,y):
        v_pos += v_count
        v_count += 1

    return str(h_pos + v_pos)
