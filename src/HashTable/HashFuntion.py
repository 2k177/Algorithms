#Defining the hash funtion with handling the collision
class HashFunction:
    def __init__(self):
        self.MAX = 100
        self.ht = [None for x in range(self.MAX)]

    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        print hash % self.MAX
        return hash % self.MAX

    def __getitem__(self, item):
        h = self.get_hash(item)
        return self.ht[h]

    def __setitem__(self, key, val):
        h = self.get_hash(key)
        self.ht[h] = val

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.ht[h] = None
if __name__ == '__main__':
    ob =HashFunction()
    ob["march 9"]=310                                       #inbuilt function to set the value for corresponding key
    ob["JAN 2"] = 90
    print ob.ht                                             # inbuilt funtion to get the dict value
    del ob["march 9"]                                       #inbuilt funtion to delete the value for corresponding key mapped
    print ob.ht