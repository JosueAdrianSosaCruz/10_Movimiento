#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.Add commentMore actions
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.beep()

mA = Motor(Port.A)
mB = Motor(Port.B)

mA.run(-300)
mB.run(-300)
wait(2050)

mA.run(300)
mB.run(300)
wait(2050)
mA.brake()
mB.brake()