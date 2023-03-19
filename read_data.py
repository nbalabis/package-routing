import csv
from hash_map import HashMap
from package import Package
from truck import Truck
from location import Location
from time import mktime

packages = HashMap()
distance_matrix = []
locations = HashMap()

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

# Initialize trucks
hub = locations.get('4001 South 700 East')
on_time_departure = mktime((2023, 3, 20, 8, 0, 0, 0, 0, 0))
late_departure = mktime((2023, 3, 20, 10, 20, 0, 0, 0, 0))
truck1 = Truck(1, hub, on_time_departure)
truck2 = Truck(2, hub, on_time_departure)
truck3 = Truck(3, hub, late_departure)

# Load package data into a hash table
with open('./data/package_info.csv') as package_csv:
    package_reader = csv.reader(package_csv, delimiter=',')
    for package_data in package_reader:
        package_id = int(package_data[0])
        delivery_location = locations.get(package_data[1])
        packages.add(package_id, Package(package_data, delivery_location))

        # Load trucks
        if packages.get(package_id).notes == 'Can only be on truck 2':
            truck2.load_package(packages.get(package_id))
        elif package_id in [13, 14, 15, 16, 19, 20]:
            truck1.load_package(packages.get(package_id))
        elif packages.get(package_id).notes == 'Delayed on flight---will not arrive to depot until 9:05 am':
            truck3.load_package(packages.get(package_id))
        elif packages.get(package_id).notes == 'Wrong address listed':
            truck3.load_package(packages.get(package_id))
        else:
            if not truck1.is_full():
                truck1.load_package(packages.get(package_id))
            elif not truck3.is_full():
                truck3.load_package(packages.get(package_id))
            else:
                truck2.load_package(packages.get(package_id))
