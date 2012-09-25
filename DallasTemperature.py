from nanpy.OneWire import OneWire
import time

class DallasTemperature():

    def __init__(self, pin):
        self.__ds = OneWire(pin)
        self.__data = 0

    def __fetchAddress(self):
        ds_address = self.__ds.search()
        #print "The address of the sensor is R=%s" % ds_address.get()

        if ds_address == "1":
            return False

        self.__ds.reset()
        self.__ds.select(ds_address)
        self.__ds.write(0x44, 1)        #start conversion, with parasite power on at the end

        time.sleep(1)                   #maybe 750ms is enough, maybe not

        present = self.__ds.reset()
        self.__ds.select(ds_address)
        self.__ds.write(0xBE)
        return True

    def __fetchData(self):

        data = []

        #print "DATA",

        for i in range(9):
            val = self.__ds.read()
            #print "%s" % val,
            data.append(val)

        raw = (data[1] << 8) | data[0]

        type = 1

        if type == 0:

            raw = raw << 3;        # 9 bit resolution default
            if data[7] == 0x10:
                raw = (raw & 0xFFF0) + 12 - data[6]    # count remain gives full 12 bit resolution

        else:
            cfg = (data[4] & 0x60)

            if cfg == 0x00:
                raw = raw << 3;    # 9 bit resolution, 93.75 ms
            elif cfg == 0x20:
                raw = raw << 2;    # 10 bit res, 187.5 ms
            elif cfg == 0x40:
                raw = raw << 1;    # 11 bit res, 375 ms 
            else:
                pass               #default is 12 bit resolution, 750 ms conversion time

        self.__data = raw

    def getCelsius(self):
        if self.__fetchAddress():
            self.__fetchData()
        return self.__data / 16.0

    def getFahrenheit(self):
        if self.__fetchAddress():
            self.__fetchData()
        return self.getCelsius() * 1.8 + 32.0
