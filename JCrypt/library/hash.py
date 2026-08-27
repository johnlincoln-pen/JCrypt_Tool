import hashlib


def hash_messages():
    print(hashlib.algorithms_available)
    algorithm = input("What type of hash do you want? :  ").strip().lower()
    message = input("Enter the message to hash: ")

    digest = hashlib.new(algorithm, message.encode("utf-8")).hexdigest()
    print(f"{message}: {digest}")


