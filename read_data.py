import csv
from hash_map import HashMap

with open('./data/package_info.csv') as package_csv:
    hash_map = HashMap()
    package_reader = csv.reader(package_csv, delimiter=',')
    for package in package_reader:
        hash_map.add(package[0], package)
