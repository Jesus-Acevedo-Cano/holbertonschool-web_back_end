#!/usr/bin/python3
""" MRU caching """

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRU cache class """
    def __init__(self):
        """ constructor """
        self.cache = []
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key not in self.cache_data:
                self.cache.append(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.cache.pop(-2)
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.cache.remove(key)
        self.cache.append(key)
        return self.cache_data[key]
