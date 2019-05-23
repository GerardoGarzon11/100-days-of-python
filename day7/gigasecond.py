from datetime import datetime
from datetime import timedelta
from math import pow

def add_gigasecond(moment):
    return moment + timedelta(seconds = int(pow(10,9)))