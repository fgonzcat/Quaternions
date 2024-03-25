#!/usr/bin/env python
import math

class Quaternion:

 def __init__(self, a=0,b=0,c=0,d=0):
  self.a = a
  self.b = b
  self.c = c
  self.d = d
 #def __call__(self): return "Quaternion"

 def __add__(self, o):
  if isinstance(o, int) or isinstance(o, float): o = Quaternion(o)
  return  Quaternion( self.a + o.a, self.b + o.b, self.c + o.c, self.d + o.d  )
 def __radd__(self,o):     return self.__add__(o)

 def __sub__(self, o):
  if isinstance(o, int) or isinstance(o, float): o = Quaternion(o)
  return Quaternion( self.a - o.a, self.b - o.b, self.c - o.c, self.d - o.d  )

 def __neg__(self): return -1.0*self

 # Quaternion multiplication
 # x | 1   i    j    k
 #---------------------
 # 1 | 1   i    j    k
 # i | i  -1    k   -j
 # j | j  -k   -1    i 
 # k | k   j   -i   -1
 def __mul__(self,f):
  if isinstance(f, int) or isinstance(f, float):
   s = Quaternion( f*self.a, f*self.b, f*self.c, f*self.d)
  elif isinstance(f, Quaternion):
   a1 = self.a;   a2 = f.a
   b1 = self.b;   b2 = f.b
   c1 = self.c;   c2 = f.c
   d1 = self.d;   d2 = f.d
   sA= a1*a2-b1*b2-c1*c2-d1*d2
   sB= a1*b2+b1*a2+c1*d2-d1*c2
   sC= a1*c2-b1*d2+c1*a2+d1*b2
   sD= a1*d2+b1*c2-c1*b2+d1*a2
   s = Quaternion(sA, sB, sC, sD)
  return s
 def __rmul__(self,f):
  if isinstance(f, int) or isinstance(f, float): return self*f

 def __div__(self,f):
  if isinstance(f, int) or isinstance(f, float):
   f = (1.0/f)
   return self*f

 def __abs__(self):
  return math.sqrt(self.a*self.a + self.b*self.b + self.c*self.c + self.d*self.d)

 def __pow__(self,x):
  if isinstance(x, int):
   if x==0: return 1.0 + 0*I
   elif x>0:
    q = self
    for j in range(1,x):    q = self*q
    return q 
   elif x<0:
    return self.inv()**(-x)
  elif isinstance(x, float):
    phi =  self.phase()
    exp_nxp = math.cos(x*phi)  + self.n() *math.sin(x*phi)
    return math.exp(self.a)*exp_nxp


 def __str__(self):
  st = ""
  if abs(self.a)<1e-15: self.a = 0.0

  if self.a!=0: st += str(self.a)
  if self.b!=0:
   if self.a!=0: st+='+'
   st += str(self.b)+'i'
  if self.c!=0:
   if self.a!=0 or self.b!=0: st+='+'
   st += str(self.c)+'j'
  if self.d!=0:
   if self.a!=0 or self.b!=0 or self.c!=0: st+='+'
   st += str(self.d)+'k'
  if self.a==0 and self.b==0 and self.c==0 and self.d==0: st += '0' 
  return st 
  #return '(%s+%si+%sj+%sk)' % (self.a, self.b, self.c, self.d)

 def v(self):
  # z = a + ib + cj + dk = a + v
  return Quaternion( 0.0, self.b, self.c, self.d)
 def n(self):
  return self.v()/abs(self.v()) 
 def conj(self):
  return Quaternion( self.a, -self.b, -self.c, -self.d)
 def inv(self):
  mod2inv = 1.0/(self.a*self.a + self.b*self.b + self.c*self.c + self.d*self.d)
  return self.conj()*mod2inv
 def phase(self):
  return 2.0*math.acos(self.a/abs(self))   # cos(O/2)= a/|z| to match rotations in O 
  
 
I = Quaternion(0,1,0,0)
J = Quaternion(0,0,1,0)
K = Quaternion(0,0,0,1)

def phase(Q): return Q.phase()

def polar(Q):  # README: https://math.stackexchange.com/questions/1496308/how-can-i-express-a-quaternion-in-polar-form
 '''
 z = a + ib + cj + dk = a + V = |z| ( a/|z| +  V/|z| )
 |z|^2 = a^2 + |V|^2  ==>    (a/|z|)^2 + ( |V|/|z| )^2 = 1 
                             cos(O)^2 +  sin(O)^2     = 1  for some angle O such that.
                             cos(O)= a/|z|  ;   sin(O) = |V|/|z|

          Then z = a + V  =  |z| [ cos(O) + n sin(O) ]  = |z| exp( n O)
 '''
 return abs(Q),phase(Q)


def exp(Q):
 if isinstance(Q, type(I)): 
  # z = a + ib + cj + dk = a + V 
  if abs(Q)==0.0: return 1.0
  V =  abs(Q.v())
  expV = math.cos(V)  + Q.n() *math.sin(V)
  return exp(Q.a)*expV
 else:
  return math.exp(Q)

def log(Q):
 if isinstance(Q, type(I)): 
  # z = |z| exp( n O) 
  return log(abs(Q))  + Q.n()*phase(Q) 
 else:
  return math.log(Q)


def sqrt(Q):
 if isinstance(Q, type(I)): 
  # z = |z| exp( n O) 
  return Q**0.5
 else:
  return math.sqrt(Q)

def Cross(Q1, Q2):
 # For simplicity, we define Q1xQ2 = V1xV2  (ignore real part of quaterion to define Cross product) 
 if isinstance(Q1, type(I)) and isinstance(Q2, type(I)):
  b1,c1,d1 = Q1.b,Q1.c,Q1.d
  b2,c2,d2 = Q2.b,Q2.c,Q2.d
  V1xV2= Quaternion(0.0, c1*d2-d1*c2, -b1*d2+d1*b2, b1*c2-c1*b2 )
  return V1xV2  # Shold be equal to [Q1,Q2]/2 , but this is more efficient 

def Dot(Q1,Q2):
 # For simplicity, Q1xQ2 = V1xV2  (ignore real part of quaterion to define Cross product) 
 if isinstance(Q1, type(I)) and isinstance(Q2, type(I)):
  return Q1.b*Q2.b + Q1.c*Q2.c + Q1.d*Q2.d

def Rotate(Q,axis,phi):
 q = Q.v()
 n = axis.n()
 u = math.cos(phi/2.0) + n*math.sin(phi/2.0)
 return u*q*u.inv()
