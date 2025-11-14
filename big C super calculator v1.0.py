#include <stdio.h>
import math

print("""welcome to the 2 dimensional-area,perimeter,volume and surface area calculator by big C
use a converter to convert lengths into centimeters fr easier calculation""")

while True:
    try:
        shape = input("what shape are you looking to calculate its value?")

        if ((shape).strip().lower()) == "circle":
            
            try:
                parameter = input("what parameters do you need from your circle;area,circumference?")
                
                if ((parameter).strip().lower()) == "area":
                    print("okay,you want the area of the circle, what measurements do you currently have?")
                    print("(a).radius")
                    print("(b).diameter")
                    print("(c).circumference")
                    print("(d).none")

                    choice = input("which option represents you current  measurements? just choose one. ")

                    if ((choice).strip().lower()) == "a":
                        try:
                            circ_rad = int(input("what is the radius"))

                            circ_area = ((22/7)*((circ_rad)**2))

                            print(f"your circle has an area of {circ_area} cm2")
                            continue
                        except ValueError:
                            print("try a number little boy!!")

                    elif ((choice).strip().lower()) == "b":
                        try:
                            circ_diam = int(input("what is the circle's diameter? "))
                            circ_rad = ((circ_diam)/2)

                            circ_area = ((22/7)*((circ_rad)**2))

                            print(f"your circle has an area of {circ_area} cm2")
                            continue
                        
                        except ValueError:
                            print("try a number little boy!!")

                    elif ((choice).strip().lower()) == "c":
                        try:
                            circ_circ = int(input("what is the circle's circumference? "))
                            circ_rad = ((circ_circ)/(44/7))

                            circ_area = ((22/7)*((circ_rad)**2))

                            print(f"your circle has an area of {circ_area} cm2")
                            continue
                        
                        except ValueError:
                            print("try a number little boy!!")

                    elif ((choice).strip().lower()) == "d":
                        print("oops! that is currently beyond my scope")
                        continue

                    else:
                        print("try the given options ie. a,b,c,d")
                        continue

                elif ((parameter).strip().lower())== "circumference":
                    print("you chose circumference,which of the below measurements do you currently have?:")
                    print("(a).radius")
                    print("(b).diameter")
                    print("(c).area")
                    print("(d).none")

                    choice = input("which option represents your measurements?: ")

                    if ((choice).strip().lower()) == "a":
                        try:
                            circ_rad =  int(input("what is the radius of the circle?:"))

                            circ_circ = (2*(22/7)*(circ_rad))

                            print(f"your circle has a circumference of {circ_circ} cm")
                            continue

                        except ValueError:
                            print("try a number")
                            continue

                    elif ((choice).strip().lower()) == "b":
                        try:
                            circ_diam = int(input("what is the diameter of your circle?: "))

                            circ_circ = ((22/7)*(circ_diam))

                            print(f"you circle has a circumference of {circ_circ} cm")
                            continue

                        except ValueError:
                            print("try a number")

                    elif ((choice).strip().lower()) == "c":
                        try:
                            circ_area = int(input("what is the area of your circle?: "))

                            circ_rad = (math.sqrt((circ_area)/(22/7)))
                            circ_circ = ((22/7)*((circ_rad)*2))

                            print(f"you circle has a circumference of {circ_circ} cm")
                            continue

                        except ValueError:
                            print("try a number")

                    elif ((choice).strip().lower()) == "d":
                        print("oops!!that's curently beyond my scope")
                        continue

                    else:
                        print("please try the given options; a,b,c,d")
                        continue

                else:
                    print("for a circle,you can only calculate the area and circumference")
                    continue

            except ValueError:
                print("please enter a valid entry eg. area ,circumference")
                            
        elif ((shape).strip().lower()) == "triangle":
            try:
                parameter = input("""you selected a triangle.
And what parameters are you looking to calculate?eg.volume,area,perimeter....etc?""")

                if ((parameter).strip().lower()) == "volume":
                    print("Oops! two-dimensional shapes like triangles,do not have volume! try a different figure")
                    continue

                elif ((parameter).strip().lower()) == "perimeter":
                    try:
                        print("okay,so we are calculating the perimeter of a triangle,go ahead and give me the dimensions below")
                        dim_tri_s1 = int(input("Side 1: "))
                        dim_tri_s2 = int(input("side 2: "))
                        dim_tri_s3 = int(input("side 3: "))

                        tri_peri = (dim_tri_s1) + (dim_tri_s2) + (dim_tri_s3)

                        print(f"your triangle has a perimeter of {tri_peri} centimeters")
                        continue

                    except ValueError:
                        print("oops! invalid input,use a number")
                        continue

                elif ((parameter).strip().lower()) == "area" or ((parameter).strip().lower()) == "surfacearea":
                    try:
                        pythag_check = input("does this triangle have :(3 or 2?) known sides?")

                        if pythag_check == "2":
                            try:
                                sides = input("""pheew! this is a tough one....which sides are present on this thing?:
(a) hypotenuse and base
(b) hypotenuse and height
(c) base and height
use the letter representing your choice to answer""")
                                if ((sides).strip().lower()) == "a":
                                    try:
                                        dim_tri2_s1 = int(input("hypotenuse(this is the biggest side):"))
                                        dim_tri2_s2 = int(input("base(the side that has a perpendicular(90 degrees to another side)):"))

                                        height = (((dim_tri2_s1)**2)-((dim_tri2_s2)**2))

                                        tri_area = ((1/2)*(dim_tri2_s2)*(height))

                                        print(f"the area of your triangle is {tri_area} centimeters")

                                    except ValueError:
                                        print("try using numbers little boy:[")
                                        continue

                                elif ((sides).strip().lower()) == "b":
                                    try:
                                        dim_tri2_s11 = int(input("hypotenuse(this is the biggest side):"))
                                        dim_tri2_s22 = int(input("""height(the side that has a perpendicular(90 degrees -
                                                             to another side)):"""))

                                        base = (((dim_tri2_s11)**2)-((dim_tri2_s22)**2))

                                        tri2_area = ((1/2)*(base)*(dim_tri2_s22))

                                        print(f"the area of your triangle is {tri2_area} centimeters")

                                    except ValueError:
                                        print("try a number little boy")
                                        continue

                                else:
                                    try:
                                        dim_tri2_s111 = int(input("height(the side that has a perpendicular(90 degrees to another side)): "))
                                        dim_tri2_s222 = int(input("base(the other side that has a perpendicular): "))
                                        
                                        tri3_area = ((1/2)*(dim_tri2_s222)*(dim_tri2_s111))

                                        print(f"your triangle has an area of {tri3_area} ")

                                    except ValueError:
                                        print("try a number little boy")
                                        continue


                            except ValueError:
                                print("try a number little boy")
                                continue

                        elif pythag_check == "3":
                            try:
                                sides = input("""im only going to need the two sides that are perpendicular
                                              to each other""")
                                
                                dim_tri2_s1111 = int(input("one perpendicular side(90 degrees to another side):"))
                                dim_tri2_s2222 = int(input("one perpendicular side(90 degrees to another side):"))

                                tri4_area = ((1/2)*(dim_tri2_s2222)*(dim_tri2_s1111))

                                print(f"your triangle has an area of {tri4_area}")


                            except ValueError:
                                print("try a number little boy")
                                continue

                        else:
                            if pythag_check == "1" or (int(pythag_check)) == 0:
                                print("oops! problems involving angles is coming soon,stay tuned;]")
                                continue

                            elif (int(pythag_check)) > 3 or (int(pythag_check)) < 0 :
                                print("a triangle has 3 sides,wait,do you even have a triangle??try again with number 2 or 3 ")
                                continue

                    except ValueError:
                        print("try a number little boy")
                        continue

            except ValueError:
                print("try a parameter like area,perimeter...etc, little boy")
                continue

        elif ((shape).strip().lower()) == "square":
            try:
                print("ooh,my favorite shape,square(4 equal sides)")

                par2 = input("and what parameters are you looking to calculate?area/perimeter?")

                if ((par2).strip().lower()) == "area" or ((par2).strip().lower()) == "surfacearea":
                    try:
                        sq_s = int(input("what is one known side of the square?"))

                        sq_area = ((sq_s)**2)

                        print(f"your square has an area of {sq_area} square centimeters(cm2)") 
                        continue
                    except ValueError:
                        print("try a number little boy!")
                        continue

                elif ((par2).strip().lower()) == "perimeter":
                    try:
                        sq_s2 = input("what is one known side of the square?")

                        sq_peri = ((int(sq_s2))*4)

                        print(f"your square has a perimeter of {sq_peri} centimeters")
                        continue

                    except ValueError:
                        print("try a number little boy!!")

                else:
                    if ((par2).strip().lower()) == "volume":
                        print("sorry bud! a square doesn't have volume")
                        continue
                    
                    else:
                        print("oops! can't help with that!")
                        continue

            except ValueError:
                print("try a parameter like volume,surface area...etc, little boy!!")

        elif ((shape).strip().lower()) == "rectangle":
            try:
                rec_par = input("what parameters do you need from the rectangle?(area/perimeter)")

                if ((rec_par).strip().lower()) == "area":
                    try:
                        sid_rec_check = input("do you know how many sides of this rectangle are known?yes/no")

                        if (sid_rec_check.strip().lower()) == "no":
                            print("""oops!can't help find the area of a rectangle without-
                           at least two sides or one side and a diagonal,
                          ask someone to help""")
                            continue

                        else:
                            if (sid_rec_check.strip().lower()) == "yes":
                                try:
                                    length = input("side one(any): ")
                                    width = input("side2(other): ")

                                    rec_area = (int(length)) * (int(width))

                                    print(f"your rectangle has an area o {rec_area}")
                                    continue
                                except ValueError:
                                    print("try a number little boy!")
                                    continue

                            else:
                                print("sorry!!Calculator AI is coming sooni won't be able to help you on this until then")
                                continue

                    except ValueError:
                        print("try a yes/no little boy!")
                        continue

                elif ((rec_par).strip().lower()) == "perimeter":
                    try:
                        sid_rec_check2 = input("do you know how many sides of this rectangle are known?yes/no")
                        
                        if ((sid_rec_check2).strip().lower())== "no":
                            print("""oops!can't help find the perimeter of a rectangle without-
                           at least two sides or one side and a diagonal,
                          ask someone to help""")
                            continue

                        else:
                            if ((sid_rec_check2).strip().lower()) == "yes":
                                try:
                                    length1 = input("one side(any): ")
                                    width1 = input("other side: ")

                                    rec_peri = ((int(length1))+(int(width1))*2)

                                    print(f"your rectangle has a perimeter of {rec_peri} centimeters(cm)")
                                    continue

                                except ValueError:
                                    print("try a number little boy!")
                                    continue

                            else:
                                print("AI calc is coming soon,i can't help you with your request until then")
                                continue
                    
                    except ValueError:
                        print("try a number little boy!")
                        continue
                    

            except ValueError:
                print("try a parameter like volume,surface area...etc little boy!")
                continue


        elif ((shape).strip().lower()) == "cube":
            try:
                print("A cube?! Damn,aight let's have it")

                cub_par =  input("and what do you need out of it?(volume/surface area)")

                if ((cub_par).strip().lower()) == "volume":
                    try:
                        print("okay,so volume. I'mma need a little more details")

                        cub_dim = input("whats the length of your favorite side?")

                        cub_volume = ((int(cub_dim))**3)

                        print(f"your cube has a volume of {cub_volume}")
                        continue

                    except ValueError:
                        print("try a number little boy!")
                        continue

                elif ((cub_par).strip().lower()) == "area" or ((cub_par).strip().lower()) == "surfacearea":
                    try:
                        print("okay,so area. I'mma need a little more details")

                        cub_dim2 = input("whats the length of your favorite side?")

                        cub_volume = ((int(cub_dim))**3)

                        print(f"your cube has a volume of {cub_volume}")
                        continue

                    except ValueError:
                        print("try a number little boy")

                else:
                    print("oops! you can only calculate the surface area and volume of a cube at this time")
                    continue

            except ValueError:
                        print("try a parameter like volume,surface area etc little boy!")
                        continue

        elif ((shape).strip().lower()) == "cuboid":
            try:
                print("A cuboid?! Damn,aight let's have it")

                cuboid_par =  input("and what do you need out of it?(volume/surface area)")

                if ((cuboid_par).strip().lower()) == "volume":
                    try:
                        print("okay,so volume. I'mma need a little more details")

                        cuboid_dim1 = input("what's the length of one face?")
                        cuboid_dim2 = input("what's the width of that face?")
                        cuboid_dim3 = input("what is the z-axis(perpendicular to length)?")
                        
                        cuboid_volume = ((int(cuboid_dim1))*(int(cuboid_dim2))*(int(cuboid_dim3)))

                        print(f"your cuboid has a volume of {cuboid_volume} cubic centimeters(cm3)")
                        continue

                    except ValueError:
                        print("try a number little boy!")
                        continue

                elif ((cuboid_par).strip().lower()) == "area" or ((cuboid_par).strip().lower()) == "surface area":
                    try:
                        print("okay,so area. I'mma need a little more details")

                        cuboid_dim11 = input("whats the length of the base face?")
                        cuboid_dim22 = input("what is the width of that face?")
                        cuboid_dim33 = input("what is the z-axis(perpendicular to length)?")

                        cuboid_area = ((((int(cuboid_dim11))*(int(cuboid_dim22)))*2)+(((int(cuboid_dim11))*(int(cuboid_dim33)))*2)+((int(cuboid_dim22))*(int(cuboid_dim33))))

                        print(f"your cuboid has a surface area of {cuboid_area}")
                        continue

                    except ValueError:
                        print("try a number little boy")

                else:
                    print("oops! you can only calculate the surface area and volume of a cuboid at this time")
                    continue

            except ValueError:
                print("try a parameter eg. volume,surface area etc little boy!")
                continue

        elif ((shape).strip().lower()) == "cylinder":
            try:
                cyl_dim_check = input("do you have the radii and/or diameters and/or top/base-circumference AND the length/height of the cylinders?(yes/no)")

                if ((cyl_dim_check).strip().lower()) == "no":
                    print("Oops! can't calculate any parameters at this time")
                    continue

                elif ((cyl_dim_check).strip().lower()) == "yes":
                    try:
                        cyl_par = input("and what parameters do you need of your cylinder?")

                        if ((cyl_par).strip().lower()) == "volume":
                            try:
                                cyl_dims = input("""which details of the cylinder do you have :
                                         (a)radius and height
                                         (b)circumference and height
                                         (c)base area and height
                                         (d)diameter and height
                                         (e)none of the above""")
                        
                                if ((cyl_dims).strip().lower()) == "a":
                                    try:
                                        cyl_rad = input("what is the radius of its base? ")
                                        cyl_h = input("what is its height? ")

                                        cyl_vol = (((22/7)*((int(cyl_rad))**2))*(int(cyl_h)))

                                        print(f"your cylinder has a volume of {cyl_vol} cubic centimeters(cm3)")
                                        continue

                                    except ValueError:
                                        print("try a number, little boy")
                                        continue

                                elif ((cyl_dims).strip().lower()) == "b":
                                    try:
                                        cyl_circ = input("what is the circumference of its base? ")
                                        cyl_h1 = input("what is its height? ")

                                        cyl_rad1 = ((int(cyl_circ))/((2)*(22/7)))

                                        cyl_vol1 = (((22/7)*((int(cyl_rad1))**2))*(int(cyl_h1)))

                                        print(f"your cylinder has a volume of {cyl_vol1} cubic centimeters(cm3)")
                                        continue

                                    except ValueError:
                                        print("try a number, little boy")
                                        continue

                                elif ((cyl_dims).strip().lower()) == "c":
                                    try:
                                        cyl_b_area = input("what is the area of its base? ")
                                        cyl_h11 = input("what is its height? ")

                                        cyl_rad11 = (math.sqrt((int(cyl_b_area))/(22/7)))

                                        cyl_vol11 = (((22/7)*((int(cyl_rad11))**2))*(int(cyl_h11)))

                                        print(f"your cylinder has a volume of {cyl_vol11} cubic centimeters(cm3)")
                                        continue

                                    except ValueError:
                                        print("try a number,little boy")
                                        continue

                                elif ((cyl_dims).strip().lower()) == "d":
                                    try:
                                        cyl_diam = input("what is the diameter of its base? ")
                                        cyl_h111 = input("what is its height? ")

                                        cyl_rad111 = ((int(cyl_diam))/2)

                                        cyl_vol111 = (((22/7)*((cyl_rad111)**2))*(int(cyl_h111)))

                                        print(f"your cylinder has a volume of {cyl_vol111} cubic centimeters(cm3)")
                                        continue
                                    
                                    except ValueError:
                                        print("try a number, little boy")
                                        continue

                                else:
                                    if ((cyl_dims).strip().lower()) == "e":
                                        print("sorry,your problem is beyond my scope at this time. check in again after the update")
                                        continue

                                    else:
                                        print("oops! i currently dont understand natural human language,try again with the given options:a,b,c or d")
                                        continue

                            except ValueError:
                                print("try a,b,c,d or e  little boy")
                                continue

                        elif ((cyl_par).strip().lower()) == "surfacearea" or ((cyl_par).strip().lower()) == "area":
                            try:
                                cyl_dims2 = input("""which details of the cylinder do you have :
                                         (a)radius and height
                                         (b)circumference and height
                                         (c)base area and height
                                         (d)diameter and height
                                         (e)none of the above""")
                                
                                if (((cyl_dims2).strip().lower())) == "a":
                                    try:
                                        cyl2_rad = int(input("what is the radius of its base? "))
                                        cyl2_h = int(input("what is its height? "))

                                        cyl2_s_a_1c = ((2*(cyl2_rad))*(22/7) * cyl2_h) + (((22/7))*(cyl2_rad))
                                        cyl2_s_a_2c = ((2*(cyl2_rad))*(22/7) * cyl2_h) + ((2*(22/7))*(cyl2_rad))
                                        cyl2_s_a_xc = ((2*(cyl2_rad))*(22/7) * cyl2_h)

                                        print(f"""assuming your cylinder is closed on both ends,its surface area is{cyl2_s_a_2c} square centimeters(cm2)")
                                              esle; assuming 1 closed end,you are looking at {cyl2_s_a_1c} square centimeters(cm2)
                                              else; assuming both ends are open,its surface area is {cyl2_s_a_xc} square centimeters(cm2)""")
                                        continue

                                    except ValueError:
                                        print("try a number,little boy")
                                        continue

                                elif (((cyl_dims2).strip().lower())) == "b":
                                    try:
                                        cyl2_circ = int(input("what is the circumference of its base? "))
                                        cyl2_h1 = int(input("what is its height? "))

                                        cyl2_rad1 = ((int(cyl2_circ))/((2)*(22/7)))
                                        
                                        cyl2_s_a_11c = ((2*(cyl2_rad1))*(22/7) * cyl2_h1) + (((22/7))*(cyl2_rad1))
                                        cyl2_s_a_22c = ((2*(cyl2_rad1))*(22/7) * cyl2_h1) + ((2*(22/7))*(cyl2_rad1))
                                        cyl2_s_a_xxc = ((2*(cyl2_rad1))*(22/7) * cyl2_h1)

                                        print(f"""assuming your cylinder is closed on both ends,its surface area is{cyl2_s_a_22c} square centimeters(cm2)")
                                              esle; assuming 1 closed end,you are looking at {cyl2_s_a_11c} square centimeters(cm2)
                                              else; assuming both ends are open,its surface area is {cyl2_s_a_xxc} square centimeters(cm2)""")
                                        continue

                                    except ValueError:
                                        print("try a number,little boy")
                                        continue

                                elif ((cyl_dims2).strip().lower()) == "c":
                                    try:
                                        cyl2_b_a = int(input("what is the area of its base? "))
                                        cyl2_h11 = int(input("what is its height? "))

                                        cyl2_rad11 = (math.sqrt((int(cyl_b_area))/(22/7)))
                                        
                                        cyl2_s_a_111c = ((2*(cyl2_rad11))*(22/7) * cyl2_h11) + (((22/7))*(cyl2_rad11))
                                        cyl2_s_a_222c = ((2*(cyl2_rad11))*(22/7) * cyl2_h11) + ((2*(22/7))*(cyl2_rad11))
                                        cyl2_s_a_xxxc = ((2*(cyl2_rad11))*(22/7) * cyl2_h11)

                                        print(f"""assuming your cylinder is closed on both ends,its surface area is{cyl2_s_a_222c} square centimeters(cm2)")
                                              esle; assuming 1 closed end,you are looking at {cyl2_s_a_111c} square centimeters(cm2)
                                              else; assuming both ends are open,its surface area is {cyl2_s_a_xxxc} square centimeters(cm2)""")
                                        continue

                                    except ValueError:
                                        print("try a number,little boy")
                                        continue

                                elif ((cyl_dims2).strip().lower()) == "d":
                                    try:
                                        cyl2_diam = input("what is the diameter of its base? ")
                                        cyl2_h111 = input("what is its height? ")

                                        cyl2_rad111 = ((int(cyl2_diam))/2)

                                        cyl2_s_a_1111c = ((2*(cyl2_rad111))*(22/7) * cyl2_h111) + (((22/7))*(cyl2_rad111))
                                        cyl2_s_a_2222c = ((2*(cyl2_rad111))*(22/7) * cyl2_h111) + ((2*(22/7))*(cyl2_rad111))
                                        cyl2_s_a_xxxxc = ((2*(cyl2_rad111))*(22/7) * cyl2_h111)

                                        print(f"""assuming your cylinder is closed on both ends,its surface area is{cyl2_s_a_2222c} square centimeters(cm2)")
                                              esle; assuming 1 closed end,you are looking at {cyl2_s_a_1111c} square centimeters(cm2)
                                              else; assuming both ends are open,its surface area is {cyl2_s_a_xxxxc} square centimeters(cm2)""")
                                        continue
                                    
                                    except ValueError:
                                        print("try a number, little boy")
                                        continue

                                else:
                                    if ((cyl_dims2).strip().lower()) == "e":
                                        print("sorry,your problem is beyond my scope at this time. check in again after the update")
                                        continue

                                    else:
                                        print("oops! i currently dont understand natural human language,try again with the given options:a,b,c or d")
                                        continue

                            except ValueError:
                                print("oops,try a,b,c,d or e,little boy")
                                continue

                    except ValueError:
                        print("try a parameter, eg. surface area ,volume....little boy")
                        continue
            
            except ValueError:
                print("answer the question correctly,use words")

    except ValueError:
        print("try another shape,circles are not yet included!!")

        

                                        



                            

                            

                            

                            
                                



                        
                        

                        
                        


                    


            



            



                    

                    






                            
                                    

                                
                                
