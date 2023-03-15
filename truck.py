from nna import nna


class Truck:
    def __init__(self, name, hub):
        self.max_packages = 16
        self.packages = []
        self.name = str(name)
        self.hub = hub
        self.location = hub

    def load_package(self, package):
        if not self.is_full():
            self.packages.append(package)
            package.update_status('In Transit')
            return True
        print('ERROR: TRUCK ' + self.name + ' IS FULL')
        return False

    def deliver_packages(self):
        packages_to_deliver = []
        for package in self.packages:
            if package.location == self.location:
                packages_to_deliver.append(package)
        for package in packages_to_deliver:
            print('     Package ' + package.id + ' delivered')
            package.update_status('Delivered')
            self.packages.remove(package)

    def get_packages(self):
        return self.packages

    def is_full(self):
        return not len(self.packages) < self.max_packages

    def next_stop(self):
        # Find the nearest neighbor
        package = nna(self.location, self.packages)
        print('Delivering package: ' + package.id)

        # Travel to it (how to make this take time?)
        print('     Travelling ' + str(
            package.location.get_distance_to(self.location)) + ' miles to ' + package.location.address)
        self.location = package.location

        # Remove all packages that have that address once you get to it
        self.deliver_packages()

    def start(self):
        # Special case: no packages left - return to hub
        while len(self.packages) > 0:
            self.next_stop()

        print('All packages delivered! Returning to hub')
        self.location = self.hub
