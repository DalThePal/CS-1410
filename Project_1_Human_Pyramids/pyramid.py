import sys
import time

HUMAN_WEIGHT = 200
cache = {}
cache_count = 0
call_count = 0

def weightOn(r, c):
    """recursively calculated the weight a human is carrying"""
    global call_count
    call_count += 1

    if (r, c) in cache:
        global cache_count
        cache_count += 1
        weight = cache[(r,c)]

    elif c > r or c < 0:
        weight = -HUMAN_WEIGHT
        cache[(r,c)] = weight

    else:
        weight = HUMAN_WEIGHT + (weightOn(r - 1, c) / 2) + (weightOn(r - 1, c - 1) / 2)
        cache[(r,c)] = weight

    # print(weight)
    return weight

def buildPyramid(rows):
    """loop through the number of rows and creates a pyramid by calling the weightOn function"""
    pyramid = []

    for i in range(0, rows):
        pyramid.append([])

        for j in range(0, i + 1):
            weight = weightOn(i, j)
            pyramid[i].append(weight)
            print('%.2f ' % weight, end='')

        print('\n')
    
    return 
    

def buildPyramidTwo(r, c):
    """just like buildPyramid but recursive :) but prints upside down :("""

    if r < 0:
        return

    elif c < 0 :
        print('\n')
        return buildPyramidTwo(r-1, r-1)

    else:
        print(weightOn(r, c), end=" ")
        return buildPyramidTwo(r, c - 1)

    return 
    
   

def main():
    start_time = time.perf_counter()

    help(weightOn)
    help(buildPyramid)
    help(buildPyramidTwo)

    num_rows = int(sys.argv[1])
    buildPyramid(num_rows)
    # buildPyramidTwo(num_rows, num_rows)
    stop_time = time.perf_counter()

    print('Elapsed time: ' + str(stop_time - start_time) + ' seconds')
    print('Number of function calls: ' + str(call_count))
    print('Number of cache hits: ' + str(cache_count))
    
    
if __name__ == "__main__":
    main()