#!/usr/bin/env python

# a simple example to read from a DHT sensor

from nanpy import DHT

# http://learn.adafruit.com/dht/connecting-to-a-dhtxx-sensor
# DHT sensor connected to digital pin 10
dht = DHT(10, DHT.DHT22)

print("Temperature is %.2f degrees Celcius" % dht.readTemperature(False))
print("Temperature is %.2f degrees Fahrenheit" % dht.readTemperature(True))
print("Humidity is %.2f %%" % dht.readHumidity())

