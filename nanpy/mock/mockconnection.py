import logging

from nanpy.mock.mockeeprom import MockEEPROM
from nanpy.mock.mockinfo import MockInfo
from nanpy.mock.mockram import MockRAM
from nanpy.mock.mockservo import MockServo
from nanpy.mock.mockstepper import MockStepper


log = logging.getLogger(__name__)


ALL_CLASSES = [
               MockInfo, 
               MockRAM, 
               MockEEPROM,
               MockServo,
               MockStepper,
               ]
    

class MockConnection(object):
    state = 0
    obj_id = 0
    param_count = 0
    
    def __init__(self):
        self.objects = dict([(c.firmware_id, c()) for c in ALL_CLASSES])
        self.objects['Info'].class_names = [x.firmware_id for x in ALL_CLASSES]

    def elaborate(self,):
        for n, x in self.objects.items():
            if n == self.class_name:
                self.return_value = x.elaborate(self.obj_id, self.func_name, self.params)
                return
        assert 0
        
    def write(self, value):
        log.debug('sending:%s', repr(value))
        assert value.endswith('\x00')
        
        value = value[0:-1]
        
        assert value == value.strip()
        
        if self.state == 0:
            self.class_name = value
            self.state += 1
        elif self.state == 1:
            self.obj_id = int(value)
            self.state += 1
        elif self.state == 2:
            self.param_count = int(value)
            self.state += 1
        elif self.state == 3:
            self.func_name = value
            self.params = []
            self.state += 1
            if self.param_count == 0:
                self.elaborate()
                self.state = 0
        elif self.state == 4:
            self.params.append(value)
            self.param_count -= 1
            if self.param_count == 0:
                self.elaborate()
                self.state = 0
                
        assert self.state<=4
        assert self.param_count<=10
        assert self.param_count>=0
        
    def readline(self):
        s = '%s\r\n' % self.return_value
        log.debug('received:%s', repr(s))
        return s

