#!/usr/bin/env python

# a simple example to read from a DHT sensor

from nanpy import DHT

# http://learn.adafruit.com/dht/connecting-to-a-dhtxx-sensor
# DHT sensor connected to digital pin 10
dhts = [
    DHT(6, DHT.DHT11),
    DHT(7, DHT.DHT11),
    DHT(8, DHT.DHT11)
]

for i, dht in enumerate(dhts):
    print("DHT %d" % i)
    print("Temperature is %.2f degrees Celcius" % dht.readTemperature(False))
    print("Temperature is %.2f degrees Fahrenheit" % dht.readTemperature(True))
    print("Humidity is %.2f %%" % dht.readHumidity())

