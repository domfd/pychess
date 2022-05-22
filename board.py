import pygame

height = 496
width = 496
scr_width = 800
scr_height = 600
letters = {0:"H", 1:"G", 2:"F", 3:"E", 4:"D", 5:"C", 6:"B", 7:"A"}

def getsize():
    return (width,height)

grid = [[0 for x in range(8)] for y in range(8)]
for y in range(8):
    for x in range(8):
        grid[y][x] = (((scr_width-width)/2)+(x*width/8),((scr_height-height)/2)+(y*height/8))

positions = {}
for y in range(8):
    for x in range(8):
        positions[letters[y] + str(x + 1)] = grid[y][x]    


def find_cell(xy):
    # TODO
    # check in which grid[x][y] the coords are!
    return grid[x][y]



