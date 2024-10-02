import math
import argparse

parser = argparse.ArgumentParser(description='Положение точки и окружности')    
parser.add_argument('circle_center_file', type=str)
parser.add_argument('points_list_file', type=str)
args = parser.parse_args()

with open(args.circle_center_file, 'r') as file:
    x_c, y_c = map(float, file.readline().split())
    r = float(file.read())
#print(x_c, y_c, r)
points = []
with open(args.points_list_file, 'r') as file:
    for line in file:
        x, y = map(float, line.split())
        points.append((x, y))
        
for x, y in points:
    distance = math.sqrt((x - x_c) ** 2 + (y - y_c) ** 2)
    if distance == r:
        print("0")
    elif distance < r:
        print("1")
    else:
        print("2")