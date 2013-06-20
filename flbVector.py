# -*- coding: utf-8 -*- 
##    This file is part of fablab-bois
##    see: www.
##    written by Gerard Nespoulous
##     contact: ggclarinette@gmail.com
##    
##   
##
##   FLB free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    FLB is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with FLB.  If not, see <http://www.gnu.org/licenses/>.


from math import radians, cos, sin, sqrt



def OShGlobalCoord(
    p,
    origin,
    vx,vy,vz
        ):
    return [ 
            origin[0]+p[0]*vx[0]+p[1]*vy[0]+p[2]*vz[0] , 
            origin[1]+p[0]*vx[1]+p[1]*vy[1]+p[2]*vz[1] , 
            origin[2]+p[0]*vx[2]+p[1]*vy[2]+p[2]*vz[2] , 
            ]
    
def OShLocalCoord(
                  p, 
                  origin, 
                  vx, vy, vz
                  ):
    M=[
       vx, 
       vy, 
       vz
       ]
    inv=invmat(M)
    p1=[
        p[0]-origin[0], 
        p[1]-origin[1],
        p[2]-origin[2],        
        ]
    i0=inv[0]
    i1=inv[1]
    i2=inv[2]
    return [
            p1[0]*i0[0]+p1[1]*i1[0]+p1[2]*i2[0], 
            p1[0]*i0[1]+p1[1]*i1[1]+p1[2]*i2[1], 
            p1[0]*i0[2]+p1[1]*i1[2]+p1[2]*i2[2]
            ]
            
def OShRotateAxis(
                  angle, v, 
                  vx, vy, vz
                  ):
    """
    angle in degrees
    v=3D vector, or 0,1,2 (for x,y,z axis)
    vx vy vz should be a orthonormal basis
    """
    M1=[
        vx, 
        vy, 
        vz
        ]
    Mrot=rotationMatrix(angle, v)
    
    M2=Multmat(Mrot, M1)
    return M2
            
#### OPERATIONS SUR VECTEURS 

def OShDot(v1, v2):
    """
    produit scalaire
    """
    if len(v1)==3:
        return (v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2])
    else:
        return (v1[0]*v2[0]+v1[1]*v2[1])

def OShNorme(p):
    """
    retourne la norme d'un vecteur
    """
    
    return sqrt( OShDot(p, p))
    
def OShNvect(p):
    """
    retourne le vecteur normé basé sur p
    """
    v=[]
    if len(p)>3:
        p=[p[0], p[1], p[2]]
    N=OShNorme(p)
    for coord in p:
        v.append(coord/N)
        
    return v
    
def OShCross(v, w):
    """
    produit vectoriel
    cross product
Ux = Vy * Wz - Wy * Vz;
Uy = Vz * Wx - Wz * Vx;
Uz = Vx * Wy - Wx * Vy; 
    """
    u0=v[1]*w[2]-w[1]*v[2]
    u1=v[2]*w[0]-w[2]*v[0]
    u3=v[0]*w[1]-w[0]*v[1]
    return [u0, u1, u3]
    
def OShColinear(v1, v2):

    if OShNorme(OShCross(v1, v2))==0:
        return True
    return False
    
def OShSousVect(u, v):
    """
    soustract two vectors
    returns u-v
    """
    n=len(u)
    w=[]
    for i in range(n):
        w.append(u[i]-v[i])
    return w
    
def OShAddVect(u, v):
    """
    Add two vectors
    """
    n=len(u)
    w=[]
    for i in range(n):
        w.append(u[i]+v[i])
    return w

def OShMultVect(s, v):
    """
    s scalar
    v, vector
    """
    u=[]
    for coord in v:
        u.append(coord*s)
    return u

def OShVxVyVz(vx,vy=None,  vz=None):
    """
    Makes un orthonormal basis
    """
    VX=[1, 0, 0]
    VY=[0, 1, 0]
    VZ=[0, 0, 1]    
    if vz==None:
        if OShColinear(vx, VZ):
            v_x=OShNvect(vx)
            v_y=VY
            v_z=OShCross(v_x, v_y)
        else:
            v_x=OShNvect(vx) 
#            v_z=OShNvect( cross(v_x, VY)   )
            v_y=OShMultVect(-1, OShNvect( OShCross(v_x, VZ)   )  )   
            v_z=OShNvect( OShCross(v_x, v_y)   )            
    else:
            v_x=OShNvect(vx)
            v_y=OShNvect( OShCross(v_x, vz)   )    
            v_z=OShNvect( OShCross(v_x, v_y)   )
    return [v_x, v_y, v_z]
    
#### OPERATION SUR MATRICES
# C'est un ensemble de codes sources permettant d'effectuer les opérations matricielles, à savoir
# l'addtion, la multiplication, le déterminant, la comatrice, la transposée d'une matrice, l'inverse d'une matrice
#Extraire une ligne i et une colonne j d'une matrice. Notez q'une matrice a pour syntaxe:
# A=[[a, b],[c,d]], la matrice est représentée ligne par ligne donc A est équivalent à:   
# [a   b]
# [ c  d]




