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
import flbVector


class FlbAsterBeam():
    """
    This is a class used by flbBeam object
    its purpose is to have all data/methods used for mechanical computation
    in a distinct block for the convenience of programming
    """
    
    def __init__(self, beam):
        self.beam=beam
        self.listPoints=[[0., "ORI", 1], [beam.getLength(), "END", 1]]
        self.dicPoints={"ORI":0,  "END":1}
        
        self.listNodesGroups=[]
        self.listGroups=[]
        self.listMultipleGroups=[]
        
    def __repr__(self):
        """
        representation of a beam with print python function
        
        """
        rep= "FlbAsterBeam \n"
        rep= rep + self.beam.__repr__()

        return rep
        
        
    def addPoint(self, x, name="P", div=1):
        """
        x= abscisse of new point (can be <0 or > length of initial beam)
        name= name of the point (if already taken, automaticly incremented)
        div= number of division of element at the rigth for meshing
        """
        newList=[]
        n=len(self.listPoints)
        
        if self.dicPoints.has_key(name):
            name=name + "%i" %n
        
        if x < self.listPoints[0][0]:
            newList.append([x, name, div])
            newList.extend(self.listPoints)
            for item in self.dicPoints.items():
                print item[1]
                self.dicPoints[item[0]]=item[1]+1
            self.dicPoints[name]=0
        elif x>self.listPoints[n-1][0]:
            newList=self.listPoints
            self.listPoints.append([x, name, div])
            self.dicPoints[name]=n
        else:
            j=0
            for i in range(n-1):
                
                p1=self.listPoints[i]
                newList.append(p1)
                j=j+1
                self.dicPoints[p1[1]]=i
                p2=self.listPoints[i+1]
                
                if x>p1[0] and x<p2[0]:
                    newList.append([x, name, div])
                    self.dicPoints[name]=j
                    j=j+1
            newList.append(p2)
            self.dicPoints[p2[1]]=j 
        
        
        self.listPoints=newList
        return self
    
    
    
    def makeGroup(self, p1="ORI",  p2="END"):
        """
        a groupe is an interval between two points
        when meshing, a group of points and a group of elements is created
        """
        self.listGroups.append([p1, p2])
        return self
    
    def makeNodesGroup(self, list=[]):
        """
        makes a group of nodes
        
        """
        self.listNodesGroups.extend(list)
        return self
    
    
    def getOrigin(self):
        return self.beam.getOrigin()
    def getVx(self):
        return self.beam.vx
    def getVy(self):
        return self.beam.vy
    def getVz(self):
        return self.beam.vz
            
            
