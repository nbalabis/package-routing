class Package:
    def __init__(self, data, location):
        self.id = data[0]
        self.location = location
        self.deadline = data[5]
        self.mass = data[6]
        self.notes = data[7]
        self.status = 'At Hub'
        self.load_time = None
        self.delivery_time = None

    # Updates package status in hash map
    def update_status(self, status):
        self.status = status

    def update_location(self, location):
        print('Updating package ' + str(self.id) + ' delivery address to ' + location.address + '\n')
        self.location = location
