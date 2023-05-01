class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [[] for i in range(self.size)]
        
    def hash_function(self, key):
        return key % self.size
    
    def insert(self, key, value):
        hash_key = self.hash_function(key)
        already_exists = False
        for index, item in enumerate(self.hash_table[hash_key]):
            if item[0] == key:
                self.hash_table[hash_key][index] = (key, value)
                already_exists = True
                break
        if not already_exists:
            self.hash_table[hash_key].append((key, value))
            
    def search(self, key):
        hash_key = self.hash_function(key)
        for item in self.hash_table[hash_key]:
            if item[0] == key:
                return item[1]
        return "Key not found"
    
    def delete(self, key):
        hash_key = self.hash_function(key)
        for index, item in enumerate(self.hash_table[hash_key]):
            if item[0] == key:
                del self.hash_table[hash_key][index]
                return "Key deleted"
        return "Key not found"
    
    def print_all(self):
        for index, item in enumerate(self.hash_table):
            if item:
                print(index, end=" ")
                for pair in item:
                    print("-->", pair, end=" ")
                print()
        
        
Value_list = [3, 2, 9, 11, 7]
size = len(Value_list)
hash_table = HashTable(size)
for value in Value_list:
    hash_table.insert(value, value)
        
while True:
    print("\nChoose one of the following options:")
    print("1. Construct the whole hash table")
    print("2. Add a new element to the hash table")
    print("3. Update a value of a certain key")
    print("4. Delete an element from the hash table")
    print("5. Search for an element in the hash table")
    print("6. Print all elements with their keys")
    print("Enter 'q' to quit")
    choice = input("> ")
        
    if choice == '1':
        hash_table.print_all()
    elif choice == '2':
        key = int(input("Enter key: "))
        value = int(input("Enter value: "))
        hash_table.insert(key, value)
        print("Element added successfully")
    elif choice == '3':
        key = int(input("Enter key: "))
        value = int(input("Enter new value: "))
        hash_table.insert(key, value)
        print("Value updated successfully")
    elif choice == '4':
        key = int(input("Enter key: "))
        message = hash_table.delete(key)
        print(message)
    elif choice == '5':
        key = int(input("Enter key: "))
        result = hash_table.search(key)
        print(result)
    elif choice == '6':
        hash_table.print_all()
    elif choice == 'q':
        break
    else:
        print("Invalid choice. Try again")
            
