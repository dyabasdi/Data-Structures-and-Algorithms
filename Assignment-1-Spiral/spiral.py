import math

def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral dimeter"""
    spiral = [[0 for rows in range(dim)] for columns in range(dim)]
    column = (dim//2)
    row = (dim//2)
    spiral_number = 1
    max_spiral_numbers = column
    spiral[row][column] = 1
    number=2
    for _ in range (max_spiral_numbers):
        down_spaces = 1 + 2*(spiral_number - 1)
        spaces = 2 + 2*(spiral_number - 1)
        column += 1
        spiral[row][column] = number
        number+=1
        for _ in range (down_spaces):
            row+=1
            spiral[row][column] = number
            number+=1
        for _ in range (spaces):
            column-=1
            spiral[row][column] = number
            number+=1
        for _ in range (spaces):
            row-=1
            spiral[row][column] = number
            number+=1
        for _ in range (spaces):
            column+=1
            spiral[row][column] = number
            number+=1
        spiral_number+=1
    return spiral

def sum_sub_grid(grid, val):
    """
    Input: grid a 2-D list containing a spiral of numbers
           val is a number within the range of numbers in
           the grid
    Output:
    sum_sub_grid returns the sum of the numbers (including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """
    if val>len(grid)*len(grid):
        return 0
    for row in range(len(grid)):
        for column in range(len(grid)):
            if grid[row][column]==val:
                index=[row, column]
                break
    total=0
    column=index[1]-1
    row=index[0]-1
    for runs in range(3):
        if row<0:
            row+=1
            continue
        for runs in range(3):
            if column<0:
                column+=1
                continue
            if(row<len(grid) and column<len(grid)):
                total+=grid[row][column]
            column+=1
        column = index[1]-1
        row+=1
    total-=val
    return total

def main():
    """
    A Main Function to read the data from input,
    run the program and print to the standard output.
    """

    # read the dimension of the grid and value from input file
    dim = int(input())

    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1

    # create a 2-D list representing the spiral
    mat = create_spiral(dim)

    while True:
        try:
            sum_val = int(input())

            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)

            # print the sum
            print(adj_sum)
        except EOFError:
            break

if __name__ == "__main__":
    main()
