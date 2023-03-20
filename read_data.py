import csv
from hash_map import HashMap
from package import Package
from truck import Truck
from location import Location
import convert_time

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
departure_1 = convert_time.to_epoch(8)
departure_2 = convert_time.to_epoch(9, 5)
departure_3 = convert_time.to_epoch(10, 20)
truck1 = Truck(1, hub, departure_1)
truck2 = Truck(2, hub, departure_2)
truck3 = Truck(3, hub, departure_3)

# Load package data into a hash table
with open('./data/package_info.csv') as package_csv:
    package_reader = csv.reader(package_csv, delimiter=',')
    for package_data in package_reader:
        package_id = int(package_data[0])
        delivery_location = locations.get(package_data[1])
        deadline_str = package_data[5]
        if deadline_str == "EOD":
            deadline = convert_time.to_epoch(17)
        else:
            deadline_hour = int(deadline_str[0:deadline_str.find(':')])
            deadline_minute = int(deadline_str[deadline_str.find(':') + 1:deadline_str.find(' ')])
            deadline = convert_time.to_epoch(deadline_hour, deadline_minute)
        packages.add(package_id, Package(package_data, delivery_location, deadline))

        # Load trucks
        if packages.get(package_id).notes == 'Can only be on truck 2':
            truck2.load_package(packages.get(package_id))
        elif package_id in [13, 14, 15, 16, 19, 20]:
            truck1.load_package(packages.get(package_id))
        elif packages.get(package_id).notes == 'Delayed on flight---will not arrive to depot until 9:05 am':
            truck2.load_package(packages.get(package_id))
        elif packages.get(package_id).notes == 'Wrong address listed':
            truck3.load_package(packages.get(package_id))
        elif packages.get(package_id).deadline < convert_time.to_epoch(17):
            if not truck1.is_full():
                truck1.load_package(packages.get(package_id))
            else:
                truck2.load_package(packages.get(package_id))
        else:
            if not truck3.is_full():
                truck3.load_package(packages.get(package_id))
            elif not truck1.is_full():
                truck1.load_package(packages.get(package_id))
            else:
                truck2.load_package(packages.get(package_id))
