class Package:
    def __init__(self, data, location, deadline):
        self.id = data[0]
        self.location = location
        self.deadline = deadline
        self.city = data[2]
        self.zip = data[4]
        self.mass = data[6]
        self.notes = data[7]
        self.status = 'At Hub'
        self.load_time = None
        self.delivery_time = None
        self.on_time = True

    # Updates package status in hash map
    def update_status(self, status):
        self.status = status

    def update_location(self, location):
        print('Updating package ' + str(self.id) + ' delivery address to ' + location.address + '\n')
        self.location = location

    def deliver(self, time):
        self.status = 'Delivered'
        self.delivery_time = time
        if time > float(self.deadline):
            self.on_time = False
