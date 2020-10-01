import sys
import types

if sys.version_info[0] > 2:  # Python 3+
    create_bound_method = types.MethodType
else:
    def create_bound_method(func, obj):
        return types.MethodType(func, obj, obj.__class__)


class Strategy:
    def __init__(self, func=None):
        self._url = ""
        self._columns = ""
        self._scoring = ""

        if func:
            self.execute = create_bound_method(func, self)

    def execute(self):
        print(self._url)
