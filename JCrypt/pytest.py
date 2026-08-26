from library import hash

print("Welcome to the JCrypt")
print("1. Hash a message")

user_chaoice = int(input("enter the option you want to : "))

if user_chaoice == 1:
    hash.hash_messages()

else:
    print("Invalid option. Please try again.")