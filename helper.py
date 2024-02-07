import math

class Helper(object):
    def getAngledPoint(angle,longueur,cx,cy): # cx cy point depart
        x = (math.cos(angle)*longueur)+cx
        y = (math.sin(angle)*longueur)+cy
        return (x,y)
    getAngledPoint = staticmethod(getAngledPoint)
    
    def calcAngle(x1,y1,x2,y2): #angle en RADIAN ATTENTION!!!
         dx = x2-x1
         dy = y2-y1
         angle = (math.atan2(dy,dx) )
         return angle
    calcAngle = staticmethod(calcAngle)
    
    def calcDistance(x1,y1,x2,y2): # on se rapproche  si jsui rendu, nouvelle cible
         dx = (x2-x1)**2     # strip abs FAIT
         dy = (y2-y1)**2
         distance=math.sqrt(dx+dy)
         return distance
    calcDistance = staticmethod(calcDistance)

