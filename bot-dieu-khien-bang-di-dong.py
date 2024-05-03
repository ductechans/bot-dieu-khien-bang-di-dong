from ble import *
from rover import *
import music
from yolobit import *
button_a.on_pressed = None
button_b.on_pressed = None
button_a.on_pressed_ab = button_b.on_pressed_ab = -1
import time

def on_ble_message_string_receive_callback(chu_E1_BB_97i):

  if chu_E1_BB_97i == ('!B516'):
    rover.forward(30, 0.2)
  elif chu_E1_BB_97i == ('!B615'):
    rover.backward(30, 0.2)
  elif chu_E1_BB_97i == ('!B714'):
    rover.turn_left(30, 0.15)
  elif chu_E1_BB_97i == ('!B814'):
    rover.turn_right(30, 0.15)
  elif chu_E1_BB_97i == ('!B219'):
    music.play(music.DADADADUM, wait=False)
  elif chu_E1_BB_97i == ('!B318'):
    display.set_all('#ff0000')
  elif chu_E1_BB_97i == ('!B11:'):
    display.set_all('#00ff00')
  elif chu_E1_BB_97i == ('!B417'):
    display.set_all('#ff0000')
  else:
    rover.stop()

ble.on_receive_msg("string", on_ble_message_string_receive_callback)

def on_ble_connected_callback():
  global chu_E1_BB_97i
  display.set_all('#00ff00')

ble.on_connected(on_ble_connected_callback)

def on_ble_disconnected_callback():
  global chu_E1_BB_97i
  display.set_all('#000000')

ble.on_disconnected(on_ble_disconnected_callback)

def on_ble_message_string_receive_callback(chu_E1_BB_97i):

  if chu_E1_BB_97i == ('!B516'):
    rover.forward(30, 0.2)
  elif chu_E1_BB_97i == ('!B615'):
    rover.backward(30, 0.2)
  elif chu_E1_BB_97i == ('!B714'):
    rover.turn_left(30, 0.15)
  elif chu_E1_BB_97i == ('!B814'):
    rover.turn_right(30, 0.15)
  elif chu_E1_BB_97i == ('!B219'):
    music.play(music.DADADADUM, wait=False)
  elif chu_E1_BB_97i == ('!B318'):
    display.set_all('#ff0000')
  elif chu_E1_BB_97i == ('!B11:'):
    display.set_all('#00ff00')
  elif chu_E1_BB_97i == ('!B417'):
    display.set_all('#ff0000')
  else:
    rover.stop()

ble.on_receive_msg("string", on_ble_message_string_receive_callback)

if True:
  music.play(music.POWER_UP, wait=False)
  display.scroll('OK')
  display.set_all('#000000')

while True:
  time.sleep_ms(500)
