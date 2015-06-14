#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

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
    """
    assert i > 0
    assert j > 0
    assert i < 999999
    assert j < 999999
    """
    max_cycles = 0
    cycles = 0
    start = i
    stop = j

    if i > j:
        start = j
        stop = i
    if start <= 0 or stop > 999999:
        return 0
    if start == 1 and stop == 1:
        return 1       
    if start == stop:
        return compute_cycles(start)

    for i in range(start,stop + 1):
        cycles = compute_cycles(i)
        if cycles > max_cycles:
            max_cycles = cycles

    assert max_cycles > 0
    return max_cycles

#Helper function for collatz_eval.Computes the cycle length of int num 
def compute_cycles(num):
    assert num > 0
    cycles = 1

    while num != 1:
        if num % 2 == 0:
            num  = num / 2
        else:
            num = 3 * num + 1
        cycles += 1

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
