#!/usr/bin/env python3

# -------
# imports
# -------

import sys
lazy_cache = {} #dictionary used for storing cycle lengths
# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0
    assert i < 999999
    assert j > 0
    assert j < 999999

    max_cycles = 0
    cycles = 0
    m = 0
    start = i
    stop = j

    if i > j:
        start = j
        stop = i
    if start == 1 and stop == 1:
        return 1
    if start == stop:
        return compute_cycles(start)

    m = (stop // 2) + 1 #range optimization studied in class
    if start < m:
        start = m

    for i in range(start,stop + 1):
        if i in lazy_cache:
            cycles = lazy_cache[i]
        else:
            cycles = compute_cycles(i)

        if cycles > max_cycles:
            max_cycles = cycles

    assert max_cycles > 0
    return max_cycles

#Helper function for collatz_eval.Computes the cycle length of int num 
def compute_cycles(num):
    assert num > 0
    cycles = 1
    original_num = num
    cached_val = 0

    while num != 1:
        if num in lazy_cache:
            cached_val = (lazy_cache[num] + cycles) - 1
            lazy_cache[original_num] = cached_val
            assert cached_val > 0 
            return cached_val
        else:
            if num % 2 == 0:
                num  = num >> 1
                cycles += 1
            else:
                num =(3 * num + 1) >> 1
                cycles += 2
    lazy_cache[original_num] = cycles

    assert cycles > 0
    return cycles	

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)

# ----
# main
# ----

if __name__ == "__main__" :
    collatz_solve(sys.stdin, sys.stdout)

"""
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
# That creates the file Collatz.html
"""