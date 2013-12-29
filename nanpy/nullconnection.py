class NullConnection(object):

    def write(self, value):
        print('sending:%s' % repr(value))

    def readline(self):
        return ''

    def flush_input(self):
        """Flush input buffer, discarding all it's contents."""
