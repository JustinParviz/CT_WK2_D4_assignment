def square_footage():
    length = input("What is the length of your house? ")
    width = input("What is the width of your house? ")
    return int(length) * int(width)

def circumference_of_circle():
    radius = input("What is the radius of your circle? ")
    pi = 3.14
    return (2 * int(radius) * pi)