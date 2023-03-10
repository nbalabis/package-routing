class HashMap:
    def __init__(self):
        self.size = 128
        self.map = [None] * self.size

    # Hash a key
    def __get_hash(self, key):
        hashed_key = 0
        for char in str(key):
            hashed_key += ord(char)
        return hashed_key % self.size

    # Add a key-value pair to the hash table or update an existing one
    def add(self, key, value):
        hashed_key = self.__get_hash(key)
        key_value = [key, value]

        if self.map[hashed_key] is None:
            self.map[hashed_key] = list([key_value])
            return True
        for key_value in self.map[hashed_key]:
            if key_value[0] == key:
                key_value[1] = value
                return True
        self.map[hashed_key].append(key_value)
        return True

    # Delete a key-value pair from the hash table
    def delete(self, key):
        hashed_key = self.__get_hash(key)

        if self.map[hashed_key] is None:
            return False
        for i in range(0, len(self.map[hashed_key]) + 1):
            if self.map[hashed_key][i][0] == key:
                self.map[hashed_key].pop(i)
                return True
            return False

    # Get a specific value from the hash table
    def get(self, key):
        hashed_key = self.__get_hash(key)

        if self.map[hashed_key] is not None:
            for key_value in self.map[hashed_key]:
                if key_value[0] == key:
                    return key_value[1]
        return None
