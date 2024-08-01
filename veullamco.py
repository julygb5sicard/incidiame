class MyObject:
    def __init__(self, writable):
        self._writable = writable

    def writable(self):
        return self._writable

obj = MyObject(False)

for i in range(10):
    if not obj.writable():
        break
    print(i)  # This will not be executed if obj is not writable
