#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Une LED branchée à la pin 18 clignote
import sys

import RPi.GPIO as GPIO
# bibliothèque pour utiliser les GPIO
import time # bibliothèque pour gestion du temps

from programs.pin_mapping import pin_mapping

pins = pin_mapping[sys.argv[1]]
interupt = pins['INTERUPT']
down = pins['DOWN']
up = pins['UP']
action = pin_mapping[sys.argv[2]]

GPIO.setmode(GPIO.BCM)
# mode de numérotation des pins
GPIO.setup(interupt, GPIO.OUT)
GPIO.setup(down, GPIO.OUT)
GPIO.setup(up, GPIO.OUT)

GPIO.output(interupt, GPIO.HIGH)

if action == 'DOWN':
    GPIO.output(up, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(down, GPIO.HIGH)
elif action == 'UP':
    GPIO.output(up, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(down, GPIO.HIGH)
else:
    GPIO.output(up, GPIO.LOW)
    time.sleep(0.2)
    GPIO.output(down, GPIO.LOW)

time.sleep(15)
GPIO.cleanup()