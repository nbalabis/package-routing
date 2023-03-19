from read_data import packages, locations, truck1, truck2, truck3
from time import mktime
import lookup

truck1.start()
truck2.start()
packages.get(9).update_location(locations.get('410 S State St'))
truck3.start()

lookup.all_packages(7)
lookup.all_packages(9)
lookup.all_packages(10)
lookup.all_packages(12, 30)
