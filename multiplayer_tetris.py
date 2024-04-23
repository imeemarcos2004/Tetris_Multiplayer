import pygame
import random
from PIL import Image
import webbrowser

pygame.init()
pygame.font.init()

s_width = 1500
s_height = 700
play_width = 665
play_height = 600
play_width1 = 665
play_height1 = 600
block_size = 30
block_size1 = 30

top_left_x = 10
top_left_y = 100

top_left_x1 = 815
top_left_y1 = 100

S = [['.....',
      '.....',
      '..00.',
      '.00..',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '...0.',
      '.....']]

Z = [['.....',
      '.....',
      '.00..',
      '..00.',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '.0...',
      '.....']]

J = [['.....',
      '.0...',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..00.',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '...0.',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '.00..',
      '.....']]

I = [['..0..',
      '..0..',
      '..0..',
      '..0..',
      '.....'],
     ['.....',
      '0000.',
      '.....',
      '.....',
      '.....']]

O = [['.....',
      '.....',
      '.00..',
      '.00..',
      '.....']]

L = [['.....',
      '...0.',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..0..',
      '..00.',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '.0...',
      '.....'],
     ['.....',
      '.00..',
      '..0..',
      '..0..',
      '.....']]

T = [['.....',
      '..0..',
      '.000.',
      '.....',
      '.....'],
     ['.....',
      '..0..',
      '..00.',
      '..0..',
      '.....'],
     ['.....',
      '.....',
      '.000.',
      '..0..',
      '.....'],
     ['.....',
      '..0..',
      '.00..',
      '..0..',
      '.....']]


# O = ""


##############################

# def image1(image):
#     # Define the grid
#     image = image
#     grid = [
#     ['.....',
#     '.....',
#     '.00..',
#     '.00..',
#     '.....']
#     ]

#     # Define pixel colors
#     colors = {
#     '.': (255, 255, 255),  # White
#     '0': (0, 0, 0)          # Black
#     }

#     # Determine image dimensions
#     height = len(grid)
#     width = len(grid[0][0])

#     # Create a new image with white background
#     image = Image.new('RGB', (width, height), color='white')
#     pixels = image.load()

#     # Convert grid to image
#     for y in range(height):
#         for x in range(width):
#             pixel_color = colors[grid[0][y][x]]
#             pixels[x, y] = pixel_color

#     # Save or display the image
#     image.show()  # Display the image
#     # image.save('output.png')  # Save the image
# # O = image1(image1)



shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
shape_colors1 = [(255, 255, 0), (255, 10, 100), (29, 255, 255), (255, 0, 255), (180, 165, 11), (120, 70, 25), (128, 109, 12)]
class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0

class Piece1(object):
    def __init__(self, x1, y1, shape1):
        self.x1 = x1
        self.y1 = y1
        self.shape1 = shape1
        self.color1 = shape_colors1[shapes.index(shape1)]
        self.rotation1 = 0

def create_grid(locked_pos = {}):
    grid = [[(0,0,0) for _ in range(22)] for _ in range(20)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c
    return grid

def create_grid1(locked_pos = {}):
    grid = [[(0,0,0) for _ in range(22)] for _ in range(20)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_pos:
                c = locked_pos[(j, i)]
                grid[i][j] = c
    return grid

def valid_space(shape, grid):
    accepted_pos = [[(j, i) for j in range(22) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]
    
    formatted = convert_shape_format(shape)
    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True

def valid_space1(shape, grid):
    accepted_pos = [[(j, i) for j in range(22) if grid[i][j] == (0,0,0)] for i in range(20)]
    accepted_pos = [j for sub in accepted_pos for j in sub]
    
    formatted = convert_shape_format1(shape)
    for pos in formatted:
        if pos not in accepted_pos:
            if pos[1] > -1:
                return False
    return True


def convert_shape_format(shape):
    positions = []
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x + j, shape.y + i))
    
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions

def convert_shape_format1(shape):
    positions = []
    format = shape.shape1[shape.rotation1 % len(shape.shape1)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                positions.append((shape.x1 + j, shape.y1 + i))
    
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def check_lost1(positions):
    for pos in positions:
        x1, y1 = pos
        if y1 < 1:
            return True
    return False

def get_shape():
    return Piece(5, 0, random.choice(shapes))
def get_shape1():
    return Piece1(5, 0, random.choice(shapes))

def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (1000,300))

def draw_text_middle1(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (170, 300))

def draw_text_middle2(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (420, 200))

def developed_by(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (520, 302))




def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, (128,128,128), (sx, sy + i * block_size), (sx + play_width, sy + i * block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128,128,128), (sx + j * block_size, sy ), (sx + j * block_size, sy + play_height))

