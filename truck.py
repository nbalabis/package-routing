from nna import nna


class Truck:
    def __init__(self, name, hub, departure_time):
        self.max_packages = 16
        self.packages = []
        self.name = str(name)
        self.hub = hub
        self.location = hub
        self.time = departure_time

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
            package.update_status('Delivered')
            package.delivery_time = self.time
            print('     Package ' + package.id + ' delivered')
            self.packages.remove(package)

    def get_packages(self):
        return self.packages

    def is_full(self):
        return not len(self.packages) < self.max_packages

    def next_stop(self):
        package = nna(self.location, self.packages)
        self.time += 1
        self.location = package.location
        self.deliver_packages()

    def start(self):
        print('Truck ' + self.name + ' leaving the Hub')
        while len(self.packages) > 0:
            self.next_stop()
        print('All packages delivered! Returning to hub')
        self.location = self.hub
