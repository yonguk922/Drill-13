import game_framework
import pause_mode
from pico2d import *
import game_world
from boy import Boy
from grass import Grass

item_image = None
item_mode = False
selected_ball = 1


def handle_events():
    global item_mode, selected_ball

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_p:
            game_framework.push_mode(pause_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            item_mode = not item_mode
        elif item_mode and event.type == SDL_KEYDOWN:
            if event.key == SDLK_0:
                selected_ball = 0
            elif event.key == SDLK_1:
                selected_ball = 1
            elif event.key == SDLK_2:
                selected_ball = 2
            else:
                boy.handle_event(event)
        elif item_mode:
            boy.handle_event(event)
        else:
            boy.handle_event(event)



def init():
    global boy, item_image, item_mode, selected_ball

    item_image = load_image('item_select.png')
    item_mode = False
    selected_ball = 1

    boy = Boy()
    game_world.add_oject(boy)

    grass = Grass()
    game_world.add_oject(grass, 0)



def update():
    boy.ball_type = selected_ball
    game_world.update()


def render():
    clear_canvas()
    game_world.render()
    if item_mode:
        item_image.draw(get_canvas_width() // 2, get_canvas_height() // 2)
    update_canvas()

def finish():
    global item_image
    game_world.clear()
    del item_image

def pause():
    pass

def resume():
    pass

import title_mode
