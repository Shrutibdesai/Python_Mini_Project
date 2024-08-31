import random
import string

def generate_password(length=12, use_special_chars=True, use_digits=True, use_uppercase=True, use_lowercase=True):
    # Create a pool of characters based on the user's preferences
    characters = ""
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation

    # Ensure that the pool is not empty
    if not characters:
        raise ValueError("At least one type of character must be selected!")

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    length = int(input("Enter the desired length of the password: "))
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_special_chars, use_digits, use_uppercase, use_lowercase)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
