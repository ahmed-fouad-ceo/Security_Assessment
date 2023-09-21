import os

def read_sensitive_data():
    # Sensitive data should be stored in environment variables
    # Retrieve the secret key from an environment variable
    secret_key = os.environ.get('SECRET_KEY')
    if secret_key is not None:
        print("Secret Key:", secret_key)
    else:
        print("Secret Key not found")

def execute_command():
    # Avoid using os.system, which can execute arbitrary commands
    print("Executing a safe command")

def use_of_insecure_function():
    # Avoid using eval, which is insecure
    print("Avoided insecure function")

if __name__ == '__main__':
    read_sensitive_data()
    execute_command()
    use_of_insecure_function()
