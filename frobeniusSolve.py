import numpy as np
# def cartesian_product(colList):
#     return np.dstack(np.meshgrid(colList)).reshape(-1, 2)
def cartesian_product(arrays):
    ndim = len(arrays)
    # *: decompose into discrete inputs
    return (np.stack(np.meshgrid(*arrays), axis=-1)
              .reshape(-1, ndim))

def solvefrob(coefs,b):
    'Solve the frobenius equation given coefficients and the intercept'
    for i in range(len(coefs)):
        assert coefs[i]>0
    assert b>0
    dim = 1
    # list(range((b//i)+1))
    rngAll = []
    for i in coefs:
        rng = (b//i)+1
        dim *= rng
        rngAll.append(np.arange(rng))
    # print(rngAll)
    # coeffs = np.zeros((dim, len(coefs)))

    # rngAll = np.array(rngAll)
    # rngAllInd = np.arange(len(rngAll))
    # for i in range(len(coefs)):
    #     if (i != len(coefs)-1):
    #         col = np.tile(np.arange(rngAll[i]), np.prod(rngAll[rngAllInd != i]))
    #     else:
    #         col = np.repeat(np.arange(rngAll[i]), np.prod(rngAll[rngAllInd != i]))
    #     assert len(col) == dim
    #     # print(col.shape)
    #     # print(coeffs.shape)
    #     # print(coeffs[:, i].shape)
    #     coeffs[:, i] = col
    coeffs = cartesian_product(rngAll)

    # print(coeffs)
    res = coeffs @ np.array(coefs).T
    # print(res)
    # print(res==b)
    # print(sum(res==b))
    coeffs = coeffs[res == b, :]
    coeffs = coeffs[coeffs[:, 0].argsort()]
    coeffs = coeffs.tolist()
    tupCoeffs = [tuple(i) for i in coeffs]
    return tupCoeffs

# def main():
#     sol = solvefrob([1,2,3,5],10) 
#     # print(sol)
#     return 0

# main()