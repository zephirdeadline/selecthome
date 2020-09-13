#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# Une LED branchée à la pin 18 clignote
import sys

import RPi.GPIO as GPIO
# bibliothèque pour utiliser les GPIO
import time # bibliothèque pour gestion du temps

from programs.pin_mapping import pin_mapping

pin = pin_mapping[sys.argv[1]]
GPIO.setmode(GPIO.BCM)
# mode de numérotation des pins
GPIO.setup(pin, GPIO.OUT)

if GPIO.input(pin) == 1:
    GPIO.output(pin, GPIO.LOW)
else:
    GPIO.output(pin, GPIO.HIGH)
