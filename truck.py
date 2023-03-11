class Truck:
    def __init__(self, name):
        self.max_packages = 16
        self.packages = []
        self.name = str(name)
        # self.location = ????

    def load_package(self, package):
        if not self.is_full():
            self.packages.append(package)
            package.update_status('In Transit')
            return True
        print('ERROR: TRUCK ' + self.name + ' IS FULL')
        return False

    def get_packages(self):
        print(self.packages)

    def is_full(self):
        return not len(self.packages) < self.max_packages
