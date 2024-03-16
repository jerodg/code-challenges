# print("Hello")

# Dimmer switch, 0+ lightbulbs

# Dimmer min and max levels
MIN_LEVEL = 5  # "hardware bug"
MAX_LEVEL = 15


# Level.        | 5      | 10      | 20 (max brightness)
# ------------------------------------------
# 0            | 0      | 0       | 0 (brightness)
# 5            | 2.5    | 5       | 10
# 10           | 5      | 10      | 20

# Max lightbulb wattage is 200 watts

class Bulb(object):
    max_brightness = 10

    def __init__(self, level):
        self.level = level - 5
        self.current_brightness = self.set_brightness(level)

    def set_brightness(self, level):
        # if self.current_brightness != self.max_brightness:

        self.current_brightness = (self.level * self.max_brightness) / (MAX_LEVEL - MIN_LEVEL)
        # self.current_brightness = self.level / self.max_brightness

        print(f'set brightness to {self.current_brightness}')


class DimmerSwitch(Bulb):

    def __init__(self, wattage):
        super().__init__(wattage)
        self.level = 5

    def increase_level(self):
        if self.level <= MAX_LEVEL:
            self.level += 1
            self.set_brightness(self.level)

        print(f'set level to {self.level}')

    def decrease_level(self):
        if self.level >= MIN_LEVEL():
            self.level -= 1
            self.set_brightness(self.level)

        print(f'set level to {self.level}')


ds = DimmerSwitch(10)
ds.increase_level()
ds.increase_level()
ds.increase_level()
ds.increase_level()
ds.increase_level()
