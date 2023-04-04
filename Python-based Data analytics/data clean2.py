
import math as m
import numpy as np

# File: mystats_solution.py

def is_iter(v):
    v_is_iter = True
    try:
        iter(v)
    except:
        v_is_iter = False
    return v_is_iter

# define the mean function here
def mean(arg1, *args):
    nvals = 0
    if is_iter(arg1):
        sm = sum(arg1)
        nvals += len(arg1)
    else:
        sm = arg1
        nvals += 1
    for v in args:
        if (is_iter(v)):
            sm += sum(v)
            nvals += len(v)
        else:
            sm += v
            nvals += 1
    return sm / nvals

# define the stddev function here
def stddev(arg1, *args):
    mn = mean(arg1, args)  # sample mean
    smsq = 0               # sum of (value - mean) ** 2
    nvals = 0
    if is_iter(arg1):
        for val in arg1:
            smsq += (val - mn) ** 2
        nvals += len(arg1)
    else:
        smsq = (arg1 - mn) ** 2
        nvals += 1
    for v in args:
        if (is_iter(v)):
            for val in v:
                smsq += (val - mn) ** 2
            nvals += len(v)
        else:
            smsq += (v - mn) ** 2
            nvals += 1
    return m.sqrt(smsq / (nvals - 1))   # sample standard deviaiton

# define the median function here
def median(arg1, *args):
    all_vals = []     # one list of all values, so we can sort
    if is_iter(arg1):
        all_vals += list(arg1)
    else:
        all_vals += [arg1]
    for v in args:
        if (is_iter(v)):
            all_vals += list(v)
        else:
            all_vals += [v]
    all_vals.sort()
    avlen = len(all_vals)
    if avlen % 2 == 1:
        # odd?  then return middle value
        return all_vals[avlen // 2]
    else:
        # even?  then return mean of two middle values
        half_avlen = avlen // 2
        return (all_vals[half_avlen - 1] + all_vals[half_avlen]) / 2
    

# define the mode function here
def mode(arg1, *args):
    val_to_count = {}    # count occurrences of each value
    max_count = 0
    if is_iter(arg1):
        for v in arg1:
            if v in val_to_count:
                val_to_count[v] += 1
            else:
                val_to_count[v] = 1
            if val_to_count[v] > max_count:
                max_count = val_to_count[v]
    else:
        if arg1 in val_to_count:
            val_to_count[arg1] += 1
        else:
            val_to_count[arg1] = 1
        if val_to_count[arg1] > max_count:
            max_count = val_to_count[arg1]
    for a in args:
        if is_iter(a):
            for v in a:
                if v in val_to_count:
                    val_to_count[v] += 1
                else:
                    val_to_count[v] = 1
                if val_to_count[v] > max_count:
                    max_count = val_to_count[v]
        else:
            if a in val_to_count:
                val_to_count[a] += 1
            else:
                val_to_count[a] = 1
            if val_to_count[a] > max_count:
                max_count = val_to_count[a]
    mode_list = []
    for k in val_to_count.keys():
        if val_to_count[k] == max_count:
            mode_list += [k]
    mode_list.sort()
    return tuple(mode_list)

if __name__ == '__main__':
    print('The current module is:', __name__)
    
    print('mean(1) should be 1.0, and is:', mean(1))
    print('mean(1,2,3,4) should be 2.5, and is:', mean(1,2,3,4))
    print('mean(2.4,3.1) should be 2.75, and is:', mean(2.4,3.1))
    # print('mean() should FAIL:', mean())
    
    v1 = {1, 2, 3}     # a set is iterable
    print(v1, "is iterable:", is_iter(v1))
    v2 = 123
    print(v2, "is iterable:", is_iter(v2))
    
    print('mean([1,1,1,2]) should be 1.25, and is:',
                                   mean([1,1,1,2]))
    print('mean((1,), 2, 3, [4,6]) should be 3.2,' +
          'and is:', mean((1,), 2, 3, [4,6]))
    
    for i in range(10):
        print("Draw", i, "from Norm(0,1):",
                            np.random.randn())
    
    ls50 = [ np.random.randn() for i in range(50) ]
    print("Mean of", len(ls50), "values from Norm(0,1):",
                            mean(ls50))
    
    ls10000 = [ np.random.randn() for i in range(10000) ]
    print("Mean of", len(ls10000), "values from Norm(0,1):",
                            mean(ls10000))
    
    np.random.seed(0)
    a1 = np.random.randn(10)
    print(a1)    # should display an ndarray of 10 values
    print("the mean of a1 is:", mean(a1))
    print("the stddev of a1 is:", stddev(a1))
    print("the median of a1 is:", median(a1))
    print("median(3, 1, 5, 9, 2):", median(3, 1, 5, 9, 2))
    print("mode(1, 2, (1, 3), 3, [1, 3, 4]) is:",
                mode(1, 2, (1, 3), 3, [1, 3, 4]))