def rotationMatrix(angle,axis=None):
    """Return a rotation matrix over angle, optionally around axis.

    The angle is specified in degrees.
    If axis==None (default), axis=[0,0,1]
    Else, axis should specifying the rotation axis in a 3D world. It is either
    one of 0,1,2, specifying a global axis, or a vector with 3 components
    specifying an axis through the origin.
    In either case a 3x3 rotation matrix is returned.
    Note that:
      rotationMatrix(angle,[1,0,0]) == rotationMatrix(angle,0) 
      rotationMatrix(angle,[0,1,0]) == rotationMatrix(angle,1) 
      rotationMatrix(angle,[0,0,1]) == rotationMatrix(angle,2)
    but the latter functions calls are more efficient.
    The result is returned as an array.
    
## This function is inspired from of pyFormex 0.7.2 Release Tue Sep 23 16:18:43 2008
## pyFormex is a Python implementation of Formex algebra
## Website: http://pyformex.berlios.de/
## Copyright (C) Benedict Verhegghe (benedict.verhegghe@ugent.be) 
##
## This program is distributed under the GNU General Public License
## version 2 or later (see file COPYING for details)
    """
    a = radians(angle)
    c = cos(a)
    s = sin(a)
    if axis==None:
        axis=[0, 0, 1]
#        f = [[c,s],[-s,c]]
    if axis ==0:
        axis=[1, 0, 0]
    if axis==1:
        axis=[0, 1, 0]
    if axis==2:
        axis=[0, 0, 1]
#    if type(axis) == int:
#        f = [[0.0 for i in range(3)] for j in range(3)]
#        axes = list(range(3))
#        i,j,k = axes[axis:]+axes[:axis]
#        f[i][i] = 1.0
#        f[j][j] = c
#        f[j][k] = s
#        f[k][j] = -s
#        f[k][k] = c
#    else:
    t = 1-c
    X,Y,Z = axis
    f = [ [ t*X*X + c  , t*X*Y + s*Z, t*X*Z - s*Y ],
          [ t*Y*X - s*Z, t*Y*Y + c  , t*Y*Z + s*X ],
          [ t*Z*X + s*Y, t*Z*Y - s*X, t*Z*Z + c   ] ]
        
    return f





def Extrtlincol(m,n,M):
      "retourne la matrice A sans la m ième ligne et la n ième colonne"
      Mlin=len(M)
      result=[]
      Rep=[]
      for i in range(Mlin):
            if i!=m:
                  for j in range(Mlin):
                        if (j!=n):
                              result.append(M[i][j])
      for k in range(0,len (result),Mlin-1):
            Rep.append(result[k:k+Mlin-1])
      return Rep
##################################################
def Det(A):
      " retourne le déterminat de la matrice A"
      if len(A)==1:
            return A[0][0]
      if len(A)==2:
            r=A[0][0]*A[1][1]-A[0][1]*A[1][0]
            return r
      else:
            s=0
            j=0
            while j<len(A):
                  B=Extrtlincol(j,0,A)
                  if j%2==0:
                        s=s+A[j][0]*Det(B)
                  else:
                        s=s-A[j][0]*Det(B)
                  j=j+1
            return s
######################################################                  
def  comat(A):
      "Donne la comatrice d'une matrice A"
      N=len (A)
      k=0
      com=[None]*N
      while k<N:
            com[k]=[0]*N
            l=0
            while l<N:
                  B=Extrtlincol(k,l,A)
                  if (k+l)%2==0:
                        com[k][l]=(Det(B))
                  else:
                        com[k][l]=((-1)*Det(B))
                  l=l+1
            k=k+1
      return com
###################################################
def transpos(A):
      "Donne la transposée d'une matrice A"
      N=len(A)
      M=[None]*N
      for i in range(N):
            M[i]=[0]*N
            for j in range(N):
                  M[i][j]=A[j][i]
      return M
#####################################################
def multcoef(A,r):
      "Donne le produit d'une matrice A par le coefficient r"
      N=len(A)
      Mat=[None]*N
      for i in range(N):
            Mat[i]=[0]*N
            for j in range(N):
                  Mat[i][j]=r*A[i][j]
      return Mat
######################################################                  
      
def invmat(A):
      "Donne l'inverse d'une matrice carrée  A"
      d=Det(A)
      if d==0:
          # pas inversible
            return None
      else:
            B=multcoef(comat(A),1./d)
            inv=transpos(B)
      return inv
###############################################################      
def Multmat( Mat1,Mat2):
      "Donne le produit de deux matrices"
      Mat1lign,Mat1col= len (Mat1), len (Mat1[0])
      Mat2lign,Mat2col= len (Mat2), len (Mat2[0])
      A=[]
      M=[None]*Mat1lign
      if  Mat1col!=Mat2lign:
            print(" Erreur!  Votre première matrice à un nombre de colonne\ n inferieur à celle de la seconde matrice")
      for  i in  range(Mat1lign):
            M[i]=[0]*Mat2col
            for j in range(Mat2col):
                  for k in range(Mat1col):
                        M[i][j]=M[i][j]+Mat1[i][k]*Mat2[k][j]
##      for m in range(Mat1lign):
##            print(M[m])
      return M
####################################################
def Addmat(M1,M2):
      "Additionne deux matrices carrées"
      N=len(M1)
      M=[None]*N
      for i in range (N):
            M[i]=[0]*N
            for j in range (N):
                  M[i][j]=M1[i][j]+M2[i][j]
      return M
      
      
      
###################
# operation sur des listes de points

def OShBarycentre(listPoints, listMass=None):
    """
    """
    G=[0, 0, 0]
    i=0
    totalMass=0
    for point in listPoints:
        if listMass:
            mass=listMass[i]
        else:
            mass=1
        if i==0:
            G=[point[0]*mass, 
               point[1]*mass, 
               point[2]*mass]
        else:
            G=[
               G[0]+point[0]*mass, 
               G[1]+point[1]*mass, 
                G[2]+point[2]*mass
                ]
        totalMass=totalMass+mass
        i=i+1
    G=[
           G[0]/totalMass, 
           G[1]/totalMass, 
            G[2]/totalMass
       ]
    return G
    
    
    
