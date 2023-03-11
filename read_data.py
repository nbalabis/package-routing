import csv
from hash_map import HashMap
from package import Package
from truck import Truck

# Initialize trucks
truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)

# Load package data
with open('./data/package_info.csv') as package_csv:
    hash_map = HashMap()
    package_reader = csv.reader(package_csv, delimiter=',')
    for package_data in package_reader:
        package_id = int(package_data[0])
        hash_map.add(package_id, Package(package_data))
        if not truck1.is_full():
            truck1.load_package(hash_map.get(package_id))
        elif not truck2.is_full():
            truck2.load_package(hash_map.get(package_id))
        else:
            truck3.load_package(hash_map.get(package_id))

with open('./data/distances.csv') as distance_csv:
    distance_matrix = []
    distance_reader = csv.reader(distance_csv, delimiter=',')
    for address in distance_reader:
        distance_matrix.append(address)
