class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class ListMapping:
    def __init__(self):
        self.entries = []

    def put(self, key, value):
        for entry in self.entries:
            if entry.key == key:
                entry.value = value
                return
        new_entry = Entry(key, value)
        self.entries.append(new_entry)

    def get(self, key):
        for entry in self.entries:
            if entry.key == key:
                return entry.value
        raise KeyError("Key not found")

    def remove(self, key):
        for entry in self.entries:
            if entry.key == key:
                self.entries.remove(entry)
                return
        raise KeyError("Key not found")

    def search(self, key):
        for entry in self.entries:
            if entry.key == key:
                return entry
        return None

    def size(self):
        return len(self.entries)

    def __contains__(self, key):
        for entry in self.entries:
            if entry.key == key:
                return True
        return False

    def __iter__(self):
        for entry in self.entries:
            yield (entry.key, entry.value)
