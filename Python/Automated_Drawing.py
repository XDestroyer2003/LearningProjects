# when  run goto the paint or any drawing software for the mouse to start drawing

import numpy as np
import pyautogui as py
import time
thetha = np.linspace(0, 2 * np.pi, 100)
radius = 120
x = radius * np.cos(thetha)+500
y = radius * np.sin(thetha)+500
time.sleep(3)
for x1, y1 in zip(x, y):
    x_out = 60 * np.cos(thetha) + x1
    y_out = 60 * np.sin(thetha) + y1
    py.move(x1, y1)
    for x_in, y_in in zip(x_out, y_out):
        py.dragTo(x_in, y_in)
