import re

def check_password_strength(password):
    # Minimum length check
    if len(password) < 8:
        return False
    
    # Uppercase and lowercase letters check
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False
    
    # Digit check
    if not any(char.isdigit() for char in password):
        return False
    
    # Special character check
    special_characters = r"[!@#$%^&*(),.?\":{}|<>]"
    if not re.search(special_characters, password):
        return False
    
    # Password meets all criteria
    return True

def main():
    # Take user input for password
    password = input("Enter your password: ")
    
    # Check password strength
    if check_password_strength(password):
        print("Password is strong!")
    else:
        print("Password does not meet the criteria. Please ensure it has at least 8 characters, both uppercase and lowercase letters, at least one digit, and at least one special character.")

if __name__ == "__main__":
    main()
