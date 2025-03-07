# We will import two modules that being random and string
import random 
import string  

def generate_password(length):
    # Combine all characters (uppercase, lowercase, digits, punctuation)
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password by choosing 'length' number of characters from all_characters
    password = ''.join(random.choice(all_characters) for i in range(length))
    
    return password  

# Ask the user for the desired password length
password_length = int(input("Enter the desired password length: "))

# Generate and print the password
print("Generated Password: ", generate_password(password_length))
