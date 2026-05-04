import math

def convert():
    radians = float(input("Въведи радиани: "))
    degree = radians * 180 / math.pi

    print(degree)

convert()