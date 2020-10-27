#!/usr/bin/python3
""" LIFO caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO cache class """
    def __init__(self):
        """ constructor """
        self.discard = None
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key and item:
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            del self.cache_data[self.discard]
            print("DISCARD: {}".format(self.discard))

        if key is not None:
            self.discard = key

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
