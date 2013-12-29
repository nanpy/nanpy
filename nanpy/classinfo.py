from nanpy.arduinoboard import arduinomethod, returns, FirmwareClass
from nanpy.memo import memoized


class FirmwareError(Exception):
    pass


def check4firmware(cls):
    if not hasattr(check4firmware, 'names'):
        check4firmware.names = dict()
    cls_name = cls.get_firmware_id()
    assert cls_name not in check4firmware.names.keys()
    check4firmware.names[cls_name] = cls

    def getinstance(connection):
        if cls_name == 'Info':
            return cls(connection)

        if connection is not None:
            if not hasattr(connection, 'classinfo'):
                connection.classinfo = ClassInfo(connection)
            if cls_name not in connection.classinfo.firmware_id_list:
                raise FirmwareError(
                    '''%s ['%s'] is missing from firmware!''' %
                    (cls, cls_name))
        return cls(connection)
#     getinstance.__name__ = cls.__name__
    return getinstance


@check4firmware
class ClassInfoArray(FirmwareClass):
    firmware_id = 'Info'

    @property
    @memoized
    @returns(int)
    @arduinomethod
    def count(self):
        pass

    @memoized
    @arduinomethod
    def name(self, index):
        pass


class ClassInfo(object):

    """Which classes are compiled into the firmware?"""

    def __init__(self, connection):
        self.firmware_class_status = dict()
        self.unknown_firmware_ids = []

        self._arr = ClassInfoArray(connection=connection)

        ls = [self._arr.name(i) for i in range(self._arr.count)]
        assert len(ls)
        self.firmware_id_list = sorted(ls)

        for cls in check4firmware.names.values():
                self.firmware_class_status[cls.__name__] = False

        for x in self.firmware_id_list:
            cls = check4firmware.names.get(x)
            if cls:
                self.firmware_class_status[cls.__name__] = True
            else:
                self.unknown_firmware_ids.append(x)
