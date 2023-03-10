import csv
from hash_map import HashMap
from package import Package
from truck import Truck
from location import Location

packages = HashMap()
distance_matrix = []
locations = HashMap()

# Initialize trucks
truck1 = Truck(1)
truck2 = Truck(2)
truck3 = Truck(3)

# Load package data into a hash table
with open('./data/package_info.csv') as package_csv:
    package_reader = csv.reader(package_csv, delimiter=',')
    for package_data in package_reader:
        package_id = int(package_data[0])
        packages.add(package_id, Package(package_data))
        
        # Load trucks
        if not truck1.is_full():
            truck1.load_package(packages.get(package_id))
        elif not truck2.is_full():
            truck2.load_package(packages.get(package_id))
        else:
            truck3.load_package(packages.get(package_id))

# Load distances into an adjacency matrix
with open('./data/distances.csv') as distance_csv:
    distance_reader = csv.reader(distance_csv, delimiter=',')
    for address in distance_reader:
        distance_matrix.append(address)

# Load location data into a hash table
with open('./data/location_names.csv') as location_csv:
    location_reader = csv.reader(location_csv, delimiter=',')
    for location_data in location_reader:
        location_id = int(location_data[0])
        location_name = location_data[1]
        location_address = location_data[2]
        distances = distance_matrix[location_id]
        locations.add(location_address, Location(location_id, location_name, location_address, distances))
