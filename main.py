from read_data import packages, truck1, truck2, truck3

print('-----Package Status-----')
for package in packages.get_all():
    print('Package ' + package.id + ': ' + package.status)

truck1.start()
truck2.start()
truck3.start()

print('-----Package Status-----')
for package in packages.get_all():
    print('Package ' + package.id + ': ' + package.status)
