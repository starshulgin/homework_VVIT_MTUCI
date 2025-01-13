class Circle:
    def __init__(self,radius):
        self.radius = radius

    def get_radius(self, radius):
        return radius

    def set_radius(self):
        new_radius = int(input("Enter new radius:"))
        self.radius = new_radius
        print(self.radius)

circlePrint = Circle(3.14)
circlePrint.set_radius()
