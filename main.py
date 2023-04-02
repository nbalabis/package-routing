# Nicholas Balabis, Student ID: 001314467

import ui
from read_data import packages, locations, truck1, truck2, truck3
import convert_time

# Set initial delivery state
deliveries_completed = False


# Begin package routing for each truck
def start():
    truck1.start()
    truck2.start()
    packages.get(9).update_location(locations.get('410 S State St'))
    truck3.start()


# Print an overview including time of completion and total distance traveled
def get_info():
    print('----------------------------------------------------')
    print('    ALL PACKAGES SUCCESSFULLY DELIVERED ON TIME!')
    print(
        f'The final truck returned to the Hub at {convert_time.to_readable(max([truck1.time, truck2.time, truck3.time]))}')
    print(
        f'The trucks traveled a total distance of {str("%.1f" % (truck1.total_distance + truck2.total_distance + truck3.total_distance))} miles')
    print('----------------------------------------------------')


# Welcome message
print("""
----------------------------------------------------------------------
                 WELCOME TO THE WGUPS ROUTING PROGRAM
----------------------------------------------------------------------
Please choose from the list of available commands:
     -Type 'start' to begin package routing
     -Type 'quit' to exit the program 
     -Type 'help' at any time to see a list of all available commands
""")

# Prompt user input and start UI flow
user_input = input(":").lower()
lookup_input = ""
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
                get_info()
                print('The following commands are now available:')
                print("     -Type 'lookup' to view packages at any point during the delivery process")
                print("     -Type 'info' to see an overview of the package deliveries\n")

            deliveries_completed = True

    elif user_input == 'info':
        if not deliveries_completed:
            print("\nDeliveries have not been completed yet.")
            print("     -Type 'start' to begin package routing\n")
        else:
            print("")
            get_info()
            print("")

    elif user_input == 'lookup':
        if not deliveries_completed:
            print("\nDeliveries have not been completed yet.")
            print("     -Type 'start' to begin package routing\n")
        else:
            ui.lookup_menu(lookup_input, deliveries_completed)

    elif user_input == 'help':
        ui.get_help(lookup_input, deliveries_completed)

    else:
        print('\nInvalid command.')
        ui.get_help(lookup_input, deliveries_completed)

    user_input = input(':').lower()
if user_input == 'quit':
    ui.exit_program()
