def nna(location, packages):
    shortest_distance = 1000
    for package in packages:
        distance = package.location.get_distance_to(location)
        if distance < shortest_distance:
            shortest_distance = distance
            next_package = package
    return next_package
