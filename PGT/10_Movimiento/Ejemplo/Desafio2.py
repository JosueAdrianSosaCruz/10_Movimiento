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


# Create your objects here.
ev3 = EV3Brick()



# Motores en puertos C y D, ajusta dirección si es necesario
mC = Motor(Port.C)
mD = Motor(Port.D)  # Invierte este si sigue avanzando

ev3.speaker.beep()

# Giro 1: girar a la derecha
mC.run(300)
mD.run(-300)
wait(1500)
mC.brake()
mD.brake()
wait(500)

# Giro 2: girar a la izquierda
mC.run(-300)
mD.run(300)
wait(1500)
mC.brake()
mD.brake()
wait(500)

# Giro 3: giro rápido a la derecha
mC.run(500)
mD.run(-500)
wait(1000)
mC.brake()
mD.brake()