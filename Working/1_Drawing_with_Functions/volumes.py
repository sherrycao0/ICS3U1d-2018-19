


import math

#volunme of cylinder
def volume(r, h):
    return math.pi * (r ** 2) * h

radius = int(input("Enter radius: "))
height = int(input("Enter height: "))

print(volume(radius, height))



#volume of cone
def volume(r, h):
    return 1/3 * (math.pi * (r ** 2) * h)

print(volume(radius, height))


#volume of sphere
def volume(r, h):
    return 4/3 * (math.pi * (r ** 3))

print(volume(radius, height))




