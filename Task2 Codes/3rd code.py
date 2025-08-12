import secrets
import string

def create_password(size):
    if size < 4:
        return "Password length must be at least 4."

    # Pools of characters
    pools = {
        "upper": string.ascii_uppercase,
        "lower": string.ascii_lowercase,
        "digit": string.digits,
        "symbol": string.punctuation
    }

    # Start with one character from each pool
    password_list = [secrets.choice(pools[key]) for key in pools]

    # Fill the rest with any type of character
    all_characters = "".join(pools.values())
    password_list.extend(secrets.choice(all_characters) for _ in range(size - 4))

    # Shuffle securely
    secrets.SystemRandom().shuffle(password_list)

    return "".join(password_list)

try:
    user_length = int(input("Enter desired password length: "))
    print("Generated secure password:", create_password(user_length))
except ValueError:
    print("Please enter a valid number.")
