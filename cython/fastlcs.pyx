import numpy as np
cimport numpy as np

cimport cython

@cython.boundscheck(False)
@cython.wraparound(True)
def lcs(s1, s2):
    cdef int x,y, longest, x_longest, s1_len, s2_len
    cdef int m[200][200]
    cdef char* s1_ = s1
    cdef char* s2_ = s2

    s1_len = len(s1_)
    s2_len = len(s2_)

    for x in range(1, 1 + s1_len):
        for y in range(1, 1 + s2_len):
            if s1_[x - 1] == s2_[y - 1]:
                m[x][y] = m[x - 1][y - 1] + 1
                if m[x][y] > longest:
                    longest = m[x][y]
                    x_longest = x
            else:
                m[x][y] = 0
    return s1[x_longest - longest: x_longest]