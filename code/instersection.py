def is_intersection(v1, v2, intersection_depth,
                    check_neighs_depth):
    if intersection_depth == 0:
        return True

    if not is_parallel(v1, v2):
        parallel_1 = v1.getParallelNeigh()
        parallel_2 = v2.getParallelNeigh()
        if parallel_1 and parallel_2:
            return is_intersection(parallel_1, parallel_2,
                  intersection_depth - 1, check_neighs_depth)

    if check_neighs_depth > 0:
        parallel_1 = v1.getParallelNeigh()
        parallel_2 = v2.getParallelNeigh()
        if parallel_1 and parallel_2:
            return is_intersection(parallel_1, parallel_2,
                  intersection_depth, check_neighs_depth - 1)





