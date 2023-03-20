from read_data import packages, locations, truck1, truck2, truck3
import lookup
import convert_time

deliveries_completed = False


def start():
    truck1.start()
    truck2.start()
    packages.get(9).update_location(locations.get('410 S State St'))
    truck3.start()


print("""
----------------------------------------------------------------------
                 WELCOME TO THE WGUPS ROUTING PROGRAM
----------------------------------------------------------------------
Please choose from the list of available commands:
     -Type 'start' to begin package routing
     -Type 'quit' to exit the program 
     -Type 'help' at any time to see a list of all available commands
""")

user_input = input(":").lower()
while user_input != 'quit':
    if user_input == 'start':
        if deliveries_completed:
            print('\nDeliveries have already been completed.\n')
        else:
            print("")
            truck1.print_packages()
            truck2.print_packages()
            truck3.print_packages()
            start()
            late_packages = []
            for package in packages.get_all():
                if package.on_time is False:
                    late_packages.append(package.id)
            if len(late_packages) > 0:
                print('--------------------------------------------------')
                print('               ERROR: LATE DELIVERY')
                print('Package(s): ', end="")
                for package_id in late_packages:
                    print(package_id, end=" ")
                print('were delivered late.')
                print('Please re-load trucks and try again.')
                print('--------------------------------------------------\n')
            else:
                print('----------------------------------------------------')
                print('    ALL PACKAGES SUCCESSFULLY DELIVERED ON TIME!')
                print(
                    f'The final truck returned to the Hub at {convert_time.to_readable(max([truck1.time, truck2.time, truck3.time]))}')
                print(
                    f'The trucks traveled a total distance of {str("%.1f" % (truck1.total_distance + truck2.total_distance + truck3.total_distance))} miles')
                print('----------------------------------------------------\n')
            deliveries_completed = True
    user_input = input(':').lower()
if user_input == 'quit':
    exit()
# lookup.all_packages(7)
# lookup.all_packages(9)
# lookup.all_packages(10)
# lookup.all_packages(12, 30)
