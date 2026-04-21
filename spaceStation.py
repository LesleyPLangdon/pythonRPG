import pgzrun
player = {
    "x": 2,
    "y": 2,
    "color": (0, 255, 180)
}
TITLE = "Space Station"
WIDTH = 640
HEIGHT = 480

TILE_SIZE = 32

# 0 = floor, 1 = wall
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

FLOOR_COLOR = (30, 30, 60)
WALL_COLOR  = (80, 140, 180)

def draw():
    screen.fill((20, 20, 40))
    for row_index, row in enumerate(MAP):
        for col_index, tile in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            color = WALL_COLOR if tile == 1 else FLOOR_COLOR
            screen.draw.filled_rect(
                Rect(x, y, TILE_SIZE, TILE_SIZE),
                color
            )
def draw():
    screen.fill((20, 20, 40))
    for row_index, row in enumerate(MAP):
        for col_index, tile in enumerate(row):
            x = col_index * TILE_SIZE
            y = row_index * TILE_SIZE
            color = WALL_COLOR if tile == 1 else FLOOR_COLOR
            screen.draw.filled_rect(
                Rect(x, y, TILE_SIZE, TILE_SIZE),
                color
            )
    # draw the player as a small circle in the center of their tile
    screen.draw.filled_circle(
        (player["x"] * TILE_SIZE + TILE_SIZE // 2,
         player["y"] * TILE_SIZE + TILE_SIZE // 2),
        TILE_SIZE // 2 - 4,
        player["color"]
    )

SPEED = 0.1
player = {
    "x": 2.0,
    "y": 2.0,
    "color": (0, 255, 180),
    "move_timer": 0.0
}

def update(dt):
    player["move_timer"] += dt
    if player["move_timer"] < SPEED:
        return
    player["move_timer"] = 0

    new_x = player["x"]
    new_y = player["y"]

    if keyboard.left:
        new_x -= 1
    if keyboard.right:
        new_x += 1
    if keyboard.up:
        new_y -= 1
    if keyboard.down:
        new_y += 1

    # check map boundaries
    if new_x < 0 or new_y < 0 or new_y >= len(MAP) or new_x >= len(MAP[0]):
        return

    # check for wall collision
    if MAP[int(new_y)][int(new_x)] == 0:
        player["x"] = new_x
        player["y"] = new_y
pgzrun.go()