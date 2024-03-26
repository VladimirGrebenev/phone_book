from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

# Create an instance of the HTTPBasicAuth class
auth = HTTPBasicAuth()

# Create a dictionary of users and their hashed passwords
users = {
    "admin": generate_password_hash("pass")
}

@auth.verify_password
def verify_password(username, password):
    """
    A function that verifies the password for a given username.

    Parameters:
    - username (str): The username to verify.
    - password (str): The password to check against the username.

    Returns:
    - str: The username if password is verified, None otherwise.
    """
    if username in users and check_password_hash(users.get(username), password):
        return username
