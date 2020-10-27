#!/usr/bin/python3
""" LFU caching """

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFU cache class """
    def __init__(self):
        """ constructor """
        self.cache = []
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            if key in self.cache_data:
                self.cache.remove(key)
            self.cache_data[key] = item
            self.cache.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discard = self.cache.pop(0)
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        self.cache.remove(key)
        self.cache.append(key)
        return self.cache_data[key]