def draw_grid1(surface, grid):
    sx = top_left_x1
    sy = top_left_y1

    for i in range(len(grid)):
        pygame.draw.line(surface, (128,128,128), (sx, sy + i * block_size1), (sx + play_width1, sy + i * block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128,128,128), (sx + j * block_size1, sy ), (sx + j * block_size1, sy + play_height1))

def ding_music():
    pygame.mixer.init()
    pygame.mixer.music.load("D:/Tetris_Multiplayer/media/ding.mp3")
    pygame.mixer.music.play()

def clear_rows(grid, locked):
    inc = 0
    for i in range(len(grid) -1, -1, -1):
        row = grid[i]
        if (0,0,0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked[(j, i)]
                except:
                    continue

    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newyKey = (x, y + inc)
                locked[newyKey] = locked.pop(key)
    return inc


def clear_rows1(grid1, locked1):
    inc = 0
    for i in range(len(grid1) -1, -1, -1):
        row = grid1[i]
        if (0,0,0) not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked1[(j, i)]
                except:
                    continue

    if inc > 0:
        for key in sorted(list(locked1), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newyKey = (x, y + inc)
                locked1[newyKey] = locked1.pop(key)
    return inc




def draw_next_shape(shape, surface):
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('next shape', 1, (255,255,255))
    surface.blit(label, (900,15))

    sx = 1150
    sy = 18
    format = shape.shape[shape.rotation % len(shape.shape)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j * 15, sy + i * 15, 15, 15), 0)
    pygame.display.update()

    
    # pygame.display.update()


def tetris_text(surface):
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 50)
    label = font.render('TETRIS', 1, (255,255,255))
    surface.blit(label, (645,15))


def draw_next_shape1(shape, surface1):
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('next shape', 1, (255,255,255))
    surface1.blit(label, (20, 20))
    
    sx1 = 290
    sy1 = 18
    format = shape.shape1[shape.rotation1 % len(shape.shape1)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface1, shape.color1, (sx1 + j * 15, sy1 + i * 15, 15, 15), 0)

    pygame.display.update()

    
    # pygame.display.update()


def draw_window(surface, grid, grid1, score=0, score1=0, last_score = 0, last_score1 = 0):
    surface.fill((0,0,0))
 
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255,255,255))

    surface.blit(label, (top_left_x + play_width/2 - (label.get_width() / 2), 30))
    surface.blit(label, (top_left_x1 + play_width/2 - (label.get_width() / 2), 30))
    
    surface.fill((0,0,0))


    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Score ' + str(score), 1, (255,255,255))
    label1 = font.render('Score ' + str(score1), 1, (255,255,255))

    surface.blit(label, (1280, 20))
    surface.blit(label1, (450, 20))
    tetris_text(win)


    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size), 0)
    pygame.draw.rect(surface, (255,0,0), (top_left_x, top_left_y, play_width, play_height), 4)



    for a in range(len(grid1)):
        for b in range(len(grid1[a])):
            pygame.draw.rect(surface, grid1[a][b], (top_left_x1 + b * block_size1, top_left_y1 + a * block_size1, block_size1, block_size1), 0)
    pygame.draw.rect(surface, (255,0,0), (top_left_x1, top_left_y1, play_width1, play_height1), 4)

    
    draw_grid(surface, grid)
    draw_grid1(surface, grid1)
   
