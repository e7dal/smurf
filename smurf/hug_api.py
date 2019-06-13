from itertools import cycle
import hug
import smurf
from smurf.docopt_cli import ri
#123456789012345678901234567890123456789012 #
class Smurf():                              #
 def __init__(i,n):                         # 
  i.n=n                                     #
  i.ml=[]                                   #
 def pcs(i,s,t=0.2):                        #
  i.ml.append(s)                            #
#123456789012345678901234567890123456789012 #
_examples="_f=hello&_t=world"               #
@hug.get('/smurf', examples=_examples)      #
def get_smurf(_f:hug.types.text,            #
              _t:hug.types.text):           #
 '''get a smurf, a morfing string'''        #
 sm=Smurf('smurf')                          #
 print("from=%s&to=%s"%(_f,_t))             #
 r=smurf.docopt_cli.m(_f,_t,0,C=sm.pcs)     #
 return sm.ml                               #
#123456789012345678901234567890123456789012 #
_examples="_f=hello&_t=world"               #
@hug.get('/circle', examples=_examples)     #
def get_circle(_f:hug.types.text,           #
               _t:hug.types.text):          #
 '''get a smurf, a morfing string'''        #
 sm1=Smurf('smurf1')                        #
 sm2=Smurf('smurf2')                        #
 print("from=%s&to=%s"%(_f,_t))             #
 r=smurf.docopt_cli.m(_f,_t,0,C=sm1.pcs)    #
 r=smurf.docopt_cli.m(_t,_f,0,C=sm2.pcs)    #
 return sm1.ml+sm2.ml                       #
#123456789012345678901234567890123456789012 #
@hug.get('/cycle', examples=_examples)      #
def get_cycle(_f:hug.types.text,            #
              _t:hug.types.text):           #
 '''get a smurf, a morfing string'''        #
 global ml                                  #
 ml=[]                                      #
 sm=Smurf('smurf')                          #
 print("from=%s&to=%s"%(_f,_t))             #
 r=smurf.docopt_cli.m(_f,_t,sm.pcs)         #
 r=smurf.docopt_cli.m(_t,_f,_d)             #
 #res=r+r[1:-1]                             #
 cres=cycle(ml)                             #
 for l in cres:                             #
  print('yielding',l)                       #
  yield l                                   #
  #BROKEN, fix this!drip?                   #
 #return ml                                 #
#123456789012345678901234567890123456789012 #
v={}                                        #
_examples="_i=42"                           #
@hug.get('/get', examples=_examples  )      #
def get_random(_i:hug.types.text):          #
 '''get a random string from a smurf'''     #
 global ml                                  #
 global v                                   #
 if _i not in v:                            #
  tg='merhaba dünya:)'                      #
  eg='hello world:)'                        #
  sm=Smurf('greet')                         #
  r=smurf.docopt_cli.m(tg,eg,0,C=sm.pcs)    #
  v[_i]=sm.ml                               #
 ml=v[_i]                                   #
 r=ri(1,len(ml)-1)                          #
 rs=ml[r]                                   #
 print("id=%s"%(_i))                        #
 print("r=%d"%(r))                          #
 print("rs=%s"%(rs))                        #
 return rs                                  #
#123456789012345678901234567890123456789012 #
