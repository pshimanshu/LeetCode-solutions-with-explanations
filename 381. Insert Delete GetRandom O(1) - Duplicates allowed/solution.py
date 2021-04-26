class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ms = []        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.ms.append(val)
        if self.ms.count(val)>1:            
            return False
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.ms:
            self.ms.remove(val)
            return True
        return False        

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.ms[random.randint(0,len(self.ms)-1)]
        
