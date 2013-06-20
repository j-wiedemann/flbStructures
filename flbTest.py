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
import flbBeam
import flbModel
import flbAsterBeam
import flbAster

if __name__=="__main__":   
    print("coucou")
    monModele=flbModel.FlbModel()
    
    
    mapoutre=flbBeam.FlbBeam()
    mapoutre.setOrigin([0, 0, 0])
    mapoutre.setVx([1, 0, 0])
    print(mapoutre)
    
    
    print("###############")
    ab=flbAsterBeam.FlbAsterBeam(mapoutre)
    
    poutre2=flbBeam.FlbBeam().setName("gaga")
    ab2=flbAsterBeam.FlbAsterBeam(poutre2)
    print(ab)
    monModele.addBeam(ab)
    monModele.addBeam(ab2)



    ab.addPoint(0.5, "P", 2)

    for p in ab.listPoints:
        print(p,  ab.dicPoints[p[1]])
    monModele.makeMesh()
    
    print flbAster.FlbWriteAsterNodes(monModele)
    print flbAster.FlbWriteAsterElem(monModele)
