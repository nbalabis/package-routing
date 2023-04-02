import convert_time
import lookup
from read_data import packages, locations


# Display help for the lookup menu
def get_lookup_help():
    print("\nChoose an identifier to view a filtered list of packages at a given time:")
    print("     -Type 'id' to view a specific package")
    print("     -Type 'address' to filter by delivery address")
    print("     -Type 'deadline' to filter by delivery deadline")
    print('                                   -OR-\n')
    print("     -Type 'all' to view the statuses of all packages at a given time\n")


# Display exit message
def exit_program():
    print('\n-------------------------------------------------------')
    print('     THANK YOU FOR USING THE WGUPS ROUTING PROGRAM')
    print('-------------------------------------------------------')
    exit()


# Display general help menu with available commands
def get_help(lookup_input, deliveries_completed, menu_input=""):
    if lookup_input == "":
        print('\nPlease choose from the list of available commands:')
        if not deliveries_completed:
            print("     -Type 'start' to begin package routing")
        else:
            print("     -Type 'lookup' to view packages at any point during the delivery process")
            print("     -Type 'info' to see an overview of the package deliveries")
    else:
        print('---------------------------------------------------------------------')
        if menu_input == "":
            print("     -Type 'cancel' to leave the Package Lookup Menu")
        else:
            print("     -Type 'cancel' to return to the Package Lookup Menu")
    print("     -Type 'quit' to exit the program")
    print("     -Type 'help' at any time to see a list of all available commands\n")


# Validate a time input
def validate_time(time_input):
    try:
        hours = int(time_input[0:time_input.find(':')])
        minutes = int(time_input[time_input.find(':') + 1:len(time_input)])
    except:
        print('\nInvalid entry.')
        print('Please enter a valid time between 00:00 and 23:59\n')
        return []
    else:
        if 24 > hours > -1 and 60 > minutes > -1 and ':' in time_input:
            return [hours, minutes]
        else:
            print('\nInvalid entry.')
            print('Please enter a valid time between 00:00 and 23:59\n')
            return []


# Menu to look up the status of all packages
def lookup_all_menu(lookup_input, deliveries_completed):
    print('\nEnter a valid time between 00:00 and 23:59\n')
    menu_input = input(':').lower()
    while menu_input != 'cancel':
        if menu_input == 'quit':
            exit_program()
        elif menu_input == 'help':
            print('\nEnter a valid time between 00:00 and 23:59')
            get_help(lookup_input, deliveries_completed, menu_input)
        else:
            time_to_lookup = validate_time(menu_input)
            if len(time_to_lookup) > 0:
                lookup.all_packages(time_to_lookup[0], time_to_lookup[1])
        menu_input = input(':').lower()
    if menu_input == 'cancel':
        print('\n-----------------------------')
        print('     PACKAGE LOOKUP MENU')
        print('-----------------------------')
        get_lookup_help()


# Menu to look up the status of a package with a particular ID
def lookup_id_menu(lookup_input, deliveries_completed):
    print('\nEnter a valid package ID\n')
    menu_input = input(':').lower()
    while menu_input != 'cancel':
        if menu_input == 'quit':
            exit_program()
        elif menu_input == 'help':
            print('\nEnter a valid package ID')
            get_help(lookup_input, deliveries_completed, menu_input)
        else:
            try:
                package = packages.get(int(menu_input))
            except:
                print('\nInvalid entry.')
                print('Please enter a valid time package ID\n')
            else:
                if package is not None:
                    print('\nEnter a valid time between 00:00 and 23:59\n')
                    menu_input = input(':').lower()
                    while menu_input != 'cancel':
                        if menu_input == 'quit':
                            exit_program()
                        elif menu_input == 'help':
                            print('\nEnter a valid time between 00:00 and 23:59')
                            get_help(lookup_input, deliveries_completed, menu_input)
                        else:
                            time_to_lookup = validate_time(menu_input)
                            if len(time_to_lookup) > 0:
                                lookup.specific_packages("ID", [package], time_to_lookup[0], time_to_lookup[1])
                                break

                        menu_input = input(':').lower()
                    if menu_input == 'cancel':
                        break
                else:
                    print('\nInvalid entry.')
                    print('Please enter a valid package ID\n')
        menu_input = input(':').lower()
    if menu_input == 'cancel':
        print('\n-----------------------------')
        print('     PACKAGE LOOKUP MENU')
        print('-----------------------------')
        get_lookup_help()


