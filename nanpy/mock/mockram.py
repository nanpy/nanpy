import logging

log = logging.getLogger(__name__)

class MockRAM(object):
    firmware_id = "RAM"

    def __init__(self):
        self.memory = [0, 1, 2, 3, 4, 5, 255, 255]
        self.free = 3
        
    def elaborate(self, obj_id, name, params):
        if name == "size":
            return len(self.memory)
        elif name == "read":
            return self.memory[int(params[0])]
        elif name == "write":
            self.memory[int(params[0])] = int(params[1])
        elif name == "free":
            return self.free
