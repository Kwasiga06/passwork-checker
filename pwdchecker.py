import re

def load_common_passwords(file_path = 'common-passwords.txt'):
    """Load common passwords from a file"""
    try:
        with open(file_path, 'r') as file:
            return set(line.strip() for line in file if line.strip())
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found")
        return set()
    
def is_strong_password(password, common_passwords):
    """Check if the password is strong"""
    score = 0
    reasons = []
    if len(password) >= 12:
        score += 2
        reasons.append("✓ Length is strong")
    elif len(password) >= 8:
        score += 1
        reasons.append("✓ Length is acceptable")
    else:
        reasons.append("✗ Length is too short")
    if re.search(r'[A-Z]', password):
        score += 1
        reasons.append("✓ Contains uppercase letters")
    else:
        reasons.append("✗ Missing uppercase letters")
    if re.search(r'[a-z]', password):
        score += 1
        reasons.append("✓ Contains lowercase letters")
    else:
        reasons.append("✗ Missing lowercase letters")
    if re.search(r'[0-9]', password):
        score += 1
        reasons.append("✓ Contains numbers")
    else:
        reasons.append("✗ Missing numbers")
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
        reasons.append("✓ Contains special characters")
    else:
        reasons.append("✗ Missing special characters")
    
    if password in common_passwords:
        reasons.append("✗ Found in common.breached passwords list")
        score = 0  # Reset score if password is common
    else:
        score += 2
        reasons.append("✓ Not found in breached password list")
    
    if score >= 7:
        password_strength = "✅ Strong"
    elif score >= 4:
        password_strength = "⚠️ Moderate"
    else:
        password_strength = "❌ Weak"

    return password_strength, reasons

if __name__ == "__main__":
    common_passwords = load_common_passwords()
    while True:
        password = input("Enter a password to check its strength: ")
        strength, reasons = is_strong_password(password, common_passwords)
        print(f"Password Strength: {strength}")
        print("Reasons:")
        for reason in reasons:
            print(reason)
        print("Thank you for using the password checker!")
        again = input("Would you like to check another password? (y/n): ").strip().lower()
        if again != 'y':
            print("Goodbye!")
            break