import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

pinCLK = digitalio.DigitalInOut(board.GP2)
pinDT  = digitalio.DigitalInOut(board.GP3)
pinSW  = digitalio.DigitalInOut(board.GP4)

pinCLK.switch_to_input(pull=digitalio.Pull.UP)
pinDT.switch_to_input(pull=digitalio.Pull.UP)
pinSW.switch_to_input(pull=digitalio.Pull.UP)

pins = [
    board.GP14, board.GP15, board.GP16, board.GP17,
    board.GP18, board.GP19, board.GP20, board.GP21,
    board.GP22, board.GP26, board.GP27, board.GP28,
]

F_KEYS = [
    Keycode.F24, Keycode.F20, Keycode.F16, Keycode.F23,
    Keycode.F19, Keycode.F15, Keycode.F22, Keycode.F18,
    Keycode.F14, Keycode.F21, Keycode.F17, Keycode.F13,
]

class ButtonState:
    def __init__(self, pin, keycode):
        self.pin = digitalio.DigitalInOut(pin)
        self.pin.direction = digitalio.Direction.INPUT
        self.pin.pull = digitalio.Pull.UP
        self.keycode = keycode
        self.pressed = False

buttons = [ButtonState(p, k) for p, k in zip(pins, F_KEYS)]

last_state_CLK = pinCLK.value
last_state_DT = pinDT.value

mode = 0  # 0 = volume; 1 = playback
last_button_time = 0
click_count = 0
button_pressed = False
last_rotate_time = 0

DOUBLE_CLICK_DELAY = 0.3  # in seconds

while True:
    for btn in buttons:
        if not btn.pin.value:  # LOW = pressed
            if not btn.pressed:
                kbd.press(btn.keycode)
                btn.pressed = True
        else:
            if btn.pressed:
                kbd.release(btn.keycode)
                btn.pressed = False

    current_time = time.monotonic()
    current_state_CLK = pinCLK.value
    current_state_DT = pinDT.value

    # Rotace
    if current_state_CLK != last_state_CLK:
        if current_state_DT != current_state_CLK:
            if mode == 0:
                cc.send(ConsumerControlCode.VOLUME_INCREMENT)
            elif mode == 1 and (current_time - last_rotate_time) > 0.5:
                cc.send(ConsumerControlCode.SCAN_NEXT_TRACK)
                last_rotate_time = current_time
        else:
            if mode == 0:
                cc.send(ConsumerControlCode.VOLUME_DECREMENT)
            elif mode == 1 and (current_time - last_rotate_time) > 0.5:
                cc.send(ConsumerControlCode.SCAN_PREVIOUS_TRACK)
                last_rotate_time = current_time

    last_state_CLK = current_state_CLK
    last_state_DT = current_state_DT

    # Pressed button detection
    if not pinSW.value and not button_pressed:
        button_pressed = True
        if current_time - last_button_time < DOUBLE_CLICK_DELAY:
            click_count += 1
        else:
            click_count = 1
        last_button_time = current_time

    # Button release
    if pinSW.value and button_pressed:
        button_pressed = False

    # Doubleclick treshold
    if click_count == 2 and (current_time - last_button_time) > DOUBLE_CLICK_DELAY:
        mode = (mode + 1) % 2
        print("Přepnuto na mód:", mode)
        click_count = 0

    # Pressed
    if click_count == 1 and (current_time - last_button_time) > DOUBLE_CLICK_DELAY:
        if mode == 1:
            cc.send(ConsumerControlCode.PLAY_PAUSE)
        elif mode == 0:
            cc.send(ConsumerControlCode.MUTE)
        click_count = 0

    time.sleep(0.001)
