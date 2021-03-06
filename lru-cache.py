import collections

class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
         
        self.capacity = capacity
        self.cache = collections.OrderedDict()
        self.size = 0
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
       
        return self.cache.pop(key,-1)
       
        
        pass

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if self.size == self.capacity:
            self.cache.popitem(False)
        
        self.cache[key] = value
        self.size += 1


        pass

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)


print(our_cache.get(3))