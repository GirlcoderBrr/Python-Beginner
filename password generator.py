import random

def generate_password(length):
    password = ""
    for _ in range(length):
        random_chr = chr(random.randint(33, 126))
        password += random_chr
    return password
password_length = 12
print("Your password is:", generate_password(password_length))