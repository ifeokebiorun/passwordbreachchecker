import hashlib
import requests

def hash_password(password):
    sha1 = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    return sha1

def check_breach(password):
    sha1 = hash_password(password)
    prefix = sha1[:5]
    suffix = sha1[5:]

    url = "https://api.pwnedpasswords.com/range/" + prefix
    response = requests.get(url)

    hashes = response.text.splitlines()

    for line in hashes:
        parts = line.split(":")
        hash_suffix = parts[0]
        count = parts[1]
        if hash_suffix == suffix:
            return int(count)

    return 0

def check_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters, ideally 12+")

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    if has_upper:
        score += 1
    else:
        feedback.append("Add an uppercase letter")

    if has_lower:
        score += 1
    else:
        feedback.append("Add a lowercase letter")

    if has_digit:
        score += 1
    else:
        feedback.append("Add a number")

    if has_symbol:
        score += 1
    else:
        feedback.append("Add a symbol (!, @, #, etc.)")

    return score, feedback

if __name__ == "__main__":
    password = input("Enter a password to check: ")

    breach_count = check_breach(password)
    score, feedback = check_strength(password)

    print(f"\nPassword: {'*' * len(password)}")

    if breach_count > 0:
        print(f"⚠️ Found in {breach_count} breaches!")
    else:
        print("✅ Not found in any known breaches.")

    print(f"Strength score: {score}/6")
    if feedback:
        print("Suggestions:")
        for tip in feedback:
            print(f"  - {tip}")
    else:
        print("Strong password!")