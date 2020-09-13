#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
LOOK LIKE PUSH BUTTON
"""
import sys

import RPi.GPIO as GPIO
# bibliothèque pour utiliser les GPIO 
import time # bibliothèque pour gestion du temps

from programs.pin_mapping import pin_mapping

pin = pin_mapping[sys.argv[1]]

# mode de numérotation des pins
GPIO.setmode(GPIO.BCM)

GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, GPIO.HIGH)
time.sleep(0.2)
GPIO.output(pin, GPIO.LOW)
GPIO.cleanup()
