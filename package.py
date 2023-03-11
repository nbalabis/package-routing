class Package:
    def __init__(self, data):
        self.id = data[0]
        self.address = data[1]
        self.city = data[2]
        self.state = data[3]
        self.zip = data[4]
        self.deadline = data[5]
        self.mass = data[6]
        self.notes = data[7]
        self.status = 'At Hub'

    # Updates package status in hash map
    def update_status(self, status):
        self.status = status
