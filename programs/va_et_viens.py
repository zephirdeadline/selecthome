#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Une LED branchée à la pin 18 clignote
import sys

import RPi.GPIO as GPIO
# bibliothèque pour utiliser les GPIO 
import time # bibliothèque pour gestion du temps

from programs.pin_mapping import pin_mapping

pins = pin_mapping[sys.argv[0]]
va = pins['VA']
viens = pins['VIENS']
time_to_wait = 0.5
GPIO.setmode(GPIO.BCM)
# mode de numérotation des pins 
GPIO.setup(va, GPIO.OUT)
GPIO.setup(viens, GPIO.OUT)


def switch_pin(to_open, to_close):
    GPIO.output(to_open, GPIO.LOW)
    time.sleep(time_to_wait)
    GPIO.output(to_close, GPIO.HIGH)


if GPIO.input(va) == 1 :
    switch_pin(va, viens)
else:
    switch_pin(viens, va)
