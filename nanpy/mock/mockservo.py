import logging

from nanpy.mock.mockobject import MockObject


log = logging.getLogger(__name__)

class MockServo(MockObject):
    firmware_id = "Servo"

    def factory(self, params):
        d = dict(
             pin=int(params[0]),
             angle=0,
             )
        return d
        
    def elaborate(self, obj_id, name, params):
        if name == "read":
            return self.objects[obj_id]['angle']
        elif name == "write":
            self.objects[obj_id]['angle'] = int(params[0])
            return 0
        elif name == "writeMicroseconds":
            raise NotImplementedError
        elif name == "readMicroseconds":
            raise NotImplementedError
        elif name == "detach":
            self.objects[obj_id]['pin'] = None
            return 0
        elif name == "attached":
            return self.objects[obj_id]['pin'] is not None
        return MockObject.elaborate(self, obj_id, name, params)
