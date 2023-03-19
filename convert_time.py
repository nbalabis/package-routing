from time import mktime, ctime


def to_epoch(hours, minutes=0):
    return mktime((2023, 3, 20, hours, minutes, 0, 0, 0, 0))


def to_readable(epoch_time):
    return ctime(epoch_time)[11:16]
