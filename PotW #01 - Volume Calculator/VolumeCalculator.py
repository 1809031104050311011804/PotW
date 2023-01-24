import numpy as numpy

welcome_message = """This calculator currently supports the following types of geometric shapes:
        Cube
        Cuboid
        Cone
        Cylinder
        Sphere
"""
print(welcome_message)

shape_choice = input("What shape would you like to calculate the volume of? ")

#Cube
if shape_choice == "Cube":
    shape_choice = shape_choice.lower()
    shape_variables = "edge length"
    print("You chose {}! For this shape, you will need to input {}.".format(shape_choice, shape_variables))
    try:
        edge_length = float(input("Length of the edge: "))
    except ValueError:
        print("Enter valid numbers (i.e. 1, 3.14, etc.).")
    volume = edge_length**3
    volume = round(volume, 2)
    print("The volume of a {} with an edge length of {} is {}!".format(shape_choice, edge_length, volume))

#Cuboid
elif shape_choice == "Cuboid":
    shape_choice = shape_choice.lower()
    shape_variables = "length, width, and height"
    print("You chose {}! For this shape, you will need to input {}.".format(shape_choice, shape_variables))
    try:
        length = float(input("Length: "))
        width = float(input("Width: "))
        height = float(input("Height: "))
    except ValueError:
        print("Enter valid numbers (i.e. 1, 3.14, etc.).")
    volume = length * width * height
    volume = round(volume, 2)
    print("The volume of a {} with a length of {}, width of {}, and height of {} is {}!".format(shape_choice, length, width, height, volume))

#Cone
elif shape_choice == "Cone":
    shape_choice = shape_choice.lower()
    shape_variables = "base radius and cone height"
    print("You chose {}! For this shape, you will need to input {}.".format(shape_choice, shape_variables))
    try:
        base_radius = float(input("Radius of the base: "))
        cone_height = float(input("Height of the cone: "))
    except ValueError:
        print("Enter valid numbers (i.e. 1, 3.14, etc.).")
    volume = (1/3) * np.pi * (base_radius**2) * cone_height
    volume = round(volume, 2)
    print("The volume of a {} with a base radius of {} and a cone height of {} is {}!".format(shape_choice, base_radius, cone_height, volume))

#Cylinder
elif shape_choice == "Cylinder":
    shape_choice = shape_choice.lower()
    shape_variables = "base radius and cylinder height"
    print("You chose {}! For this shape, you will need to input {}.".format(shape_choice, shape_variables))
    try:
        base_radius = float(input("Radius of the base: "))
        cylinder_height = float(input("Height of the cylinder: "))
    except ValueError:
        print("Enter valid numbers (i.e. 1, 3.14, etc.).")
    volume = np.pi * (base_radius**2) * cylinder_height
    volume = round(volume, 2)
    print("The volume of a {} with a base radius of {} and a cylinder height of {} is {}!".format(shape_choice, base_radius, cylinder_height, volume))

elif shape_choice == "Sphere":
    shape_choice = shape_choice.lower()
    shape_variables = "radius"
    print("You chose {}! For this shape, you will need to input {}.".format(shape_choice, shape_variables))
    try:
        radius = float(input("Radius of the sphere: "))
    except ValueError:
        print("Enter valid numbers (i.e. 1, 3.14, etc.).")
    volume = (4/3) * np.pi * (radius**3)
    volume = round(volume, 2)
    print("The volume of a {} with a radius {} is {}!".format(shape_choice, radius, volume))
    
#Unsupported Shape
else:
    print("Please choose a supported shape.")

