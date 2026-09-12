# generates SHA-256 hashes for input strings and files

import hashlib
import sys

# convert user string to hash
def hash_string(user_string):
    return hashlib.sha256(user_string.encode('utf-8')).hexdigest()

# convert file to hash
def hash_file(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, 'rb') as f:
               for byte_block in iter(lambda: f.read(4096), b''):
                  sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return "Error: File not found."

# user directory
print("SHA-256 Hash Generator")
print("1. Hash a string")
print("2. Hash a file")

# gets user choice
choice = input("Choose an option (1 or 2): ").strip()

if choice == '1':
    # gets user input for string hash
    text = input("Enter the string to hash: ")
    # calls hash_string() and outputs hash
    print(f"SHA-256: {hash_string(text)}")

elif choice == '2':
    # gets user input for file hash
    path = input("Enter the path to the file: ").strip()
    # calls hash_file() and outputs hash
    print(f"SHA-256: {hash_file(path)}")
else:
    print ("Invalid choice.")