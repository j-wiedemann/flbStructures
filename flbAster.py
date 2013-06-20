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




        
def FlbWriteAsterNodes(model):
    m="% mesh by FlbAsterMesh \n"
    name=model.name
    m=m +"% modele : " +name +" \n"
    m=m+ "COOR_3D \n"
    i=0
    for node in model.listNodes:
        print node

        m=m+ "M%i  %f %f %f \n" %(i, node[0], node[1],  node[2])
        i=i+1
    m=m+"FINSF \n"
    return m
            
def FlbWriteAsterElem(model):
    m="% mesh by FlbAsterMesh \n"
    name=model.name
    m=m +"% modele : " +name +" \n"
    m=m+ "SEG2 \n"
    i=0
    for elem in model.listElems:
        

        m=m+ "S%i  M%i M%i  \n" %(i, elem[0], elem[1])
        i=i+1
    m=m+"FINSF \n"
    return m
            
            
            
            
