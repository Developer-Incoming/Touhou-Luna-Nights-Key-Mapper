from pynput.mouse import Listener
from pynput.mouse import Button
from keyboard import press, release
from time import sleep # uses sleep because press_and_release isn't considered an output for the game

# # Make sure to edit the key configurations in the game to matchup with the keys below, or edit them to your will.
# LMB
attack = "k"
# MMW
skill_change_up = "r"
skill_change_down = "f"


def on_click(x, y, button, pressed):
    if button == Button.left:
        if pressed: press(attack)
        else: release(attack)

def on_scroll(x, y, dx, dy):
    if dy > 0:
        press(skill_change_up)
        sleep(0.25)
        release(skill_change_up)
        
    if dy < 0:
        press(skill_change_down)
        sleep(0.25)
        release(skill_change_down)
        

with Listener(on_scroll=on_scroll, on_click=on_click) as listener:
    listener.join()
