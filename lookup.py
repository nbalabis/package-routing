import time

from read_data import packages


def local_time(hours, minutes):
    return time.mktime((2023, 3, 20, hours, minutes, 0, 0, 0, 0))


def all_packages(hours, minutes=0):
    epoch_time = local_time(hours, minutes)
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
    print('\n')
