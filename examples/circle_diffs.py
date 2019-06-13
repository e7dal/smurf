from itertools import cycle
import random
import sys
import requests
import leven


f="abcdefghijklmnopqrstuvwxyz"
t=f[::-1] #reverse
try:
    r=requests.get('http://0.0.0.0:8000/circle?_f=%s&_t=%s'%(f,t))
except:
    print('smurf hug api started?')
    print('try: hug -m smurf.hug_api')
    sys.exit(-1)

rj=r.json()

rjc=cycle(rj)
l=len(rj)
p=n=None
print('circle:edit distances should be 1')
while l:
    if not p:p=next(rjc)
    n=next(rjc)
    print(p,n,leven.levenshtein(p,n))
    p=n
    l-=1

print('random:edit distances should not be always 1')
l=len(rj)
p=n=None
random.shuffle(rj)
rjc=cycle(rj)
while l:
    if not p:p=next(rjc)
    n=next(rjc)
    print(p,n,leven.levenshtein(p,n))
    p=n
    l-=1

