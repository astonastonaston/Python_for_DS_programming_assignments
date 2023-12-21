import numpy as np
# EPSILON = 1e-3
def find_convex_cover(pvertices,clist):
    """
    Finds the optimum radius of circles such that all vertices are contained
    :param pvertices:
    :param clist:
    :return:
    """
    assert isinstance(clist, list)
    for cents in clist:
        assert type(cents)==tuple
        assert len(cents) == 2
        for coordinate in cents:
            assert type(coordinate) in (float, int)
    for cents in pvertices:
        assert len(cents) == 2
        for coordinate in cents:
            # print(coordinate, type(coordinate))
            assert type(coordinate) in (float, int, np.float64)
    pvertices = np.array(pvertices)
    clist = np.array(clist)
    # print(pvertices[:, None])
    vert_cent_dists = pvertices[:, None] - clist
    # print(r)
    # print(pvertices[:, None].shape)
    # print(clist.shape)
    # print(r.shape)
    vert_cent_dist_norm = np.apply_along_axis(np.linalg.norm, -1, vert_cent_dists)
    # print(D)
    argmins = np.argmin(vert_cent_dist_norm, axis=-1)
    # print(argmins)
    radii = {}
    for i in range(len(clist)):
        radii[i] = 0
    # radii = defaultdict(int)
    for i, argmin in enumerate(argmins):
        radii[argmin] = max(vert_cent_dist_norm[i, argmin], radii[argmin])
    return [radii[i] for i in range(len(clist))]


# pvertices = [[0.573, 0.797],
# [0.688, 0.402],
# [0.747, 0.238],
# [0.802, 0.426],
# [0.757, 0.796],
# [0.589, 0.811]]
# clist = [(0.7490863467660889, 0.4917635308023209),
# (0.6814339441396109, 0.6199470305156477),
# (0.7241617773773865, 0.6982813914515696),
# (0.6600700275207232, 0.7516911829987891),
# (0.6315848053622062, 0.7730550996176769),
# (0.7348437356868305, 0.41342916986639894),
# (0.7597683050755328, 0.31729154508140384)]

# if __name__ == '__main__':
#     import matplotlib.pyplot as plt

#     ##### Arguments
#     pvertices = np.array([[0.573, 0.797],
#                         [0.688, 0.402],
#                         [0.747, 0.238],
#                         [0.802, 0.426],
#                         [0.757, 0.796],
#                         [0.589, 0.811]])

#     clist = [(0.7490863467660889, 0.4917635308023209),
#                     (0.6814339441396109, 0.6199470305156477),
#                     (0.7241617773773865, 0.6982813914515696),
#                     (0.6600700275207232, 0.7516911829987891),
#                     (0.6315848053622062, 0.7730550996176769),
#                     (0.7348437356868305, 0.41342916986639894),
#                     (0.7597683050755328, 0.31729154508140384)]
#     ######## End Arguments


#     figure, axes = plt.subplots()
#     x, y = zip(*pvertices)
#     axes.scatter(x, y)
#     xc, yc = zip(*clist)
#     axes.scatter(xc, yc)

#     result = find_convex_cover(pvertices, clist)

#     print("Test Case Provided\n")
#     print("prediction | label | error | threshold")
#     print("-" * 15)
#     for predict, label in zip(result, [0, 0, 0.10297280518543134, 0, 0.06374182913818943, 0.0684588720095565, 0.07987784828713643]):
#         error = predict - label
#         row = [str(predict), str(label), str(error), str(error < EPSILON)]
#         print(" | ".join(row))

#     for c, radius in zip(clist, result):
#         cc = plt.Circle(c, radius, alpha=0.2)
#         axes.add_artist(cc)

#     plt.xlim(0.2, 1)
#     plt.ylim(0.2, 1)
#     plt.title("Minimum-area Circles Covering All Vertices")
#     plt.legend(["Vertices", "Circle Centers"])
#     plt.show()