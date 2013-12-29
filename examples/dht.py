#!/usr/bin/env python

# a simple example to read from a DHT sensor

from nanpy import DHT

# http://learn.adafruit.com/dht/connecting-to-a-dhtxx-sensor
# DHT sensor connected to digital pin 10
dht = DHT(10,DHT.DHT22)

print("temperature is %f degrees Celcius" % dht.readTemperature())
print("temperature is %f degrees Celcius" % dht.readTemperature(False))
print("temperature is %f degrees Fahrenheit" % dht.readTemperature(True))
print("humidity is %f %%" % dht.readHumidity())

