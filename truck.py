class Truck:
    def __init__(self):
        self.max_packages = 16
        self.packages = []

    def load_package(self, package):
        if len(self.packages) < self.max_packages:
            self.packages.append(package)
            return True
        return False

    def get_packages(self):
        print(self.packages)
