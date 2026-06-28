import random
import string

print("===== PASSWORD CREATOR =====")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits

choice = input("Include special symbols? (yes/no): ").lower()

if choice == "yes":
    characters += string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:")
print(password)

if length >= 12:
    print("Security Level: Strong")
elif length >= 8:
    print("Security Level: Medium")
else:
    print("Security Level: Weak")