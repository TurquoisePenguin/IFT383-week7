#!/usr/bin/python
class Vehicle:
    _wheels=4
    _doors=2
    _fuel=100.0
    _temperature=105.0

    #constructor
    def __init__(self, wheels, doors, fuel, temperature):
        self._wheels = int(wheels)
        self._doors = int(doors)
        self._fuel = float(fuel)
        self._temperature = float(temperature)

    #getters
    def getWheels(self):
        return self._wheels

    def getDoors(self):
        return self._doors

    def getFuel(self):
        return self._fuel

    def getTemperature(self):
        return self._temperature

    #setters
    def setFuel(self, fuel):
        self._fuel = float(fuel)

