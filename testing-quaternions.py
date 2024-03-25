#!/usr/bin/env python
from Quaternion    import *
import cmath as cmath

print I,J,K
print I*2

print "1*I",I*1
print "I*I",I*I
print "J*J",J*J
print "K*K",K*K
print "I*J",I*J
print "J*I",J*I
print "I*K",I*K
print "K*I",K*I
print "J*K",J*K
print "K*J",K*J
print "I*J*K",I*J*K

print ""

a = Quaternion(1,1,1,2)
b = Quaternion(3,2,0,-2)
print "A*B=",a*b
print "B*A=",b*a
print "abs(A)",abs(a)
print "A.v()",a.v()
C = complex(1,3)
print "C.polar",cmath.polar (complex(1,1) )
print "C.phase",cmath.phase( complex(1,1) )
print "C.real",C.real 
print "C.real",C.imag 
print ""
a = Quaternion(0,1,2,1)
print "A",a
print "B",b
print "A/4",a/4
print "A.v=", a.v()
print "A.n=", a.n()
print "A.conj=", a.conj()
print "A*A.conj=", a*a.conj()
print "A{-1}=", a.inv()
print "A*A^{-1}", a*a.inv()
print "a^{-1}",a.inv()
print "A.n()", a.n()
print "A.phase",phase ( a )/math.pi
print "A.polar",polar ( a )
print "exp(A)",exp(a)
print "A*exp(n*v)",abs(a)*exp(a.n()*phase(a) )  # this should be equal to a
print "log(J)",log(J)
print "exp(J)",exp(J)
print "J**3",J**3
print "K**3",K**(-3) ,"(K^-1 =",K**(-1),")"
print "(I+J)**2=", (I+J)**2
print "(I+J)**-2=", (I+J)**(-2)
print "A**3",a**3
print "A**-3",a**(-3)
print "A**3 * A**(-3)", a**3 * a**(-3), '==',1
print "A**0.5", a**0.5
print "sqrt(A)", sqrt(a)
print "A*A",a*a
print "-A*Conj(A)",-a*a.conj()
print "n^2", a.n()**2
print "q^2/|q|^2=", a*a ,"/",abs(a)**2, "=", a*a/abs(a)**2

## ROTATIONS ##
theta = math.pi/2
axis = I
axis = axis/abs(axis)
U = math.cos(theta/2.0) + axis*math.sin(theta/2.0)
print "U=",U,"Phase=",U.phase()/math.pi*180,"  U^2=",U*U
a = Quaternion(0 ,-1,1,3)
b = Quaternion(0,3,1,4)
c = Quaternion(0,3,9,4)
print "a=",a
print "b=",b
print "c=",c
print "2*Cross(a, b)=",2*Cross(a,b), "  =  ", "Conmutator [a,b]=",a*b-b*a
print "Dot(a,b)=",Dot(a,b)
print "a x (bxc)=",Cross(a, Cross(b,c)  )
print "(a.c)b -(a.b)c =",Dot(a,c)*b - Dot(a,b)*c
print "Rotate(pi,K)I (pi rad around K axis)s", K*I*K.inv()
Q = I+J
axis = K
print "Rotate(I+J, K,pi/2)", Rotate(Q,axis, math.pi/4)
z = Quaternion(8,-1,-3,1)
q = Q.v()
print "z q z^{-1}", z*q*z.inv()
print "u q u^{-1}", (z/abs(z)) * q * (z/abs(z))**(-1)
print "Rotate(q, n,theta)", Rotate(q, z.n(), z.phase()) 

print "zQz^{-1}= ",z*Q*z**(-1)
print "a+q'= ", Q.a + Rotate(Q.v() , z.n(), z.phase() )
print "Conj(a*b)", (a*b).conj()
print "Conj(b)*Conj(a)", b.conj()*a.conj()
print "Conj(a)*Conj(b)", a.conj()*b.conj()
print "Cross(a,b)=      ", Cross(a,b)
print "Conj(Cross(a,b))=", Cross(a,b).conj()

## PERFORMANCE ##
#for i in range(int(1e6)):
# c = z.inv()
#print c
