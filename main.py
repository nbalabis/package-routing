from read_data import packages, locations, truck1, truck2, truck3
import lookup
import convert_time

deliveries_completed = False


def start():
    truck1.start()
    truck2.start()
    packages.get(9).update_location(locations.get('410 S State St'))
    truck3.start()


def get_help():
    print('\nPlease choose from the list of available commands:')
    if not deliveries_completed:
        print("     -Type 'start' to begin package routing")
    else:
        print("     -Type 'info' to see an overview of the package deliveries")
    print("     -Type 'quit' to exit the program")
    print("     -Type 'help' at any time to see a list of all available commands\n")


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
            print('\nDeliveries have already been completed.')
            print("     -Type 'info' to see an overview of the package deliveries\n")
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

    elif user_input == 'info':
        if not deliveries_completed:
            print("\nDeliveries have not been completed yet.")
            print("     -Type 'start' to begin package routing\n")
        else:
            print('\n----------------------------------------------------')
            print('    ALL PACKAGES SUCCESSFULLY DELIVERED ON TIME!')
            print(
                f'The final truck returned to the Hub at {convert_time.to_readable(max([truck1.time, truck2.time, truck3.time]))}')
            print(
                f'The trucks traveled a total distance of {str("%.1f" % (truck1.total_distance + truck2.total_distance + truck3.total_distance))} miles')
            print('----------------------------------------------------\n')

    elif user_input == 'help':
        get_help()

    else:
        print('\nInvalid command.')
        get_help()

    user_input = input(':').lower()
if user_input == 'quit':
    print('\n-------------------------------------------------------')
    print('     THANK YOU FOR USING THE WGUPS ROUTING PROGRAM')
    print('-------------------------------------------------------')
    exit()
# lookup.all_packages(7)
# lookup.all_packages(9)
# lookup.all_packages(10)
# lookup.all_packages(12, 30)
