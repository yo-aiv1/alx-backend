#!/usr/bin/env python3

""" cashing system """


from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    basic LIFO caching class
    """
    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None or item is not None:
            if key in self.cache_data:
                del self.cache_data[key]

            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                LastKey = list(self.cache_data.keys())[-2]
                print("DISCARD: {}".format(LastKey))
                del self.cache_data[LastKey]

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            try:
                return self.cache_data[key]
            except KeyError:
                pass
