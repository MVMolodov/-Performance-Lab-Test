import math
import argparse

parser = argparse.ArgumentParser(description='Положение точки и окружности')    
parser.add_argument('file_with_nums', type=str)
args = parser.parse_args()

myint = []
with open(args.file_with_nums, 'r') as file:
    nums = [int(line.strip()) for line in file]
# print(nums)
avg = round(sum(nums) / len(nums))
steps = 0
# print(avg)
for i in range(len(nums)):
    steps = steps + abs(nums[i] - avg)
print(steps)
