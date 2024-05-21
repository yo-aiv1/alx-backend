#!/usr/bin/env python3

""" cashing system """


from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    basic MRU caching class
    """
    CacheLog = {}

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                freq = self.CacheLog.pop(key)
                self.cache_data.pop(key)
                self.CacheLog[key] = freq + 1
            else:
                if len(self.cache_data) >= LFUCache.MAX_ITEMS:
                    LFUKey = min(self.CacheLog, key=self.CacheLog.get)
                    self.CacheLog.pop(LFUKey)
                    self.cache_data.pop(LFUKey)
                    print('DISCARD: {}'.format(LFUKey))

                self.CacheLog[key] = 1
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key in self.CacheLog:
            freq = self.CacheLog.pop(key)
            self.CacheLog[key] = freq + 1
        return self.cache_data.get(key, None)
