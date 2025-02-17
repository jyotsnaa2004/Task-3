import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    # Initialize an empty character set
    char_set = ""
    
    # Add character sets based on user input
    if use_uppercase:
        char_set += string.ascii_uppercase
    if use_lowercase:
        char_set += string.ascii_lowercase
    if use_digits:
        char_set += string.digits
    if use_symbols:
        char_set += string.punctuation
    
    # Ensure the char_set is not empty
    if not char_set:
        raise ValueError("At least one character type must be selected.")
    
    # Generate the password
    password = ''.join(random.choice(char_set) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Get user input
    try:
        length = int(input("Enter the password length: "))
        if length < 1:
            print("Password length must be at least 1.")
            return
    except ValueError:
        print("Invalid input! Please enter a valid number for the password length.")
        return
    
    use_uppercase = input("Include uppercase letters (Y/N)? ").strip().lower() == 'y'
    use_lowercase = input("Include lowercase letters (Y/N)? ").strip().lower() == 'y'
    use_digits = input("Include digits (Y/N)? ").strip().lower() == 'y'
    use_symbols = input("Include symbols (Y/N)? ").strip().lower() == 'y'
    
    # Generate the password based on the user's input
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
    
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
