class MockObject(object):
    def __init__(self):
        self.objects = []

    def elaborate(self, obj_id, name, params):
        if name == "new":
            x = self.factory(params)
            self.objects.append(x)
            return len(self.objects) - 1
        if name == "remove":
            del self.objects[int(params[0])]
            return 0
