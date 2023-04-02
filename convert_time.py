from time import mktime, ctime


# Convert hours & minutes to epoch time
def to_epoch(hours, minutes=0):
    return mktime((2023, 3, 20, hours, minutes, 0, 0, 0, 0))


# Convert an epoch time to the format hh:mm
def to_readable(epoch_time):
    return ctime(epoch_time)[11:16]
