# Time Complexity : O(1)
# Space Complexity : O(N^2)


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = 1000
        self.bucketitems = 1001
        self.hashset = [None]* self.buckets
        
    def bucket(self,key):
        return key % self.buckets
    
    def bucketitem(self,key):
        return key /self.bucketitems

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket = self.bucket(key)
        bucketitem = self.bucketitem(key)
        if self.hashset[bucket] == None:
            self.hashset[bucket] = [False]*self.bucketitems
        
        self.hashset[bucket][bucketitem] = True
        
    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucket = self.bucket(key)
        bucketitem = self.bucketitem(key)
        if self.hashset[bucket]!=None:
            self.hashset[bucket][bucketitem] = False
        
        
    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucket = self.bucket(key)
        bucketitem = self.bucketitem(key)
        return self.hashset[bucket]!=None and self.hashset[bucket][bucketitem]
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)