import os
from src.maths import add, substract

def get_secret(secret_name):
    # Security Vulnerability: Using os.environ directly can expose sensitive information
    return os.environ.get(secret_name)

print(get_secret("MY_SECRET"))
print(add(1,2))
