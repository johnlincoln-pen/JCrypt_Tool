from library import hash
from library import encrypt
from library import decrypt


print("Welcome to the JCrypt")
print("1. Hash a message         2. Encrypt a message   " \
"3. Decrypt a message")

user_choice = int(input("enter the option you want to : "))

if user_choice == 1:
    hash.hash_messages()

if user_choice == 2:
    encrypt.main()

if user_choice == 3:
    decrypt.main()


else:
    print("Invalid option. Please try again.")
