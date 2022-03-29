from time import time
from random import random

print(f'{(time()+random()*10000)%10000000:.0f}')