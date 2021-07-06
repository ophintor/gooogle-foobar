from fractions import Fraction, gcd
import numpy as np

def is_terminal(state):
    return all(x == 0 for x in state)

def get_terminal_states(m):
    terminal_states = []
    current_state = 0
    for state in m:
        if is_terminal(state):
            terminal_states.append(current_state)
        current_state += 1

    return terminal_states

def get_I():
    I = []
    for i in range(0,10):
        I.append([])
        for j in range(0,10):
            I[i].append(1) if i == j else I[i].append(0)

    return I


def get_R_Q(m, terminal_states):
    R = []
    Q = []
    m_index = 0
    rq_index = 0

    for state in m:
        if not is_terminal(state):
            R.append([])
            Q.append([])
            for s in range(0, len(state)):
                if s in terminal_states:
                    R[rq_index].append(m[m_index][s])
                else:
                    Q[rq_index].append(m[m_index][s])
            rq_index += 1
        m_index += 1

    return R, Q

def update_R_Q(R, Q):
    new_Q = []
    new_R = []

    for q_line in range(0, len(Q)):
        new_Q.append([])
        for q_unit in range(0, len(Q)):
            if Q[q_line][q_unit] != 0:
                new_Q[q_line].append(float(Q[q_line][q_unit])/float(sum(Q[q_line]) + sum(R[q_line])))
            else:
                new_Q[q_line].append(0)

    for r_line in range(0, len(R)):
        new_R.append([])
        for r_unit in range(0, len(R[0])):
            if R[r_line][r_unit] != 0:
                new_R[r_line].append(float(R[r_line][r_unit])/float(sum(Q[r_line]) + sum(R[r_line])))
            else:
                new_R[r_line].append(0)

    return new_R, new_Q

def get_F(I, Q):
    F=[]
    size = min(len(I), len(Q))

    for i in range(0, size):
        F.append([])
        for j in range(0, size):
            F[i].append((I[i][j]) - (Q[i][j]))

    F = np.linalg.inv(F)

    return F

def get_solution(FR_0):
    solution = []
    denominators = [Fraction(x).limit_denominator().denominator for x in FR_0]

    common_denominator = denominators[0]
    for d in denominators[1:]:
        common_denominator = common_denominator // gcd(common_denominator, d) * d

    for i in FR_0:
        solution.append(Fraction(i).limit_denominator().numerator * common_denominator / Fraction(i).limit_denominator().denominator)
    solution.append(sum(solution))

    return solution

def solution(m):
    terminal_states = get_terminal_states(m)
    solution = []
    if 0 not in terminal_states:
        I = get_I()
        R, Q = get_R_Q(m, terminal_states)
        R, Q = update_R_Q(R, Q)
        F = get_F(I, Q)
        FR = np.matmul(F, R)
        solution = get_solution(FR[0])
    else:
        for i in range(0, len(terminal_states)+1):
            if i == 0 or i == len(terminal_states):
                solution.append(1)
            else:
                solution.append(0)

    return solution
