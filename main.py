from read_data import packages, truck1, truck2, truck3
import time

truck1.start()
truck2.start()
truck3.start()


def get_all_packages(epoch_time):
    print('---ALL PACKAGES AT ' + time.ctime(epoch_time)[11:16] + '---')
    delivered = []
    transit = []
    hub = []

    for package in packages.get_all():
        if package.delivery_time <= epoch_time:
            delivered.append(package)
        elif package.load_time <= epoch_time:
            transit.append(package)
        else:
            hub.append(package)
    print('     At Hub:')
    print('          ', end="")
    for package in hub:
        print(str(package.id), end=" ")
    print('')
    print('     En Route:')
    print('          ', end="")
    for package in transit:
        print(str(package.id), end=" ")
    print('')
    print('     Delivered:')
    print('          ', end="")
    for package in delivered:
        print(str(package.id), end=" ")
    print('')


def local_time(hours, seconds=0):
    return time.mktime((2023, 3, 20, hours, seconds, 0, 0, 0, 0))


get_all_packages(local_time(7))
get_all_packages(local_time(8))
get_all_packages(local_time(8, 15))
get_all_packages(local_time(9, 25))
