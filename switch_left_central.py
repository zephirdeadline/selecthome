#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# Une LED branchée à la pin 18 clignote 
import RPi.GPIO as GPIO 
# bibliothèque pour utiliser les GPIO 
import time # bibliothèque pour gestion du temps 
pin=26
power=GPIO.LOW
GPIO.setmode(GPIO.BCM) 
# mode de numérotation des pins 
GPIO.setup(pin,GPIO.OUT) 
GPIO.output(pin,GPIO.HIGH) 
time.sleep(0.2)
GPIO.output(pin,GPIO.LOW) 
GPIO.cleanup()