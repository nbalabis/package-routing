import convert_time
from read_data import packages


def all_packages(hours, minutes=0):
    epoch_time = convert_time.to_epoch(hours, minutes)
    print('\n-------------------------------------------------------------------------')
    print('                          ALL PACKAGES AT ' + convert_time.to_readable(epoch_time))
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
    print('\n-------------------------------------------------------------------------')
    print("Lookup another time or type 'cancel' to return to the Package Lookup Menu\n")


def specific_packages(criteria, selected_packages, hours, minutes=0):
    epoch_time = convert_time.to_epoch(hours, minutes)
    print('\n-------------------------------------------------------------------------\n')
    for package in selected_packages:
        print(f'                          PACKAGE {package.id} AT {convert_time.to_readable(epoch_time)}')
        print(f'ID: {package.id}')
        print(f'ADDRESS: {package.location.address}')
        print(f'CITY: {package.city}')
        print(f'ZIP: {package.zip}')
        print(f'WEIGHT: {package.mass}kg')
        if package.notes != '':
            print(f'NOTE: {package.notes}')
        else:
            print('NOTE: None')
        print(f'DEADLINE: {convert_time.to_readable(package.deadline)}')
        if package.delivery_time <= epoch_time:
            print(f'STATUS: Delivered at {convert_time.to_readable(package.delivery_time)}\n')
        elif package.load_time <= epoch_time:
            print('STATUS: En Route\n')
        else:
            print('STATUS: At Hub\n')
    print('-------------------------------------------------------------------------')
    print(f"Lookup another {criteria} or type 'cancel' to return to the Package Lookup Menu\n")
