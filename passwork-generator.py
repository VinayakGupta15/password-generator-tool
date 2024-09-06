import random
import string

def generate_password(length, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    # Define the character sets to choose from based on user preferences
    char_pool = ''
    
    if use_lowercase:
        char_pool += string.ascii_lowercase
    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_special_chars:
        char_pool += string.punctuation
    
    # Ensure the pool is not empty
    if not char_pool:
        raise ValueError("No character types selected. Please enable at least one character type.")
    
    # Generate the password by randomly selecting characters from the pool
    password = ''.join(random.choice(char_pool) for _ in range(length))
    
    return password

# Example usage
if __name__ == "__main__":
    # Get user input for password length and preferences
    length = int(input("Enter the desired password length: "))
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    # Generate the password
    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
    
    print(f"Generated password: {password}")
