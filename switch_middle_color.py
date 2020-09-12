#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Une LED branchée à la pin 18 clignote 
import RPi.GPIO as GPIO 
# bibliothèque pour utiliser les GPIO 
import time # bibliothèque pour gestion du temps 
pin1=17
pin2=4
GPIO.setmode(GPIO.BCM) 
# mode de numérotation des pins 
GPIO.setup(pin1,GPIO.OUT) 
GPIO.setup(pin2,GPIO.OUT)

if GPIO.input(pin1) == 1 :
  GPIO.output(pin1,GPIO.LOW)
  time.sleep(0.5)
  GPIO.output(pin2,GPIO.HIGH)
else:
  GPIO.output(pin2,GPIO.LOW)
  time.sleep(0.5)
  GPIO.output(pin1,GPIO.HIGH)