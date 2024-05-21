#!/usr/bin/env python3

""" cashing system """


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    basic FIFO caching class
    """
    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                FirstKey = next(iter(self.cache_data))
                print("DISCARD: {}".format(FirstKey))
                del self.cache_data[FirstKey]

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            try:
                return self.cache_data[key]
            except KeyError:
                pass
