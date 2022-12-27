from man_dist import man_dist
import datetime

start = datetime.datetime.now()

with open('test.txt', 'r') as file:
    inputs = file.read()

inputs = [[[coord.split(', ') for coord in part.split('Sensor at ')][-1] for part in line.split(': closest beacon is at ')] for line in inputs.strip().split('\n')]
inputs = [[[int(coord.split('=')[-1]) for coord in part] for part in line] for line in inputs]

[print(line) for line in inputs]

sensor_map = {}
beacon_exclusion_zone = []

for sensor, beacon in inputs:
    sensor_key = ','.join(map(str, sensor))
    sensor_map[sensor_key] = {
        'closest_beacon': beacon,
        'beacon_distance': man_dist(sensor, beacon)
    }

print(sensor_map)

print(f'elapsed: {datetime.datetime.now() - start}')
