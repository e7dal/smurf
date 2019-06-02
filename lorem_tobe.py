import random
import time
import docopt_cli as smurf
smurf
m=smurf.m
 
t=0.05
#m('merhaba dünya:)','hello world:)',0.2)
lorem="""Lorem ipsum dolor sit amet, consectetur adipiscing elit,..."""
tobe="""To be, or not to be, that is the question"""

while True:
 m(lorem,tobe,t)
 time.sleep(0.5)
 m(tobe,lorem,t)
 time.sleep(0.5)
