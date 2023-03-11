class Location:
    def __init__(self, location_id, name, address, distances):
        self.id = location_id
        self.name = name
        self.address = address
        self.distances = distances

    # Get distance to another Location
    def get_distance_to(self, location):
        distance = self.distances[location.id]
        if distance == '':
            distance = location.get_distance_to(self)
        return float(distance)
