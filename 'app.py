import os

def read_sensitive_data():
    # Intentionally hardcoding sensitive data
    secret_key = "my_secret_key"
    print(f"Secret Key: {secret_key}")

def execute_command():
    # Intentionally using os.system without proper sanitization
    user_input = input("Enter a command to execute: ")
    os.system(user_input)

def use_of_insecure_function():
    # Intentionally using an insecure function
    eval("print('Insecure function used')")

read_sensitive_data()
execute_command()
use_of_insecure_function()
