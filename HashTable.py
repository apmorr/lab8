from Lab.lab8.ListMappping import ListMapping


class HashTable:
    def __init__(self, size):
        self.size = size
        self.buckets = [ListMapping() for i in range(size)]
        self.num_entries = 0

    def _get_bucket(self, key):
        bucket_index = hash(key) % self.size
        return self.buckets[bucket_index]

    def put(self, key, value):
        bucket = self._get_bucket(key)
        try:
            bucket.get(key)
        except KeyError:
            self.num_entries += 1
        bucket.put(key, value)
        if self.num_entries / self.size > 0.75:
            self.__double()

    def get(self, key):
        bucket = self._get_bucket(key)
        return bucket.get(key)

    def __double(self):
        self.size *= 2
        new_buckets = [ListMapping() for i in range(self.size)]
        for bucket in self.buckets:
            for key, value in bucket:
                new_bucket = new_buckets[hash(key) % self.size]
                new_bucket.put(key, value)
        self.buckets = new_buckets
