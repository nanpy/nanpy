from nanpy.arduinotree import ArduinoTree


# set it to 1000 for a good test (4 minutes)
REPEAT_TEST = 10


def test_long():
    a = ArduinoTree()
    for x in range(REPEAT_TEST):
        print (x, ('uptime: %s sec' % (a.api.millis() / 1000.0)))
        a.soft_reset()

