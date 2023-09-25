"""
Author: [Natanya Anderson]
Assignment / Part: HW6 - Q1 (depending on the file name)
Date due: 2022-10-20, 11:59pm
I pledge that I have completed this assignment without
collaborating with anyone else, in conformance with the
NYU School of Engineering Policies and Procedures on
Academic Misconduct.
"""

# Ask input for type of touch y
# Ask for strength of touch y
# Four different touches, single double hold swipe
# If touch = swipe, ONLY direction can be up, down, left. If touch != swipe, direction is no direction
# If touch = hold, ONLY ask for duration which can be any pos int. Strength only matters here. Range is 0.0 to 1.0.
# Three functions in this problem: give_haptic_feedback(), register_touch(), and main func get_touch()
# give_haptic_feedback(touch_ratio). If touch_ratio 0.0-0.5, function will print "Vibrating once...". If 0.5-2.0, print "Vibrating twice". If > 2.0, print "Vibrating thrice..."
# touch_ratio = strength / duration
# register_touch(touch_type,direction,duration,strength), check for type of touch
from touchTypes import TouchType, SwipeDirection

SINGLE_TOUCH = TouchType.SINGLE_TOUCH
DOUBLE_TAP = TouchType.DOUBLE_TAP
SWIPE = TouchType.SWIPE
HOLD = TouchType.HOLD
UP = SwipeDirection.UP
DOWN = SwipeDirection.DOWN
LEFT = SwipeDirection.LEFT
RIGHT = SwipeDirection.RIGHT
NO_DIRECTION = SwipeDirection.NO_DIR

def get_touch():
  strength = 0.1
  duration = 0.1
  direction = NO_DIRECTION
  touch = input("What type of touch did the user preform? [single/double/swipe/hold] ")
  if touch == "swipe":
    touch_type = SWIPE
    direction_way = input("In what direction did the user swipe? ")
    if direction_way == "up":
      direction = UP
    else:
      direction = DOWN
  elif touch == "hold":
    touch_type = HOLD
    duration = int(input("For how long did the user hold the touch? "))
  elif touch == "single":
    touch_type = SINGLE_TOUCH
  elif touch == "double":
    touch_type = DOUBLE_TAP
  strength = float(input("How strong was the user's touch? [0.0 to 1.0] "))

  register_touch(touch_type, direction, duration, strength)

def give_haptic_feedback(touch_ratio):
  if touch_ratio > 0.0 and touch_ratio < 0.5:
    print("Vibrating once...")
  elif touch_ratio >= 0.5 and touch_ratio <= 2.0:
    print("Vibrating twice...")
  elif touch_ratio > 2.0:
    print("Vibrating thrice...")

def register_touch(touch_type, direction, duration, strength):
 if touch_type == SINGLE_TOUCH:
   print("Registering single touch...")
 elif touch_type == DOUBLE_TAP:
   print("Registering double touch...")
 elif touch_type == SWIPE:
   print("Registering swipe...")
   if direction == UP:
     print("Exiting app...")
   elif direction == LEFT or direction == RIGHT:
     print("Changing page...")
   elif direction == DOWN:
     print("Scrolling up...")
 elif touch_type == HOLD:
   print("Registering hold...")
   touch_ratio = strength / duration
   give_haptic_feedback(touch_ratio)





def main():
  get_touch()

main()