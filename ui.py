import lookup
from read_data import packages


def get_lookup_help():
    print("\nChoose an identifier to view a filtered list of packages at a given time:")
    print("     -Type 'id' to view a specific package")
    print("     -Type 'address' to filter by delivery address")
    print("     -Type 'deadline' to filter by delivery deadline")
    print("     -Type 'city' to filter by delivery city")
    print("     -Type 'zip' to filter by delivery zip code")
    print("     -Type 'weight' to filter by package weight")
    print("     -Type 'status' to filter by delivery status\n")
    print('                                   -OR-\n')
    print("     -Type 'all' to view the statuses of all packages at a given time\n")


def exit_program():
    print('\n-------------------------------------------------------')
    print('     THANK YOU FOR USING THE WGUPS ROUTING PROGRAM')
    print('-------------------------------------------------------')
    exit()


def get_help(lookup_input, deliveries_completed):
    if lookup_input == "":
        print('\nPlease choose from the list of available commands:')
        if not deliveries_completed:
            print("     -Type 'start' to begin package routing")
        else:
            print("     -Type 'lookup' to view packages at any point during the delivery process")
            print("     -Type 'info' to see an overview of the package deliveries")
    else:
        print('---------------------------------------------------------------------')
        print("     -Type 'cancel' to leave the Package Lookup Menu")
    print("     -Type 'quit' to exit the program")
    print("     -Type 'help' at any time to see a list of all available commands\n")


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


def lookup_all_menu(lookup_input, deliveries_completed):
    print('\nEnter a valid time between 00:00 and 23:59\n')
    menu_input = input(':').lower()
    while menu_input != 'cancel':
        if menu_input == 'quit':
            exit_program()
        elif menu_input == 'help':
            print('\nEnter a valid time between 00:00 and 23:59')
            get_help(lookup_input, deliveries_completed)
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


def lookup_id_menu(lookup_input, deliveries_completed):
    print('\nEnter a valid package ID\n')
    menu_input = input(':').lower()
    while menu_input != 'cancel':
        if menu_input == 'quit':
            exit_program()
        elif menu_input == 'help':
            print('\nEnter a valid package ID')
            get_help(lookup_input, deliveries_completed)
        else:
            try:
                package = packages.get(int(menu_input))
            except:
                print('\nInvalid entry.')
                print('Please enter a valid time package ID\n')
            else:
                if package is not None:
                    # get time input
                    print(package)
                else:
                    print('\nInvalid entry.')
                    print('Please enter a valid time package ID\n')

        menu_input = input(':').lower()


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
        else:
            print('\nInvalid entry.')
            get_lookup_help()
        lookup_input = input(':').lower()
    if lookup_input == 'cancel':
        lookup_input = ""
        get_help(lookup_input, deliveries_completed)
