import sys
import time


# Input: v an integer representing the minimum lines of code and
#        k an integer representing the productivity factor
# Output: computes the sum of the series (v + v // k + v // k**2 + ...)
#         returns the sum of the series
def sum_series (v, k):
    z = 1
    output = v
    while v//k**z != 0:
        output += v//(k**z)
        z+=1
    return output


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using linear search
def linear_search (n, k):
    the_v = 1
    the_k = k
    while True:
        if sum_series(the_v, the_k) >= n:
            return the_v
        the_v += 1


# Input: n an integer representing the total number of lines of code
#        k an integer representing the productivity factor
# Output: returns v the minimum lines of code to write using binary search
def binary_search (n, k):
    # lst = []
    # for j in range(n):
    #     lst.append(sum_series(j,k))
    low = 0
    the_v = 0
    high = n
    the_x = -1
    while low <= high:
        the_v = (high + low)//2
        if sum_series(the_v, k) < n:
            low = the_v + 1
        else:
            the_x = the_v
            high = the_v - 1
    if the_x == -1:
        return the_v
    return the_x

def main():
    # read number of cases
    line = sys.stdin.readline()
    line = line.strip()
    num_cases = int (line)

    for _ in range (num_cases):
        line = sys.stdin.readline()
        line = line.strip()
        inp =  line.split()
        n = int(inp[0])
        k = int(inp[1])

        start = time.time()
        print("Binary Search: " + str(binary_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()

        start = time.time()
        print("Linear Search: " + str(linear_search(n, k)))
        finish = time.time()
        print("Time: " + str(finish - start))

        print()
        print()

if __name__ == "__main__":
    main()
