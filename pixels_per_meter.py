import math

def pixels_per_meter_x(alt):
    return ((alt * math.tan(math.radians(62.2 / 2))) / (640 / 2))

def pixels_per_meter_y(alt):
    return ((alt * math.tan(math.radians(48.8 / 2))) / (480 / 2))