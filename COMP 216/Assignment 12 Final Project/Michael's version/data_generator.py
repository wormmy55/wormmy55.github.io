import random
import math
from time import asctime
from json import dumps

class DataGenerator:
    def __init__(self, ymin=0, ymax=60, daily_mean=19, daily_amps=[1.2, 2, 3, 2.5, 3.5], stddev=2.4):
        self.ymin = ymin
        self.ymax = ymax
        self.daily_mean = daily_mean
        self.daily_amps = daily_amps
        self.daily_freqs = [2.5 * math.pi / 100, 1 * math.pi / 100, 2 * math.pi / 100, 1.2 * math.pi / 100, 1.8 * math.pi / 100]
        self.stddev = stddev
        self.t = 0

    def get_json_data(self):
        daily_variation = sum([amp * math.sin(self.t * freq) for amp, freq in zip(self.daily_amps, self.daily_freqs)])
        value = self.daily_mean + daily_variation + random.gauss(0, self.stddev * 2)
        data = {'time': asctime(), 'value': value}
        self.t += 1
        return dumps(data)
