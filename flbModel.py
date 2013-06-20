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


class FlbModel():
    """
    fem model for beam structure
    """
    
    def __init__(self,name="model"):
        self.name=name
        self.beamList=[]
        self.beamDic={}
    
        self.linkList=[]
        self.Dic={}
        self.Nbeam=0
        
        self.listNodes=[]
        self.dicNodes={}
        
        self.listElems=[]
        
        self.listNodesGroups=[]
        self.listGroups=[]
        self.listMultipleGroups=[]
        
        
    def addBeam(self, beam):
        self.Nbeam=self.Nbeam+1
        self.beamList.append(beam)
        beam.num=self.Nbeam
        
        
    def makeMesh(self):
        
        n=0
        for beam in self.beamList:
            print beam.beam.name
            i=0
            k=0
            np=len(beam.listPoints)
            listNodes=[]
            for point in beam.listPoints:
               
                localCoord=[point[0], 0, 0]
                pointName=point[1]
                print point
                globalCoord=flbVector.OShGlobalCoord(localCoord, beam.getOrigin(), beam.getVx(), beam.getVy(), beam.getVz())
                print globalCoord
                self.listNodes.append(globalCoord)
                listNodes.append(n)
                i=i+1
                n=n+1
                
                div=point[2]
                if i<np and div>0:
                    point2=beam.listPoints[i]
                    for j in range(div):
                        localCoord=[point[0]+(j+1)*(point2[0]-point[0])/(div+1), 0, 0]
                        globalCoord=flbVector.OShGlobalCoord(localCoord, beam.getOrigin(), beam.getVx(), beam.getVy(), beam.getVz())
                        print globalCoord
                        self.listNodes.append(globalCoord)
                        listNodes.append(n)
                        n=n+1
            for j in range(len(listNodes)):
                if j>0:
                    self.listElems.append([listNodes[j-1],listNodes[j] ])
    
        return
        
        
        
