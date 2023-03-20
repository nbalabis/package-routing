from nna import nna
import convert_time


class Truck:
    def __init__(self, name, hub, departure_time):
        self.max_packages = 16
        self.packages = []
        self.name = str(name)
        self.hub = hub
        self.location = hub
        self.time = departure_time
        self.speed = 18
        self.total_distance = 0

    def load_package(self, package):
        if not self.is_full():
            self.packages.append(package)
            package.update_status('En Route')
            package.load_time = self.time
            return True
        print('ERROR: TRUCK ' + self.name + ' IS FULL')
        return False

    def deliver_packages(self):
        packages_to_deliver = []
        for package in self.packages:
            if package.location == self.location:
                packages_to_deliver.append(package)
        for package in packages_to_deliver:
            package.deliver(self.time)
            if package.on_time:
                status = 'on time'
            else:
                status = 'LATE'
            print(f'     {convert_time.to_readable(self.time)}: Package {package.id} delivered {status}')
            self.packages.remove(package)

    def get_packages(self):
        return self.packages

    def is_full(self):
        return not len(self.packages) < self.max_packages

    def next_stop(self):
        package = nna(self.location, self.packages)
        distance = package.location.get_distance_to(self.location)
        self.total_distance += distance
        time_in_seconds = ((1 / self.speed) * distance) * (60 * 60)
        self.time += time_in_seconds
        self.location = package.location
        self.deliver_packages()

    def start(self):
        print('Truck ' + self.name + ' leaving the Hub at ' + convert_time.to_readable(self.time))
        while len(self.packages) > 0:
            self.next_stop()
        print('     All packages delivered! Returning to hub')
        self.return_to_hub()

    def return_to_hub(self):
        distance = self.hub.get_distance_to(self.location)
        self.total_distance += distance
        time_in_seconds = ((1 / self.speed) * distance) * (60 * 60)
        self.time += time_in_seconds
        self.location = self.hub
        print('Truck ' + self.name + ' arriving at the Hub at ' + convert_time.to_readable(self.time))
        print('     Travelled a total of ' + str("%.1f" % self.total_distance) + ' miles \n')

    def print_packages(self):
        print('Truck ' + self.name + ' loaded with packages:')
        print('     ', end="")
        for package in self.get_packages():
            print(package.id, end=" ")
        print('')
        print('     Special Notes:')
        for package in self.get_packages():
            if package.notes != '':
                print('          ' + str(package.id) + ': ' + package.notes)
        print('')
