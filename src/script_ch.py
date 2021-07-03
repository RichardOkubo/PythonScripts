import hashlib

file_1 = "file_1.txt"
file_2 = "file_2.txt"

hash_1 = hashlib.new("ripemd160")
hash_2 = hashlib.new("ripemd160")

hash_1.update(open(file_1, "rb").read())
hash_2.update(open(file_2, "rb").read())

print(
    f"File {file_1} is different from file {file_2}: {hash_1.hexdigest()} != {hash_2.hexdigest()}"
    if hash_1.digest() != hash_2.digest() else
    f"File {file_1} and {file_2} are similar: {hash_1.hexdigest()} == {hash_2.hexdigest()}"
)