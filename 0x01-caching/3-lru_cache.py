#!/usr/bin/env python3

""" cashing system """


from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    basic LRU caching class
    """
    CacheLog = {}

    def UpdateLog(self, key, value):
        if key not in self.CacheLog:
            self.CacheLog[key] = 0

        for k in self.CacheLog.keys():
            if self.cache_data[k] == value:
                continue
            self.CacheLog[k] += 1

    def GetLRU(self):
        LRUKey = max(self.CacheLog, key=lambda k: self.CacheLog[k])
        self.CacheLog[LRUKey] = 0
        return LRUKey

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None or item is not None:
            self.cache_data[key] = item
            self.UpdateLog(key, item)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                LRUKey = self.GetLRU()
                print("DISCARD: {}".format(LRUKey))
                del self.cache_data[LRUKey]
                del self.CacheLog[LRUKey]

    def get(self, key):
        """
        Get an item by key
        """
        if key is not None:
            try:
                return self.cache_data[key]
            except KeyError:
                pass
