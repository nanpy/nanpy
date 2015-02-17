import logging

log = logging.getLogger(__name__)


class MockInfo(object):
    firmware_id = "Info"

    def __init__(self, class_names=None):
        self.class_names = class_names
        
    
    def elaborate(self, obj_id, name, params):
        if name == "count":
            return len(self.class_names)
        elif name == "name":
            return self.class_names[int(params[0])]

