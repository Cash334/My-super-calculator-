#this is my supercalculator v4 first attempt. it's 2158 h right now,23rd dec 2025.
#my previous version v3, had 661 lines with very little functionality. now that ive mastered oop,i'm anticipating somewhere around 300 or less lines.
#let's have it

#2d_shape class which is abstract with all their values - perimeter(/circumference) and area(v5 which will be the final,will be able to calculate angles and unknown
      #dimensions for every form of the shapes ie. a scalene triangle and isosceless triangle. i will then include shapes like rhombus-es and parallelograms
from abc import ABC,abstractmethod
import math

class IIShape(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(IIShape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Triangle(IIShape):
    def __init__(self,base,height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def perimeter(self):
        hyp = math.sqrt((self.base**2) + (self.height**2))
        return self.base + self.height + hyp

class Square(IIShape):
    def __init__(self,length):
        super().__init__(length)

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return self.length * 4

class Rectangle(IIShape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.height

    def perimeter(self):
        return 2(self.length + self.height)

class Rhombus(IIShape):
    def __init__(self,length):
        self.length = length

    def area(self):
        return self.length ** 2

    def perimeter(self):
        return self.length * 4

class Paralellogram(IIShape):
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.height

    def perimeter(self):
        return 2*(self.length + self.height)

class Trapezium(IIShape):#i will assume one slant height
    def __init__(self,b_length,t_length,height):
        self.b_length = b_length
        self.t_length = t_length
        self.height = height

    def area(self):
        rec = self.b_length * self.height
        tri = 0
        tri_base = self.t_length - self.b_length
        tri_height = self.height
        tri += (1/2*(tri_base * tri_height))
        return tri

    def perimeter(Self):
        tri_base = self.t_length - self.b_length
        hyp = math.sqrt((self.height**2)+(tri_base**2))
        return self.t_length + self.b_length + self.height + hyp

class IIIShape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def surface_area(self):
        pass

    @abstractmethod
    def volume(self):
        pass

class Cylinder(IIIShape):
    def __init__(self,b_radius,height):
        self.b_radius = b_radius
        self.height = height

    def surface_area(self):
        return 3.14 * 2 * self.b_radius * self.height

    def volume(self):
        return 3.14 * (self.b_radius ** 2) * self.height

class Cube(IIIShape):
    def __init__(self,b_length):
        self.b_length = b_length

    def surface_area(self):
        return (2*(self.b_length * self.b_width)) + (2*(self.b_length * self.height)) + (2*(self.height * self.width))

    def volume(self):
        return self.b_length * self.b_width * height

class Cuboid(IIIShape):
    def __init__(self,b_length,b_width,height):
        self.b_length = b_length
        self.b_width = b_width
        self.height = height

    def surface_area(self):
        return (2*(self.b_length * self.b_width)) + (2*(self.b_length * self.height)) + (2*(self.height * self.width))

    def volume(self):
        return self.b_length * self.b_width * height

class Pyramid(IIIShape):
    def __init__(self,b_length,height):
        self.b_length = b_length
        self.height = height

    def surface_area(self):#i will assume a square base pyramid
        #to find the height of the faces, i need o find the half of the diagonal of the base to apply pythagora's theorem
        diagonal = math.sqrt(((self.b_length)**2)*2)
        hyp = math.sqrt((diagonal**2) + (self.height**2))
        face_area = 0.5 * self.b_length * hyp
        return ((4 * face_area) + (self.b_length ** 2))

    def volume(self):
        return (1/3 *(self.b_length * self.b_width))* height

class Sphere(IIIShape):
    def __init__(self,radius):
        self.radius = radius

    def surface_area(self):
        return 4*(3.14*(self.radius **2))

    def volume(self):
        return 4/3*(3.14*(self.radius**3))

class Cone(IIIShape):
    def __init__(self,b_radius,height):
        self.b_radius = b_radius
        self.height = height

    def surface_area(self):
        return 1/3*((self.b_radius*2) * 3.14) * self.height

    def volume(self):
        return 1/3*(3.14 *(self.b_radius ** 2)) * self.height

def calculator():
    #i reached this point at 2314h 
    print("welcome to the supercalculator v4")
    print("you may enter 'exit' at any point to exit the app")
    while True:
        try:
            shape_type = input("what type of shape do you wish to work woth today? 3d/2d:\n")
            if "exit" in shape_type:
                print("exiting...")
                break
            
            elif "2" in shape_type:
                try:
                    shape_name = input("what's the name of your shape?  ").lower()
                    if "exit" in shape_name:
                        print("exiting...")
                        break
                    
                    elif "tri" in shape_name:
                        base = int(input("enter base: "))
                        height = int(input("enter height: "))
                        tri = Triangle(base,height)
                        
                        try:
                            value = input("what value do you want?(area/perimeter): ").lower()
                            if "are" in value:
                                print(f"{tri.area()} cm2")

                            elif "per" in value:
                                print(f"{tri.perimeter()} cm")

                            else:
                                print("please check for typos in your answer")

                        except ValueError:
                            print("please enter the 'area' or 'perimeter'")

                    elif "cir" in shape_name:
                        radius = int(input("enter radius: "))
                        circ = Circle(radius)

                        try:
                            value = input("enter 'area' or 'circumference': ").lower()
                            if "are" in value:
                                print(f"{circ.area()} cm2")

                            elif "per" in value:
                                print(f"{circ.perimeter()} cm")

                            else:
                                print("please check for typos in your answer")

                        except ValueError:
                            print("please enter the 'area' or 'perimeter'")

                    elif "sq" in shape_name:
                        width = int(input("enter given side: "))
                        sq = Square(width)
                        try:
                            value = input("enter 'area' or 'perimeter': ").lower()
                            if "are" in value:
                                print(f"{sq.area()} cm2")

                            elif "peri" in value:
                                print(f"{sq.perimeter()} cm")

                            else:
                                print("please check for typos in your answer")

                        except ValueError:
                            print("please enter 'area' or 'perimeter'")

                    elif "rect" in shape_name:
                        width = int(input("enter width: "))
                        length = int(input("enter length: "))
                        rec = Rectangle(length,width)
                        try:
                            value = input("enter 'area' or 'perimeter': ").lower()
                            if "are" in value:
                                print(f"{rec.area()} cm2")

                            elif "peri" in value:
                                print(f"{rec.perimeter()} cm")

                            else:
                                print("please check for typos in your answer")

                        except ValueError:
                            print("please enter 'area' or 'perimeter'")
                    #took a break at 2335h, it was quite late for me. will resume tomorrow
                    #resumed on 24th dec(next day) 1700h
                    elif "rho" in shape_name:
                        length = int(input("enter given side: "))
                        rho = Rhombus(length)
                        try:
                            value = input("what value of the rhombus do you want?(area/perimeter): ").lower()
                            if "are" in value:
                                print(f"{rho.area()} cm2")

                            elif "peri" in value:
                                print(f"{rho.perimeter()}cm")

                            else:
                                print("please check for typos in your answer")

                        except ValueError:
                            print("enter 'area' or 'perimeter'")

                    elif "para" in shape_name:
                        length = int(input("enter lenght: "))
                        width = int(input("enter width: "))
                        para = Paralellogram(length,width)
                        try:
                            value = input("what value of the rhombus do you want?(area/perimeter): ").lower()
                            if "are" in value:
                                print(f"{para.area()}cm2")

                            elif "peri" in value:
                                print(f"{para.perimeter()}cm")

                            else:
                                print("please check for typos in your answer")

                        except ValueError:
                            print("please enter 'area' or 'perimeter'")

                    elif "trap" in shape_name:
                        t_length = int(input("enter shorter length: "))
                        b_length = int(input("enter longer length: "))
                        height = int(input("enter height(width): "))
                        trap = Trapezium(b_length,t_length,height)
                        try:
                            value = input("what value of the rhombus do you want?(area/perimeter): ").lower()
                            if "are" in value:
                                print(f"{trap.area()}cm2")

                            elif "peri" in value:
                                print(f"{trap.perimeter()}cm")

                            else:
                                print("please check for typos in your answer")

                        except ValueError:
                            print("please enter 'area' or 'perimeter'")

                    else:
                        print("that shape name is either non-2d or beyond my current scope")

                except ValueError:
                    print("please enter a valid shape name")

            elif "3" in shape_type:
                try:
                    shape_name = input("what 3d shape are you working with today? ")
                    if "exit" in shape_name:
                        print("exiting...")
                        break
                    
                    elif "cube" in shape_name:
                        length= int(input("enter one given side: "))
                        cube = Cube(length)
                        try:
                            value = input("what value do you need? surface area/volume: ").lower()
                            if "sur" in value:
                                print(f"{cube.surface_area()}cm2")

                            elif "vol" in value:
                                print(f"{cub.volume()}cm3")

                            else:
                                print("please check for typos in your answer")

                        except ValueError:
                            print("please enter a valid value")

                    elif "cuboid" in shape_name:
                        length = int(input("enter base length: "))
                        width = int(input("enter base width: "))
                        height = int(input("enter body height(z-axis): "))
                        cuboid = Cuboid(length,width,height)
                        try:
                            value = input("what value do you need? surface area/volume: ").lower()
                            if "sur" in value:
                                print(f"{cuboid.surface_area()}cm2")

                            elif "vol" in value:
                                print(f"{cuboid.volume()}cm3")

                            else:
                                print("please check for typos in your answer")

                        except ValueError:
                            print("please enter a valid value like 'surface area' or 'volume'")

                    elif "cyl" in shape_name:
                        radius = int(input("enter base radius: "))
                        height = int(input("enter body height: "))
                        cyl = Cylinder(radius,height)
                        try:
                            value = input("what value do you need? surface area/volume: ").lower()
                            if "sur" in value:
                                print(f"{cyl.surface_area()}cm2")

                            elif "vol" in value:
                                print(f"{cyl.volume()}cm3")

                            else:
                                print("please check for typos in your answer")

                        except ValueError:
                            print("please enter a valid value like 'surface area' or 'volume'")

                    
                    elif "pyr" in shape_name:
                        print("my current scope only covers square base pyramids")
                        length = int(input("enter base length: "))
                        height = int(input("enter body height: "))
                        pyr = Pyramid(length,height)
                        try:
                            value = input("what value do you need? surface area/volume: ").lower()
                            if "sur" in value:
                                print(f"{pyr.surface_area()}cm2")

                            elif "vol" in value:
                                print(f"{pyr.volume()}cm3")

                            else:
                                print("please check for typos in your answer")

                        except ValueError:
                            print("please enter a valid value like 'surface area' or 'volume'")

                    elif "sph" in shape_name:
                        radius = int(input("enter the radius of the sphere: "))
                        sph = Sphere(radius)
                        try:
                            value = input("what value do you need? surface area/volume: ").lower()
                            if "sur" in value:
                                print(f"{sph.surface_area()}cm2")

                            elif "vol" in value:
                                print(f"{sph.volume()}cm3")

                            else:
                                print("please check for typos in your answer")

                        except ValueError:
                            print("please enter a valid value like 'surface area' or 'volume'")

                    elif "con" in shape_name:
                        radius = int(input("enter the radius of the base of the cone: "))
                        height = int(input("enter the height of the cone: "))
                        con = Cone(radius,height)
                        try:
                            value = input("what value do you need? surface area/volume: ").lower()
                            if "sur" in value:
                                print(f"{con.surface_area()}cm2")

                            elif "vol" in value:
                                print(f"{con.volume()}cm3")

                            else:
                                print("please check for typos in your answer")

                        except ValueError:
                            print("please enter a valid value like 'surface area' or 'volume'")

                    else:
                        print("that 3d shape either doesn't exist or is beyond my current scope,please try another")

                except ValueError:
                    print("please enter a valid shape name")

            else:
                print("that type of shape doesn't,please try '2d' or '3d'")

        except ValueError:
            print("please enter a valid shape type eg. 2d or 3d")

if __name__ == "__main__":
    calculator()
