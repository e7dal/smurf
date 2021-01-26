import random
import time
from smurf.docopt_cli import m

import time
import signal
import sys

def signal_handler(sig, frame):
 print('thanks for watching!Bye:)')
 sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


t=0.1
FROM=open("from.txt","r").read()
TO=open("to.txt","r").read()

def ps(s,v,t=1.42):
    print("~"*42)
    print(s,v)
    print("~"*42)
    time.sleep(t)

ps("string morfing","back and forth ad infinitum")
ps("FROM\n",FROM)
ps("TO:\n",TO)
ps("DELAY:",t)
print('Are you ready for this')
print('Press Ctrl+C to stop...')
for i in range(3,0,-1):
 ps('starting in :',f'{i} seconds',1.0)

while True:
 m(FROM,TO,t)
 time.sleep(1.5)
 m(TO,FROM,t)
 time.sleep(1.5)
