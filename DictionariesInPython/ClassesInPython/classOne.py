class Point:
    def __init__(self,x,y):
        self.xCoord=x
        self.yCoord=y


    def getX(self):
        return self.xCoord

    def getY(self):
        return self.yCoord


pointA=Point(3,4)
pointB=Point(0,0)

x=pointA.getX()
y=pointB.getY

print("(" + str(x) + ", "str(y) + ")")