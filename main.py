from read_data import packages, locations, truck1, truck2, truck3
from time import mktime
import lookup

truck1.start()
truck2.start()
packages.get(9).update_location(locations.get('410 S State St'))
truck3.start()


def local_time(hours, minutes=0):
    return mktime((2023, 3, 20, hours, minutes, 0, 0, 0, 0))


lookup.all_packages(local_time(7))
lookup.all_packages(local_time(9))
lookup.all_packages(local_time(10))
lookup.all_packages(local_time(12, 30))
