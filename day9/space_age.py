MERCURY = 31557600 * 0.2408467;
VENUS = 31557600 * 0.61519726
EARTH = 31557600 * 1
MARS = 31557600 * 1.8808158
JUPITER = 31557600 * 11.862615
SATURN = 31557600 * 29.447498
URANUS = 31557600 * 84.016846
NEPTUNE = 31557600 * 164.79132

class SpaceAge(object):
    def __init__(self, seconds):
        self.seconds = seconds

    def precision2Div(self, planet):
    	return round(self.seconds / planet, 2)

    def on_mercury(self):
    	return self.precision2Div(MERCURY)

    def on_venus(self):
    	return self.precision2Div(VENUS)

    def on_earth(self):
    	return self.precision2Div(EARTH)

    def on_mars(self):
    	return self.precision2Div(MARS)

    def on_jupiter(self):
    	return self.precision2Div(JUPITER)

    def on_saturn(self):
    	return self.precision2Div(SATURN)

    def on_uranus(self):
    	return self.precision2Div(URANUS)

    def on_neptune(self):
    	return self.precision2Div(NEPTUNE)
