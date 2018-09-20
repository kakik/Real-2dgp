from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def move_character(from_x, from_y, to_x, to_y):
    global x, y
    x_speed = (to_x - from_x) / 32
    y_speed = (to_y - from_y) / 32

    for i in (1, 32):
        x += x_speed
        y += y_speed

def handle_events():
    global running
    global x, y
    global mx, my
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, KPU_HEIGHT // 2 - event.y + 52

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                move_character(x, y, mx, my)

        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False



open_canvas()
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
mx, my = 0, 0
frame = 0
hide_cursor()

while running:
    handle_events()
    clear_canvas()

    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    if mx > x:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    else:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    hand_arrow.clip_draw(0, 0, 50, 52, mx, my)
    update_canvas()
    frame = (frame + 1) % 8

    delay(0.05)
    handle_events()

close_canvas()
