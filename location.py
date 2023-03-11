class Location:
    def __init__(self, location_id, name, address, distances):
        self.id = location_id
        self.name = name
        self.address = address
        self.distances = distances

    def get_distance_to(self, location):
        return self.distances[location.id]
