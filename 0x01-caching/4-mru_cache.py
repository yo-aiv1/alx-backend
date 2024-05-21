#!/usr/bin/env python3

""" cashing system """


from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    basic MRU caching class
    """
    CacheLog = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None or item is not None:
            if key in self.cache_data:
                self.CacheLog.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                LRUKey = self.CacheLog.pop(-1)
                del self.cache_data[LRUKey]
                print("DISCARD:", LRUKey)

            self.CacheLog.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.CacheLog.remove(key)
            self.CacheLog.append(key)
            return self.cache_data[key]
