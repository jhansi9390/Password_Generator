import random
import string

def generate_password(length):
    if length <= 0:
        return "Invalid length!"
    
    characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main program
try:
    user_input = int(input("Enter desired password length: "))
    password = generate_password(user_input)
    print(f"\n🔐 Your Generated Password: {password}")
except ValueError:
    print("Please enter a valid number!")
