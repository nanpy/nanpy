from config import config
from nanpy.arduinotree import ArduinoTree
from nanpy.serialmanager import serial_manager


def soft_reset():
    serial_manager.sleep_after_connect = config['sleep_after_connect']
    ArduinoTree().soft_reset()


def setup():
    soft_reset()
