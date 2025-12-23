import random
import string

def generate_random_password(length=12):
       
    # Define the character sets for the password
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits
    
    # Combine all character sets
    all_chars = lowercase_chars + uppercase_chars + digit_chars
    
    # Ensure at least one character from each set is included to meet criteria
    # This approach generates random selections until the desired length is met.
    password_list = []
    
    # Guarantee at least one of each type
    password_list.append(random.choice(lowercase_chars))
    password_list.append(random.choice(uppercase_chars))
    password_list.append(random.choice(digit_chars))
    
    # Fill the remaining length with random choices from the combined pool
    if length > 3:
        for _ in range(length - 3):
            password_list.append(random.choice(all_chars))
    elif length < 3:
        # Handle case where desired length is less than 3, truncating the guaranteed elements
        password_list = password_list[:length]
        
    # Shuffle the generated password characters to ensure randomness in character order
    random.shuffle(password_list)
    
    # Join the list of characters into a single string
    password = "".join(password_list)
    
    return password

# --- Example Usage ---

# Generate a password with the default length (12 characters)
password_1 = generate_random_password()
print(f"Generated Password 1: {password_1}")
