import csv
from hash_map import HashMap

with open('./data/package_info.csv') as package_csv:
    hash_map = HashMap()
    package_reader = csv.reader(package_csv, delimiter=',')
    for package in package_reader:
        hash_map.add(package[0], package)

with open('./data/distances.csv') as distance_csv:
    distance_matrix = []
    distance_reader = csv.reader(distance_csv, delimiter=',')
    for address in distance_reader:
        distance_matrix.append(address)
