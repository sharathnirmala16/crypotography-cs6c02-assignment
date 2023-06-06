import hashlib

class MessageHashing:
    @staticmethod
    def compute(message : str) -> str:
        hash_obj = hashlib.sha256()
        hash_obj.update(message.encode('utf-8'))
        hash_value = hash_obj.hexdigest()
        return hash_value
    
message = "Hello World"
original_hash = MessageHashing.compute(message)
print("Original Hash:", original_hash)

received_hash = MessageHashing.compute(message)
print("Received Hash:", received_hash)

if received_hash == original_hash:
    print("The received message is not compromised.")
else:
    print("The received message is compromised!")

another_messsage = "hello world"

changed_hash = MessageHashing.compute(another_messsage)
print("Another message:", changed_hash)

if changed_hash == original_hash:
    print("The received message is not compromised,")
else:
    print("The received message is compromised!")
