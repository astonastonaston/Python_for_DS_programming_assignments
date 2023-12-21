def __count_paths(m, n, blocks, curr_pos):
    'Solve the frobenius equation given coefficients and the intercept'
    (rw, col) = curr_pos
    if ((rw==m-1)&(col==n-1)):
        return 1
    if ((curr_pos in blocks) or (rw > m-1) or (col > n-1)):
        return 0
    curr_pos_dn = (rw+1, col)
    curr_pos_ri = (rw, col+1)
    return __count_paths(m, n, blocks, curr_pos_dn) + __count_paths(m, n, blocks, curr_pos_ri)


def count_paths(m, n, blocks):
    'Solve the frobenius equation given coefficients and the intercept'
    return __count_paths(m, n, blocks, (0,0))

# def main():
#     print(count_paths(3,4,[(0,3),(1,1)]))
#     return 0

# main()