class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")    

point1 = Point()
point1.draw()     

point2 = Point()
point1.x = 10
point1.y = 20
point2.x = 1
print(point2.x)