def play_background_music():
    pygame.time.Clock()
    pygame.mixer.init()
    pygame.mixer.music.load("D:/Tetris_Multiplayer/media/background.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.play(-1)


def pause_background_music():
    pygame.mixer.init()
    pygame.mixer.music.pause()



def main(win):
    play_background_music()
    locked_position = {}
    locked_position1 = {}
    grid = create_grid(locked_position)
    grid1 = create_grid1(locked_position1)

    change_piece = False
    change_piece1 = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    current_piece1 = get_shape1()
    next_piece1 = get_shape1()
    
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.4
    level_time = 0
    score = 0
    score1 = 0

    while run:
        
        pygame.mixer.init()
        pygame.init()
        
        grid = create_grid(locked_position)
        grid1 = create_grid1(locked_position1)
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time / 1000 > 5:
            level_time = 0
            if level_time> 0.12:
                level_time -= 0.005

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not(valid_space(current_piece, grid)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

            current_piece1.y1 += 1
            if not(valid_space1(current_piece1, grid1)) and current_piece1.y1 > 0:
                current_piece1.y1 -= 1
                change_piece1 = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pause_background_music()
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause_background_music()
                    run = False
                    
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x += 1

                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.x -= 1

                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.y -= 1

                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if not (valid_space(current_piece, grid)):
                        current_piece.rotation -= 1

                if event.key == pygame.K_a:
                    current_piece1.x1 -= 1
                    if not (valid_space1(current_piece1, grid1)):
                        current_piece1.x1 += 1

                if event.key == pygame.K_d:
                    current_piece1.x1 += 1
                    if not (valid_space1(current_piece1, grid1)):
                        current_piece1.x1 -= 1

                if event.key == pygame.K_s:
                    current_piece1.y1 += 1
                    if not (valid_space1(current_piece1, grid1)):
                        current_piece1.y1 -= 1

                if event.key == pygame.K_w:
                    current_piece1.rotation1 += 1
                    if not (valid_space1(current_piece1, grid1)):
                        current_piece1.rotation1 -= 1


        shape_pos = convert_shape_format(current_piece)
        shape_pos1 = convert_shape_format1(current_piece1)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.color
                grid[y][x] = current_piece.color

        for i in range(len(shape_pos)):
            x, y = shape_pos1[i]
            if y > -1:
                grid1[y][x] = current_piece1.color1
                grid1[y][x] = current_piece1.color1

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_position[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            score += clear_rows(grid, locked_position) * 10

        if change_piece1:
            for pos in shape_pos1:
                p = (pos[0], pos[1])
                locked_position1[p] = current_piece1.color1
            current_piece1 = next_piece1
            next_piece1 = get_shape1()
            change_piece1 = False
            score1 += clear_rows1(grid1, locked_position1) * 10
            
        
        draw_next_shape(next_piece, win)
        draw_next_shape1(next_piece1, win)
        draw_window(win, grid1, grid, score, score1)
        pygame.display.update()
        

        if check_lost(locked_position):
            draw_text_middle(win, "you lost", 80, (255, 255, 255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
        if check_lost1(locked_position1):
            draw_text_middle1(win, "you lost", 80, (255, 255, 255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False

    draw_next_shape(next_piece,win)
    draw_next_shape1(next_piece1,win)
    pygame.display.update()

font5 = pygame.font.SysFont(None, 40)
BLUE = (0, 0, 255)
def create_link(surface, text, font, color, x, y, url):
    x = 750
    y = 315
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft=(x, y))
    surface.blit(text_surface, text_rect)
    link_rect = pygame.Rect(x, y, text_rect.width, text_rect.height)
    return link_rect, url


def main_menu(win):
    pygame.init()
    run = True
    while run:
        win.fill((0,0,0))
        link_rect, url = create_link(win, "Lovely Jane Colis", font5, BLUE, 50, 50, "https://www.facebook.com/profile.php?id=100025628571179")
        draw_text_middle2(win, "Press Any Key To Play", 60, (255, 255, 255))

        developed_by(win, "Developed by", 30, (255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    if link_rect.collidepoint(pos):
                        webbrowser.open(url)
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_ESCAPE:
                    run = False
                    pygame.display.quit()
                else:
                    main(win)
             
    pygame.display.quit() 

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)

