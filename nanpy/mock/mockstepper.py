import logging

from nanpy.mock.mockobject import MockObject


log = logging.getLogger(__name__)

    
class MockStepper(MockObject):
    firmware_id = "Stepper"

    def factory(self, params):
        d = dict(
             revsteps=int(params[0]),
             pin1=int(params[1]),
             pin2=int(params[2]),
             speed=0,
             )
        return d
    
    def elaborate(self, obj_id, name, params):
        if name == "setSpeed":
            self.objects[obj_id]['speed'] = int(params[0])
            return 0
        elif name == "step":
            assert self.objects[obj_id]
            return 0
        return MockObject.elaborate(self, obj_id, name, params)
        
