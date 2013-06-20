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

import flbVector            # functions for geometrical calculation
import flbAsterBeam

class FlbBeam():
    """
    Structural beam
    """
    def __init__(self):
        self.name="poutre"
        self.setOrigin(0., 0., 0.)
        self.len=1.
        self.setVx()
        self.num=0
        self.setSection()
        
    def __repr__(self):
        """
        representation of a beam with print python function
        
        """
        print ("""
                    ________
                    |           |
                    |           |
                    |           |
                    L______ |
                    """)
        rep= "FlbBeam \n"
        rep= rep+self.getName() +"\n"
        rep=rep + "origine [%s , %s, %s] \n" %(self.getOrigin()[0], self.getOrigin()[1], self.getOrigin()[2] )
        rep=rep+ "Vx %s \n" %self.vx
        rep=rep+ "Vy %s \n" %self.vy
        rep=rep+ "Vz %s \n" %self.vz
        return rep
        
    def setName(self, ans="poutre"):
        """
        set the name of the beam
        """
        self.name=ans
        return self
    
    def getName(self):
        """
        returns the name of the beam
        """
        return self.name
        
    def setOrigin(self, x=[0, 0, 0], y=None, z=None ):
        """
        set the origin
        
        ex:
        mapoutre.setOrigin(x,y,z)
        or
        mapoutre.setOrigin([x,y,z])
        
        """
        if y==None:
            self.origin=x
        elif z==None:
            self.origin=[x, y, 0.]
        else:
            self.origin=[x, y, z]
        return self

    def getOrigin(self):
        """
        returns a python array [x,y,z]
        """
        return self.origin
        
    def setLength(self, l=1.):
        """
        Set the length of the beam
        """
        self.len=l
        return self
        
        
    def getLength(self):
        """
        return the length of the beam
        """
        return self.len
        
    def setSection(self, param=[0.1, 0.2],  type="rectangle"):
        """
        set the section of the beam
        only type="rectangle" (defaut)
        param=[b,h] (base , heigth)  = (y dim, z dim )
        """
        self.sectionType=type
        self.sectionParam=param
        return self
        
        
    def setVx(self,  V=[1, 0, 0]):
        """
        set the Vx axis
        longitudinal axe of the beam
        the Vz axis (dim H for rectangular beam)
        and Vy axis (dim B for rectangular beam)
        are calculated so that Vz is in Vx - global Z plane if possible
        
        """
        vxyz=flbVector.OShVxVyVz(vx=V,vy=None,  vz=None)
        self.vx=vxyz[0]
        self.vy=vxyz[1]
        self.vz=vxyz[2]
        return self
    def setVy(self,  V=[0, 0, 1]):
        self.yAxis=V
        return self       
        
        
        
    ####################################
    def setGLMatrix(self, matrix):
        """
        Matrix is a openGL like matrix:
        vx 0
        vy 0
        vz 0
        loc 1
        
        used in particular to import blender objects
        """
        
        self.setVx(matrix[0])
        self.setVy(matrix[1])
        self.setVz(matrix[2])
        self.setOrigin([matrix[3][0], matrix[3][1],matrix[3][2]])
        return self
        
        
    def getGLMatrix(self):
        m=[
           [self.vx()[0], self.vx()[1], self.vx()[2], 0], 
           [self.vy()[0], self.vy()[1], self.vy()[2], 0], 
           [self.vz()[0], self.vz()[1], self.vz()[2], 0],
           [self.origin()[0], self.origin()[1], self.origin()[2], 1],
           ]
        
        return m
    
        
