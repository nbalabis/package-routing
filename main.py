from read_data import packages, truck1, truck2, truck3

truck1.start()
truck2.start()
truck3.start()


def get_all_packages(time):
    print('---ALL PACKAGES AT ' + str(time) + '---')
    delivered = []
    transit = []
    hub = []

    for package in packages.get_all():
        if package.delivery_time <= time:
            delivered.append(package)
        elif package.load_time <= time:
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


get_all_packages(7)
get_all_packages(8)
get_all_packages(12)
get_all_packages(23)
