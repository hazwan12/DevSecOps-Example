import os

def get_secret(secret_name):
    # Security Vulnerability: Using os.environ directly can expose sensitive information
    return os.environ.get(secret_name)

def add(a,b):return a+b  # Linting Error: No spaces around the operator and no newline after the colon

print(get_secret("MY_SECRET"))
print(add(1,2))
