"""
You are given a 2d grid of `"1"`s and `"0"`s that represents a "map". The
`"1"`s represent land and the `"0"s` represent water.

You need to write a function that, given a "map" as an argument, counts the
number of islands. Islands are defined as adjacent pieces of land that are
connected horizontally or vertically. You can also assume that the edges of the
map are surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
"""
from collections import deque

def numIslands(grid):
    # Your code here
    num_islands = 0
    # iterate through our map 
    for i, row in enumerate(grid):
        for j, loc in enumerate(row):
            # what do we do when we see a 1? 
            # we need to figure out how large that island is 
            # the island could just consist of a single 1, or
            # it could have other 1's connected to it 
            if loc == "1":
                num_islands += 1
                # when we encounter a 1, we need to traverse that island 
                # by looking to the right and by looking down 
                # we can use either a depth-first traversal or a breadth-first traversal
                # doesn't matter which one we choose, since it doesn't matter the order
                # in which we visit them 
                stack = [(i, j)] 
                # toggle this 1 to a 0
                grid[i][j] = "0"

                while len(stack) > 0:
                    r, c = stack.pop()
                    # look to the left
                    if c > 0 and grid[r][c-1] == '1':
                        # add that spot to our stack so that we'll visit it 
                        stack.append((r, c - 1))
                        grid[r][c-1] = '0' 

                    # look to the right
                    # we need to increment the col index by 1 
                    # we also need to make sure that col + 1 is still in bounds 
                    if c < len(row) - 1 and grid[r][c+1] == '1':
                        # add that spot to our stack so that we'll visit it 
                        stack.append((r, c + 1))
                        grid[r][c+1] = '0'

                    # look up
                    if r > 0 and grid[r-1][c] == '1':
                        # add that spot to our stack so that we'll visit it 
                        stack.append((r - 1, c))
                        grid[r-1][c] = '0' 

                    # look down 
                    if r < len(grid) - 1 and grid[r+1][c] == '1':
                        # add that spot to our stack so that we'll visit it 
                        stack.append((r + 1, c))
                        grid[r+1][c] = '0' 

            # over the course of traversing an island, how do we avoid
            # double-counting 1's we've already seen before? 
            # toggle any 1's we've accounted for to a 0 to avoid double-counting 
            # keep a separate data structure that keeps track of the coordintes
            # that we've already visited 

    return num_islands

grid = [
  ['0', '1'],
  ['1', '1']
]

print(numIslands(grid))