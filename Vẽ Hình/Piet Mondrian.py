# mondrian.py
import cairo 
import random
# the size of the image
IMAGE_WIDTH = 500
IMAGE_HEIGHT = 500
# the size of the tile grid
MAP_WIDTH = 50
MAP_HEIGHT = 50
# the size of each tile
TILE_SIZE = 10
MAX_LINES = 15
MIN_LINES = 6
MAX_RECTS = 5
MIN_RECTS = 1
tiles = {}
#colors (0,white),(1,black),(2,red),(3,yellow)(4,blue)
def generate_tiles():
    # build tile map
    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            # set every tile to white
            tiles[x,y] = 0
    draw_lines()
def draw_lines():
    total_lines = random.randint(MIN_LINES,MAX_LINES)
    print(total_lines)
    for h in range(int(total_lines/2)):
        y = random.randint(0,MAP_HEIGHT)
        for x in range(MAP_WIDTH):
            tiles[x,y] = 1
    for v in range(int(total_lines/2)):
        x = random.randint(0,MAP_WIDTH)
        for y in range(MAP_HEIGHT):
            tiles[x,y] = 1
    fill_rects()
def fill_rects():
    total_rects = random.randint(MIN_RECTS,MAX_RECTS)
    max_iters = 5
    for i in range(max_iters):
        for r in range(total_rects):
            x = random.randint(0,MAP_WIDTH-1)
            y = random.randint(0,MAP_HEIGHT-1)
            if tiles[x,y] == 0:
                color = random.randint(2,4)
                flood_recursion(x,y,0,color)
def flood_recursion(x,y,start_color,update_color):
    width = MAP_WIDTH
    height = MAP_HEIGHT
    if tiles[x,y] != start_color:
        return
    elif tiles[x,y] == update_color:
        return
    else:
        tiles[x,y] = update_color
        neighbors = [(x-1,y),(x+1,y),(x-1,y-1),(x+1,y+1),(x-1,y+1),(x+1,y-1),(x,y-1),(x,y+1)]
        for n in neighbors:
            if 0 <= n[0] <= width-1 and 0 <= n[1] <= height-1:
                flood_recursion(n[0],n[1],start_color,update_color)
def draw_map():
    # draw tile map using pycairo
    surface = cairo.ImageSurface(cairo.FORMAT_RGB24, IMAGE_WIDTH, IMAGE_HEIGHT)
    ctx = cairo.Context(surface)
    for x in range(MAP_WIDTH):
        for y in range(MAP_HEIGHT):
            size = TILE_SIZE
            ctx.rectangle(x*size,y*size,x+size,y+size)
            if tiles[x,y] == 0:
                ctx.set_source_rgb(1,1,1)
            elif tiles[x,y] == 1:
                ctx.set_source_rgb(0,0,0)
            elif tiles[x,y] == 2:
                ctx.set_source_rgb(1,0,0)
            elif tiles[x,y] == 3:
                ctx.set_source_rgb(1,1,0)
            else:
                ctx.set_source_rgb(0,0,1)
ctx.fill()
surface.write_to_png('mondrian.png')
generate_tiles()
draw_map()