# Menu to look up the status of packages sharing the same delivery address
def lookup_address_menu(lookup_input, deliveries_completed):
    print('\nEnter a valid delivery address\n')
    menu_input = input(':')
    while menu_input.lower() != 'cancel':
        if menu_input.lower() == 'quit':
            exit_program()
        elif menu_input.lower() == 'help':
            print('\nEnter a valid delivery address')
            get_help(lookup_input, deliveries_completed, menu_input.lower())
        else:
            location = locations.get(menu_input)
            if location is not None:
                print('\nEnter a valid time between 00:00 and 23:59\n')
                menu_input = input(':').lower()
                while menu_input != 'cancel':
                    if menu_input == 'quit':
                        exit_program()
                    elif menu_input == 'help':
                        print('\nEnter a valid time between 00:00 and 23:59')
                        get_help(lookup_input, deliveries_completed, menu_input)
                    else:
                        time_to_lookup = validate_time(menu_input)
                        if len(time_to_lookup) > 0:
                            selected_packages = []
                            for package in packages.get_all():
                                if package.location == location:
                                    selected_packages.append(package)
                            lookup.specific_packages("address", selected_packages, time_to_lookup[0], time_to_lookup[1])
                            break

                    menu_input = input(':').lower()
                if menu_input == 'cancel':
                    break
            else:
                print('\nInvalid entry.')
                print('Enter a valid delivery address\n')
        menu_input = input(':')
    if menu_input.lower() == 'cancel':
        print('\n-----------------------------')
        print('     PACKAGE LOOKUP MENU')
        print('-----------------------------')
        get_lookup_help()


# Menu to look up the statuses of all packages sharing the same deadline
def lookup_deadline_menu(lookup_input, deliveries_completed):
    print('\nEnter a valid deadline between 00:00 and 23:59\n')
    menu_input = input(':').lower()
    while menu_input != 'cancel':
        if menu_input == 'quit':
            exit_program()
        elif menu_input == 'help':
            print('\nEnter a valid deadline between 00:00 and 23:59')
            get_help(lookup_input, deliveries_completed, menu_input)
        else:
            time_to_lookup = validate_time(menu_input)
            if len(time_to_lookup) > 0:
                selected_packages = []
                epoch_time = convert_time.to_epoch(time_to_lookup[0], time_to_lookup[1])
                for package in packages.get_all():
                    if package.deadline <= epoch_time:
                        selected_packages.append(package)
                if len(selected_packages) < 1:
                    print('\n-------------------------------------------------------------------------\n')

                    print(
                        f'There are no packages with a delivery deadline at or before {convert_time.to_readable(epoch_time)}')
                    print('\n-------------------------------------------------------------------------')
                    print(f"Lookup another deadline or type 'cancel' to return to the Package Lookup Menu\n")
                else:
                    print(
                        f'Displaying all packages with a delivery deadline at or before {convert_time.to_readable(epoch_time)}')
                    lookup.specific_packages("deadline", selected_packages, time_to_lookup[0], time_to_lookup[1])
        menu_input = input(':').lower()
    if menu_input == 'cancel':
        print('\n-----------------------------')
        print('     PACKAGE LOOKUP MENU')
        print('-----------------------------')
        get_lookup_help()


# Lookup menu with all lookup options displayed
def lookup_menu(lookup_input, deliveries_completed):
    print('\n-----------------------------')
    print('     PACKAGE LOOKUP MENU')
    print('-----------------------------')
    get_lookup_help()
    lookup_input = input(':').lower()
    while lookup_input != 'cancel':
        if lookup_input == 'quit':
            exit_program()
        elif lookup_input == 'help':
            get_lookup_help()
            get_help(lookup_input, deliveries_completed)
        elif lookup_input == 'all':
            lookup_all_menu(lookup_input, deliveries_completed)
        elif lookup_input == 'id':
            lookup_id_menu(lookup_input, deliveries_completed)
        elif lookup_input == 'address':
            lookup_address_menu(lookup_input, deliveries_completed)
        elif lookup_input == 'deadline':
            lookup_deadline_menu(lookup_input, deliveries_completed)
        else:
            print('\nInvalid entry.')
            get_lookup_help()
        lookup_input = input(':').lower()
    if lookup_input == 'cancel':
        lookup_input = ""
        get_help(lookup_input, deliveries_completed)
