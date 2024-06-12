import random
import string

# Generate a dataset of 1000 random key-value pairs
data_set = { ''.join(random.choices(string.ascii_letters + string.digits, k=10)): ''.join(random.choices(string.ascii_letters + string.digits, k=15)) for _ in range(1000)}

# Define a simple custom hashing function
def custom_hash(key, mod_value=1024):
    hash_value = 0
    for char in key:
        hash_value = (hash_value * 31 + ord(char)) % mod_value
    return hash_value

# Create a hash map (list of lists for handling collisions)
hash_map_size = 1024
hash_map = [[] for _ in range(hash_map_size)]

# Insert key-value pairs into the hash map
def insert(key, value):
    index = custom_hash(key)
    # Handle collision by chaining
    for kvp in hash_map[index]:
        if kvp[0] == key:
            kvp[1] = value
            return
    hash_map[index].append([key, value])

# Retrieve value by key
def retrieve(key):
    index = custom_hash(key)
    for kvp in hash_map[index]:
        if kvp[0] == key:
            return kvp[1]
    return None

# Populate the hash map with the data set
for key, value in data_set.items():
    insert(key, value)

# Display the list of keys and their corresponding values
print("List of keys and their corresponding values:")
for key, value in data_set.items():
    print(f"Key: {key} -> Value: {value}")

# Interactive key retrieval
def interactive_retrieval():
    while True:
        key = input("Enter a key to retrieve the value (or 'exit' to quit): ")
        if key.lower() == 'exit':
            break
        value = retrieve(key)
        if value is not None:
            print(f"Value: {value}")
        else:
            print("Key not found.")

# Call the interactive retrieval function
interactive_retrieval()
