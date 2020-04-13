class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return (f'{self.hour} : {self.minute} : {self.second}')


def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


x = int_to_time(1584177718)

print(x)
