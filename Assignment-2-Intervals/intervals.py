"""
    Input: tuples_list is an unsorted list of tuples denoting intervals
    Output: a list of merged tuples sorted by the lower number of the
    interval
"""
import sys


def merge_tuples (tuples_list):
    """Merge the tuples"""

    # ADD YOUR CODE HERE ... AND REMOVE THIS Line
    tuples_list=sorted(tuples_list)
    x=0
    y=x+1
    while x <(len(tuples_list)-1):
        while y < (len(tuples_list)):
            lower1=tuples_list[x][0]
            lower2=tuples_list[y][0]
            upper1=tuples_list[x][1]
            upper2=tuples_list[y][1]
            case1=upper1 in range(lower2,upper2)
            case2=upper2 in range(lower1,upper1)
            case3=lower2 in range(lower1,upper1)
            if(case1 or case2 or case3):
                tuple=(min(lower1,lower2),max(upper1,upper2))
                tuples_list.insert(x,tuple)
                tuples_list.remove(tuples_list[x+1])
                tuples_list.remove(tuples_list[y])
                y-=1
            y+=1
        x+=1
        y=x+1
    return tuples_list # Replace this 



def sort_by_interval_size (tuples_list):
    """
    Input: tuples_list is a list of tuples of denoting intervals
    Output: a list of tuples sorted by ascending order of the
    size of the interval if two intervals have the size then it will sort by the
    lower number in the interval
    """

    # Add Your Code HERE ... AND REMOVE THIS Line
    y=1
    for x in range(len(tuples_list)-1):
        while y < len(tuples_list):
            range1=abs(tuples_list[x][1]-tuples_list[x][0])
            range2=abs(tuples_list[y][1]-tuples_list[y][0])
            case1=range1>range2
            case2=range1==range2
            case3=tuples_list[x][0]>tuples_list[y][0]
            if(case1 or (case2 and case3)):
                tuples_list[x],tuples_list[y]=tuples_list[y],tuples_list[x]
                y-=1
            y+=1
        y=x+1
    return tuples_list # Replace this.



def main():
    """
    Open file intervals.in and read the data and create a list of tuples
    """
    sys.stdin.readline()

    tup_list = []
    tup_list = sys.stdin.readlines()

    tuples_list = []
    for m_tuple in tup_list:
        tup = m_tuple.split()
        tuples_list.append(tuple((int(tup[0]), int(tup[1]))))

    # merge the list of tuples
    merged = merge_tuples(tuples_list)

    # sort the list of tuples according to the size of the interval
    sorted_merge = sort_by_interval_size(merge_tuples(tuples_list))

    # write the output list of tuples from the two functions
    print(merged)
    print(sorted_merge)

if __name__ == "__main__":
    main()
